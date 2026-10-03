# ArcKit Knowledge Base Viewer

Herramienta web moderna e intuitiva para consultar y verificar la base de conocimiento de artefactos de arquitectura del programa **Core Banking — Caja de Ahorros de Panamá**.

## Características

- **Dashboard** — Vista general con métricas: 17 artefactos, 193 requisitos, 37 riesgos, 3 RFPs coordinados
- **Visor de Documentos** — Renderizado completo de Markdown con tabla de contenido y metadata
- **Búsqueda Full-Text** — Búsqueda instantánea en todos los documentos con snippets de contexto
- **Matriz de Trazabilidad** — Mapeo de 143 requisitos (BR/FR/NFR/INT/DR) a través de los 17 artefactos
- **Autenticación** — Acceso restringido a usuarios autorizados configurados fuera del código

## Configuración de Acceso

La aplicación no incluye credenciales en el código. Antes de iniciarla:

1. **Clave de firma JWT** — defina `KB_SECRET_KEY` con un valor aleatorio de al menos 32 caracteres (la app no arranca sin ella):

   ```bash
   export KB_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
   ```

2. **Usuarios** — copie `users.example.json` a `users.json` (ignorado por git) o apunte `KB_USERS_FILE` a otra ruta. Cada usuario tiene su propio hash scrypt con sal, generado con:

   ```bash
   python passwords.py
   ```

Variables opcionales: `KB_HOST` (por defecto `127.0.0.1`), `KB_PORT` (`8000`), `KB_LOGIN_MAX_FAILURES` (`5`) y `KB_LOGIN_WINDOW_SECONDS` (`900`) para el bloqueo por intentos fallidos de inicio de sesión (por IP y por correo).

## Ejecución Local

```bash
cd kb-viewer
pip install -r requirements.txt
cp users.example.json users.json   # editar con usuarios y hashes reales
export KB_SECRET_KEY="..."
python app.py
# Abrir http://localhost:8000
```

## Artefactos Incluidos

| ID | Tipo | Descripción |
|----|------|-------------|
| ARC-001-REQ-v2.0 | Requisitos | 193 requisitos (BR/FR/NFR/INT/DR) |
| ARC-001-STKE-v1.0 | Stakeholders | 27 stakeholders, 17 drivers, 10 metas |
| ARC-001-DPIA-v1.0 | DPIA | Evaluación de impacto a la protección de datos |
| ARC-001-SOW-CBS-v1.0 | SOW CBS | RFP formal para Core Banking System |
| ARC-001-SOW-ERP-v1.0 | SOW ERP | RFP formal para ERP externo |
| ARC-001-SOW-AML-v1.0 | SOW AML | RFP formal para motor AML con IA |
| ARC-001-EVAL-v2.0 | Evaluación | Marco de evaluación multi-track (CBS+ERP+AML) |
| ARC-001-SECD-v1.0 | Seguridad | Secure by Design Assessment (NIST CSF 2.0) |
| ARC-001-SOBC-v2.0 | Business Case | SOBC Green Book — B/. 150-195M a 7 años |
| ARC-001-RISK-v2.0 | Riesgos | 37 riesgos Orange Book (6 categorías) |
| ARC-001-RSCH-v2.0 | Investigación | Research CBS+ERP+AML vendors |
| + 6 Tech Notes | Notas Técnicas | Regulación SBP, Acuerdo 1-2026, AML, etc. |

## Stack Técnico

- **Backend:** Python + FastAPI (auto-discovery de archivos .md)
- **Frontend:** Tailwind CSS + Alpine.js + Marked.js (embebido en app.py)
- **Auth:** JWT (HS256) + contraseñas por usuario con scrypt y sal, con límite de intentos de login
- **Parser:** Extracción dinámica de metadata, secciones, tablas y requisitos desde Markdown
