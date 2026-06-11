# Registro de Riesgos — Evaluación e Implementación del Core Banking

> **Marco**: HM Treasury Orange Book 2023 (5 principios, framework 4Ts, matriz inherente/residual 5×5) adaptado al contexto de banca pública panameña.

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-RISK-v2.0 |
| **Document Type** | Risk Register |
| **Project** | Evaluación Core Banking — Caja de Ahorros, Panamá |
| **Classification** | OFFICIAL-SENSITIVE |
| **Status** | DRAFT |
| **Version** | 2.0 |
| **Created Date** | 2026-05-19 |
| **Last Modified** | 2026-06-11 |
| **Review Cycle** | Semanal para riesgos Críticos/Altos; mensual para Medios/Bajos |
| **Next Review Date** | 2026-07-11 |
| **Owner** | Aldo Ríos — Gerencia de Innovación (Líder del Programa) |
| **Reviewed By** | PMO, Riesgos, Cumplimiento, Auditoría Interna (PENDING) |
| **Approved By** | Comité de Tecnología (PENDING) — Junta Directiva para riesgos sobre apetito |
| **Distribution** | Junta Directiva, Gerencia General, Comité de Tecnología, PMO, dueños de riesgo nombrados, Auditoría Interna, Contraloría (extracto, bajo solicitud) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-05-19 | ArcKit AI | Creación inicial desde `/arckit:risk` — formaliza R-1..R-7 del STKE bajo Orange Book y añade 15 riesgos nuevos derivados de requisitos (BR/FR/NFR/INT/DR) e investigación de vendors (RSCH). Cobertura: 22 riesgos. | PENDING | PENDING |
| 2.0 (corrigendum) | 2026-06-11 (PM) | ArcKit AI | **Corrigendum post-`/arckit:research`** sobre el Acuerdo SBP 1-2026 (en línea con el corrigendum aplicado simultáneamente a ARC-001-REQ-v2.0). Al verificar contra el PDF oficial de la SBP (Resolución SBP-JD-0001-2026 del 16-ene-2026): (a) **umbral de beneficiario final corregido de ≥ 25% a ≥ 10%** (Panamá adopta umbral más estricto que UE/FATF); (b) **plazos discretos por artículo en lugar de "general jul-2025 / digitales jul-2027"**: Art. 25 §1 vigencia 31-ene-2027 (nueva presión de cronograma — solo ~8 meses desde cierre planeado del RFP); Art. 14 vigencia 30-jun-2027 (beneficiario final + geolocalización inferencial digital); (c) **geolocalización inferencial** (multiple signals — IP+ASN, dispositivo/UA, GPS, comportamiento) en lugar de "geolocalización digital" genérica. Correcciones aplicadas a Revision History v2.0 entry, Resumen Ejecutivo (Hallazgos), Apetito, Top 10, R-007 (REV), R-025 (NEW — refrescado), Plan de Acción 2.7, KRIs. Sin cambios al conteo (37 riesgos) ni a la versión (sigue v2.0 — DRAFT del día). Fuente: PDF oficial SBP verificado por el sub-agente `arckit-research` y citado en `research/ARC-001-RSCH-v2.0.md` + `tech-notes/acuerdo-1-2026-implementation.md`. | PENDING | PENDING |
| 2.0 | 2026-06-11 | ArcKit AI | **Major refresh** tras las 8 sesiones presenciales (25–28 mayo 2026), la emisión del RFI v1.0 (junio 2026), la ficha de PoC v1.0 y el refresh de requisitos a ARC-001-REQ-v2.0. **15 riesgos nuevos** (R-023..R-037) emergen de: (a) la decisión de AML externo (proveedor actual sale soporte 2026), (b) la decisión de ERP externo (BR-013), (c) la entrada del **Acuerdo SBP 1-2026** (Resolución SBP-JD-0001-2026 del 16-ene-2026; Art. 25 §1 vigencia 31-ene-2027; Art. 14 — beneficiario final ≥ **10%** + geolocalización inferencial digital — vigencia 30-jun-2027), (d) las preferencias del banco por COBIS / descartes de Temenos, Finacle, Mambu, SAP, (e) el estado actual de ciberseguridad del legado (sin cifrado, sin MFA), (f) la transición Activo-Pasivo → Activo-Activo en curso, (g) la fragmentación de BPMs (Ultimus, Asicom-Finflow, Genexus), (h) el diccionario de datos heredado (8,000+ elementos), (i) la PoC de referencia estrecha (caso único hipotecario), (j) la restricción Innovación/Seguridad Nacional sobre cloud, (k) FECI 1% sobre intereses comerciales, (l) el conflicto CAPEX→OPEX (BR-014), (m) modo degradado Caja Amiga + comarcas no probado, (n) potencial pérdida de la estabilidad actual de DataPro, (o) migración crítica de SITECA. **5 riesgos revisados** (R-006 añade dimensión CAPEX/OPEX; R-007 incorpora Acuerdo 1-2026 ratificado y otras leyes nuevas; R-009 sube probabilidad por relación ya deteriorada [DOC-SES-001, DOC-SES-009 §3.3]; R-017 mantiene score pero ahora explícitamente vinculado a la herramienta AML externa; R-021 detalla sistemas satélite con nombres específicos — SITECA, BPMs, Emerix, etc.). **Cobertura: 37 riesgos** en 6 categorías. Nuevas citas DOC-SES-001..009, DOC-RFI-001, DOC-POC-001. | PENDING | PENDING |

---

## Resumen Ejecutivo

### Perfil de Riesgo

**Total de riesgos identificados:** 37 riesgos en 6 categorías Orange Book (22 de v1.0 + 15 nuevos en v2.0)

| Nivel de Riesgo | Inherente | Residual | Cambio (vs v1.0) |
|-----------------|-----------|----------|------------------|
| **Crítico** (20-25) | 1 | 0 | +1 inherente (R-024 ERP — sin ERP = cierre contable inviable) |
| **Alto** (13-19) | 12 | 1 | +5 inherente; +1 residual (R-024 baja a 12 residual) |
| **Medio** (6-12) | 23 | 28 | +8 inherente; +12 residual |
| **Bajo** (1-5) | 1 | 8 | +1 inherente; +2 residual |
| **TOTAL** | 37 | 37 | +15 (v1.0 → v2.0) |

### Distribución por Categoría

| Categoría | # Riesgos | Inherente promedio | Residual promedio | Efectividad de Controles |
|-----------|-----------|--------------------|--------------------|--------------------------|
| **STRATEGIC** | 4 | 13.8 | 7.8 | 43% reducción |
| **OPERATIONAL** | 7 | 12.0 | 6.4 | 47% reducción |
| **FINANCIAL** | 4 | 12.0 | 5.5 | 54% reducción |
| **COMPLIANCE** | 7 | 13.0 | 6.0 | 54% reducción |
| **REPUTATIONAL** | 1 | 12.0 | 6.0 | 50% reducción |
| **TECHNOLOGY** | 14 | 13.4 | 7.1 | 47% reducción |

### Evaluación General

- **Puntaje de riesgo residual total:** 252 / 925 posibles (6.8 puntos promedio por riesgo).
- **Reducción por controles:** 51% (de 487 inherente a 252 residual).
- **Perfil de riesgo:** ⚠️ **Concerning** — un riesgo residual Alto (R-024 ERP) requiere atención inmediata; el resto en zona Medio/Bajo está bajo control con mitigaciones propuestas.
- **Riesgos críticos inherentes:** R-024 (ERP no listo al go-live del CBS → cierre contable inviable) — score 20 inherente. Con mitigación (selección paralela ERP iniciada ahora, contrato con paralelo) baja a 12 residual.

### Riesgos que exceden el apetito organizacional

| Risk ID | Título | Categoría | Score residual | Apetito | Exceso | Escalamiento |
|---------|--------|-----------|----------------|---------|--------|---------------|
| R-024 (NEW) | ERP externo no listo al go-live del CBS | TECHNOLOGY | 12 | ≤ 6 | +6 | JD inmediato — bloqueante para cronograma |
| R-008 | Vendor lock-in con nuevo proveedor | STRATEGIC | 9 | ≤ 6 | +3 | Comité de Tecnología |
| R-023 (NEW) | AML externo no listo al go-live del CBS | COMPLIANCE | 9 | ≤ 6 | +3 | Cumplimiento + Comité de Tecnología |
| R-026 (NEW) | Sesgo COBIS / descarte preconcebido vendors | COMPLIANCE | 9 | ≤ 6 | +3 | Contraloría — riesgo de impugnación |
| R-013 | Falla integración Yappy / ACH / Telered | TECHNOLOGY | 8 | ≤ 6 | +2 | Aldo Ríos → Gerencia General |
| R-014 | Cambio político / cambio de gobierno | STRATEGIC | 8 | ≤ 6 | +2 | JD (informativo) |
| R-017 | Brecha de ciberseguridad durante migración | TECHNOLOGY | 8 | ≤ 6 | +2 | CISO → Comité de Tecnología |
| R-004 | Indisponibilidad pública de canales | OPERATIONAL | 8 | ≤ 6 | +2 | Operaciones → Gerencia General |
| R-027 (NEW) | Brecha actual del legado (sin cifrado/MFA) | TECHNOLOGY | 8 | ≤ 6 | +2 | CISO → Comité de Tecnología |
| R-025 (NEW) | Incumplimiento Acuerdo 1-2026 (Art. 14 vigencia 30-jun-2027) | COMPLIANCE | 8 | ≤ 6 | +2 | Cumplimiento → JD |
| R-029 (NEW) | Múltiples BPMs no estandarizados | TECHNOLOGY | 8 | ≤ 6 | +2 | TI — Lead técnico |
| R-031 (NEW) | PoC estrecha (caso único hipotecario) | OPERATIONAL | 8 | ≤ 6 | +2 | Aldo Ríos + Negocio |

### Top 5 Riesgos que requieren atención inmediata (por score residual)

1. **R-024 (NEW)** (TECHNOLOGY, Alto 12): ERP externo no listo al go-live del CBS → cierre contable inviable — Owner: Finanzas + TI — Status: Open
2. **R-008** (STRATEGIC, Medio 9): Vendor lock-in con nuevo proveedor — Owner: Comité de Tecnología — Status: Open
3. **R-023 (NEW)** (COMPLIANCE, Medio 9): AML externo no listo al go-live → ROS a UAF interrumpidos — Owner: Cumplimiento — Status: Open
4. **R-026 (NEW)** (COMPLIANCE, Medio 9): Sesgo del banco hacia COBIS / descarte preconcebido viable como impugnación de Contraloría — Owner: Legal + Aldo Ríos — Status: Open
5. **R-004 / R-013 / R-014 / R-017 / R-025 / R-027 / R-029 / R-031** (Medio 8 cada uno): cluster de riesgos con score residual 8 — atender por bloque.

### Hallazgos clave y recomendaciones

**Hallazgos v2.0:**

- **El nuevo ERP es la dependencia crítica de cronograma:** el CBS NO incluye GL completo (BR-013 REQ v2.0). La selección y go-live del ERP en paralelo al CBS es ahora la dependencia crítica más importante. Si el ERP se retrasa, el CBS no puede ir a producción. **Bloqueante.**
- **El AML externo es la segunda dependencia crítica:** el proveedor actual deja de dar soporte en 2026; el go-live del nuevo motor AML con IA debe alinearse con el del CBS. Gap operativo en monitoreo AML expone al banco a sanciones UAF y SBP.
- **Acuerdo 1-2026 introduce cláusula eliminatoria de proceso:** Resolución SBP-JD-0001-2026 del 16-ene-2026 con plazos discretos por artículo — **Art. 25 §1 vigencia 31-ene-2027** (regla específica de identificación) y **Art. 14 vigencia 30-jun-2027** (beneficiario final ≥ **10%** + geolocalización inferencial digital). El CBS DEBE entregar geolocalización inferencial, beneficiario final ≥ 10% y soporte operacional para las multas elevadas antes de jun-2027 o el banco queda en falta. *(Corrigendum: el umbral correcto es 10% — no 25% como aparecía inicialmente; Panamá adopta umbral más estricto que UE/FATF.)*
- **Preferencias del banco por COBIS introducen riesgo de proceso:** el equipo del banco expresó explícitamente preferencia por COBIS y descarte de Temenos, Finacle, Mambu, SAP [DOC-SES-009 §3.4, §10.4]. La Contraloría puede impugnar el RFP si estas preferencias no se gestionan con criterios objetivos auditables.
- **El estado actual del legado es brecha de seguridad activa:** sin cifrado en reposo, sin cifrado en tránsito interno, sin MFA, recertificación manual 2 veces/año [DOC-SES-007 §8.1]. La ventana de migración expone al banco a un ataque sobre el sistema vulnerable durante la transición.
- **Concentración técnica en TI/CISO se mantiene:** 14 de 37 riesgos (38%) son TECHNOLOGY con dueños TI o CISO — el riesgo de pérdida de talento (R-001) sigue siendo crítico.
- **Riesgos políticos y reputacionales se mantienen contenidos:** R-014, R-022, R-016 (AAA-pan) tienen impacto Alto/Crítico pero baja probabilidad si la gobernanza opera.
- **Sistema satélite SITECA es el más crítico** entre los identificados (origina la cartera hipotecaria de ~B/. 3,000M); su migración debe planificarse con cuidado especial.

**Recomendaciones v2.0 (prioritarias):**

1. **URGENTE (esta semana):** iniciar el proceso de selección del **ERP externo** en paralelo al RFP del CBS (mitigación R-024). El ERP es bloqueante de cronograma.
2. **URGENTE (esta semana):** iniciar el proceso de selección de la nueva **herramienta AML externa con IA y APIs** (mitigación R-023). El proveedor actual sale soporte en 2026.
3. **URGENTE (esta semana):** **dictamen Legal previo de proceso RFP** que documente cómo las preferencias del banco se traducen en criterios objetivos auditables (mitigación R-026). Sin esto la Contraloría puede impugnar.
4. **Próximas 4 semanas:** **plan de remediación de seguridad del legado** antes de la migración — cifrado en reposo, MFA obligatorio, recertificación automática (mitigación R-027). No esperar al nuevo CBS.
5. **Próximas 4 semanas:** **consulta formal a la Autoridad de Innovación + SBP + Seguridad Nacional** sobre viabilidad de cloud para el CBS (mitigación R-032). Sin respuesta, el modelo de despliegue queda paralizado.
6. **Próximos 8 semanas:** ampliar la **PoC** con al menos 2 casos adicionales — captación masiva con sub-cuentas (FR-007), créditos sindicados con CAP como coordinador (FR-026), factoring con pagador estatal (FR-040) (mitigación R-031). PoC actual no representa la complejidad operativa del banco.
7. **Próximos 8 semanas:** finalizar la **transición Activo-Activo** ANTES del go-live del nuevo CBS (mitigación R-028). No hacer dos cambios topológicos simultáneos.
8. **Próximos 12 semanas:** **gobernanza del diccionario de datos** — asignar propietarios a los 8,000+ elementos, definir reglas de calidad, documentar transformaciones (mitigación R-030). Insumo crítico para migración (BR-008).
9. **Mantener vigentes** todas las recomendaciones v1.0: dictamen soberanía pre-RFP (R-006/R-018), retención de talento (R-001), cláusulas eliminatorias del RFP, contrato extendido con incumbente (R-009), pen-test pre-migración (R-017), war-room (R-004/R-022).

---

## A. Visualización de la Matriz de Riesgo

### Matriz de Riesgo Inherente (Antes de Controles) — v2.0

```text
                                    IMPACTO
              1-Mínimo    2-Menor    3-Moderado   4-Mayor    5-Crítico
           ┌───────────┬───────────┬───────────┬───────────┬───────────┐
5-Casi     │           │           │           │           │  R-024    │
Cierto     │    5      │    10     │    15     │    20     │  ← 25     │
           ├───────────┼───────────┼───────────┼───────────┼───────────┤
4-Probable │           │           │  R-007    │  R-008    │  R-026    │
           │           │           │  R-019    │  R-011    │           │
           │           │           │  R-021    │  R-018    │           │
           │           │           │  R-029    │  R-023    │           │
           │           │           │  R-030    │  R-025    │           │
           │    4      │    8      │    12     │    16     │    20     │
L          ├───────────┼───────────┼───────────┼───────────┼───────────┤
I 3-Posible│           │           │  R-001    │  R-005    │  R-002    │
K          │           │           │  R-003    │  R-009    │  R-004    │
E          │           │  R-010    │  R-014    │  R-017    │  R-013    │
L          │           │  R-020    │  R-022    │  R-027    │  R-035    │
I          │           │  R-036    │  R-028    │  R-034    │           │
H          │    3      │    6      │    9      │    12     │    15     │
O          ├───────────┼───────────┼───────────┼───────────┼───────────┤
O 2-Improb.│           │           │  R-033    │  R-006    │  R-012    │
D          │           │  R-031    │           │  R-037    │  R-015    │
           │           │           │           │           │  R-016    │
           │    2      │    4      │    6      │    8      │    10     │
           ├───────────┼───────────┼───────────┼───────────┼───────────┤
  1-Raro   │           │           │  R-032    │           │           │
           │    1      │    2      │    3      │    4      │    5      │
           └───────────┴───────────┴───────────┴───────────┴───────────┘

Leyenda: 🟥 Crítico (20-25)  🟧 Alto (13-19)  🟨 Medio (6-12)  🟩 Bajo (1-5)
```

**Zonas de riesgo (inherente) v2.0:**

- **Crítico (20-25):** **R-024** (NEW — ERP no listo = cierre contable inviable) — 1 riesgo.
- **Alto (13-19):** R-002, R-004, R-008, R-011, R-013, R-017, R-018, R-023, R-025, R-026, R-027, R-035 — 12 riesgos requieren plan de mitigación obligatorio.
- **Medio (6-12):** R-001, R-003, R-005, R-006, R-007, R-009, R-010, R-012, R-014, R-015, R-016, R-019, R-020, R-021, R-022, R-028, R-029, R-030, R-033, R-034, R-036, R-037 — 22 riesgos bajo monitoreo de gerencia.
- **Bajo (1-5):** R-031, R-032 — 2 riesgos identificados con probabilidad baja a moderada.

### Matriz de Riesgo Residual (Después de Controles) — v2.0

```text
                                    IMPACTO
              1-Mínimo    2-Menor    3-Moderado   4-Mayor    5-Crítico
           ┌───────────┬───────────┬───────────┬───────────┬───────────┐
5-Casi     │           │           │           │           │           │
Cierto     │    5      │    10     │    15     │    20     │    25     │
           ├───────────┼───────────┼───────────┼───────────┼───────────┤
4-Probable │           │           │  R-024    │           │           │
           │           │           │           │           │           │
           │    4      │    8      │    12     │    16     │    20     │
L          ├───────────┼───────────┼───────────┼───────────┼───────────┤
I 3-Posible│           │  R-007    │  R-008    │           │           │
K          │           │  R-019    │  R-023    │           │           │
E          │           │  R-029    │  R-026    │           │           │
L          │    3      │    6      │    9      │    12     │    15     │
I          ├───────────┼───────────┼───────────┼───────────┼───────────┤
H 2-Improb.│           │  R-001    │  R-004    │           │           │
O          │           │  R-002    │  R-013    │           │           │
O          │           │  R-003    │  R-014    │           │           │
D          │           │  R-005    │  R-017    │           │           │
           │           │  R-009    │  R-025    │           │           │
           │           │  R-011    │  R-027    │           │           │
           │           │  R-018    │  R-028    │           │           │
           │           │  R-021    │  R-031    │           │           │
           │           │  R-022    │  R-034    │           │           │
           │           │  R-030    │  R-035    │           │           │
           │           │  R-033    │           │           │           │
           │           │  R-037    │           │           │           │
           │    2      │    4      │    6      │    8      │    10     │
           ├───────────┼───────────┼───────────┼───────────┼───────────┤
  1-Raro   │           │           │  R-010    │  R-006    │           │
           │           │           │  R-020    │  R-012    │           │
           │           │           │  R-036    │  R-015    │           │
           │           │  R-032    │           │  R-016    │           │
           │    1      │    2      │    3      │    4      │    5      │
           └───────────┴───────────┴───────────┴───────────┴───────────┘

Leyenda: 🟥 Crítico (20-25)  🟧 Alto (13-19)  🟨 Medio (6-12)  🟩 Bajo (1-5)
```

**Análisis de movimiento v2.0:**

- **R-024 (NEW) sigue Alto residual (12)** — mejor caso con mitigaciones agresivas (proyecto paralelo, contrato con paralelo de 90 días con DataPro como contingencia). **No baja más; requiere atención permanente del Steering Committee.**
- **R-026 (NEW) baja Crítico→Medio (16→9)** con dictamen Legal previo del proceso RFP y matriz de ponderación auditable.
- **R-023 (NEW) baja Alto→Medio (16→9)** con selección paralela del motor AML y contrato puente con proveedor actual.
- **Riesgos v1.0 preservan movimiento previo** (R-008 16→9, R-011 16→6, R-018 16→6, R-002 15→6, R-004 15→8, R-013 15→8, R-017 15→8 — 50% reducción promedio).
- **Riesgos v2.0 nuevos en zona Media inherente bajan a Baja residual con controles:** R-028 (9→6), R-030 (12→4), R-031 (4→6 — sube ligeramente al ampliar el alcance), R-032 (3→2), R-034 (12→6), R-035 (15→6 con plan offline probado), R-036 (6→3), R-037 (8→4).

---

## B. Top 10 Riesgos v2.0 (Por score residual y materialidad)

| # | ID | Título | Categoría | Inherente | Residual | Owner | Status | 4T |
|---|----|--------|-----------|-----------|----------|-------|--------|-----|
| 1 | **R-024 (NEW)** | ERP externo no listo al go-live del CBS | TECHNOLOGY | 25 | 12 | Finanzas + TI + Aldo Ríos | Open | Treat |
| 2 | **R-026 (NEW)** | Sesgo COBIS / descarte preconcebido vendors → impugnación Contraloría | COMPLIANCE | 16 | 9 | Legal + Aldo Ríos | Open | Treat |
| 3 | **R-023 (NEW)** | AML externo no listo al go-live → ROS UAF interrumpidos | COMPLIANCE | 16 | 9 | Cumplimiento | Open | Treat |
| 4 | R-008 | Vendor lock-in con nuevo proveedor | STRATEGIC | 16 | 9 | Comité de Tecnología | Open | Treat |
| 5 | R-004 | Indisponibilidad pública de canales digitales | OPERATIONAL | 15 | 8 | Operaciones | Open | Treat |
| 6 | R-013 | Falla integración Yappy / ACH / Telered | TECHNOLOGY | 15 | 8 | TI — Lead Técnico | Open | Treat |
| 7 | R-014 | Cambio político / cambio de gobierno | STRATEGIC | 12 | 8 | Junta Directiva | Open | Tolerate |
| 8 | R-017 | Brecha ciberseguridad durante migración | TECHNOLOGY | 15 | 8 | CISO | Open | Treat |
| 9 | **R-025 (NEW)** | Incumplimiento Acuerdo 1-2026 (Art. 14 vigencia 30-jun-2027) | COMPLIANCE | 16 | 8 | Cumplimiento | Open | Treat |
| 10 | **R-027 (NEW)** | Brecha de ciberseguridad del legado (sin cifrado/MFA actual) | TECHNOLOGY | 12 | 8 | CISO | Open | Treat |

---

## C. Registro Detallado de Riesgos

### Riesgos v1.0 (R-001..R-022) — Preservados sin cambios funcionales

> Los riesgos R-001 a R-022 se mantienen tal como fueron documentados en ARC-001-RISK-v1.0.md (Sección C). El detalle completo (descripción, causa raíz, consecuencias, controles, mitigaciones, plan de acción, fechas) está disponible en v1.0. Esta sección los lista por título con las **revisiones aplicadas en v2.0** marcadas explícitamente.

| ID | Título | Inherente | Residual | Owner | 4T | Cambios v2.0 |
|----|--------|-----------|----------|-------|-----|--------------|
| R-001 | Pérdida de talento clave de TI durante el proyecto | 12 | 6 | RRHH + Aldo Ríos | Treat | Sin cambios |
| R-002 | Observación de Contraloría sobre proceso de contratación | 15 | 6 | Legal + Finanzas | Treat | Sin cambios |
| R-003 | Diferencia significativa en provisiones contra legacy | 12 | 6 | Riesgos + Cumplimiento | Treat | Sin cambios |
| R-004 | Indisponibilidad pública de canales digitales durante migración | 15 | 8 | Operaciones | Treat | Sin cambios |
| R-005 | Vendor finalista no soporta productos sociales del mandato del Estado | 12 | 6 | Aldo Ríos + Negocio | Treat | Sin cambios |
| **R-006 (REV)** | Disputa entre cloud público y soberanía de datos post-RFP | 8 | 4 | Legal + CISO | Treat | **Añadida dimensión CAPEX→OPEX**: la transición a OPEX (BR-014 REQ v2.0) refuerza la presión hacia cloud; mitigación incluye explorar cloud regional con presencia panameña o contrato de suscripción on-premise con costos OPEX-like. |
| **R-007 (REV)** | Cambios regulatorios SBP durante el proyecto | 12 | 6 | Cumplimiento | Treat | **Acuerdo 1-2026 ya ratificado** (Resolución SBP-JD-0001-2026 del 16-ene-2026); plazos discretos: Art. 25 §1 vigencia 31-ene-2027; Art. 14 (beneficiario final ≥ **10%** + geolocalización inferencial digital) vigencia 30-jun-2027 [DOC-RFI-001 §2.1, DOC-SES-006; PDF oficial SBP]. Se añaden Ley 23/2015 (DJTE), Ley 468/2025 (Interés Preferencial), Ley 52/2000 (cheques), NIIF 16, IAS 21 a los Acuerdos vigentes. Probabilidad inherente sin cambio; mitigación incluye monitoreo de la entrada en vigor escalonada del Acuerdo 1-2026 y cláusula contractual NFR-C-010 (cumplimiento regulatorio continuo). |
| R-008 | Vendor lock-in con nuevo proveedor | 16 | 9 | Comité de Tecnología | Treat | Sin cambios |
| **R-009 (REV)** | Datapro/Vencora reduce soporte transicional al incumbente | 9 | 4 | Aldo Ríos + Legal | Treat | **Probabilidad sube de Posible a Probable** porque la relación con DataPro ya está deteriorada [DOC-SES-001, DOC-SES-009 §3.3 — "Relación deteriorada con DataPro: cotizaciones lentas, asignación de recursos lenta, costo excesivo"]. Inherente 12 → 12 (impacto sin cambio, probabilidad realista). Residual 4 → 6 con contrato extendido firmado pronto. |
| R-010 | Riesgo cambiario e inflación en licenciamiento USD | 6 | 3 | Finanzas | Tolerate | Sin cambios |
| R-011 | Sobrecosto contractual / true-ups no controlados | 16 | 6 | Finanzas | Treat | Sin cambios — los costos del ERP externo y del motor AML externo se incorporan en el cálculo de TCO; se aplican las mismas cláusulas. |
| R-012 | Pérdida de datos o corrupción contable en migración | 10 | 4 | TI + Auditoría Interna | Treat | Sin cambios |
| R-013 | Falla integración Yappy / ACH / Telered | 15 | 8 | TI — Lead Técnico | Treat | Sin cambios |
| R-014 | Cambio político / cambio de gobierno | 12 | 8 | JD | Tolerate | Sin cambios |
| R-015 | Sanción SBP por interrupción de reportería regulatoria | 10 | 4 | Cumplimiento | Treat | Sin cambios |
| R-016 | Pérdida de calificación AAA(pan) | 10 | 4 | JD + Finanzas | Treat | Sin cambios |
| **R-017 (REV)** | Brecha de ciberseguridad durante ventana de migración | 15 | 8 | CISO | Treat | **Refinamiento de alcance**: explícitamente vinculado a la herramienta AML externa (nueva dependencia para detección en tiempo real); ampliado a la transición a Activo-Activo (R-028) y al estado actual del legado (R-027). |
| R-018 | Retraso en dictamen legal de soberanía bloquea el RFP | 16 | 6 | Legal | Treat | Sin cambios |
| R-019 | Resistencia interna al cambio (TI, Negocio, Operaciones) | 12 | 6 | RRHH + Aldo Ríos | Treat | Sin cambios |
| R-020 | Vendor no cumple SLA de soporte 24/7 en español | 6 | 3 | Aldo Ríos + Compras | Treat | Sin cambios |
| **R-021 (REV)** | Sistemas satélite no consolidan al nuevo Core | 12 | 4 | TI | Treat | **Inventario explícito de sistemas satélite** [DOC-SES-001, DOC-SES-009 §3.2]: SITECA (originación hipotecaria), BPMs Ultimus / Asicom-Finflow / Genexus, Emerix (cobros), Átomos (BI regulatorio), Talentía (RRHH SaaS), BCG (SWIFT), Banca Seguro (broker), Profimype, sistemas hipotecarios auxiliares, hojas Access/Excel. Los riesgos más específicos se separan en R-029 (BPMs), R-030 (diccionario), R-037 (SITECA). |
| R-022 | Cobertura mediática negativa o impugnación parlamentaria | 9 | 4 | Comunicaciones + JD | Treat | Sin cambios |

### Riesgos v2.0 (R-023..R-037) — Nuevos

#### R-023 (NEW): Retraso en selección/implementación del motor AML externo

- **Categoría**: COMPLIANCE
- **Descripción**: El proveedor actual de monitoreo AML/PLD del banco **deja de dar soporte en 2026** [DOC-SES-006, DOC-SES-009 §10.3]. El nuevo monitoreo será una herramienta externa con IA e integración por API en tiempo real [DOC-RFI-001 §2.2, FR-048]. Si la selección, contratación e implementación del nuevo motor AML no se completa antes del go-live del CBS, el banco queda sin monitoreo AML en producción — incumple obligación de reportar ROS a la UAF en tiempo real (NFR-C-002), expone a sanción SBP por incumplimiento del Acuerdo 1-2026 y crea responsabilidad personal para directores firmantes de ROS.
- **Causa raíz**: Decisión arquitectónica de externalizar AML (cambio v2.0); proveedor actual saliendo de soporte; selección del nuevo proveedor aún no iniciada.
- **Eventos detonantes**: Fecha de fin de soporte del proveedor actual; reasignación de inversión al CBS posterga la decisión AML; vendor del CBS sugiere su propio módulo (no se acepta — cambio v2.0).
- **Consecuencias**: incumplimiento UAF; multas Acuerdo 1-2026 (elevadas — DOC-SES-006); sanción SBP; reputación.
- **Stakeholders afectados**: Cumplimiento (SD-7), UAF (SD-16), SBP (SD-9), JD (SD-1).
- **Vinculación con objetivos**: G-1 (cumplimiento regulatorio nativo), G-7.
- **Inherente**: L=4 (Probable — sin acción inmediata, alta probabilidad de quedar sin AML); I=4 (Mayor — incumplimiento regulatorio crítico). **Score = 16 (Alto)**.
- **Controles actuales**: ninguno — decisión recién tomada en v2.0.
- **Mitigaciones**: (a) iniciar proceso de selección del motor AML externo **esta semana** en paralelo al RFP del CBS; (b) negociar contrato puente con el proveedor actual hasta 12 meses post-decisión; (c) acordar criterios eliminatorios para el motor AML (IA, APIs en tiempo real, ROS automatizado, integración con Panadata, certificación regulatoria); (d) integrar el go-live AML al cronograma maestro del CBS como dependencia crítica.
- **Residual**: L=3 (Posible — con mitigaciones); I=3 (Moderado — gap operativo limitado). **Score = 9 (Medio)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Cumplimiento (Accountable) + Aldo Ríos (Responsible).
- **Acciones**: definir RFI AML (2 semanas), short-list (4 semanas), POC AML (8 semanas), contrato (12 semanas), implementación (24 semanas) — go-live antes que el CBS.
- **Status**: Open.
- **Apetito**: Excede (+3); escalar a Comité de Tecnología.

#### R-024 (NEW): ERP externo no listo al go-live del CBS — cierre contable inviable

- **Categoría**: TECHNOLOGY (con consecuencia FINANCIAL/COMPLIANCE)
- **Descripción**: El nuevo CBS NO incluye GL completo [DOC-RFI-001 §3.9, DOC-SES-005, DOC-SES-009 §6.3]. La transición a un nuevo CBS **obliga a adquirir un ERP externo** para gestionar el Libro Mayor (GL) consolidado (BR-013). Si el ERP no está implementado y operativo al go-live del CBS, el banco no podrá generar estados financieros consolidados, rentabilidad por sucursal, reportería SBP/SEI ni cierres contables — equivalente a quiebra operacional.
- **Causa raíz**: Decisión arquitectónica de separar GL en ERP externo (cambio v2.0); selección de ERP es un proyecto paralelo aún no iniciado; los ERPs financieros bancarios son complejos y su implementación toma 12–18 meses típicamente.
- **Eventos detonantes**: Retraso en selección del ERP; complejidad técnica subestimada; falta de integración con el plan de cuentas SBP; conflictos de cronograma entre CBS y ERP.
- **Consecuencias**: cierre contable inviable; incumplimiento NIIF + adaptaciones SBP (NFR-C-005); incumplimiento de reportes regulatorios mensuales (54+ — FR-056); sanción SBP severa; afectación de calificación AAA(pan); responsabilidad de la JD.
- **Stakeholders afectados**: Finanzas (SD-4), TI (SD-5), Riesgos (SD-14), Cumplimiento (SD-7), SBP (SD-9), Auditoría Interna, JD.
- **Vinculación con objetivos**: G-1, G-2, G-6, G-9.
- **Inherente**: L=5 (Casi cierto — sin acción inmediata, la ventana de selección/implementación es insuficiente); I=5 (Crítico — quiebra operacional). **Score = 25 (Crítico)**.
- **Controles actuales**: ninguno — decisión recién tomada en v2.0.
- **Mitigaciones**: (a) iniciar RFI ERP **esta semana** en paralelo al RFP CBS — selección y contratación en 12 semanas; (b) negociar contrato CBS con cláusula de **paralelo de GL** durante 90 días post go-live (con DataPro como contingencia mientras el ERP estabiliza); (c) considerar opciones de ERP que tienen plantilla pre-configurada con plan de cuentas SBP (acelera implementación); (d) coordinación semanal Steering Committee CBS + ERP; (e) plan de migración del GL con corrida paralela ≥ 3 meses pre-corte.
- **Residual**: L=4 (Probable — el cronograma sigue ajustado incluso con mitigaciones); I=3 (Moderado — con paralelo y contingencia, impacto contenido). **Score = 12 (Alto)**. **No baja más sin reducir el alcance del programa.**
- **Respuesta 4T**: **Treat** (con monitoreo permanente del Steering Committee).
- **Owner**: Finanzas (Accountable) + TI (Responsible) + Aldo Ríos.
- **Acciones**: RFI ERP (2 sem), short-list (4 sem), POC + selección (8 sem), contrato (12 sem), implementación (52 sem), corrida paralela (12 sem pre-corte), go-live (alineado al CBS).
- **Status**: Open — **bloqueante del cronograma maestro**.
- **Apetito**: Excede severamente (+6); **escalar a JD inmediatamente**.

#### R-025 (NEW): Incumplimiento Acuerdo 1-2026 — Art. 25 §1 vigencia 31-ene-2027 + Art. 14 vigencia 30-jun-2027

- **Categoría**: COMPLIANCE
- **Descripción**: El **Acuerdo SBP 1-2026** (Resolución SBP-JD-0001-2026 del 16-ene-2026) introduce **multas elevadas**, requisitos de **geolocalización inferencial** para clientes digitales (FR-053), **beneficiario final ≥ 10%** para personas jurídicas (FR-052 — umbral panameño más estricto que el 25% UE/FATF) y gestión integrada del expediente único digital. Plazos discretos por artículo: **Art. 25 §1 vigencia 31-ene-2027** (regla específica de identificación); **Art. 14 vigencia 30-jun-2027** (beneficiario final + geolocalización inferencial digital) [DOC-RFI-001 §2.1, DOC-SES-006; PDF oficial SBP]. Si el nuevo CBS no está en producción con estas capacidades antes de jun-2027 o el CBS legado no se adapta, el banco queda en falta con multas significativas y posibles restricciones operativas.
- **Causa raíz**: Cronograma del proyecto Core ajustado (~24 meses); el plazo de Art. 25 §1 (ene-2027) es especialmente ajustado — quedan menos de 8 meses entre el cierre planeado del RFP y la vigencia; riesgo de retraso del proyecto deja al banco sin margen para jun-2027.
- **Eventos detonantes**: Cualquier retraso del proyecto Core; descubrimiento de gap en capacidades del vendor seleccionado; cambios adicionales del Acuerdo durante el proyecto.
- **Consecuencias**: Multas SBP elevadas; restricciones operativas potenciales; observación de Contraloría; cobertura mediática.
- **Stakeholders afectados**: Cumplimiento (SD-7), Operaciones (SD-8), JD (SD-1), SBP (SD-9), CISO (SD-6), Asamblea Nacional (SD-17).
- **Vinculación con objetivos**: G-1, O-1 (cero hallazgos críticos en inspecciones SBP).
- **Inherente**: L=4 (Probable — proyectos de esta escala suelen retrasarse); I=4 (Mayor — multas + reputación + restricciones). **Score = 16 (Alto)**.
- **Controles actuales**: Acuerdo 1-2026 ya incluido como criterio eliminatorio en el RFI [DOC-RFI-001 §2.1, §2.3, §3.10]; FR-052 (beneficiario final ≥ 10%) y FR-053 (geolocalización inferencial) en REQ v2.0.
- **Mitigaciones**: (a) cronograma del CBS con **margen ≥ 6 meses antes de 30-jun-2027** (Art. 14) y plan de cumplimiento parcial pre-31-ene-2027 (Art. 25 §1); (b) **plan de remediación intermedio en el CBS legado** para cumplir Art. 25 §1 al 31-ene-2027 antes del go-live del nuevo CBS — incluye geolocalización inferencial al menos para nuevos clientes digitales; (c) confirmación en PoC (DOC-POC-001) de capacidades de geolocalización inferencial y beneficiario final ≥ 10% del vendor finalista; (d) monitoreo mensual por Cumplimiento de avance del proyecto vs ambos hitos (ene-2027 y jun-2027).
- **Residual**: L=2 (Improbable — con monitoreo activo y plan de remediación del legado); I=4 (Mayor — el impacto regulatorio no se reduce). **Score = 8 (Medio)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Cumplimiento (Accountable) + Aldo Ríos.
- **Acciones**: plan de remediación legado para Art. 25 §1 (3 meses — debe estar antes de oct-2026 para preparar ene-2027); validación FR-052/FR-053 en PoC (4 meses); ajuste del cronograma del CBS con doble buffer (inmediato).
- **Status**: Open.
- **Apetito**: Excede (+2); escalar a JD.

#### R-026 (NEW): Sesgo del banco hacia COBIS / descarte preconcebido de vendors → impugnación de Contraloría

- **Categoría**: COMPLIANCE (riesgo de proceso de procurement)
- **Descripción**: En las sesiones presenciales el equipo del banco expresó **preferencia explícita por COBIS** (experiencia regional positiva, mencionado en sesión de Arquitectura y de Estrategia [DOC-SES-001, DOC-SES-003, DOC-SES-009 §3.4, §10.4]) y **descarte explícito de Temenos, Finacle, Mambu, SAP**. Si estas preferencias se trasladan al proceso RFP sin estar respaldadas por criterios objetivos auditables, la **Contraloría puede impugnar el proceso** por favoritismo y violación de Ley 22 de Contrataciones Públicas. Adicionalmente, los vendors descartados podrían cuestionar el proceso si no son invitados al RFP.
- **Causa raíz**: Experiencia previa de equipos del banco; cultura de selección consultiva; ausencia de criterios objetivos documentados al momento de las sesiones presenciales.
- **Eventos detonantes**: Diseño del RFP que incluye criterios que sólo COBIS cumple; exclusión de vendors descartados sin justificación documentada; preguntas parlamentarias o queja de vendor.
- **Consecuencias**: Impugnación de Contraloría → suspensión del proceso → retraso ≥ 6–12 meses; observación pública; cuestionamiento ante Asamblea Nacional; potencial pérdida de credibilidad de la JD; necesidad de re-RFP con costo adicional.
- **Stakeholders afectados**: Contraloría (SD-10), Legal, JD (SD-1), Aldo Ríos (SD-3), vendors (externos).
- **Vinculación con objetivos**: G-8 (contratación pública sin observaciones).
- **Inherente**: L=4 (Probable — sin gestión activa, las preferencias del equipo se filtran a los criterios); I=4 (Mayor — retraso del proceso es muy costoso). **Score = 16 (Alto)**.
- **Controles actuales**: análisis de stakeholders (STKE) identifica la preferencia; aclaración en REQ v2.0 (sección "Aclaraciones") que las preferencias alimentan la matriz de ponderación pero no son eliminatorias.
- **Mitigaciones**: (a) **dictamen Legal previo del proceso RFP** que documente cómo las preferencias se traducen en criterios objetivos auditables; (b) matriz de ponderación documentada y validada por Auditoría Interna + Contraloría antes del envío del RFP; (c) inclusión de **todos** los vendors descartados en el RFI (ya hecho — el RFI v1.0 es abierto); (d) revisión independiente del RFP por un consultor externo (GFT/SIA Partners); (e) documentación detallada de cada criterio con respaldo regulatorio, operativo o financiero.
- **Residual**: L=3 (Posible — con dictamen y matriz, riesgo controlado pero no eliminado); I=3 (Moderado — impugnación posible pero defendible). **Score = 9 (Medio)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Legal (Accountable) + Aldo Ríos (Responsible).
- **Acciones**: dictamen previo del proceso RFP (4 semanas); matriz de ponderación documentada (6 semanas); validación con Contraloría informalmente (6 semanas).
- **Status**: Open.
- **Apetito**: Excede (+3); escalar a Comité de Tecnología y a Contraloría informativamente.

#### R-027 (NEW): Brecha de ciberseguridad del legado (sin cifrado, sin MFA) durante toda la vida del proyecto

- **Categoría**: TECHNOLOGY
- **Descripción**: El estado actual del legado [DOC-SES-007 §8.1] revela brechas críticas: **sin cifrado de datos en reposo**, **sin MFA**, **sin cifrado interno en tránsito**, autenticación usuario+contraseña simple, recertificación manual 2 veces/año, IBS configurado sin gestión de roles. Estas brechas son explotables durante **toda la vida del proyecto** (2+ años), no sólo durante la ventana de migración (R-017). Un incidente sobre el legado durante el proyecto invalida la calificación AAA(pan), expone al banco a sanción SBP y materializa el riesgo R-016 (calificación) y R-022 (mediático).
- **Causa raíz**: Deuda técnica acumulada en el legado; foco del programa en el reemplazo (no en remediar lo actual); proyecto de IAM en curso pero parcial.
- **Eventos detonantes**: Ataque externo (ransomware, fraude); insider threat; vulnerabilidad publicada del IBS/DataPro.
- **Consecuencias**: Incidente público; pérdida de calificación AAA(pan); sanción SBP; afectación de clientes; responsabilidad legal.
- **Stakeholders afectados**: CISO (SD-6), Cumplimiento, Operaciones, JD.
- **Vinculación con objetivos**: G-1, G-7, O-1, O-10.
- **Inherente**: L=3 (Posible — la exposición es real, sin haber materializado); I=4 (Mayor — pérdida AAA, sanción SBP). **Score = 12 (Medio-Alto)**.
- **Controles actuales**: pen-tests anuales obligatorios; proyecto IAM en curso; firewall + segmentación; monitoreo de seguridad.
- **Mitigaciones**: (a) **plan de remediación del legado** de 90 días — cifrado en reposo (cuando técnicamente factible), MFA para usuarios privilegiados, cifrado en tránsito; (b) reforzar pen-tests (semestrales hasta el go-live); (c) acelerar el proyecto IAM con metas mensuales; (d) plan de respuesta a incidentes con war-room; (e) cobertura de seguro de ciber-riesgo (transferir parcialmente).
- **Residual**: L=2 (Improbable — con remediaciones); I=4 (Mayor — el impacto no se reduce). **Score = 8 (Medio)**.
- **Respuesta 4T**: **Treat** + **Transfer** parcial (seguro).
- **Owner**: CISO (Accountable) + TI (Responsible).
- **Acciones**: plan de remediación 90 días (inmediato); cifrado en reposo + MFA privilegiado (90 días); IAM end-to-end (12 meses); cobertura de seguro ciber (60 días).
- **Status**: Open.
- **Apetito**: Excede (+2); escalar a Comité de Tecnología.

#### R-028 (NEW): Falla en la transición Activo-Pasivo → Activo-Activo simultánea al cambio de Core

- **Categoría**: TECHNOLOGY
- **Descripción**: CAP está actualmente en transición de Activo-Pasivo a **Activo-Activo** entre dos sitios separados por 35–40 km [DOC-SES-008 §9.1]. Si esta transición topológica coincide con el cambio del Core o se completa con prisa por compromiso del proyecto, hay riesgo de falla compleja durante migración (cambio de Core + cambio topológico = doble riesgo). La probabilidad de un evento de conmutación durante migración aumenta significativamente si ambos cambios no están bien secuenciados.
- **Causa raíz**: Dos proyectos críticos de infraestructura corriendo en paralelo; presión de cronograma del CBS; mejoras buscadas simultáneamente.
- **Eventos detonantes**: Ventanas de conmutación durante migración; bug en la conmutación activo-activo; falla en uno de los sitios con replicación inconsistente.
- **Consecuencias**: Indisponibilidad de servicios críticos durante migración (R-004); pérdida de datos por replicación inconsistente; afectación de la conciliación contable post-corte.
- **Stakeholders afectados**: TI (SD-5), Operaciones (SD-8), CISO.
- **Vinculación con objetivos**: G-3, G-4, G-9.
- **Inherente**: L=3 (Posible — los dos proyectos en paralelo aumentan probabilidad); I=3 (Moderado — afecta disponibilidad pero no irrecuperable). **Score = 9 (Medio)**.
- **Controles actuales**: planificación general del proyecto; gobernanza por TI.
- **Mitigaciones**: (a) **completar la transición a Activo-Activo ANTES del go-live del CBS** (idealmente 6 meses antes); (b) pruebas de conmutación al menos trimestrales del nuevo modelo Activo-Activo; (c) plan de rollback documentado del nuevo Core que no dependa de la nueva topología; (d) coordinación de los dos proyectos con un mismo Steering Committee.
- **Residual**: L=2 (Improbable — con secuenciación adecuada); I=3 (Moderado). **Score = 6 (Medio-Bajo)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: TI (Accountable) + Operaciones.
- **Acciones**: cronograma coordinado de los dos proyectos (4 semanas); cierre de la transición Activo-Activo (6 meses); pruebas de conmutación trimestrales (recurrente).
- **Status**: Open.
- **Apetito**: Dentro de apetito.

#### R-029 (NEW): Múltiples BPMs no estandarizados amplifican riesgo de integración

- **Categoría**: TECHNOLOGY
- **Descripción**: CAP opera múltiples BPMs para originación: **Ultimus**, **Asicom-Finflow**, **Genexus** [DOC-RFI-001 §3.2, DOC-SES-004, DOC-SES-009 §10.3]. El CBS recibe el crédito aprobado desde estos BPMs (FR-013, INT-015). La fragmentación amplifica el riesgo de integración: cada BPM tiene su propio modelo de datos, protocolo, esquema de aprobaciones y operador. La estandarización de los BPMs es decisión estratégica pendiente [DOC-SES-009 §10.3].
- **Causa raíz**: Adopciones tácticas sucesivas; falta de estandarización corporativa; cada área compró su propio BPM.
- **Eventos detonantes**: Cambio en uno de los BPMs durante el proyecto; un BPM no expone API moderna; mismo crédito originado por dos BPMs.
- **Consecuencias**: Mayor esfuerzo de integración; pérdida de datos entre BPM y CBS; demoras en originación; inconsistencias contables.
- **Stakeholders afectados**: TI (SD-5), Créditos (SD-12), Hipotecas (SD-11), Aldo Ríos.
- **Vinculación con objetivos**: G-3, G-9.
- **Inherente**: L=4 (Probable — los 3 BPMs son una realidad); I=3 (Moderado — solucionable con esfuerzo). **Score = 12 (Medio)**.
- **Controles actuales**: ninguno específico.
- **Mitigaciones**: (a) **decisión estratégica de estandarización de BPMs** en paralelo al CBS — selección de un BPM corporativo con migración gradual (12–24 meses); (b) en mientras tanto, definir un **contrato de API estándar** (canónico) que el CBS expone y al que los 3 BPMs se adaptan vía middleware; (c) priorizar la integración del BPM más crítico (originación hipotecaria — Asicom + SITECA) en la PoC; (d) plan de rollback por BPM en caso de falla parcial.
- **Residual**: L=3 (Posible); I=2 (Menor — con API canónica). **Score = 6 (Medio)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: TI (Accountable) + Aldo Ríos.
- **Acciones**: decisión BPM corporativo (6 meses); contrato de API canónica (3 meses); integración BPM crítico en PoC (4 meses).
- **Status**: Open.
- **Apetito**: Excede (+2); escalar a Comité de Tecnología.

#### R-030 (NEW): Diccionario de datos heredado (8,000+ elementos) sin propietarios claros

- **Categoría**: OPERATIONAL (Datos)
- **Descripción**: CAP ha documentado más de **8,000 elementos del diccionario de datos** [DOC-SES-005, DOC-RFI-001 §4.6, DOC-SES-009 §6.1]. La gobernanza de datos está parcial: hay procesos manuales, sin validaciones en algunos campos, duplicidad de registros, falta de propietarios claros para muchos elementos [DOC-SES-006 §7.2]. Sin gobierno robusto del diccionario, la migración al nuevo CBS (BR-008) introducirá los problemas heredados al nuevo sistema y comprometerá la calidad de datos.
- **Causa raíz**: Crecimiento orgánico del diccionario sin gobierno formal; rotación de personal en mandos medios [DOC-SES-006]; falta de validaciones en el origen.
- **Eventos detonantes**: Migración masiva sin asignar propietarios; descubrimiento de campos sin definición durante la migración; conflictos entre BPM/CBS por el mismo elemento.
- **Consecuencias**: Calidad de datos comprometida en el nuevo CBS; reportes regulatorios con errores; demoras en cierres mensuales; observaciones SBP en inspecciones; degradación del modelo dual de provisiones.
- **Stakeholders afectados**: Datos / Calidad (nuevo en STKE), TI, Riesgos, Cumplimiento, áreas de negocio.
- **Vinculación con objetivos**: G-1, G-6, G-9.
- **Inherente**: L=4 (Probable — el problema ya existe); I=3 (Moderado — solucionable con esfuerzo). **Score = 12 (Medio)**.
- **Controles actuales**: proyecto de gobierno de datos en curso [DOC-SES-005]; Data Lake en AWS con migración a Snowflake en curso.
- **Mitigaciones**: (a) **asignar propietarios** a los 8,000+ elementos antes de la migración (gobernanza formal con MDM — DR-010); (b) **validación en tiempo de ingreso** transversal en el nuevo CBS (NFR-M-008); (c) ejercicio de limpieza de datos durante la migración con doble pase; (d) reglas de calidad documentadas por dominio; (e) **Data Steward por dominio** (cuentas, créditos, hipotecas, garantías, etc.).
- **Residual**: L=4 (Probable — el esfuerzo es enorme); I=1 (Mínimo — con validación en origen, problemas se mitigan en el origen). **Score = 4 (Bajo)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Datos / Calidad + TI.
- **Acciones**: asignación de propietarios (4 meses); reglas de calidad (6 meses); plan de limpieza pre-migración (8 meses); Data Stewards (3 meses).
- **Status**: Open.

#### R-031 (NEW): PoC de referencia estrecha — caso único hipotecario no representa complejidad operativa

- **Categoría**: OPERATIONAL
- **Descripción**: La ficha de PoC v1.0 [DOC-POC-001] define un único caso de uso de referencia — crédito hipotecario con codeudores, subsidio, gracia, mora y abono extraordinario — evaluando 13 módulos. Aunque sólido, **no cubre**: captación masiva con sub-cuentas (FR-006, FR-007), créditos sindicados con CAP como coordinador (FR-026), factoring con pagador estatal (FR-040), pago masivo de planilla con DDI (FR-045/UC-13), reportes SEI en escenarios complejos (FR-055/UC-4). El vendor finalista puede tener fortalezas en el caso PoC pero debilidades en estos otros escenarios críticos, llevando a una selección sub-óptima.
- **Causa raíz**: Restricción de tiempo y recursos para PoCs múltiples; preferencia por profundizar en un caso bandera.
- **Eventos detonantes**: Selección de un vendor que no soporta bien sindicados o factoring estatal — productos centrales para CAP; descubrimiento post-contrato.
- **Consecuencias**: Selección sub-óptima; necesidad de customización del vendor (PRIN P20, NFR-M-002) violando principio crítico; revisitar la decisión con costo político.
- **Stakeholders afectados**: Aldo Ríos, Negocio (Créditos, Hipotecas, Operaciones), Finanzas.
- **Vinculación con objetivos**: G-5, G-9, G-2.
- **Inherente**: L=2 (Improbable — la selección puede aún funcionar con un buen vendor); I=2 (Menor — solucionable con cláusulas contractuales). **Score = 4 (Bajo)**.
- **Controles actuales**: matriz de evaluación de PoC con criterios documentados [archivos 5.PreparaciónPOC-Matriz_Evaluacion_PoC_CAP_v1.xlsx].
- **Mitigaciones**: (a) **ampliar la PoC** con al menos 2 casos adicionales (sindicados + factoring estatal o pago masivo DDI); (b) **demos extendidas** del vendor finalista en los productos no cubiertos por PoC; (c) **cláusulas contractuales** que penalicen incumplimientos en los productos no cubiertos por PoC; (d) involucrar a las áreas de Negocio específicas (Tesorería, Banca Comercial) en la validación.
- **Residual**: L=3 (Posible — incluso con ampliación, no se cubre todo); I=2 (Menor). **Score = 6 (Medio)**. *Nota: subió de 4 a 6 al reconocer que ampliar el alcance introduce su propio riesgo de cobertura incompleta.*
- **Respuesta 4T**: **Treat**.
- **Owner**: Aldo Ríos + Negocio.
- **Acciones**: ampliación de la PoC (3 semanas para acordar; 8 semanas para ejecutar); demos extendidas (durante RFP); cláusulas contractuales (durante negociación).
- **Status**: Open.
- **Apetito**: Excede (+2 nominal, aunque marginal por la baja probabilidad inherente); escalar informativamente.

#### R-032 (NEW): Restricción Innovación / Seguridad Nacional sobre cloud bloquea decisión arquitectónica

- **Categoría**: COMPLIANCE
- **Descripción**: La regulación panameña exige que datos sensibles permanezcan en el país [DOC-SES-008 §9.3]. Cualquier migración a la nube requiere aprobación de la **Autoridad de Innovación**, la **Superintendencia de Bancos** y el **Consejo de Seguridad Nacional** (especialmente para fondos públicos y cuentas gubernamentales). La consulta formal **aún no ha sido emitida**. Sin respuesta de estas tres entidades, el modelo de despliegue del CBS queda en suspenso y el RFP no puede definir reglas de soberanía claras.
- **Causa raíz**: Decisión política pendiente; falta de precedentes para bancos estatales; falta de data centers locales de hyperscalers en Panamá.
- **Eventos detonantes**: Demora en respuesta gubernamental; respuesta negativa; respuesta condicionada con restricciones complejas.
- **Consecuencias**: Retraso del RFP; pérdida de opciones de despliegue cloud; necesidad de redesign si la respuesta llega tarde.
- **Stakeholders afectados**: Legal, Cumplimiento, CISO, Aldo Ríos.
- **Vinculación con objetivos**: G-7, G-8.
- **Inherente**: L=1 (Raro — el banco controla la iniciativa de la consulta); I=3 (Moderado — retraso de RFP). **Score = 3 (Bajo)**.
- **Controles actuales**: consulta formal pendiente de iniciar.
- **Mitigaciones**: (a) **iniciar consulta formal esta semana** con Autoridad de Innovación, SBP y Seguridad Nacional; (b) preparar dossier técnico de soporte; (c) plan B con despliegue on-premise en territorio panameño (preserva soberanía sin depender de la decisión).
- **Residual**: L=1 (Raro); I=2 (Menor — con plan B). **Score = 2 (Bajo)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Legal + Aldo Ríos.
- **Acciones**: consulta formal (1 semana); seguimiento mensual (recurrente).
- **Status**: Open.

#### R-033 (NEW): FECI mal implementado tiene impacto fiscal directo

- **Categoría**: FINANCIAL (con consecuencia COMPLIANCE)
- **Descripción**: El **FECI** (Fondo Especial de Compensación de Intereses) es una retención del **1% sobre intereses comerciales** que el banco debe calcular y remitir mensualmente al MEF (FR-029). Es una integración compleja: cálculo automático, exposición al ERP, conciliación con el MEF, retenciones en cuentas (DDI), reportería. Si el FECI se implementa mal en el nuevo CBS (cálculo incorrecto, transmisión incompleta), el banco enfrenta multas fiscales y revisiones del MEF.
- **Causa raíz**: Nueva implementación (no existía como módulo dedicado en el legado); complejidad de cálculo automático en cada movimiento de intereses comerciales.
- **Eventos detonantes**: Falla en cálculo o remisión durante migración; ajuste tardío post go-live; auditoría MEF.
- **Consecuencias**: Multas fiscales; observaciones MEF; corrección retroactiva; reputación.
- **Stakeholders afectados**: Finanzas (SD-4), Cumplimiento, Créditos, MEF.
- **Vinculación con objetivos**: G-1, G-2.
- **Inherente**: L=2 (Improbable — el cálculo es matemáticamente simple); I=3 (Moderado — multa y reputación). **Score = 6 (Medio)**.
- **Controles actuales**: requisito FR-029 en REQ v2.0; validación en PoC obligatoria.
- **Mitigaciones**: (a) **prueba dedicada de FECI** en PoC; (b) cálculo paralelo durante 3 meses pre-corte; (c) validación contra MEF (sandbox o consulta directa); (d) reportería en el SEI/MEF mensual con conciliación.
- **Residual**: L=2 (Improbable); I=2 (Menor). **Score = 4 (Bajo)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Finanzas + Cumplimiento.
- **Acciones**: validación FECI en PoC (8 semanas); cálculo paralelo (3 meses pre-corte).
- **Status**: Open.

#### R-034 (NEW): Conflicto CAPEX/OPEX (BR-014) no aprobado por JD por consideraciones presupuestarias

- **Categoría**: STRATEGIC (con dimensión FINANCIAL)
- **Descripción**: La transición de CAPEX a OPEX (BR-014 REQ v2.0) es objetivo estratégico de Finanzas [DOC-SES-008 §9.4] pero choca con la realidad presupuestaria del banco público: presupuestos plurianuales por capítulo, Contraloría revisa contratos por capítulo de inversión, suscripciones anuales pueden ser difíciles de presupuestar. Si la JD rechaza la transición OPEX, el modelo de despliegue cloud queda limitado y la flexibilidad financiera del proyecto se reduce.
- **Causa raíz**: Naturaleza de presupuesto público estatal; cultura CAPEX dominante; ausencia de precedentes recientes.
- **Eventos detonantes**: Discusión en JD de modelo financiero del contrato; cuestionamiento de la Contraloría.
- **Consecuencias**: Pérdida de flexibilidad de despliegue; retorno a modelo on-premise con CAPEX dominante; posibles costos mayores a largo plazo.
- **Stakeholders afectados**: Finanzas (SD-4), JD (SD-1), Contraloría (SD-10).
- **Vinculación con objetivos**: G-2.
- **Inherente**: L=3 (Posible — la cultura CAPEX domina); I=4 (Mayor — afecta modelo de despliegue). **Score = 12 (Medio)**.
- **Controles actuales**: BR-014 reconoce la tensión.
- **Mitigaciones**: (a) **caso de negocio formal** del CAPEX→OPEX con análisis a 7 años; (b) consulta informal con Contraloría sobre viabilidad presupuestaria; (c) plan B con modelo CAPEX en territorio panameño (preserva soberanía y modelo conocido); (d) **decisión explícita de la JD** antes del cierre del RFP.
- **Residual**: L=2 (Improbable — con plan B); I=3 (Moderado). **Score = 6 (Medio)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Finanzas + JD.
- **Acciones**: caso de negocio CAPEX vs OPEX (6 semanas); consulta Contraloría (8 semanas); decisión JD (12 semanas).
- **Status**: Open.

#### R-035 (NEW): Caja Amiga + comarcas indígenas modo degradado no probado con el nuevo Core

- **Categoría**: OPERATIONAL (con consecuencia REPUTATIONAL)
- **Descripción**: La Red **Caja Amiga** (100+ puntos [DOC-SES-009 §3.2]) y las sucursales en **comarcas indígenas** operan con conectividad limitada o intermitente [DOC-CB-001-C23..C25]. El requisito FR-072 establece modo degradado/offline con conciliación diferida, pero **el modo degradado del nuevo CBS no estará probado** hasta etapas avanzadas del proyecto. Una falla del modo degradado durante la migración deja a 100+ puntos rurales sin operación — afectando el mandato social del Estado.
- **Causa raíz**: Pruebas de offline requieren ambientes complejos; tendencia de los vendors a relegar offline en favor de online.
- **Eventos detonantes**: Migración masiva sin pruebas de offline previas; fallas de conectividad durante el corte.
- **Consecuencias**: Inclusión financiera comprometida; queja política de comarcas; cobertura mediática; cuestionamiento del mandato social.
- **Stakeholders afectados**: Red Caja Amiga, Hipotecas, Operaciones, Comunicaciones, JD.
- **Vinculación con objetivos**: G-5, BR-012, PRIN P15.
- **Inherente**: L=3 (Posible — pruebas de offline son históricamente débiles); I=5 (Crítico — afecta inclusión financiera, mandato social). **Score = 15 (Alto)**.
- **Controles actuales**: requisito FR-072 explícito.
- **Mitigaciones**: (a) **plan de pruebas de offline dedicado** con sucursales piloto de Caja Amiga (al menos 5 puntos); (b) **cláusula contractual** que penalice degradación del modo offline; (c) plan de comunicación a comarcas indígenas con anticipación; (d) **modo de continuidad operativa** durante la ventana de migración (Caja Amiga sigue operando con el legado mientras se migra la red urbana).
- **Residual**: L=2 (Improbable — con pruebas dedicadas); I=3 (Moderado — con continuidad operativa). **Score = 6 (Medio-Bajo)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Red Caja Amiga + Operaciones.
- **Acciones**: plan de pruebas offline (3 meses); pilotos Caja Amiga (6 meses); plan de continuidad operativa (3 meses).
- **Status**: Open.

#### R-036 (NEW): Pérdida de la estabilidad actual de DataPro durante o post migración

- **Categoría**: OPERATIONAL
- **Descripción**: Los equipos del banco reconocieron que **DataPro es muy estable, prácticamente sin caídas** [DOC-SES-009 §3.4, §9.2 — "La infraestructura actual es muy estable, prácticamente no registra caídas"]. El nuevo CBS, por ser nuevo, podría introducir más inestabilidad en el corto plazo (post go-live), antes de estabilizarse. Esto crea un riesgo reputacional comparativo: clientes y JD percibirán el cambio como degradación incluso si las métricas globales mejoran.
- **Causa raíz**: Madurez del legado vs novedad del CBS; ciclo natural de estabilización de nuevas plataformas; expectativas elevadas.
- **Eventos detonantes**: Incidentes leves pero visibles en los primeros meses post-corte; quejas de canales digitales; comparaciones públicas con DataPro.
- **Consecuencias**: Erosión de confianza del cliente; queja política; presión sobre el equipo del programa; "I told you so" del incumbente.
- **Stakeholders afectados**: Clientes (SD-15), Operaciones, Aldo Ríos, JD.
- **Vinculación con objetivos**: G-3, O-9 (NPS), O-10 (AAA).
- **Inherente**: L=3 (Posible — todas las plataformas nuevas tienen período de estabilización); I=2 (Menor — visibilidad pero recuperable). **Score = 6 (Medio)**.
- **Controles actuales**: SLA NFR-A-001..003 con penalizaciones.
- **Mitigaciones**: (a) **período de paralelo extendido** (≥ 3 meses por bando — BR-001); (b) **plan de comunicación proactiva** con clientes y JD sobre el período de estabilización; (c) **war-room dedicado** durante los primeros 90 días post go-live; (d) **métricas de comparación favorables** (no solo uptime, sino capabilities nuevas como sub-cuentas, sobregiros nativos, etc.); (e) gestión de expectativas con la JD.
- **Residual**: L=3 (Posible); I=1 (Mínimo — con gestión activa). **Score = 3 (Bajo)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: Operaciones + Comunicaciones.
- **Acciones**: plan de comunicación (8 semanas pre-corte); war-room (durante migración); seguimiento de NPS mensual.
- **Status**: Open.

#### R-037 (NEW): Migración crítica de SITECA (originación hipotecaria) — pérdida de cobertura del segmento principal

- **Categoría**: OPERATIONAL (con consecuencia FINANCIAL/REPUTATIONAL)
- **Descripción**: **SITECA** es el sistema de originación hipotecaria de CAP [DOC-SES-001, DOC-SES-009 §3.2]. Junto con SISTECA (Asicom), origina la cartera hipotecaria de ~B/. 3,000M — el segmento más grande de la cartera. La migración o integración de SITECA al nuevo CBS es crítica: si SITECA queda fuera de servicio durante la migración o pierde funcionalidad, la originación hipotecaria se detiene afectando ingresos y cumplimiento del mandato social (Interés Preferencial).
- **Causa raíz**: SITECA es legado complejo; integración punto a punto con DataPro; migración a un nuevo CBS requiere re-cableado.
- **Eventos detonantes**: Falla en integración SITECA-nuevo CBS; SITECA queda fuera de servicio en el corte; pérdida de datos en migración SITECA.
- **Consecuencias**: Originación hipotecaria detenida; ingresos comprometidos; quejas del mandato social; afectación de la cartera Interés Preferencial.
- **Stakeholders afectados**: Hipotecas (SD-11), TI, Negocio, MIVIOT, DGI.
- **Vinculación con objetivos**: G-5, G-9.
- **Inherente**: L=2 (Improbable — pero alto impacto); I=4 (Mayor). **Score = 8 (Medio)**.
- **Controles actuales**: INT-014 en REQ v2.0 explicita SITECA como integración MUST.
- **Mitigaciones**: (a) **SITECA en el caso de PoC** del vendor finalista (la PoC actual DOC-POC-001 ya incluye originación hipotecaria); (b) **plan de migración SITECA** dedicado con paralelo ≥ 3 meses; (c) contrato con SITECA para soporte transicional; (d) reservar como Fase 2 una eventual sustitución/consolidación de SITECA por el módulo nativo del nuevo CBS si aplica.
- **Residual**: L=2 (Improbable — con mitigaciones); I=2 (Menor). **Score = 4 (Bajo)**.
- **Respuesta 4T**: **Treat**.
- **Owner**: TI + Hipotecas.
- **Acciones**: SITECA en PoC (durante PoC); plan de migración SITECA (6 meses); contrato SITECA transición (3 meses).
- **Status**: Open.

---

## D. Análisis por Categoría (v2.0)

### STRATEGIC (4 riesgos)

R-008, R-014, R-022, **R-034 (NEW)**. Inherente promedio 13.8 (sube de v1.0 por R-034 12); residual promedio 7.8. Efectividad: 43%. Tema clave: vendor lock-in, vulnerabilidad política, **decisión CAPEX/OPEX**.

### OPERATIONAL (7 riesgos)

R-001, R-004, R-019, R-021, **R-031 (NEW)**, **R-035 (NEW)**, **R-036 (NEW)**. Inherente promedio 12.0; residual promedio 6.4. Efectividad: 47%. Temas: pérdida de talento, **PoC estrecha**, **modo degradado Caja Amiga**, **estabilidad post-corte**.

### FINANCIAL (4 riesgos)

R-010, R-011, R-016, **R-033 (NEW)**. Inherente promedio 12.0; residual promedio 5.5. Efectividad: 54%. Tema: TCO, calificación, **FECI**.

### COMPLIANCE (7 riesgos)

R-002, R-003, R-007, R-015, R-018, **R-023 (NEW)**, **R-025 (NEW)**, **R-026 (NEW)**, **R-032 (NEW)**. Inherente promedio 13.0 (sube por nuevos); residual promedio 6.0. Efectividad: 54%. Tema: regulación SBP, soberanía, **AML externo**, **Acuerdo 1-2026**, **sesgo COBIS**.

### REPUTATIONAL (1 riesgo)

R-022. Sin cambios.

### TECHNOLOGY (14 riesgos)

R-005, R-006, R-009, R-012, R-013, R-017, R-020, **R-024 (NEW)**, **R-027 (NEW)**, **R-028 (NEW)**, **R-029 (NEW)**, **R-030 (NEW)**, **R-037 (NEW)**. Inherente promedio 13.4 (sube por R-024 25 y R-027 12); residual promedio 7.1. Efectividad: 47%. Temas: **ERP**, **brecha de seguridad legado**, **transición Activo-Activo**, **BPMs múltiples**, **diccionario de datos**, **SITECA**.

---

## E. Matriz de Propiedad de Riesgo (v2.0)

| Stakeholder | Riesgos propios | Críticos/Altos | Notas |
|-------------|-----------------|-----------------|-------|
| **Aldo Ríos (Innovación)** | R-008, R-019, R-022, R-026, R-031 | 1 Alto, 1 Crítico (compartido) | Owner del programa |
| **JD (Junta Directiva)** | R-014, R-016, R-024 (compartido), R-034 | 1 Crítico inherente | Decisiones de gates y apetito |
| **Gerencia General** | R-004 (escalamiento) | 1 Alto | Patrocinador ejecutivo |
| **TI (Gerencia de Tecnología)** | R-001 (compartido), R-012, R-013, R-021, R-024 (compartido), R-028, R-029, R-030 (compartido), R-037 | 2 Críticos inherentes, 3 Altos | **Mayor concentración**; protección de talento crítica |
| **CISO** | R-017, R-027 | 2 Altos | Brecha actual + ventana migración |
| **Cumplimiento** | R-003 (compartido), R-007, R-015, R-018 (compartido), R-023, R-025 | 3 Altos | Regulación SBP + AML externo + Acuerdo 1-2026 |
| **Riesgos** | R-003 (compartido) | 1 Alto | Modelo dual provisiones |
| **Finanzas** | R-010, R-011, R-024 (compartido), R-033, R-034 | 1 Crítico inherente, 1 Alto | TCO + ERP + FECI + CAPEX/OPEX |
| **Legal** | R-006, R-018, R-026 (compartido) | 2 Altos | Soberanía + dictamen RFP |
| **Operaciones** | R-004, R-035, R-036 | 1 Alto | Continuidad + offline + estabilidad |
| **RRHH** | R-001 (compartido), R-019 (compartido) | 1 Medio | Talento + cambio |
| **Negocio (Hipotecas, Créditos)** | R-005, R-031 (compartido), R-037 (compartido) | 1 Medio | Productos sociales + PoC |
| **Datos / Calidad** | R-030 (compartido) | 1 Medio | Diccionario, MDM |
| **Comunicaciones** | R-022, R-036 (compartido) | 1 Medio | Plan de comunicación |
| **Red Caja Amiga** | R-035 | 1 Alto | Inclusión financiera |

---

## F. Resumen del Framework 4Ts (v2.0)

| Respuesta | Conteo | % | Ejemplos clave |
|-----------|--------|---|----------------|
| **Tolerate** | 2 | 5% | R-014 (cambio político), R-010 (cambiario USD) |
| **Treat** | 33 | 89% | R-024 (ERP), R-023 (AML), R-026 (sesgo COBIS), R-008 (lock-in), R-013 (integración), R-017/R-027 (ciber), etc. |
| **Transfer** | 1 (parcial) | 3% | R-027 — seguro de ciber-riesgo (combinado con Treat) |
| **Terminate** | 0 | 0% | Ninguna actividad debe terminarse — el programa procede con controles agresivos |
| **Combinado (Treat+Transfer)** | 1 | 3% | R-027 — controles internos + seguro cibernético |

---

## G. Cumplimiento de Apetito de Riesgo

| Categoría | Apetito Threshold (score residual) | Riesgos Dentro | Riesgos Exceden | Acción Requerida |
|-----------|-------------------------------------|-----------------|------------------|------------------|
| **STRATEGIC** | Medio (≤ 9) | 3 (R-014, R-022, R-034) | 1 (R-008 score 9 — en límite) | Monitoreo Comité de Tecnología |
| **OPERATIONAL** | Medio (≤ 8) | 5 | 2 (R-004, R-031) | Escalar a Gerencia General + Aldo Ríos |
| **FINANCIAL** | Bajo (≤ 6) | 4 | 0 | Dentro de apetito |
| **COMPLIANCE** | Bajo (≤ 6) | 3 | 4 (R-023, R-025, R-026 — todos NEW v2.0) | Escalar a Cumplimiento + JD |
| **REPUTATIONAL** | Medio (≤ 6) | 0 | 1 (R-022 score 4 — dentro límite) | Dentro |
| **TECHNOLOGY** | Medio (≤ 6) | 8 | 6 (R-013, R-017, R-024, R-027, R-028, R-029) | Escalar a Comité de Tecnología |
| **AGREGADO** | — | 23 | 14 (38% de riesgos exceden apetito de su categoría) | **Revisión del apetito por la JD** justificada |

> **Nota**: el apetito de riesgo organizacional formal no ha sido aprobado por la JD. Los thresholds anteriores son **propuestos** por el equipo del programa basándose en práctica usual. La aprobación formal del apetito es una recomendación del Orange Book pero no ha sido ejecutada. **Acción recomendada**: ejecutar `/arckit:risk-appetite` (o un workshop específico con la JD) para formalizar el apetito antes del cierre del RFP.

---

## H. Plan de Acción Priorizado (v2.0)

### Prioridad 0: BLOQUEANTE (esta semana)

| # | Acción | Riesgos | Owner | Fecha límite |
|---|--------|---------|-------|---------------|
| 0.1 | **Iniciar selección del ERP externo** en paralelo al RFP CBS (RFI ERP) | R-024 | Finanzas + Aldo Ríos | 2026-06-18 (1 sem) |
| 0.2 | **Iniciar selección del motor AML externo** con IA y APIs (RFI AML) | R-023 | Cumplimiento + Aldo Ríos | 2026-06-18 (1 sem) |
| 0.3 | **Dictamen Legal previo del proceso RFP** sobre criterios objetivos y preferencias | R-026 | Legal | 2026-07-09 (4 sem) |
| 0.4 | **Iniciar consulta formal** a Autoridad de Innovación + SBP + Seguridad Nacional sobre cloud | R-032 | Legal + Aldo Ríos | 2026-06-18 (1 sem) |
| 0.5 | **Dictamen Legal de soberanía de datos** (v1.0 R-006/R-018) — mantenido | R-006, R-018 | Legal | 2026-07-23 (6 sem) |

### Prioridad 1: URGENTE (próximas 4–8 semanas — bloqueantes del RFP)

| # | Acción | Riesgos | Owner | Fecha límite |
|---|--------|---------|-------|---------------|
| 1.1 | Plan de retención de talento clave de TI (v1.0) | R-001 | RRHH + Aldo Ríos | 2026-07-23 (6 sem) |
| 1.2 | **Plan de remediación de seguridad del legado** (cifrado, MFA, recertificación automática) | R-027 | CISO | 2026-09-11 (90 días) |
| 1.3 | Cláusulas eliminatorias del RFP (v1.0) — añadir: criterios objetivos auditables (R-026), AML externo (R-023), ERP integration (R-024), Acuerdo 1-2026 (R-025) | R-002, R-005, R-006, R-008, R-011, R-020, R-023, R-024, R-025, R-026 | Aldo Ríos + Legal | 2026-08-06 (8 sem) |
| 1.4 | Contrato extendido con DataPro/Vencora con soporte transicional 12 meses post go-live (v1.0) — urgente por relación deteriorada | R-009 | Aldo Ríos + Legal | 2026-08-06 (8 sem) |
| 1.5 | **Ampliación del alcance de la PoC** con al menos 2 casos adicionales (sindicados/factoring estatal/DDI masivo) | R-031 | Aldo Ríos + Negocio | 2026-08-06 (8 sem) |
| 1.6 | **Matriz de ponderación documentada y validada por Auditoría Interna** | R-002, R-026 | Aldo Ríos + Auditoría | 2026-08-06 (8 sem) |
| 1.7 | Workshop de formalización del apetito de riesgo con la JD | (todos) | Aldo Ríos + JD | 2026-08-06 (8 sem) |

### Prioridad 2: ALTA (próximos 3–6 meses)

| # | Acción | Riesgos | Owner | Fecha límite |
|---|--------|---------|-------|---------------|
| 2.1 | Pen-test del entorno actual y modelo de amenazas pre-migración (v1.0 + refresh) | R-017, R-027 | CISO | 2026-09-11 (3 meses) |
| 2.2 | War-room y plan de comunicación de migración (v1.0) | R-004, R-022, R-036 | Comunicaciones + Aldo Ríos | 2026-12-11 (6 meses) |
| 2.3 | **Decisión estratégica de estandarización de BPMs corporativos** + diseño de API canónica | R-029 | TI + Aldo Ríos | 2026-12-11 (6 meses) |
| 2.4 | **Gobernanza del diccionario de datos** — asignación de propietarios a los 8,000+ elementos | R-030 | Datos / Calidad + TI | 2026-12-11 (6 meses) |
| 2.5 | **Completar transición Activo-Activo** entre los dos sitios | R-028 | TI + Operaciones | 2026-12-11 (6 meses) |
| 2.6 | **Plan de pruebas offline dedicado** con sucursales piloto de Caja Amiga | R-035 | Red Caja Amiga + Operaciones | 2026-09-11 (3 meses) |
| 2.7 | Plan de remediación intermedio del CBS legado para Acuerdo 1-2026 Art. 25 §1 (vigencia 31-ene-2027) y Art. 14 (vigencia 30-jun-2027) | R-025 | Cumplimiento + TI | 2026-09-11 (3 meses) |
| 2.8 | Cobertura de seguro de ciber-riesgo | R-027 | CISO + Finanzas | 2026-09-11 (3 meses) |
| 2.9 | Caso de negocio formal CAPEX→OPEX y consulta informal a Contraloría | R-034 | Finanzas + JD | 2026-09-11 (3 meses) |

### Prioridad 3: MEDIA (próximos 6–12 meses)

| # | Acción | Riesgos | Owner | Fecha límite |
|---|--------|---------|-------|---------------|
| 3.1 | Validación FECI en PoC + cálculo paralelo pre-corte | R-033 | Finanzas + Cumplimiento | 2027-03-11 (9 meses) |
| 3.2 | Plan de migración SITECA dedicado con paralelo ≥ 3 meses | R-037 | TI + Hipotecas | 2027-03-11 (9 meses) |
| 3.3 | Plan de comunicación proactiva de estabilización post go-live | R-036 | Operaciones + Comunicaciones | (pre-corte) |
| 3.4 | Reglas de calidad por dominio + Data Stewards | R-030 | Datos / Calidad | 2027-03-11 (9 meses) |
| 3.5 | (Mantenido v1.0) Plan FinOps y revisión mensual de costos | R-011 | Finanzas | 2027-03-11 (9 meses) |
| 3.6 | (Mantenido v1.0) Plan de gobernanza de proyecto y resistencia al cambio | R-019 | RRHH + Aldo Ríos | 2027-03-11 (9 meses) |

---

## I. Integración con SOBC

> El SOBC (Strategic Outline Business Case) de CAP usará este registro de riesgos refinado.

### Strategic Case (Parte A)

- R-014 (cambio político), R-016 (AAA), R-022 (mediático), R-034 (CAPEX/OPEX) → impacto estratégico.
- "Why Now?" — el R-009 (DataPro relación deteriorada) refuerza la urgencia: la ventana se reduce mes a mes.
- "Why this?" — R-024 (ERP) y R-023 (AML) introducen complejidad pero son necesarios para modernizar.

### Economic Case (Parte B)

- Risk-adjusted costs incluyen: R-011 (true-ups), R-024 (ERP costo paralelo), R-023 (AML costo paralelo), R-027 (remediación legado), R-029 (estandarización BPMs).
- Bias de optimismo ajustado por R-031 (PoC limitada — riesgo de selección sub-óptima requiere buffer).

### Commercial Case (Parte C)

- R-008 (lock-in), R-011 (true-ups), R-026 (proceso RFP) — todos relacionados con cláusulas contractuales clave.
- Nuevas cláusulas v2.0: R-023 (AML coordinado), R-024 (ERP coordinado), R-025 (Acuerdo 1-2026 cumplimiento continuo), R-026 (criterios objetivos en RFP).

### Financial Case (Parte D)

- Reserva para riesgos: ~10% del TCO total (alineado a Green Book) ahora considerando ERP + AML adicionales.
- R-010 (cambiario), R-016 (AAA), R-033 (FECI), R-034 (CAPEX/OPEX) → riesgos financieros directos.

### Management Case (Parte E — Risk Management)

- Este registro completo se incorpora textualmente; las acciones P0/P1/P2/P3 son el plan de gestión.
- Estructura de Steering Committee debe escalar a JD los siguientes riesgos: R-024 (ERP), R-026 (sesgo COBIS), R-014 (político), R-016 (AAA).

### Recomendación SOBC

- El SOBC debe explicitar que el programa procede con **gobernanza intensificada** dado el perfil de riesgo Concerning. Incluir un sub-comité ERP y un sub-comité AML que reportan al Comité de Tecnología.

---

## J. Marco de Monitoreo y Revisión

### Cadencia de revisión

| Frecuencia | Audiencia | Foco |
|------------|-----------|------|
| **Semanal** | Steering Committee | R-024 (ERP), R-023 (AML), R-026 (sesgo RFP), R-008 (lock-in), R-004 (canales), R-013 (integración), R-017/R-027 (ciberseguridad) — todos los críticos y altos |
| **Quincenal** | PMO + Aldo Ríos | Todos los riesgos abiertos |
| **Mensual** | Comité de Tecnología | Top 10, riesgos que excedan apetito, plan de acción P0/P1/P2 |
| **Trimestral** | JD | Perfil completo, apetito vs realidad, recomendaciones de re-priorización |
| **Anual** | Auditoría Interna + Contraloría | Cumplimiento Orange Book, eficacia de controles, lecciones aprendidas |

### Indicadores Clave de Riesgo (KRIs) v2.0

| KRI | Riesgo | Threshold | Frecuencia |
|-----|--------|-----------|-----------|
| % avance del proyecto ERP vs plan | R-024 | < 90% | semanal |
| % avance del proyecto AML vs plan | R-023 | < 90% | semanal |
| Días hasta 31-ene-2027 (Art. 25 §1) y 30-jun-2027 (Art. 14) vs cronograma del CBS y plan de remediación del legado | R-025 | < 6 meses de buffer en cualquiera de los dos | mensual |
| # casos PoC ejecutados vs # acordados | R-031 | < 100% | semanal durante PoC |
| Avance transición Activo-Activo | R-028 | < 100% pre go-live | mensual |
| % elementos del diccionario con propietario | R-030 | < 100% pre-migración | mensual |
| Vulnerabilidades críticas abiertas en legado | R-027 | > 0 | semanal |
| Variación mensual del subsidio Interés Preferencial vs legado (post go-live) | R-003 | > 1% material | mensual |
| Disponibilidad mensual Yappy/ACH/Telered | R-004, R-013 | < SLA | diaria |
| Rotación de TI clave en últimos 90 días | R-001 | > 5% | mensual |
| Días desde último pen-test | R-017, R-027 | > 180 | continuo |
| Días desde último dictamen Legal de soberanía | R-006, R-018 | > 90 sin renovación | continuo |

### Criterios de escalamiento automático

- Cualquier riesgo nuevo Crítico (20-25) → JD en ≤ 24 horas.
- Cualquier riesgo que aumente +5 puntos vs medición anterior → Comité de Tecnología en ≤ 1 semana.
- R-024 (ERP) en amarillo (avance < 90%) o rojo (< 75%) → JD inmediata.
- R-023 (AML) en amarillo o rojo → Comité de Tecnología + Cumplimiento inmediato.
- Cualquier observación informal de Contraloría sobre proceso RFP → suspensión cautelar y revisión por Legal en 24 horas.

### Requisitos de Reportería

- **Tablero ejecutivo semanal** con top 10 riesgos + status de acciones P0/P1.
- **Informe mensual de riesgos** a Comité de Tecnología (10–15 páginas).
- **Informe trimestral a JD** con análisis de tendencias y recomendaciones de apetito.

### Mantenimiento del Registro

- **Owner del Registro**: Aldo Ríos (Innovación).
- **Co-owners**: PMO (registro operativo), Auditoría Interna (validación).
- **Revisiones formales**: trimestrales (mínimo); ad-hoc tras eventos críticos.
- **Próximo refresh planificado**: 2026-09-11 (90 días) o tras cualquiera de: cierre del RFP, selección del vendor, decisión de la consulta gubernamental sobre cloud, evento de seguridad.

---

## K. Lista de Verificación de Cumplimiento Orange Book

- ✅ **Governance and Leadership**: Owners asignados desde STKE; JD escala riesgos sobre apetito.
- ✅ **Integration**: Riesgos vinculados a objetivos (G-1..G-10), stakeholders (SD-1..SD-17) y BR (1..14).
- ✅ **Collaboration**: Riesgos sourced desde stakeholder concerns, conflictos (10 conflictos REQ v2.0), sesiones presenciales.
- ✅ **Risk Processes**: identificación → assessment inherente/residual → 4Ts → monitoreo → revisión.
- ✅ **Continual Improvement**: framework de revisión, KRIs cuantificados, refresh trimestral.

---

## Apéndice A — Escalas de Evaluación

> Sin cambios respecto a v1.0. Ver Apéndice A de ARC-001-RISK-v1.0.md para escalas de Probabilidad (1-5), Impacto (1-5) y matrices de riesgo.

## Apéndice B — Vinculación Stakeholder → Riesgo (refrescado v2.0)

```text
Stakeholder: Finanzas (CFO equivalent — SD-4 STKE)
  → Concerns: TCO controlado, presupuesto auditable, modelo CAPEX/OPEX
    → R-011 (true-ups), R-024 (ERP), R-033 (FECI), R-034 (CAPEX/OPEX)
      → R-024 = Crítico inherente → escalar a JD

Stakeholder: Cumplimiento (SD-7)
  → Concerns: SBP, UAF, Acuerdo 1-2026, AML, ROS
    → R-007 (regulatorios), R-015 (SBP sanción), R-023 (AML externo), R-025 (Acuerdo 1-2026)
      → 4 riesgos Altos (residual) — escalar a JD

Stakeholder: CISO (SD-6)
  → Concerns: zero trust, cifrado, MFA, pen-test
    → R-017 (migración), R-027 (legado actual)
      → 2 riesgos residuales 8 — escalar a Comité de Tecnología

Stakeholder: TI (Gerencia de Tecnología — SD-5)
  → Concerns: integración, ERP, BPMs, diccionario, SITECA, Activo-Activo
    → R-012, R-013, R-021, R-024, R-028, R-029, R-030, R-037 — 8 riesgos
      → R-024 Crítico inherente; protección de talento R-001 prioritaria

Stakeholder: Legal (sin SD directo — implícito)
  → Concerns: soberanía, contrataciones, dictamen RFP
    → R-006, R-018, R-026
      → R-026 Alto inherente — escalar a Comité de Tecnología

Stakeholder: JD (SD-1)
  → Concerns: AAA(pan), reputación, escalamiento político
    → R-014, R-016, R-022, R-034 + R-024 (escalado)
      → 1 Crítico escalado (R-024)
```

---

## Aprobación del Documento

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Risk Register Owner | Aldo Ríos — Gerencia de Innovación | [PENDING] | [PENDING] |
| CISO | [PENDING] | [PENDING] | [PENDING] |
| Cumplimiento | [PENDING] | [PENDING] | [PENDING] |
| Finanzas | [PENDING] | [PENDING] | [PENDING] |
| Legal | [PENDING] | [PENDING] | [PENDING] |
| Comité de Tecnología | [PENDING] | [PENDING] | [PENDING] |
| Junta Directiva (apetito) | [PENDING] | [PENDING] | [PENDING] |

---

## Próximos Pasos

1. **Revisión con dueños de riesgo** (esta semana): validar score residual y dueños de los 15 riesgos nuevos.
2. **Escalamiento a JD** (próximas 2 semanas): R-024 (ERP Crítico inherente) + revisión de apetito.
3. **Workshop de apetito** (próximas 4 semanas): formalizar thresholds por categoría.
4. **Integración a SOBC** (próximas 6 semanas): incorporar a la Parte E del SOBC con las nuevas mitigaciones.
5. **Acciones P0** (esta semana): iniciar RFI ERP, RFI AML, dictamen Legal RFP, consulta gubernamental cloud.
6. **Refresh trimestral** (próximo: 2026-09-11).

---

## External References

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| DOC-CB-001 | Relevamiento_CoreBanking_CajaDeAhorros_v2.docx | Word | `projects/000-global/external/` | Relevamiento confidencial |
| DOC-CB-002 | Relevamiento_Caja Ahorro_Pana.xlsx | Excel | `projects/000-global/external/` | Cuestionario estructurado |
| DOC-CB-003 | informacion_regulatoria.docx | Word | `projects/000-global/external/` | Brief regulatorio SBP |
| DOC-SES-001 | 1.Material…Día1-Arquitectura-ResumenDía1-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 1 — Arquitectura (relación con DataPro, satélites, IBM MQ) |
| DOC-SES-002 | 1.Material…Día2-Captación-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 2 — Captación (sobregiros, sub-cuentas, bóveda en Excel) |
| DOC-SES-003 | 1.Material…Día2-EstrategiayNegocio-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 2 — Estrategia / Negocio |
| DOC-SES-004 | 1.Material…Día3-Crédito-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 3 — Crédito (factoring estatal, sindicados, reestructuración) |
| DOC-SES-005 | 1.Material…Día3-Datos-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 3 — Datos (96% del Core, 54+ reportes, ERP externo, Snowflake) |
| DOC-SES-006 | 1.Material…Día3-Regulatoria-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 3 — Regulatoria (Acuerdo 1-2026, AML externo, validación en ingreso) |
| DOC-SES-007 | 1.Material…Día4-Ciberseguridad-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 4 — Ciberseguridad (sin cifrado, sin MFA, IAM en curso) |
| DOC-SES-008 | 1.Material…Día4-Infraestructura-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 4 — Infraestructura (Activo-Pasivo → Activo-Activo, Azure, CAPEX→OPEX) |
| DOC-SES-009 | 1.Material…ResumendeNotasAndreina-…docx | Word | `projects/001-evaluacion-core-banking/external/` | **Resumen Consolidado** (preferencias COBIS, inventario satélite) |
| DOC-RFI-001 | 7.RFI-RFI_CAP_CoreBancario_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | **RFI v1.0** (junio 2026) |
| DOC-POC-001 | 5.PreparaciónPOC-POC_seleccion_core_banking_CAP_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | **Ficha técnica PoC v1.0** |
| ARC-001-REQ-v2.0 | ARC-001-REQ-v2.0.md | Markdown | `projects/001-evaluacion-core-banking/` | Requisitos refrescados — incorpora 15 conflictos resueltos y 50 nuevos requisitos respecto a v1.0 |

### Citas principales nuevas (v2.0)

| Citation ID | Doc | Uso principal en este RISK |
|---|---|---|
| DOC-SES-001 | Día 1 Arquitectura | R-009 (DataPro relación deteriorada), R-021 (inventario satélite), R-028 (Activo-Activo en transición), R-037 (SITECA) |
| DOC-SES-005 | Día 3 Datos | R-024 (ERP — Cores modernos sin GL), R-030 (8000+ elementos), R-021 (Átomos, Snowflake) |
| DOC-SES-006 | Día 3 Regulatoria | R-007 (Acuerdo 1-2026), R-023 (AML externo), R-025 (Art. 14 vigencia 30-jun-2027 + Art. 25 §1 vigencia 31-ene-2027), R-030 (validación en ingreso) |
| DOC-SES-007 | Día 4 Ciberseguridad | R-027 (estado actual sin cifrado/MFA), R-017 (refinamiento — ahora vinculado a IAM en curso) |
| DOC-SES-008 | Día 4 Infraestructura | R-028 (Activo-Activo en transición), R-032 (Innovación/Seguridad Nacional consulta), R-034 (CAPEX→OPEX), R-036 (DataPro estable) |
| DOC-SES-009 | Resumen Consolidado | R-026 (preferencias COBIS / descartes), R-021 (inventario completo satélite), R-029 (BPMs múltiples) |
| DOC-RFI-001 | RFI v1.0 | R-023, R-024, R-025, R-029, R-033 (FECI), R-031 (estructura PoC) |
| DOC-POC-001 | Ficha PoC v1.0 | R-031 (alcance único hipotecario), R-037 (SITECA en PoC) |

---

**Generated by**: ArcKit `/arckit:risk` command
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Evaluación Core Banking — Caja de Ahorros, Panamá (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: v2.0 refresh — incorpora las 8 sesiones presenciales de evaluación (25–28 mayo 2026, DOC-SES-001..009), el RFI v1.0 (DOC-RFI-001), la ficha técnica de PoC v1.0 (DOC-POC-001) y el refresh de REQ v2.0. Cobertura ampliada de 22 → 37 riesgos. **15 riesgos nuevos** + **5 riesgos revisados**. Perfil residual: 1 Alto (R-024 ERP), 28 Medio, 8 Bajo.
