#!/usr/bin/env node
/**
 * ArcKit PermissionRequest Hook — Auto-Allow Plugin-Internal Reads & Scripts
 *
 * Reading the plugin's own bundled files (templates, schemas, scripts,
 * agent prompts, references) and invoking the plugin's own bundled
 * helper scripts (validate-handoff.mjs, create-project.sh, generate-
 * document-id.sh, etc.) should not require user approval each session.
 * They are part of the plugin the user has already trusted by enabling.
 *
 * This hook auto-approves PermissionRequests for:
 *   - Read against any path under the plugin root
 *   - Bash commands that are a single bare invocation of an allowlisted
 *     ${CLAUDE_PLUGIN_ROOT}/scripts/ helper (validate-handoff.mjs,
 *     scripts/bash/*.sh helpers), optionally prefixed by node/bash/sh.
 *     Commands with shell operators (; && || | & > < `...` $(...)),
 *     multiple lines, or secret/protected-path arguments are not
 *     auto-allowed.
 *
 * Anything else (Read of project files, Bash for arbitrary commands,
 * Write of project artefacts, etc.) falls through to the normal
 * permission dialog.
 *
 * Hook Type: PreToolUse
 * Input (stdin):  JSON { tool_name, tool_input: {...}, ... }
 * Output (stdout):
 *   On match (allow):
 *     {"hookSpecificOutput": {
 *       "hookEventName": "PreToolUse",
 *       "permissionDecision": "allow",
 *       "permissionDecisionReason": "..."
 *     }}
 *   On no-match: silent pass-through (exit 0, no JSON).
 *
 * Exit code 0 always — pass-through is a non-decision, not a failure.
 * Hook auto-allow does NOT override user/project deny rules: per the
 * Claude Code docs, deny rules take precedence over plugin hook allows.
 */

import { lstatSync, readFileSync, realpathSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { basename, dirname, resolve } from 'node:path';

// Plugin root = parent of the hooks/ dir this script lives in.
const __dirname = dirname(fileURLToPath(import.meta.url));
const PLUGIN_ROOT = resolve(__dirname, '..');
const SCRIPTS_DIR = resolve(PLUGIN_ROOT, 'scripts');

function main() {
  let raw = '';
  try {
    raw = readFileSync(0, 'utf8');
  } catch {
    process.exit(0); // silent pass-through
  }
  if (!raw || !raw.trim()) process.exit(0);

  let data;
  try {
    data = JSON.parse(raw);
  } catch {
    process.exit(0);
  }

  const toolName = data.tool_name || '';
  const input = data.tool_input || {};

  if (toolName === 'Read') {
    const filePath = input.file_path || '';
    if (isUnderPluginRoot(filePath)) {
      allow(`ArcKit: auto-allowed Read of plugin-internal file (${shortPath(filePath)})`);
    }
    if (isArcKitTempfile(filePath)) {
      allow('ArcKit: auto-allowed Read of ArcKit-managed tempfile');
    }
  }

  if (toolName === 'Bash') {
    const command = input.command || '';
    if (commandTouchesPluginScripts(command)) {
      allow('ArcKit: auto-allowed Bash invocation of plugin-internal helper script');
    }
  }

  // No match — silent pass-through. Claude Code falls back to the
  // normal permission flow (user prompt, deny rules, etc.).
  process.exit(0);
}

// ── Helpers ────────────────────────────────────────────────────────────

function isUnderPluginRoot(p) {
  if (!p || typeof p !== 'string') return false;
  // Resolve to absolute, then check prefix. Don't follow symlinks; the
  // plugin's distributed files are real files in a marketplace cache.
  const abs = resolve(p).replaceAll('\\', '/');
  const root = PLUGIN_ROOT.replaceAll('\\', '/');
  return abs === root || abs.startsWith(root + '/');
}

const KNOWN_SCRIPTS = new Set([
  'validate-handoff.mjs',
  'generate-document-id.mjs',
  'bash/common.sh',
  'bash/create-project.sh',
  'bash/generate-document-id.sh',
  'bash/check-prerequisites.sh',
  'bash/list-projects.sh',
  'bash/migrate-filenames.sh',
  'bash/detect-stale-artifacts.sh',
]);

const SCRIPT_PREFIXES = [
  SCRIPTS_DIR.replaceAll('\\', '/') + '/',
  '${CLAUDE_PLUGIN_ROOT}/scripts/',
  '$CLAUDE_PLUGIN_ROOT/scripts/',
];

const INTERPRETERS = {
  node: /\.mjs$/,
  bash: /\.sh$/,
  sh: /\.sh$/,
};

const SECRET_PATTERNS = [
  /\bsk-[A-Za-z0-9_-]{20,}/,
  /\bAKIA[0-9A-Z]{16}\b/,
  /\bgh[pousr]_[A-Za-z0-9_]{20,}/,
  /\bAIza[0-9A-Za-z_-]{30,}/,
  /\bxox[baprs]-[A-Za-z0-9-]{10,}/,
  /\bntn_[A-Za-z0-9]{40,}/,
  /\bATATT[A-Za-z0-9]{20,}/,
  /-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----/,
];

const PROTECTED_BASENAMES = new Set([
  '.env', '.envrc', '.npmrc', '.pypirc', '.netrc', '.secrets',
  'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519',
  'credentials', 'credentials.json', 'service-account.json',
  'secrets.json', 'secrets.yaml', 'secrets.yml',
]);
const PROTECTED_DIRS = new Set(['.ssh', '.aws', '.gnupg', '.git']);
const PROTECTED_EXTENSIONS = ['.pem', '.key', '.p12', '.pfx', '.keystore'];

/**
 * True only when `cmd` is a single, bare invocation of an allowlisted
 * plugin helper script — optionally prefixed by its interpreter — with
 * plain arguments. Any shell operator, redirection, command substitution,
 * glob, comment or additional statement makes the command ineligible, as
 * does an argument that looks like secret material or a protected path.
 */
function commandTouchesPluginScripts(cmd) {
  const argv = tokenizeSimpleCommand(cmd);
  if (!argv || argv.length === 0) return false;

  let scriptIndex = 0;
  const interpreter = Object.hasOwn(INTERPRETERS, argv[0]) ? argv[0] : null;
  if (interpreter) scriptIndex = 1;

  const script = allowlistedScript(argv[scriptIndex]);
  if (!script) return false;
  if (interpreter && !INTERPRETERS[interpreter].test(script)) return false;

  if (SECRET_PATTERNS.some((re) => re.test(cmd))) return false;
  if (argv.slice(scriptIndex + 1).some(looksProtected)) return false;
  return true;
}

function allowlistedScript(token) {
  if (typeof token !== 'string') return null;
  for (const prefix of SCRIPT_PREFIXES) {
    if (token.startsWith(prefix)) {
      const tail = token.slice(prefix.length);
      return KNOWN_SCRIPTS.has(tail) ? tail : null;
    }
  }
  return null;
}

/**
 * Split a command into argv words, or return null if it contains anything
 * beyond plain words: only [A-Za-z0-9_./:=,@%+-] unquoted, single-quoted
 * literals, double-quoted text without backticks/backslashes/`!`, and
 * `$NAME` / `${NAME}` expansions. Backslash-newline continuations are
 * treated as whitespace.
 */
function tokenizeSimpleCommand(cmd) {
  if (!cmd || typeof cmd !== 'string') return null;
  const text = cmd.replace(/\\\r?\n/g, ' ').trim();
  if (!text) return null;

  const tokens = [];
  let current = '';
  let inWord = false;
  let i = 0;
  while (i < text.length) {
    const ch = text[i];
    if (ch === ' ' || ch === '\t') {
      if (inWord) tokens.push(current);
      current = '';
      inWord = false;
      i += 1;
      continue;
    }
    inWord = true;
    if (ch === "'") {
      const end = text.indexOf("'", i + 1);
      if (end < 0) return null;
      const literal = text.slice(i + 1, end);
      if (/[\r\n]/.test(literal)) return null;
      current += literal;
      i = end + 1;
      continue;
    }
    if (ch === '"') {
      i += 1;
      while (i < text.length && text[i] !== '"') {
        const c = text[i];
        if (c === '$') {
          const v = matchVariable(text, i);
          if (!v) return null;
          current += v;
          i += v.length;
          continue;
        }
        if (c === '`' || c === '\\' || c === '!' || c === '\n' || c === '\r') return null;
        current += c;
        i += 1;
      }
      if (i >= text.length) return null;
      i += 1;
      continue;
    }
    if (ch === '$') {
      const v = matchVariable(text, i);
      if (!v) return null;
      current += v;
      i += v.length;
      continue;
    }
    if (/[A-Za-z0-9_./:=,@%+-]/.test(ch)) {
      current += ch;
      i += 1;
      continue;
    }
    return null;
  }
  if (inWord) tokens.push(current);
  return tokens;
}

function matchVariable(text, i) {
  const m = /^\$(?:\{[A-Za-z_][A-Za-z0-9_]*\}|[A-Za-z_][A-Za-z0-9_]*)/.exec(text.slice(i));
  return m ? m[0] : null;
}

function looksProtected(arg) {
  const parts = arg.replaceAll('\\', '/').toLowerCase().split('/').filter(Boolean);
  if (parts.length === 0) return false;
  const name = parts[parts.length - 1];
  if (PROTECTED_BASENAMES.has(name) || name.startsWith('.env.')) return true;
  if (parts.some((part) => PROTECTED_DIRS.has(part))) return true;
  return PROTECTED_EXTENSIONS.some((ext) => name.endsWith(ext));
}

function isArcKitTempfile(p) {
  if (!p || typeof p !== 'string') return false;
  // ArcKit-managed tempfiles created by an orchestrator's mktemp call:
  //   /tmp/datascout-handoff.AbCdEf.json
  //   /tmp/grants-handoff.AbCdEf.json
  //   /tmp/grants-handoff-open-data.AbCdEf.json     (per-category dispatch)
  //   /tmp/gov-reuse-handoff.AbCdEf.json            (hyphenated agent name)
  //   /tmp/gov-reuse-handoff-appointment-booking.AbCdEf.json
  //   /tmp/arckit-grants-handoff.AbCdEf.json        (alt prefix form)
  //
  // Pattern: optional "arckit-" prefix, then a lowercase agent name
  // (which may itself contain hyphens, e.g. "gov-reuse"), then "-handoff",
  // then optional further hyphenated qualifiers (e.g. funder category)
  // and the mktemp random tail. Auto-allow Read against these so the
  // orchestrator can re-inspect a payload it just wrote.
  //
  // /tmp is shared and world-writable, so the name alone proves nothing:
  // another local user could plant a symlink or hard link there pointing
  // at a sensitive file. Only auto-allow a regular, single-link file owned
  // by the current user that sits directly in the real temp directory
  // (mktemp creates exactly that; sticky /tmp stops others replacing it).
  if (!/^\/tmp\/(?:arckit-)?[a-z][a-z0-9-]*-handoff(?:-[a-z][a-z0-9-]*)?[A-Za-z0-9.-]*\.json$/.test(p)) {
    return false;
  }
  return isOwnedRegularFile(p);
}

function isOwnedRegularFile(p) {
  if (typeof process.getuid !== 'function') return false;
  try {
    const st = lstatSync(p);
    if (!st.isFile() || st.isSymbolicLink()) return false;
    if (st.nlink !== 1) return false;
    if (st.uid !== process.getuid()) return false;
    return realpathSync(p) === resolve(realpathSync(dirname(p)), basename(p));
  } catch {
    return false;
  }
}

function shortPath(p) {
  if (typeof p !== 'string') return '';
  const idx = p.indexOf('/arckit-claude/');
  return idx >= 0 ? '…' + p.slice(idx) : p;
}

function allow(reason) {
  console.log(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'PreToolUse',
      permissionDecision: 'allow',
      permissionDecisionReason: reason,
    },
  }));
  process.exit(0);
}

main();
