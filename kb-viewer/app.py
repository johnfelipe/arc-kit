"""
ArcKit Knowledge Base Viewer — FastAPI Application
A modern, intuitive tool for consulting and verifying architecture artifacts.

All HTML templates are embedded in this file so the app is fully self-contained.
Artifacts are auto-discovered from the ./artifacts/ directory.
"""

import hashlib
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from jose import JWTError, jwt

from md_parser import load_all_documents, search_content, get_dashboard_stats

# --- Configuration ---
SECRET_KEY = os.environ.get("KB_SECRET_KEY", "arckit-kb-secret-2026-cap-gft")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24
DEFAULT_PASSWORD = "ArcKit2026!"

# --- Authorized Users ---
AUTHORIZED_USERS = {
    "Ricardo.Aguero@gft.com": {"name": "Ricardo Agüero", "role": "Arquitecto"},
    "Roberto.Hernandez-Robles@gft.com": {"name": "Roberto Hernández-Robles", "role": "Arquitecto"},
    "Maria-Andreina.Hidalgo@gft.com": {"name": "María Andreína Hidalgo", "role": "Arquitecta"},
    "Peter-Wilhelm@gft.com": {"name": "Peter Wilhelm", "role": "Arquitecto"},
    "Eduardo.Rojas@gft.com": {"name": "Eduardo Rojas", "role": "Arquitecto"},
}


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


DEFAULT_PASSWORD_HASH = hash_password(DEFAULT_PASSWORD)

# --- App Setup ---
app = FastAPI(
    title="ArcKit Knowledge Base",
    description="Consulta y verificación de artefactos de arquitectura — CAP Core Banking Program",
    version="1.0.0",
)

# --- Load documents at startup ---
DOCUMENTS = []
DASHBOARD_STATS = {}


@app.on_event("startup")
async def startup_load():
    global DOCUMENTS, DASHBOARD_STATS
    DOCUMENTS = load_all_documents()
    DASHBOARD_STATS = get_dashboard_stats(DOCUMENTS)


# --- Auth Helpers ---
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email and email in AUTHORIZED_USERS:
            return {"email": email, **AUTHORIZED_USERS[email]}
        return None
    except JWTError:
        return None


def get_current_user(request: Request) -> Optional[dict]:
    token = request.cookies.get("access_token")
    if not token:
        return None
    return verify_token(token)


# =====================================================================
# EMBEDDED HTML TEMPLATES
# =====================================================================

LOGIN_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ArcKit KB — Iniciar Sesión</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .gradient-bg { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%); }
        .card-glass { background: rgba(255,255,255,0.05); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); }
    </style>
</head>
<body class="gradient-bg min-h-screen flex items-center justify-center p-4">
    <div class="w-full max-w-md">
        <div class="text-center mb-8">
            <div class="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-blue-600/20 border border-blue-500/30 mb-4">
                <svg class="w-8 h-8 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
                </svg>
            </div>
            <h1 class="text-2xl font-bold text-white">ArcKit Knowledge Base</h1>
            <p class="text-slate-400 mt-2 text-sm">Caja de Ahorros — Programa Core Banking</p>
        </div>
        <div class="card-glass rounded-2xl p-8">
            {{ERROR_BLOCK}}
            <form method="POST" action="/login" class="space-y-5">
                <div>
                    <label class="block text-sm font-medium text-slate-300 mb-2">Correo corporativo</label>
                    <input type="email" name="email" required placeholder="nombre@gft.com"
                        class="w-full px-4 py-3 rounded-xl bg-slate-800/50 border border-slate-600/50 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500/50 transition-all">
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-300 mb-2">Contraseña</label>
                    <input type="password" name="password" required placeholder="Ingrese su contraseña"
                        class="w-full px-4 py-3 rounded-xl bg-slate-800/50 border border-slate-600/50 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500/50 transition-all">
                </div>
                <button type="submit"
                    class="w-full py-3 px-6 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold transition-all shadow-lg shadow-blue-600/25 hover:shadow-blue-500/40">
                    Iniciar Sesión
                </button>
            </form>
            <div class="mt-6 pt-6 border-t border-slate-700/50">
                <p class="text-xs text-slate-500 text-center">
                    Acceso restringido al equipo de arquitectura GFT.<br>17 artefactos de arquitectura disponibles.
                </p>
            </div>
        </div>
        <p class="text-center text-xs text-slate-600 mt-6">ArcKit v5.13.0</p>
    </div>
</body>
</html>"""


MAIN_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ArcKit KB — Base de Conocimiento</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
        .gradient-bg { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%); }
        .card-glass { background: rgba(255,255,255,0.03); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.08); }
        .card-glass:hover { border-color: rgba(255,255,255,0.15); }
        .sidebar { width: 280px; min-width: 280px; }
        .doc-content { max-width: 900px; }
        .markdown-body h1 { font-size: 1.5rem; font-weight: 700; margin: 1.5rem 0 0.75rem; color: #f1f5f9; }
        .markdown-body h2 { font-size: 1.25rem; font-weight: 600; margin: 1.25rem 0 0.5rem; color: #e2e8f0; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem; }
        .markdown-body h3 { font-size: 1.1rem; font-weight: 600; margin: 1rem 0 0.5rem; color: #cbd5e1; }
        .markdown-body h4 { font-size: 1rem; font-weight: 600; margin: 0.75rem 0 0.4rem; color: #94a3b8; }
        .markdown-body p { margin: 0.5rem 0; color: #94a3b8; line-height: 1.7; }
        .markdown-body ul, .markdown-body ol { margin: 0.5rem 0; padding-left: 1.5rem; color: #94a3b8; }
        .markdown-body li { margin: 0.25rem 0; line-height: 1.6; }
        .markdown-body table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.85rem; }
        .markdown-body th { background: rgba(59,130,246,0.1); color: #93c5fd; padding: 0.5rem 0.75rem; text-align: left; border: 1px solid rgba(255,255,255,0.1); font-weight: 600; }
        .markdown-body td { padding: 0.5rem 0.75rem; border: 1px solid rgba(255,255,255,0.05); color: #94a3b8; vertical-align: top; }
        .markdown-body tr:hover td { background: rgba(255,255,255,0.02); }
        .markdown-body code { background: rgba(59,130,246,0.1); color: #93c5fd; padding: 0.15rem 0.4rem; border-radius: 0.25rem; font-size: 0.85em; }
        .markdown-body pre { background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.1); border-radius: 0.5rem; padding: 1rem; overflow-x: auto; margin: 1rem 0; }
        .markdown-body pre code { background: none; padding: 0; }
        .markdown-body blockquote { border-left: 3px solid #3b82f6; padding-left: 1rem; margin: 1rem 0; color: #64748b; font-style: italic; }
        .markdown-body strong { color: #e2e8f0; }
        .markdown-body hr { border: none; border-top: 1px solid rgba(255,255,255,0.1); margin: 2rem 0; }
        .scrollbar-thin::-webkit-scrollbar { width: 6px; }
        .scrollbar-thin::-webkit-scrollbar-track { background: transparent; }
        .scrollbar-thin::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 3px; }
        .fade-in { animation: fadeIn 0.3s ease-in-out; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
        .dot-green { display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #22c55e; }
        .dot-empty { display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.05); }
    </style>
</head>
<body class="gradient-bg min-h-screen text-white" x-data="kbApp()" x-init="init()">

<!-- Top Navigation -->
<nav class="fixed top-0 left-0 right-0 z-50 border-b border-slate-700/50 bg-slate-900/80 backdrop-blur-xl">
    <div class="flex items-center justify-between px-6 py-3">
        <div class="flex items-center gap-4">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 rounded-lg bg-blue-600/20 border border-blue-500/30 flex items-center justify-center">
                    <svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
                    </svg>
                </div>
                <span class="font-semibold text-sm">ArcKit KB</span>
                <span class="text-[10px] px-1.5 py-0.5 rounded bg-blue-600/20 text-blue-400 font-medium">v1.0</span>
            </div>
            <div class="flex items-center gap-1 ml-4">
                <button @click="currentView='dashboard'" :class="currentView==='dashboard'?'bg-slate-700/50 text-white':'text-slate-400 hover:text-white'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition-all">Dashboard</button>
                <button @click="currentView='documents'" :class="currentView==='documents'?'bg-slate-700/50 text-white':'text-slate-400 hover:text-white'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition-all">Documentos</button>
                <button @click="currentView='traceability';!traceabilityData&&loadTraceability()" :class="currentView==='traceability'?'bg-slate-700/50 text-white':'text-slate-400 hover:text-white'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition-all">Trazabilidad</button>
                <button @click="currentView='search'" :class="currentView==='search'?'bg-slate-700/50 text-white':'text-slate-400 hover:text-white'" class="px-3 py-1.5 rounded-lg text-xs font-medium transition-all">Buscar</button>
            </div>
        </div>
        <div class="flex items-center gap-4">
            <div class="relative">
                <input type="text" x-model="searchQuery" @keyup.enter="doSearch()"
                    placeholder="Buscar en artefactos..." class="w-64 px-4 py-2 pl-9 rounded-lg bg-slate-800/50 border border-slate-600/50 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50">
                <svg class="absolute left-3 top-2.5 w-4 h-4 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                </svg>
            </div>
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-xs font-bold">{{USER_INITIAL}}</div>
                <span class="text-xs text-slate-400">{{USER_FIRSTNAME}}</span>
                <a href="/logout" class="ml-2 text-slate-500 hover:text-red-400 transition-colors" title="Cerrar sesión">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
                    </svg>
                </a>
            </div>
        </div>
    </div>
</nav>

<main class="pt-16 min-h-screen">

    <!-- DASHBOARD -->
    <div x-show="currentView==='dashboard'" x-transition class="p-6 fade-in">
        <div class="max-w-7xl mx-auto">
            <h1 class="text-2xl font-bold mb-1">Base de Conocimiento — Programa Core Banking</h1>
            <p class="text-slate-400 text-sm mb-6">Caja de Ahorros de Panamá — Evaluación y Selección CBS + ERP + AML</p>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 mb-8">
                <div class="card-glass rounded-xl p-5">
                    <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-blue-600/20 flex items-center justify-center text-lg">📄</div>
                    <div><p class="text-2xl font-bold" x-text="stats.total_documents">0</p><p class="text-xs text-slate-400">Artefactos</p></div></div>
                </div>
                <div class="card-glass rounded-xl p-5">
                    <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-green-600/20 flex items-center justify-center text-lg">📋</div>
                    <div><p class="text-2xl font-bold" x-text="totalReqs">0</p><p class="text-xs text-slate-400">Requisitos</p></div></div>
                </div>
                <div class="card-glass rounded-xl p-5">
                    <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-red-600/20 flex items-center justify-center text-lg">⚠️</div>
                    <div><p class="text-2xl font-bold" x-text="stats.total_risks">0</p><p class="text-xs text-slate-400">Riesgos</p></div></div>
                </div>
                <div class="card-glass rounded-xl p-5">
                    <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-purple-600/20 flex items-center justify-center text-lg">🏦</div>
                    <div><p class="text-2xl font-bold">3</p><p class="text-xs text-slate-400">RFPs</p></div></div>
                </div>
                <div class="card-glass rounded-xl p-5">
                    <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-cyan-600/20 flex items-center justify-center text-lg">📝</div>
                    <div><p class="text-2xl font-bold" x-text="Math.round(stats.total_words/1000)+'k'">0</p><p class="text-xs text-slate-400">Palabras</p></div></div>
                </div>
            </div>

            <!-- Requirement Breakdown -->
            <div class="card-glass rounded-xl p-6 mb-8">
                <h3 class="text-sm font-semibold text-slate-300 mb-4">Distribución de Requisitos por Tipo</h3>
                <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
                    <template x-for="[type, count] in Object.entries(stats.total_requirements || {})" :key="type">
                        <div class="text-center p-3 rounded-lg bg-slate-800/30">
                            <p class="text-xl font-bold text-blue-400" x-text="count"></p>
                            <p class="text-xs text-slate-500 mt-1" x-text="type"></p>
                        </div>
                    </template>
                </div>
            </div>

            <h2 class="text-lg font-semibold mb-4">Artefactos</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <template x-for="doc in documents" :key="doc.id">
                    <div @click="openDocument(doc.id)" class="card-glass rounded-xl p-5 cursor-pointer hover:border-blue-500/30 transition-all group">
                        <div class="flex items-start gap-3">
                            <span class="text-2xl flex-shrink-0" x-text="doc.category.icon"></span>
                            <div class="flex-1 min-w-0">
                                <p class="font-medium text-sm text-white group-hover:text-blue-300 transition-colors line-clamp-2" x-text="doc.title"></p>
                                <p class="text-xs mt-1.5 px-2 py-0.5 rounded-full inline-block" :style="`background:${doc.category.color}20;color:${doc.category.color}`" x-text="doc.category.name"></p>
                                <div class="flex items-center gap-3 mt-3 text-xs text-slate-500">
                                    <span x-text="doc.metadata['version']||doc.metadata['status']||''"></span>
                                    <span x-text="(doc.word_count/1000).toFixed(1)+'k palabras'"></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </template>
            </div>
        </div>
    </div>

    <!-- DOCUMENTS -->
    <div x-show="currentView==='documents'" x-transition class="flex h-[calc(100vh-4rem)]">
        <aside class="sidebar border-r border-slate-700/50 overflow-y-auto scrollbar-thin p-4 flex-shrink-0">
            <p class="text-xs font-medium text-slate-500 uppercase tracking-wider mb-3">Artefactos (<span x-text="documents.length"></span>)</p>
            <template x-for="doc in documents" :key="doc.id">
                <button @click="openDocument(doc.id)" :class="selectedDoc&&selectedDoc.id===doc.id?'bg-blue-600/10 border-blue-500/30':'border-transparent hover:bg-slate-700/30'" class="w-full text-left p-3 rounded-lg border mb-1 transition-all">
                    <div class="flex items-center gap-2">
                        <span class="text-sm" x-text="doc.category.icon"></span>
                        <span class="text-xs font-medium text-slate-300 truncate" x-text="doc.id"></span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-1 truncate" x-text="doc.category.name"></p>
                </button>
            </template>
        </aside>
        <div class="flex-1 overflow-y-auto scrollbar-thin p-8">
            <template x-if="selectedDoc">
                <div class="doc-content mx-auto fade-in">
                    <div class="mb-6">
                        <div class="flex items-center gap-2 mb-2">
                            <span class="text-2xl" x-text="selectedDoc.category.icon"></span>
                            <span class="text-xs px-2 py-0.5 rounded-full" :style="`background:${selectedDoc.category.color}20;color:${selectedDoc.category.color}`" x-text="selectedDoc.category.name"></span>
                            <span class="text-xs text-slate-500" x-text="selectedDoc.metadata['status']||'DRAFT'"></span>
                        </div>
                        <h1 class="text-xl font-bold" x-text="selectedDoc.title"></h1>
                        <div class="flex flex-wrap items-center gap-4 mt-3 text-xs text-slate-500">
                            <span x-show="selectedDoc.metadata['version']" x-text="'Versión: '+selectedDoc.metadata['version']"></span>
                            <span x-text="(selectedDoc.word_count/1000).toFixed(1)+'k palabras'"></span>
                            <span x-text="selectedDoc.line_count+' líneas'"></span>
                            <span x-show="selectedDoc.metadata['created date']" x-text="'Creado: '+selectedDoc.metadata['created date']"></span>
                        </div>
                    </div>
                    <!-- Metadata Card -->
                    <details class="card-glass rounded-xl p-4 mb-4" open>
                        <summary class="text-sm font-medium text-slate-300 cursor-pointer">Document Control</summary>
                        <div class="mt-3 grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
                            <template x-for="[key, val] in Object.entries(selectedDoc.metadata)" :key="key">
                                <div class="flex gap-2 py-1 border-b border-slate-700/30">
                                    <span class="text-slate-500 capitalize min-w-[120px]" x-text="key"></span>
                                    <span class="text-slate-300" x-text="val"></span>
                                </div>
                            </template>
                        </div>
                    </details>
                    <!-- TOC -->
                    <details class="card-glass rounded-xl p-4 mb-6">
                        <summary class="text-sm font-medium text-slate-300 cursor-pointer">Tabla de Contenido (<span x-text="selectedDoc.sections.length"></span> secciones)</summary>
                        <div class="mt-3 space-y-1 max-h-64 overflow-y-auto">
                            <template x-for="section in selectedDoc.sections" :key="section.anchor+section.title">
                                <a :href="'#'+section.anchor" :class="section.level===3?'pl-4':''" class="block text-xs text-slate-400 hover:text-blue-400 py-0.5 transition-colors" x-text="section.title"></a>
                            </template>
                        </div>
                    </details>
                    <div class="markdown-body" x-html="renderMarkdown(selectedDoc.raw_content)"></div>
                </div>
            </template>
            <template x-if="!selectedDoc">
                <div class="flex items-center justify-center h-full text-slate-500">
                    <div class="text-center">
                        <svg class="w-16 h-16 mx-auto mb-4 opacity-30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                        </svg>
                        <p class="text-sm">Seleccione un artefacto del panel izquierdo</p>
                    </div>
                </div>
            </template>
        </div>
    </div>

    <!-- TRACEABILITY -->
    <div x-show="currentView==='traceability'" x-transition class="p-6 fade-in">
        <div class="max-w-7xl mx-auto">
            <h1 class="text-2xl font-bold mb-1">Matriz de Trazabilidad</h1>
            <p class="text-slate-400 text-sm mb-6">Requisitos referenciados a través de los artefactos de arquitectura</p>
            <div x-show="loadingTrace" class="text-center py-12 text-slate-400">Cargando matriz...</div>
            <template x-if="traceabilityData">
                <div>
                    <div class="card-glass rounded-xl p-4 mb-6">
                        <div class="flex items-center gap-6 flex-wrap">
                            <div><span class="text-lg font-bold text-blue-400" x-text="traceabilityData.total_requirements"></span> <span class="text-xs text-slate-400">requisitos rastreados</span></div>
                            <div><span class="text-lg font-bold text-green-400" x-text="traceabilityData.documents.length"></span> <span class="text-xs text-slate-400">documentos</span></div>
                            <input type="text" x-model="traceFilter" placeholder="Filtrar (ej: FR-048, BR-002)..."
                                class="ml-auto w-64 px-3 py-2 rounded-lg bg-slate-800/50 border border-slate-600/50 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50">
                        </div>
                    </div>
                    <div class="overflow-x-auto card-glass rounded-xl">
                        <table class="w-full text-xs">
                            <thead>
                                <tr>
                                    <th class="text-left p-2.5 bg-slate-800/50 text-slate-300 font-medium sticky left-0 z-10 min-w-[80px]">Req ID</th>
                                    <template x-for="doc in traceabilityData.documents" :key="doc.id">
                                        <th class="p-2 bg-slate-800/50 text-slate-400 font-medium text-center" style="writing-mode:vertical-lr;min-width:36px;">
                                            <span x-text="doc.id.replace('ARC-001-','').substring(0,12)"></span>
                                        </th>
                                    </template>
                                </tr>
                            </thead>
                            <tbody>
                                <template x-for="[reqId, docIds] in filteredTraceability()" :key="reqId">
                                    <tr class="border-t border-slate-700/20 hover:bg-slate-700/20">
                                        <td class="p-2 font-mono text-blue-400 sticky left-0 bg-slate-900/95 z-10 whitespace-nowrap" x-text="reqId"></td>
                                        <template x-for="doc in traceabilityData.documents" :key="doc.id+reqId">
                                            <td class="p-2 text-center">
                                                <span x-show="docIds.includes(doc.id)" class="dot-green" title="Referenciado"></span>
                                                <span x-show="!docIds.includes(doc.id)" class="dot-empty"></span>
                                            </td>
                                        </template>
                                    </tr>
                                </template>
                            </tbody>
                        </table>
                    </div>
                    <p class="text-xs text-slate-500 mt-3" x-text="'Mostrando '+filteredTraceability().length+' de '+traceabilityData.total_requirements+' requisitos'"></p>
                </div>
            </template>
        </div>
    </div>

    <!-- SEARCH -->
    <div x-show="currentView==='search'" x-transition class="p-6 fade-in">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-2xl font-bold mb-1">Buscar en Artefactos</h1>
            <p class="text-slate-400 text-sm mb-6">Búsqueda de texto completo en todos los documentos de arquitectura</p>
            <div class="relative mb-6">
                <input type="text" x-model="searchQuery" @keyup.enter="doSearch()"
                    placeholder="Buscar requisitos, riesgos, vendors, regulaciones..."
                    class="w-full px-5 py-4 pl-12 rounded-xl bg-slate-800/50 border border-slate-600/50 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50 text-lg">
                <svg class="absolute left-4 top-5 w-5 h-5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                </svg>
                <button @click="doSearch()" class="absolute right-3 top-3 px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-500 text-sm font-medium transition-all">Buscar</button>
            </div>
            <div x-show="searchResults.length>0" class="space-y-4">
                <p class="text-sm text-slate-400"><span x-text="searchResults.length" class="font-bold text-white"></span> resultados encontrados para "<span x-text="lastQuery" class="text-blue-400"></span>"</p>
                <template x-for="result in searchResults" :key="result.doc_id">
                    <div @click="openDocument(result.doc_id)" class="card-glass rounded-xl p-5 cursor-pointer hover:border-blue-500/30 transition-all">
                        <div class="flex items-center gap-2 mb-2">
                            <span x-text="result.category.icon"></span>
                            <span class="font-medium text-sm text-blue-300" x-text="result.doc_id"></span>
                            <span class="text-xs px-2 py-0.5 rounded-full bg-blue-600/10 text-blue-400" x-text="'Relevancia: '+result.score"></span>
                        </div>
                        <p class="text-sm text-slate-300" x-text="result.title"></p>
                        <div class="mt-2 space-y-1">
                            <template x-for="(snippet, i) in result.snippets" :key="i">
                                <p class="text-xs text-slate-500 bg-slate-800/30 p-2 rounded leading-relaxed" x-text="snippet"></p>
                            </template>
                        </div>
                    </div>
                </template>
            </div>
            <div x-show="searchResults.length===0&&searchDone" class="text-center py-12 text-slate-500">
                <p>No se encontraron resultados para "<span x-text="lastQuery"></span>"</p>
            </div>
        </div>
    </div>
</main>

<script>
function kbApp(){
    return {
        currentView:'dashboard',
        documents:[],
        selectedDoc:null,
        searchQuery:'',
        searchResults:[],
        searchDone:false,
        lastQuery:'',
        traceabilityData:null,
        loadingTrace:false,
        traceFilter:'',
        stats:{total_documents:0,total_requirements:{},total_risks:0,total_words:0},
        get totalReqs(){
            return Object.values(this.stats.total_requirements||{}).reduce((a,b)=>a+b,0);
        },
        async init(){
            const res=await fetch('/api/documents');
            const data=await res.json();
            this.documents=data.documents;
            this.stats=data.stats;
        },
        async openDocument(docId){
            const res=await fetch('/api/documents/'+encodeURIComponent(docId));
            this.selectedDoc=await res.json();
            this.currentView='documents';
        },
        renderMarkdown(content){
            if(!content)return '';
            return marked.parse(content);
        },
        async doSearch(){
            if(this.searchQuery.length<2)return;
            this.currentView='search';
            this.lastQuery=this.searchQuery;
            const res=await fetch('/api/search?q='+encodeURIComponent(this.searchQuery));
            const data=await res.json();
            this.searchResults=data.results;
            this.searchDone=true;
        },
        async loadTraceability(){
            this.loadingTrace=true;
            const res=await fetch('/api/traceability');
            this.traceabilityData=await res.json();
            this.loadingTrace=false;
        },
        filteredTraceability(){
            if(!this.traceabilityData)return [];
            let entries=Object.entries(this.traceabilityData.matrix);
            if(this.traceFilter){
                const f=this.traceFilter.toUpperCase();
                entries=entries.filter(([id])=>id.toUpperCase().includes(f));
            }
            return entries.slice(0,200);
        }
    }
}
</script>
</body>
</html>"""


# --- Routes ---
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    user = get_current_user(request)
    if not user:
        html = LOGIN_HTML.replace("{{ERROR_BLOCK}}", "")
        return HTMLResponse(content=html)
    html = MAIN_HTML.replace("{{USER_INITIAL}}", user["name"][0])
    html = html.replace("{{USER_FIRSTNAME}}", user["name"].split(" ")[0])
    return HTMLResponse(content=html)


@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    email_normalized = email.strip()
    if email_normalized not in AUTHORIZED_USERS:
        error_block = '<div class="mb-6 p-3 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400 text-sm">Usuario no autorizado. Contacte al administrador.</div>'
        html = LOGIN_HTML.replace("{{ERROR_BLOCK}}", error_block)
        return HTMLResponse(content=html)
    if hash_password(password) != DEFAULT_PASSWORD_HASH:
        error_block = '<div class="mb-6 p-3 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400 text-sm">Contraseña incorrecta.</div>'
        html = LOGIN_HTML.replace("{{ERROR_BLOCK}}", error_block)
        return HTMLResponse(content=html)
    token = create_access_token({"sub": email_normalized})
    response = RedirectResponse(url="/", status_code=303)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=ACCESS_TOKEN_EXPIRE_HOURS * 3600,
    )
    return response


@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("access_token")
    return response


# --- API Endpoints ---
@app.get("/api/documents")
async def api_documents(request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="No autorizado")
    docs_summary = []
    for doc in DOCUMENTS:
        docs_summary.append({
            "id": doc["id"],
            "title": doc["title"],
            "category": doc["category"],
            "metadata": doc["metadata"],
            "sections": doc["sections"],
            "summary": doc["summary"][:500],
            "requirement_counts": doc["requirement_counts"],
            "risk_counts": {"total": doc["risk_counts"]["total"]},
            "word_count": doc["word_count"],
        })
    return {"documents": docs_summary, "stats": DASHBOARD_STATS}


@app.get("/api/documents/{doc_id}")
async def api_document_detail(doc_id: str, request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="No autorizado")
    for doc in DOCUMENTS:
        if doc["id"] == doc_id:
            return {
                "id": doc["id"],
                "title": doc["title"],
                "category": doc["category"],
                "metadata": doc["metadata"],
                "sections": doc["sections"],
                "summary": doc["summary"],
                "requirement_counts": doc["requirement_counts"],
                "risk_counts": doc["risk_counts"],
                "raw_content": doc["raw_content"],
                "word_count": doc["word_count"],
                "line_count": doc["line_count"],
            }
    raise HTTPException(status_code=404, detail="Documento no encontrado")


@app.get("/api/search")
async def api_search(q: str, request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="No autorizado")
    if not q or len(q) < 2:
        return {"results": [], "query": q}
    results = search_content(q, DOCUMENTS)
    return {"results": results, "query": q, "total": len(results)}


@app.get("/api/stats")
async def api_stats(request: Request):
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="No autorizado")
    return DASHBOARD_STATS


@app.get("/api/traceability")
async def api_traceability(request: Request):
    """Generate traceability matrix across documents."""
    user = get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="No autorizado")
    matrix = {}
    for doc in DOCUMENTS:
        content = doc["raw_content"]
        for prefix in ["BR", "FR", "NFR", "INT", "DR"]:
            pattern = re.compile(rf"\b({prefix}-\d{{3}})\b")
            for match in pattern.finditer(content):
                req_id = match.group(1)
                if req_id not in matrix:
                    matrix[req_id] = []
                if doc["id"] not in matrix[req_id]:
                    matrix[req_id].append(doc["id"])
    sorted_matrix = dict(sorted(matrix.items(), key=lambda x: x[0]))
    return {
        "matrix": sorted_matrix,
        "total_requirements": len(sorted_matrix),
        "documents": [{"id": d["id"], "title": d["title"]} for d in DOCUMENTS],
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
