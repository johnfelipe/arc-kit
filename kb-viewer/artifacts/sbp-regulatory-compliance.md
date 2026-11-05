# Tech Note: SBP Regulatory Compliance for Core Banking — Panamá

> **Template Origin**: Official | **ArcKit Version**: 5.0.1 | **Comando**: `/arckit:research`

## Document Control

| Campo | Valor |
|-------|-------|
| Document ID | ARC-001-TECH-sbp-regulatory-compliance-v1.0 |
| Document Type | Tech Note |
| Project | 001-evaluacion-core-banking (Caja de Ahorros) |
| Classification | OFFICIAL |
| Status | DRAFT |
| Version | 1.0 |
| Created Date | 2026-05-19 |
| Last Updated | 2026-05-19 |
| Owner | Cumplimiento + Innovación |

---

## Summary

El cumplimiento regulatorio panameño para Core Banking se articula sobre dos pilares interrelacionados: (a) los **Acuerdos SBP** (Superintendencia de Bancos de Panamá) que regulan riesgo de crédito, liquidez, operacional, ciberseguridad y consolidación; y (b) el **SEI** (Sistema de Envío de Información) que es el portal oficial de la SBP para envío de reportes en XML estructurado con esquemas XSD, validaciones automáticas en tres capas y workflow de roles (Administrador / Preparador / Revisor / Firmante). Caja de Ahorros, bajo **Ley 20 de 1975**, no opera bajo licencia bancaria SBP pero sí está sujeta a reportería estadística, AML/FT y prudencial equivalente a la banca privada. Adicionalmente debe cumplir reportería a la **UAF** (ROS), **FATCA / CRS**, y normas contables NIIF con adaptaciones SBP incluyendo el **modelo dual obligatorio NIIF 9 + Acuerdo 6-2000**.

## Key Findings

### Acuerdos SBP Aplicables al Diseño del Core

- **Acuerdo 4-2013** — coeficientes de liquidez obligatorios. LCR mensual al 15to día hábil; posición de liquidez diaria antes del mediodía del día hábil siguiente.
- **Acuerdo 6-2000** (con modificaciones 2008 y 2020) — clasificación de cartera A–E y provisiones mínimas 1%, 5%, 25%, 50%, 100%. Incluye clasificación por capacidad de pago con justificación auditada; contagio inter-crédito automatizado; integración con Central de Riesgos.
- **Acuerdo 5-2011** — bienes adjudicados (dación en pago) y activos fuera de uso. Valorización, deterioro, plazos de realización.
- **Acuerdo 3-2009** — consolidación de estados financieros de grupos bancarios.
- **Acuerdo 8-2010** — instrumentos financieros derivados y registro contable.
- **Resolución SBP-DJ-0014** — formato estándar de envío electrónico de información contable.
- **Acuerdo 11-2018** (sustituye 007-2011, vigencia desde 2019-12-31) — riesgo operacional. BCP testing anual obligatorio, base de datos de eventos extendida, RWA operacional, capital requirements operacionales. Reporte anual al SBP enero 31.
- **Acuerdos 2025-2026** — vigilar publicaciones SBP que pueden modificar requisitos durante implementación; activar cláusula NFR-C-010 (cumplimiento regulatorio continuo sin cobros extra).

### Modelo Dual NIIF 9 + Acuerdo 6-2000

- El banco DEBE correr **simultáneamente** los modelos NIIF 9 ECL (stages 1/2/3 con PD/LGD/EAD) y la clasificación Acuerdo 6-2000 (A–E).
- Registra mensualmente el **mayor de los dos** en P&L.
- La **diferencia** se contabiliza como **reserva regulatoria en patrimonio** sin pasar por resultados, reduciendo el capital Tier 1 computable.
- **Umbral SICR parametrizable** (default: 30 días de mora como presunción refutable; o degradación ≥ 2 grados en calificación interna).
- Series históricas ≥ 5-7 años por segmento de cartera para calibrar PD/LGD/EAD.
- **Implicación para Core**: el vendor DEBE soportar ambos modelos con corrida paralela y consolidación automática; vendors Tier-1 (Finacle, Temenos, FLEXCUBE, TCS BaNCS) tienen módulos NIIF 9 maduros adaptables a la tabla A–E SBP. Vendors Tier-2 (Cobis Topaz, Datapro) requieren demo específica del modelo dual.

### SEI (Sistema de Envío de Información SBP)

- Portal web oficial SBP para envío de toda la reportería periódica.
- Formato principal: **XML estructurado contra esquemas XSD publicados por la SBP**; también Excel/CSV estructurado y formularios web.
- **Roles jerárquicos obligatorios**: Administrador (configura usuarios), Preparador (genera reporte), Revisor (valida), Firmante (firma digital y envía — debe tener poderes: Gerente de Riesgos, Contralor o CFO).
- **Validaciones automáticas SBP en tres capas**: (1) estructura XML contra XSD, (2) aritmética (sumas, totales), (3) consistencia histórica (variaciones > 15% mes a mes generan alerta y permiten adjuntar narrativa).
- Acuse de recibo con **número de radicación** — debe almacenarse junto al dato fuente como evidencia inmutable.
- **Implicación para Core**: ningún vendor global tiene conector SEI nativo. **Todos requieren proyecto de integración**: generación de XML válido + workflow Preparador/Revisor/Firmante + firma digital + almacenamiento de radicación + pre-validación local que reproduzca las 3 capas SEI. Estimación: 6-12 semanas de SI por reporte tipo del inventario D04.
- **Evolución prevista hacia XBRL** — vigilar roadmap SBP, planificar Fase 2.

### Reportería UAF (AML/FT)

- ROS (Reportes de Operaciones Sospechosas) generados desde monitoreo AML **en tiempo real**, no batch.
- Workflow con escalamiento y aprobación documentada.
- Evidencia inmutable (WORM o equivalente).
- **Reportería sin distinción respecto a banca privada** aun para Caja de Ahorros bajo Ley 20.

### FATCA + CRS

- Identificación de US persons (FATCA) y reportables CRS durante apertura y revisión periódica.
- Reportes en formatos requeridos por IRS y autoridad fiscal local (DGI Panamá → OCDE).
- Soporte nativo requerido (NFR-C-003).

### Plan de Cuentas SBP

- Estandarizado con grupos 1xx Activos / 2xx Pasivos / 3xx Patrimonio / 4xx Ingresos / 5xx Gastos / 6xx Contingentes y de orden.
- **Códigos asignados por SBP no modificables unilateralmente** por el banco (NFR-C-006).
- Cada operación del Core debe mapearse a una cuenta válida.

### Implicaciones por Vendor

| Aspecto | Tier-1 Global | Tier-2 Regional | Datapro Incumbente |
|---------|---------------|-----------------|--------------------|
| Modelo dual NIIF 9 + 6-2000 | Módulo NIIF 9 maduro; tabla A–E adaptable con parametrización | Requiere demo específica del modelo dual completo | Mejorable; exigir corrida paralela demostrada |
| Plan de cuentas SBP | Cargable como tabla maestra; mapeo configurable | Familiar (clientes locales) | Ya implementado |
| Reportería SEI | Requiere proyecto integración (todos) | Familiar a SEI (Cobis 7 clientes PA) | Ya implementado |
| AML real-time a UAF | Módulo maduro Tier-1 | Cobis tiene fraud/AML suite; validar latencia < 200ms | Validar capacidad real-time |
| FATCA / CRS | Nativo | Validar | Validar |
| Acuerdo 11-2018 (RO) | BCP testing soportable; BD de eventos requiere módulo de riesgo operacional | Validar | Validar |

## Relevance to Projects

- **Project 001 — Caja de Ahorros — Evaluación y Selección de Core Banking** (Panamá, 2026): regulación de referencia obligatoria para criba MUST_HAVE de RFP.

## External References

| Citation ID | Source | Description |
|-------------|--------|-------------|
| SBP Acuerdo 11-2018 | <https://www.superbancos.gob.pa/documentos/leyes_y_regulaciones/acuerdos/2018/Acuerdo_11-2018.pdf> | Riesgo operacional vigente |
| SBP Acuerdos | <https://www.superbancos.gob.pa/acuerdos/bancarios> | Inventario completo de Acuerdos SBP |
| ARC-000-PRIN-v1.1 | `projects/000-global/ARC-000-PRIN-v1.1.md` | Resumen regulatorio SBP completo, citas DOC-CB-003-Cn |
| ARC-001-REQ-v1.0 | `projects/001-evaluacion-core-banking/ARC-001-REQ-v1.0.md` | Requisitos BR-002, BR-005, FR-026..033, NFR-C-001..010 |

---

**Generated by**: ArcKit `/arckit:research` agent
**Generated on**: 2026-05-19
**ArcKit Version**: 5.0.1
**Project**: Caja de Ahorros (Project 001)
**AI Model**: claude-opus-4-7 (1M context)
