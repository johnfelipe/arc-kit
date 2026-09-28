/**
 * Read auto-allow for ArcKit handoff tempfiles in /tmp.
 *
 * /tmp is shared, so a name that matches the handoff pattern is not enough:
 * the file must be a regular, single-link file owned by the current user.
 * Covers both the Claude hook and the Codex hook, which share the logic.
 */

import test from 'node:test';
import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { spawnSync } from 'node:child_process';
import { existsSync, linkSync, mkdirSync, mkdtempSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';

const HOOKS = {
  claude: resolve('plugins/arckit-claude/hooks/allow-plugin-internals.mjs'),
  // The Codex hook imports converter-generated config/, so only run it once built.
  ...(existsSync(resolve('extensions/arckit-codex/config/doc-types.mjs'))
    ? { codex: resolve('extensions/arckit-codex/hooks/arckit-codex-hook.mjs') }
    : {}),
};

function readDecision(hook, filePath) {
  const r = spawnSync('node', [hook], {
    input: JSON.stringify({ hook_event_name: 'PreToolUse', tool_name: 'Read', tool_input: { file_path: filePath } }),
    encoding: 'utf8',
  });
  assert.equal(r.status, 0, r.stderr);
  const out = r.stdout.trim() ? JSON.parse(r.stdout) : null;
  return out?.hookSpecificOutput?.permissionDecision ?? null;
}

function tmpName(tag) {
  return `/tmp/arckit-test-handoff-${tag}.${process.pid}${Math.random().toString(36).slice(2, 8)}.json`;
}

const skip = process.platform === 'win32' ? 'POSIX /tmp semantics required' : false;

for (const [name, hook] of Object.entries(HOOKS)) {
  test(`${name}: allows Read of an owned regular handoff tempfile`, { skip }, (t) => {
    const p = tmpName('ok');
    writeFileSync(p, '{}', { mode: 0o600 });
    t.after(() => rmSync(p, { force: true }));
    assert.equal(readDecision(hook, p), 'allow');
  });

  test(`${name}: does not allow a handoff-named symlink to another file`, { skip }, (t) => {
    const dir = mkdtempSync('/tmp/arckit-test-');
    const target = resolve(dir, 'secret.txt');
    writeFileSync(target, 'secret');
    const link = tmpName('symlink');
    symlinkSync(target, link);
    t.after(() => { rmSync(link, { force: true }); rmSync(dir, { recursive: true, force: true }); });
    assert.equal(readDecision(hook, link), null);
  });

  test(`${name}: does not allow a handoff-named hard link`, { skip }, (t) => {
    const dir = mkdtempSync('/tmp/arckit-test-');
    const target = resolve(dir, 'secret.txt');
    writeFileSync(target, 'secret');
    const link = tmpName('hardlink');
    linkSync(target, link);
    t.after(() => { rmSync(link, { force: true }); rmSync(dir, { recursive: true, force: true }); });
    assert.equal(readDecision(hook, link), null);
  });

  test(`${name}: does not allow a handoff-named path that does not exist`, { skip }, () => {
    assert.equal(readDecision(hook, tmpName('missing')), null);
  });

  test(`${name}: does not allow a handoff-named directory`, { skip }, (t) => {
    const p = tmpName('dir');
    mkdirSync(p);
    t.after(() => rmSync(p, { recursive: true, force: true }));
    assert.equal(readDecision(hook, p), null);
  });

  test(`${name}: does not allow non-handoff /tmp paths`, { skip }, (t) => {
    const p = `/tmp/arckit-test-notes.${process.pid}.json`;
    writeFileSync(p, '{}');
    t.after(() => rmSync(p, { force: true }));
    assert.equal(readDecision(hook, p), null);
  });
}
