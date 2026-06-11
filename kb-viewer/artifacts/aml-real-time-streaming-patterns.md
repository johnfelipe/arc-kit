# Tech Note: Patrones de Streaming AML en Tiempo Real

> **Template Origin**: Official | **ArcKit Version**: 5.13.0 | **Comando**: `/arckit:research`

## Document Control

| Campo | Valor |
|-------|-------|
| Document ID | ARC-001-TECH-aml-real-time-streaming-patterns-v1.0 |
| Document Type | Tech Note |
| Project | 001-evaluacion-core-banking (Caja de Ahorros) |
| Classification | OFFICIAL-SENSITIVE |
| Status | DRAFT |
| Version | 1.0 |
| Created Date | 2026-06-11 |
| Last Updated | 2026-06-11 |
| Owner | CISO + Cumplimiento + Innovación |

---

## Summary

A partir de v2.0 de los requisitos (FR-048 REVISADO MAJOR, INT-018), el monitoreo AML/PLD será **una herramienta externa con IA y APIs en tiempo real**, NO un módulo interno del CBS. El proveedor actual de CAP sale de soporte en 2026 [DOC-SES-006, DOC-SES-009 §10.4] y la decisión está firme [DOC-RFI-001 §2.2]. El CBS debe (a) **exponer eventos transaccionales en tiempo real** al motor AML externo con latencia < 200 ms (NFR-P-005) y (b) **bloquear transacciones bajo instrucción del motor AML** antes de la liquidación. Esta nota documenta los patrones recomendados de streaming, bloqueo bidireccional, generación de ROS y auditabilidad.

## Key Findings

### Patrón Arquitectónico Recomendado

#### Patrón "Hold-and-Score" (síncrono, RECOMENDADO para servicios críticos)

1. CBS recibe transacción del canal (ATM, Yappy, ACH, ventanilla, App).
2. CBS **persiste la transacción en estado `PENDING_AML_DECISION`** (no liquida aún).
3. CBS publica el evento al motor AML vía API REST síncrona o Kafka con respuesta correlationada.
4. Motor AML evalúa con risk scoring (geolocalización, beneficiario final, lista PEP/OFAC, behavioral) en **≤ 150 ms**.
5. Motor AML devuelve decisión: `ALLOW` / `HOLD` / `BLOCK`.
6. CBS aplica la decisión:
   - `ALLOW` → liquida y notifica resultado (latencia total < 200 ms — NFR-P-005).
   - `HOLD` → mantiene en pending; notifica a Cumplimiento; workflow manual.
   - `BLOCK` → cancela transacción; notifica al cliente con razón genérica; genera evento para auditoría.
7. Si motor AML no responde en `< 200 ms` (timeout): **fail-safe por política** — para transacciones críticas, por defecto `HOLD` y revisar manual. Definir por tipo de canal y monto.

#### Patrón "Fire-and-Monitor" (asíncrono, para servicios no críticos)

- CBS liquida la transacción inmediatamente.
- En paralelo, publica el evento al motor AML.
- Motor AML evalúa; si BLOCK, dispara revertir transacción + bloquear cliente.
- Aplicable a transacciones de bajo riesgo (saldo, consulta) — no transferencias.

### Generación de ROS (FR-049)

- Motor AML genera el ROS automáticamente cuando trigger se activa.
- CBS provee los datos transaccionales y de cliente vía API REST query (no streaming).
- Motor AML envía ROS a la UAF en formato regulatorio.
- CBS persiste evidencia (DR-018 inmutable) — workflow + escalamiento + firma.

### Listas de control

- PEP, OFAC, ONU, SBP internas, listas UAF — el motor AML las mantiene actualizadas al menos diariamente (NFR-SEC-009).
- El CBS NO duplica estas listas; consulta al motor AML cuando necesite verificar (apertura de cuenta, transferencia internacional).

### Geolocalización inferencial (Acuerdo 1-2026 — FR-053)

- Canal captura signals (IP, dispositivo, GPS si disponible).
- CBS envía signals al motor AML como atributo de la transacción / del evento de apertura.
- Motor AML infiere ubicación con confidence score.
- Discrepancia con perfil del cliente → trigger HOLD.

### Beneficiario final (Acuerdo 1-2026 — FR-052)

- Apertura jurídica → CBS expone capas societarias al motor AML (vía Panadata - INT-023).
- Motor AML identifica personas con ≥ 10% control.
- Workflow de re-evaluación periódica al motor AML.

### Bloqueo bidireccional

- Motor AML puede **bloquear cliente** (no solo transacción) → CBS marca CIF como `AML_BLOCKED` → todos los canales rechazan operaciones.
- Motor AML puede **liberar cliente** → CBS revierte marca.

### Auditabilidad e Inmutabilidad

- Cada decisión AML persiste con timestamp, modelo invocado, score, decisión, motivo (DR-018 WORM).
- Retención ≥ 7 años (NFR-C-007).
- Trazabilidad del feature usado por el motor (importante para XAI — Hawk:AI).

### Cumplimiento de NFR-P-005 latencia < 200 ms

- Motor AML cloud cercano al CBS (mismo DC o región). Hawk:AI permite on-prem para minimizar latencia.
- API REST keep-alive + pooling de conexiones.
- Cache local del CBS para risk scores recientes del mismo cliente (TTL 5 min) — solo para transacciones repetitivas.

### Implementación por vendor AML

| Vendor AML | Soporte nativo "Hold-and-Score" | Latencia típica | Bloqueo bidireccional |
|------------|---------------------------------|------------------|------------------------|
| Hawk:AI | ✅ nativo, AI-native | < 100 ms en cloud-cercano | ✅ |
| NICE Actimize SAM | ✅ nativo enterprise | < 150 ms documentado | ✅ |
| Oracle FCCM | ✅ nativo | < 200 ms documentado | ✅ |
| ComplyAdvantage | ✅ API REST | variable, validar SLA | parcial — más fuerte en screening |
| SAS AML | ⚠️ legacy, real-time limitado [DOC-RSCH-v2-12] | > 500 ms reportado | ⚠️ |
| FICO Siron | ⚠️ legacy, real-time limitado [DOC-RSCH-v2-12] | > 500 ms reportado | ⚠️ |

## Relevance to Projects

- **Project 001 — Caja de Ahorros — Evaluación y Selección de Core Banking** (Panamá, 2026): pilar arquitectónico de Categoría 3 AML (FR-048, FR-049, NFR-P-005, NFR-C-002, INT-018).

## External References

| Citation ID | Source | Description |
|-------------|--------|-------------|
| DOC-RSCH-v2-10 | <https://www.peerspot.com/products/comparisons/nice-actimize-anti-money-laundering_vs_oracle-financial-crime-and-compliance-management-cloud-service> | NICE Actimize vs Oracle FCCM real-time capabilities |
| DOC-RSCH-v2-11 | <https://hawk.ai/> | Hawk AI streaming + XAI patterns |
| DOC-RSCH-v2-12 | <https://www.symphonyai.com/resources/blog/financial-services/top-10-aml-software-banks-2026/> | Crítica a SAS / FICO Siron por falta de tiempo real |
| ARC-001-REQ-v2.0 | `projects/001-evaluacion-core-banking/ARC-001-REQ-v2.0.md` | FR-048, FR-049, NFR-P-005, NFR-C-002, INT-018 |

---

**Generated by**: ArcKit `/arckit:research` agent
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros (Project 001)
**AI Model**: Claude Opus 4.7
