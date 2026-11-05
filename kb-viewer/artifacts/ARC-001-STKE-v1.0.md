# Análisis de Stakeholders: Drivers, Metas y Resultados — Evaluación y Selección de Core Banking

> **Origen de la plantilla**: Oficial | **Versión ArcKit**: 5.0.1 | **Comando**: `/arckit:stakeholders`

## Document Control

| Campo | Valor |
|-------|-------|
| Document ID | ARC-001-STKE-v1.0 |
| Document Type | Stakeholder Drivers & Goals Analysis |
| Project | 001-evaluacion-core-banking (Caja de Ahorros — Evaluación y Selección de Core Banking) |
| Classification | OFFICIAL-SENSITIVE (equivalente a "CONFIDENCIAL – Uso interno" del relevamiento fuente) |
| Status | DRAFT |
| Version | 1.0 |
| Created Date | 2026-05-19 |
| Last Modified | 2026-05-19 |
| Review Cycle | Trimestral durante la fase de selección; semestral a partir del go-live |
| Next Review Date | 2026-08-19 |
| Owner | Aldo Ríos — Gerencia de Innovación / Líder de Programa Core Banking |
| Reviewed By | Pendiente (Gerencia General, Comité de Tecnología) |
| Approved By | Pendiente (Junta Directiva) |
| Distribution | Junta Directiva, Gerencia General, Comité de Tecnología, Cumplimiento, Riesgos, Auditoría Interna, TI, Operaciones, Finanzas, áreas de negocio (Hipotecas, Créditos, Digital), CISO, Legal, RRHH, PMO, vendors finalistas (bajo NDA) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-05-19 | ArcKit AI | Creación inicial mediante `/arckit:stakeholders`. Identificación de 27 stakeholders (18 internos + 9 externos), 17 drivers, 10 metas y 10 resultados medibles. Alineado a los principios ARC-000-PRIN-v1.1 y al relevamiento confidencial DOC-CB-001/002/003. | PENDIENTE | PENDIENTE |

---

## Resumen Ejecutivo

### Propósito

Este documento identifica a los actores clave del programa de **evaluación, selección e implementación del nuevo Core Banking de Caja de Ahorros**, sus motivaciones subyacentes (drivers), cómo se traducen en metas concretas y qué resultados medibles satisfacen a cada parte interesada. Asegura alineación, hace explícitos los conflictos y proporciona trazabilidad desde las preocupaciones individuales hasta las métricas de éxito del programa.

### Hallazgos clave

1. **El programa tiene un patrocinio fuerte y convergente** entre Junta Directiva, Gerencia General e Innovación: el reemplazo del Core es la palanca de la agenda digital y de la sostenibilidad operacional del banco más grande del Estado [DOC-CB-001-C6].
2. **El cumplimiento regulatorio es el driver dominante por encima del precio**: la integración nativa con el SEI de la SBP, el modelo dual de provisiones NIIF 9 + Acuerdo 6-2000 y la reportería UAF son condiciones eliminatorias en la evaluación [DOC-CB-001-C2, DOC-CB-003-C10, DOC-CB-003-C23].
3. **Existen tensiones reales entre velocidad (Gerencia General, Innovación) y prudencia (Operaciones, Riesgos, Contraloría)**, y entre **costo TCO (Finanzas) y exhaustividad de controles (Cumplimiento, CISO, Riesgos)**. Se documentan y se proponen estrategias de resolución (Sección "Análisis de conflictos").

### Factores Críticos de Éxito (CSF)

- **CSF-1**: Mantener la operación del Core actual sin degradación durante el proceso de selección y migración — cualquier incidente público durante el cambio puede activar fiscalización política (Asamblea Nacional, Contraloría) [DOC-CB-003-C6].
- **CSF-2**: Que el vendor finalista demuestre **integración nativa con SEI, plan de cuentas SBP, NIIF 9 + Acuerdo 6-2000 dual y soporte de productos sociales** desde la fase de PoC, no en compromiso futuro [DOC-CB-001-C2, DOC-CB-003-C7, DOC-CB-003-C10].
- **CSF-3**: Que la contratación cumpla la Ley 22 de Contrataciones Públicas sin observaciones de Contraloría, con dictamen legal previo sobre soberanía de datos [DOC-CB-001-C9, DOC-CB-001-C10].
- **CSF-4**: Que la **agenda digital activa (Super App, Yappy, A.N.D.R.E.A., Caja Amiga) no se detenga** durante el reemplazo del Core [DOC-CB-001-C6, DOC-CB-001-C7].
- **CSF-5**: Adopción del personal: capacitación en español, soporte local 24/7, gestión del cambio para las áreas de Hipotecas, Créditos y Operaciones [DOC-CB-001-C29].

### Puntuación de Alineación de Stakeholders

**Alineación general**: **MEDIA-ALTA**

El núcleo ejecutivo (Junta Directiva, Gerencia General, Innovación, TI, Cumplimiento) está alineado en la necesidad y urgencia del reemplazo. Las tensiones residen en (a) costo vs control, (b) velocidad vs cautela, y (c) cloud público vs soberanía de datos. Son tensiones gestionables mediante una estrategia de RFP con criterios eliminatorios claros y un PoC robusto. Los stakeholders externos (SBP, Contraloría, UAF) están en modo "Keep Satisfied" — no impulsan, pero pueden detener.

---

## Identificación de Stakeholders

### Stakeholders Internos

| Stakeholder | Rol / Área | Influencia | Interés | Estrategia de Engagement |
|-------------|-----------|-----------|---------|--------------------------|
| Junta Directiva | Gobierno corporativo / autoridad final | ALTA | ALTA | Reporte mensual + decisiones de gates (RFP, short-list, contrato, go-live) |
| Gerencia General | Sponsor ejecutivo del programa | ALTA | ALTA | Reunión semanal de seguimiento; aprobación de hitos |
| Aldo Ríos — Gerencia de Innovación | Líder del programa / dueño del documento | ALTA | ALTA | Implicación diaria; backlog y agenda del programa |
| Gerencia de Tecnología (TI) | Dueño técnico del Core actual y futuro | ALTA | ALTA | Implicación diaria; decisiones de arquitectura |
| Cumplimiento | Riesgo regulatorio (SBP, UAF, FATF, FATCA, CRS) | ALTA | ALTA | Compuertas de aprobación regulatoria por hito |
| Operaciones | Continuidad del negocio y de pagos | ALTA | ALTA | Reuniones de readiness; participación en pruebas |
| Finanzas | Control TCO, presupuesto, cumplimiento de Ley 22 | ALTA | ALTA | Aprobaciones de checkpoint presupuestario |
| Riesgos | Riesgo operacional, crediticio, de proveedor | ALTA | MEDIA | Revisión de modelos NIIF 9 / 6-2000 y plan de migración |
| CISO / Seguridad de la Información | Seguridad por diseño, controles, zero trust | ALTA | MEDIA | Threat model, pen-tests, controles obligatorios |
| Auditoría Interna | Aseguramiento del control y proceso | ALTA | MEDIA | Revisión de proceso y trazabilidad |
| Legal | Contratos, soberanía de datos, dictámenes | ALTA | MEDIA | Dictamen de residencia de datos pre-RFP; revisión contractual |
| Hipotecas | Área de negocio — cartera B/. 2,945M, 69,821 hipotecas activas, 65.4% subsidiadas [DOC-CB-001-C3] | MEDIA | ALTA | Workshops de requerimientos; validación de demos |
| Créditos | Área de negocio — préstamos B/. 4,943M, FGA, Profimype [DOC-CB-001-C3, DOC-CB-001-C18] | MEDIA | ALTA | Workshops de requerimientos; validación de demos |
| Digital — Super App / A.N.D.R.E.A. | Canales digitales y plataformas de IA premiadas [DOC-CB-001-C6] | MEDIA | ALTA | Definición de contratos de API; revisión de integraciones |
| Red Caja Amiga / Sucursales rurales | Canal de inclusión financiera y comarcas [DOC-CB-001-C23, DOC-CB-001-C24] | BAJA | ALTA | Pruebas de modo degradado; capacitación |
| RRHH / Cambio Organizacional | Gestión del cambio, capacitación | MEDIA | MEDIA | Plan de adopción y comunicaciones internas |
| PMO | Coordinación del programa, riesgos, dependencias | MEDIA | ALTA | Tablero de programa; cadencia quincenal |
| Comunicaciones / Marketing | Mensaje al cliente final durante migración | BAJA | MEDIA | Plan de comunicación con hitos clave |

### Stakeholders Externos

| Stakeholder | Organización | Relación | Influencia | Interés |
|-------------|-------------|---------|-----------|---------|
| SBP — Superintendencia de Bancos | Regulador (supervisión coordinada bajo Ley 20 de 1975) [DOC-CB-003-C2] | Supervisor | ALTA | ALTA |
| UAF — Unidad de Análisis Financiero | Receptor de ROS AML/FT [DOC-CB-003-C5] | Supervisor | ALTA | MEDIA |
| Contraloría General de la República | Auditor de contratos y sistemas de entidades estatales [DOC-CB-001-C9, DOC-CB-003-C6] | Supervisor / auditor | ALTA | ALTA |
| Asamblea Nacional | Fiscalización política [DOC-CB-003-C6] | Político | MEDIA | MEDIA |
| MEF — Ministerio de Economía y Finanzas | Subsidios estatales, política presupuestaria | Político / regulatorio | MEDIA | MEDIA |
| MIVIOT — Vivienda | Reportería de cartera hipotecaria social | Receptor de reportes | BAJA | MEDIA |
| Clientes (más de 650,000) [DOC-CB-001-C3] | Usuarios finales | Beneficiarios | BAJA | ALTA |
| Vendor incumbente (Datapro / e-IBS) [DOC-CB-001-C1] | Proveedor del Core actual | Proveedor saliente | MEDIA | ALTA |
| Vendors finalistas (Core Banking candidatos) | Proveedores del nuevo Core | Proveedores entrantes | MEDIA | ALTA |
| Yappy / ACH Panamá / Telered | Operadores del ecosistema de pagos panameño [DOC-CB-001-C7] | Partners de integración | MEDIA | ALTA |
| Programa "Una Cuenta Para Todos" / AMPYME (Profimype) | Programas estatales [DOC-CB-001-C18, DOC-CB-001-C22] | Beneficiarios institucionales | BAJA | MEDIA |

### Power-Interest Grid

```text
                              INTERÉS
              Bajo                                     Alto
        ┌─────────────────────────────┬─────────────────────────────────┐
        │                             │                                 │
        │       KEEP SATISFIED        │        MANAGE CLOSELY           │
   Alto │                             │                                 │
        │  • CISO / Seguridad         │  • Junta Directiva              │
        │  • Riesgos                  │  • Gerencia General             │
        │  • Auditoría Interna        │  • Aldo Ríos (Innovación)       │
        │  • Legal                    │  • Gerencia de Tecnología (TI)  │
        │  • UAF (externo)            │  • Cumplimiento                 │
        │  • Asamblea Nacional        │  • Operaciones                  │
 P      │  • MEF                      │  • Finanzas                     │
 O      │                             │  • SBP (externo)                │
 D      │                             │  • Contraloría (externo)        │
 E      ├─────────────────────────────┼─────────────────────────────────┤
 R      │                             │                                 │
        │           MONITOR           │         KEEP INFORMED           │
   Bajo │                             │                                 │
        │  • MIVIOT                   │  • Hipotecas                    │
        │  • "Una Cuenta Para Todos"  │  • Créditos                     │
        │  • Comunicaciones (Mkt)     │  • Digital (Super App/A.N.D.)   │
        │                             │  • RRHH / Cambio                │
        │                             │  • Red Caja Amiga / sucursales  │
        │                             │  • Clientes (externo)           │
        │                             │  • PMO                          │
        │                             │  • Vendor incumbente            │
        │                             │  • Vendors finalistas           │
        │                             │  • Yappy / ACH / Telered        │
        │                             │                                 │
        └─────────────────────────────┴─────────────────────────────────┘
```

| Stakeholder | Poder | Interés | Cuadrante | Estrategia |
|-------------|-------|---------|-----------|-----------|
| Junta Directiva | ALTO | ALTO | Manage Closely | Reporte mensual + aprobaciones de gates |
| Gerencia General | ALTO | ALTO | Manage Closely | Comité ejecutivo semanal |
| Aldo Ríos — Innovación | ALTO | ALTO | Manage Closely | Implicación diaria; dueño del documento |
| TI (Gerencia de Tecnología) | ALTO | ALTO | Manage Closely | Implicación diaria; lead técnico |
| Cumplimiento | ALTO | ALTO | Manage Closely | Compuertas regulatorias por hito |
| Operaciones | ALTO | ALTO | Manage Closely | Readiness reviews por release |
| Finanzas | ALTO | ALTO | Manage Closely | Checkpoint presupuestario quincenal |
| SBP (externo) | ALTO | ALTO | Manage Closely | Coordinación vía liaison; SEI sandbox |
| Contraloría (externo) | ALTO | ALTO | Manage Closely | Plan de contratación pública aprobado |
| CISO / Seguridad | ALTO | MEDIO | Keep Satisfied | Reviews de seguridad por hito |
| Riesgos | ALTO | MEDIO | Keep Satisfied | Revisión de modelos y migración |
| Auditoría Interna | ALTO | MEDIO | Keep Satisfied | Acceso a evidencia y trazabilidad |
| Legal | ALTO | MEDIO | Keep Satisfied | Dictamen pre-RFP + revisión contrato |
| UAF (externo) | ALTO | MEDIO | Keep Satisfied | Coordinación AML/ROS sin interrupción |
| Asamblea Nacional | MEDIO | MEDIO | Monitor / Satisfied | Reportería política transparente |
| MEF | MEDIO | MEDIO | Keep Informed | Reportería de subsidios alineada |
| MIVIOT | BAJO | MEDIO | Monitor | Reportería hipotecaria automática |
| Hipotecas (negocio) | MEDIO | ALTO | Keep Informed | Workshops + UAT |
| Créditos (negocio) | MEDIO | ALTO | Keep Informed | Workshops + UAT |
| Digital — Super App / A.N.D.R.E.A. | MEDIO | ALTO | Keep Informed | Contratos de API + integration testing |
| Red Caja Amiga / sucursales rurales | BAJO | ALTO | Keep Informed | Pruebas de modo degradado |
| RRHH / Cambio | MEDIO | MEDIO | Keep Informed | Plan de adopción |
| PMO | MEDIO | ALTO | Keep Informed | Tablero de programa quincenal |
| Clientes (externo) | BAJO | ALTO | Keep Informed | Comunicación pública por hito de migración |
| Vendor incumbente (Datapro) | MEDIO | ALTO | Keep Informed | Plan de salida y conocimiento; clauses contractuales |
| Vendors finalistas | MEDIO | ALTO | Keep Informed | RFP, PoC, negociación contractual |
| Yappy / ACH / Telered | MEDIO | ALTO | Keep Informed | Plan de integración + pruebas paralelas |

---

## Análisis de Drivers de Stakeholders

### SD-1: Junta Directiva — Sostenibilidad institucional y reputación AAA(pan)

**Stakeholder**: Junta Directiva de Caja de Ahorros

**Categoría**: STRATEGIC + RISK

**Driver**: Garantizar que Caja de Ahorros mantenga su rol estratégico como "Banco de la Familia Panameña" y su calificación AAA(pan) con perspectiva estable [DOC-CB-001-C3] tras el reemplazo del Core. Una migración fallida o un incidente de cumplimiento pondría en cuestión la idoneidad del gobierno corporativo ante Contraloría, Asamblea Nacional y el público.

**Contexto**: Caja de Ahorros es un banco del Estado bajo Ley 20 de 1975 [DOC-CB-003-C1], con un esquema de rendición de cuentas paralelo al de la banca privada (Contraloría + Asamblea) [DOC-CB-003-C6]. El programa de Core Banking es el contrato tecnológico más visible del banco y será auditado por la Contraloría [DOC-CB-001-C9].

**Intensidad**: CRÍTICA

**Enablers**: gobernanza clara del programa, evidencia regulatoria sólida, dictamen legal previo, calificación crediticia sostenida.

**Blockers**: incidentes públicos durante la migración, observaciones de Contraloría, sanciones SBP, descontinuación de productos sociales.

**Stakeholders relacionados**: Gerencia General (SD-2), Contraloría (SD-10), Asamblea Nacional.

---

### SD-2: Gerencia General — Modernización del Core sin disrupción operacional

**Stakeholder**: Gerencia General

**Categoría**: STRATEGIC + OPERATIONAL

**Driver**: Reemplazar el Core actual (Datapro / e-IBS) [DOC-CB-001-C1] por una plataforma moderna que habilite — y no frene — la agenda digital activa del banco (Super App, Yappy, A.N.D.R.E.A., Caja Amiga) [DOC-CB-001-C6], cumpliendo los plazos y el presupuesto aprobado por la Junta, sin disrupción al cliente final.

**Contexto**: La agenda digital de Caja de Ahorros es una de las más activas del sistema bancario panameño y un diferenciador competitivo. La modernización del Core es habilitador transversal: si se detiene, se detienen Hipotecas, Créditos, Digital y la reportería SBP simultáneamente.

**Intensidad**: CRÍTICA

**Enablers**: PoC robusto, plan de migración por fases, comunicación interna efectiva, vendor con presencia regional.

**Blockers**: parálisis por análisis, falta de consenso entre áreas, retraso por contrataciones públicas (Ley 22).

**Stakeholders relacionados**: Junta Directiva (SD-1), Innovación (SD-3), TI (SD-5), Digital (SD-13).

---

### SD-3: Aldo Ríos — Liderar la transformación tecnológica del banco

**Stakeholder**: Aldo Ríos — Gerencia de Innovación

**Categoría**: STRATEGIC + PERSONAL

**Driver**: Capitalizar el momento de transformación digital (A.N.D.R.E.A. premiada en Fintech Américas 2025, Super App, Yappy integrando 55+ instituciones [DOC-CB-001-C7]) para entregar un Core que sustente la próxima década del banco. Liderar este programa con éxito tiene impacto en su reputación profesional y en la posición de Innovación como área tractora del banco.

**Contexto**: El líder del programa carga con la coordinación entre TI, Negocio, Cumplimiento y Vendors; el éxito se medirá en disponibilidad, cumplimiento regulatorio y costo dentro del plan.

**Intensidad**: ALTA

**Enablers**: equipo de programa con seniority adecuado, autoridad delegada por la JD, presupuesto del programa aprobado en bloque, herramientas de gobernanza (ArcKit).

**Blockers**: micro-gestión por comités, decisiones tomadas fuera del programa, dilución de autoridad.

**Stakeholders relacionados**: Gerencia General (SD-2), TI (SD-5), Digital (SD-13), PMO.

---

### SD-4: Finanzas — Control de TCO y presupuesto público auditable

**Stakeholder**: Finanzas

**Categoría**: FINANCIAL

**Driver**: Mantener el costo total de propiedad (TCO) del nuevo Core dentro del presupuesto aprobado por la JD a 7 años, con visibilidad ex-ante sobre costos recurrentes (licenciamiento, mantenimiento, soporte, infraestructura, módulos opcionales). Como entidad estatal sujeta a la Ley 22 de Contrataciones Públicas y a auditoría de la Contraloría, **el costo no auditable o no presupuestado es inaceptable**.

**Contexto**: Los Core SaaS de gran escala suelen tener costos crecientes vinculados a transacciones procesadas, módulos opcionales y "true-up" anuales. La transparencia ex-ante en el contrato es esencial.

**Intensidad**: ALTA

**Enablers**: cláusulas contractuales claras de TCO, comparativos benchmark con Banco Nacional y otros bancos estatales, opciones eliminadas o escaladas controladas.

**Blockers**: módulos opcionales no listados, cláusulas de incremento automático sin tope, dependencia de licencias atadas a métricas no controladas por el banco.

**Stakeholders relacionados**: Junta Directiva (SD-1), Gerencia General (SD-2), Contraloría (SD-10).

---

### SD-5: TI (Gerencia de Tecnología) — Integración limpia con el ecosistema existente

**Stakeholder**: Gerencia de Tecnología (TI)

**Categoría**: OPERATIONAL

**Driver**: Que el nuevo Core se integre **sin reescrituras masivas** con el ecosistema actual: middleware / API Gateway existente [DOC-CB-001-C21], canales Yappy / ACH Panamá / Telered / switch de ATMs [DOC-CB-001-C7], banca digital, A.N.D.R.E.A., y sistemas satélite (Profimype, sistemas hipotecarios auxiliares) [DOC-CB-001-C18, DOC-CB-001-C19].

**Contexto**: TI tiene un mapa de integraciones complejo y un equipo limitado. Cada integración que requiere desarrollo a medida del banco aumenta el riesgo y el plazo. El acceso directo a la base de datos del Core entre sistemas está explícitamente prohibido por el Principio 11 (PRIN v1.1).

**Intensidad**: ALTA

**Enablers**: APIs publicadas con OpenAPI / AsyncAPI; documentación técnica completa en español; ambiente sandbox del vendor.

**Blockers**: Core con interfaces propietarias mal documentadas; obligación de acceso directo a tablas; vendor sin presencia local de soporte.

**Stakeholders relacionados**: Digital (SD-13), Operaciones (SD-8), vendors finalistas.

---

### SD-6: CISO / Seguridad de la Información — Cumplimiento de Zero Trust y SBP de ciberseguridad

**Stakeholder**: CISO / Seguridad de la Información

**Categoría**: COMPLIANCE + RISK

**Driver**: Implementar los controles obligatorios del Principio 4 (Seguridad por Diseño, no negociable): MFA, mTLS, secretos en bóveda, cifrado en tránsito y reposo, monitoreo AML/UAF en tiempo real, pruebas de penetración anuales, sin excepciones. El CISO firma riesgos residuales y responde ante la SBP por incidentes de ciberseguridad.

**Contexto**: La SBP publicó Acuerdos de gestión de riesgo operacional y ciberseguridad que aplican incluso bajo supervisión coordinada de bancos estatales. Un incidente de seguridad en el Core de un banco del Estado tiene visibilidad política inmediata.

**Intensidad**: CRÍTICA

**Enablers**: vendor con certificaciones reconocidas (ISO 27001 / SOC 2), pen-tests independientes, bóveda de secretos integrada, monitoreo centralizado.

**Blockers**: vendor con prácticas opacas, dependencia de personal del vendor con acceso privilegiado no auditado, integraciones con plain-text legacy.

**Stakeholders relacionados**: Cumplimiento (SD-7), Riesgos (SD-14), Auditoría Interna.

---

### SD-7: Cumplimiento — SBP, AML/UAF, FATF, FATCA, CRS sin interrupción

**Stakeholder**: Cumplimiento

**Categoría**: COMPLIANCE

**Driver**: Que la totalidad de la reportería SBP, UAF, FATCA y CRS siga generándose y enviándose por el SEI **desde el día 1** del nuevo Core, sin pérdida ni degradación. Una falla de reportería pone al banco en falta ante la SBP y la UAF, con consecuencias que escalan desde sanciones hasta restricciones operativas [DOC-CB-001-C2, DOC-CB-003-C5].

**Contexto**: Caja de Ahorros, aun operando bajo Ley 20 de 1975 con supervisión coordinada [DOC-CB-003-C2], **reporta a la SBP y a la UAF en igual medida que la banca privada** en lo estadístico, AML/FT y de tasas [DOC-CB-003-C5]. El SEI es la plataforma única de envío [DOC-CB-003-C23] con tres niveles de validación automática y firma digital obligatoria [DOC-CB-003-C24, DOC-CB-003-C26].

**Intensidad**: CRÍTICA

**Enablers**: integración nativa con SEI (XML/XSD), workflow Preparador/Revisor/Firmante alineado, modelo dual de provisiones NIIF 9 + Acuerdo 6-2000 [DOC-CB-003-C10], pre-validación local que reproduce las tres capas del SEI.

**Blockers**: vendor que ofrece "personalización futura" en vez de soporte nativo, plan de paralelo regulatorio inexistente, dependencia de servicios manuales para reportería.

**Stakeholders relacionados**: SBP (SD-9), UAF (SD-16), Riesgos (SD-14), Auditoría Interna, Contraloría (SD-10).

---

### SD-8: Operaciones — Continuidad del negocio 24/7

**Stakeholder**: Operaciones

**Categoría**: OPERATIONAL + RISK

**Driver**: Mantener la disponibilidad de canales digitales y pagos en ≥ 99.95% mensual durante y después de la migración. Las ventanas de mantenimiento no pueden coincidir con fin de mes, pago de planilla del sector público, fin de año ni días festivos nacionales [DOC-CB-001-C4]. Cualquier indisponicidad de la Super App, Yappy o ATMs es visible para 650,000+ clientes y para el ecosistema panameño de pagos (Yappy integra 55+ instituciones [DOC-CB-001-C7]).

**Contexto**: Operaciones es el área que recibe primero las quejas y absorbe el costo reputacional de cualquier interrupción. Es el área natural más conservadora ante el cambio.

**Intensidad**: CRÍTICA

**Enablers**: topología activo-activo o activo-pasivo con conmutación automática, rolling deployment / blue-green, plan de paralelo con vendor incumbente, calendario de ventanas bloqueado por Negocio.

**Blockers**: vendor sin SLA contractual ≥ 99.95%, planes de migración con cortes "big-bang", falta de personal local de soporte en español.

**Stakeholders relacionados**: TI (SD-5), Digital (SD-13), CISO (SD-6), Clientes (SD-15).

---

### SD-9: SBP (Superintendencia de Bancos) — Reportería conforme y a tiempo

**Stakeholder**: SBP — vía liaison interna y a través del SEI

**Categoría**: COMPLIANCE (driver externo)

**Driver**: Recibir toda la información estadística, prudencial, AML y de tasas conforme a Acuerdos vigentes, en los formatos y fechas límite del SEI [DOC-CB-003-C28], con plan de cuentas SBP estandarizado [DOC-CB-003-C7] y modelo contable NIIF + adaptaciones regulatorias [DOC-CB-003-C9].

**Contexto**: La SBP supervisa a Caja de Ahorros de forma coordinada/limitada por su naturaleza estatal [DOC-CB-003-C2], pero exige la misma reportería estadística y AML que a la banca privada [DOC-CB-003-C5]. En inspecciones in-situ, los examinadores toman muestra de cartera y replican la clasificación A–E [DOC-CB-003-C18]; diferencias sistemáticas con la clasificación del banco derivan en observaciones formales y provisiones adicionales.

**Intensidad**: ALTA

**Enablers**: integración SEI nativa, contagio inter-crédito automatizado [DOC-CB-003-C20], garantías y haircuts aplicados según SBP [DOC-CB-003-C21], capacidad XBRL [DOC-CB-003-C29].

**Blockers**: clasificación divergente del Acuerdo 6-2000, ausencia de capacidad XML/XSD nativa, integraciones manuales propensas a error.

**Stakeholders relacionados**: Cumplimiento (SD-7), Riesgos (SD-14), Contraloría (SD-10).

---

### SD-10: Contraloría General — Auditoría de contratos y sistemas estatales

**Stakeholder**: Contraloría General de la República

**Categoría**: COMPLIANCE + RISK (driver externo)

**Driver**: Verificar que la contratación del Core cumpla la Ley 22 de Contrataciones Públicas, que el contrato no contenga cláusulas lesivas para el Estado, que los pases a producción tengan controles auditables [DOC-CB-001-C26] y que el sistema seleccionado opere con trazabilidad contable suficiente para auditorías futuras [DOC-CB-001-C9].

**Contexto**: La Contraloría ejerce fiscalización sobre BNP y Caja de Ahorros que no aplica a la banca privada [DOC-CB-003-C6]. Es un esquema de rendición de cuentas paralelo y, en algunos aspectos, más exigente en transparencia pública.

**Intensidad**: ALTA

**Enablers**: proceso de RFP transparente y bien documentado, dictamen legal previo, contratos con cláusulas estándar, IaC versionado, pipeline CI/CD auditable.

**Blockers**: vendor sin capacidad de pasar requisitos de contratación pública [DOC-CB-001-C9], cambios manuales en producción, pases sin doble aprobación.

**Stakeholders relacionados**: Junta Directiva (SD-1), Finanzas (SD-4), Asamblea Nacional, SBP (SD-9).

---

### SD-11: Hipotecas — Cartera social y subsidio de Interés Preferencial

**Stakeholder**: Área de Hipotecas

**Categoría**: OPERATIONAL + CUSTOMER

**Driver**: Que el nuevo Core soporte la cartera hipotecaria de B/. 2,945M con 69,821 hipotecas activas, de las cuales 65.4% son hipotecas de Interés Preferencial [DOC-CB-001-C3]. El cálculo del subsidio estatal que asume el Gobierno DEBE ser automático y auditable [DOC-CB-001-C13]. Reestructuraciones, moratorias y períodos de gracia (incluidos los heredados de COVID-19) DEBEN reflejarse con exactitud contable [DOC-CB-001-C15, DOC-CB-003-C22].

**Contexto**: La cartera hipotecaria es el corazón del mandato social del banco. Una falla en cálculo de subsidio tiene impacto sobre MIVIOT y MEF y crea pasivo regulatorio.

**Intensidad**: ALTA

**Enablers**: parametrización nativa del Interés Preferencial sin desarrollo a medida, migración validada contra saldos del sistema legado, soporte de sistemas hipotecarios auxiliares para consolidación [DOC-CB-001-C19].

**Blockers**: vendor que requiere customización por código del banco para productos sociales [DOC-CB-001-C27], pérdida de historial en migración de hipotecas con condiciones especiales antiguas.

**Stakeholders relacionados**: Créditos (SD-12), MIVIOT, MEF, Riesgos (SD-14), Contraloría (SD-10).

---

### SD-12: Créditos — Modelo dual de provisiones y garantía estatal FGA

**Stakeholder**: Área de Créditos

**Categoría**: OPERATIONAL + COMPLIANCE

**Driver**: Que el nuevo Core soporte los créditos con garantía estatal del FGA con tratamiento contable y de provisión específico [DOC-CB-001-C14], los programas Profimype [DOC-CB-001-C18], los créditos verdes [DOC-CB-001-C28] y el modelo dual de provisiones **NIIF 9 ECL + Acuerdo 6-2000 A–E** [DOC-CB-003-C10, DOC-CB-003-C18] desde el día 1.

**Contexto**: El departamento de Créditos corre dos modelos de provisión en paralelo cada mes [DOC-CB-003-C17]: NIIF 9 con PD/LGD/EAD [DOC-CB-003-C16] y Acuerdo 6-2000 con tabla A–E (1%, 5%, 25%, 50%, 100%) [DOC-CB-003-C18], registrando el mayor; la diferencia va a reserva regulatoria en patrimonio sin pasar por resultados [DOC-CB-003-C17].

**Intensidad**: ALTA

**Enablers**: ejecución simultánea de los dos modelos demostrada por el vendor, soporte de contagio inter-crédito y por Central de Riesgos [DOC-CB-003-C20], umbral SICR parametrizable [DOC-CB-003-C15].

**Blockers**: vendor que ofrece solo modelo NIIF 9 con expectativa de "personalizar más tarde" el Acuerdo 6-2000.

**Stakeholders relacionados**: Hipotecas (SD-11), Riesgos (SD-14), Cumplimiento (SD-7).

---

### SD-13: Digital (Super App / A.N.D.R.E.A. / Yappy) — Continuidad de la agenda digital

**Stakeholder**: Banca Digital / Innovación de Producto

**Categoría**: STRATEGIC + CUSTOMER

**Driver**: Que el reemplazo del Core **no detenga** los lanzamientos digitales en curso. Yappy ya integra 55+ instituciones públicas y 1.6M usuarios [DOC-CB-001-C7]. A.N.D.R.E.A. (premiada Fintech Américas 2025) [DOC-CB-001-C6] y la Super App son canales principales. Las APIs hacia el Core DEBEN versionarse con compatibilidad hacia atrás durante toda la transición.

**Intensidad**: ALTA

**Enablers**: API Gateway / middleware existente como capa de abstracción [DOC-CB-001-C21], plan de migración con periodo de paralelo en producción controlada.

**Blockers**: requerimiento de reescritura masiva de integraciones, interrupciones de Yappy / ACH / Telered durante el corte.

**Stakeholders relacionados**: TI (SD-5), Operaciones (SD-8), Clientes (SD-15).

---

### SD-14: Riesgos — Modelo dual de provisiones y riesgo operacional de migración

**Stakeholder**: Riesgos

**Categoría**: RISK + COMPLIANCE

**Driver**: Validar que el modelo dual de provisiones NIIF 9 + Acuerdo 6-2000 produzca cifras coherentes contra el sistema actual antes del go-live, y que la migración (incluyendo hipotecas heredadas, restructuraciones COVID-19 [DOC-CB-001-C15] y créditos con condiciones especiales) no introduzca volatilidad espuria en provisiones. Adicionalmente, el área valida riesgos operacionales de migración (datos, integraciones, vendor lock-in).

**Intensidad**: ALTA

**Enablers**: corrida paralela de provisiones en pre-producción, modelos PD/LGD/EAD calibrados con series históricas ≥ 5-7 años [DOC-CB-003-C16], plan de migración con cortes incrementales.

**Blockers**: serie histórica corta de datos legacy [DOC-CB-001-C16], vendor con modelos cerrados (caja negra).

**Stakeholders relacionados**: Cumplimiento (SD-7), Créditos (SD-12), Auditoría Interna.

---

### SD-15: Clientes — Disponibilidad continua y experiencia consistente

**Stakeholder**: Clientes (más de 650,000)

**Categoría**: CUSTOMER

**Driver**: Acceder a sus saldos y mover dinero **sin interrupciones percibidas** durante todo el ciclo de reemplazo del Core. Recibir pagos sociales (Beca Universal, 120 a los 65, Red de Oportunidades) [DOC-CB-001-C5] en las fechas comprometidas. Que la Super App, Yappy, ATMs y sucursales sigan funcionando consistentemente.

**Intensidad**: ALTA

**Enablers**: comunicación proactiva, modo degradado bien definido, soporte al cliente reforzado durante hitos de migración.

**Blockers**: cortes inesperados, inconsistencia de saldos entre canales, retrasos en pagos sociales.

**Stakeholders relacionados**: Operaciones (SD-8), Digital (SD-13), Hipotecas (SD-11).

---

### SD-16: UAF — Reportes de Operaciones Sospechosas continuos

**Stakeholder**: UAF — Unidad de Análisis Financiero de Panamá (externo)

**Categoría**: COMPLIANCE (externo)

**Driver**: Recibir los ROS (Reportes de Operación Sospechosa) AML/FT del banco sin distinción respecto a la banca privada [DOC-CB-003-C5], con monitoreo de transacciones en tiempo real integrado al Core [DOC-CB-001-C8].

**Intensidad**: ALTA

**Enablers**: módulo AML integrado al Core nativamente, reglas configurables sin desarrollo, evidencia auditable de detección y escalamiento.

**Blockers**: detección AML por proceso batch nocturno (no real-time), falta de trazabilidad de evidencia.

**Stakeholders relacionados**: Cumplimiento (SD-7), CISO (SD-6).

---

### SD-17: Asamblea Nacional — Transparencia y valor por dinero del gasto estatal

**Stakeholder**: Asamblea Nacional

**Categoría**: POLITICAL (externo)

**Driver**: Ejercer fiscalización política sobre el uso de recursos en un banco del Estado [DOC-CB-003-C6]. Preguntas parlamentarias sobre costo, vendor, proceso de selección y disponibilidad son escenarios reales.

**Intensidad**: MEDIA

**Enablers**: dossier de transparencia público preparado, alineación con Contraloría, hitos comunicados públicamente.

**Blockers**: incidentes públicos, costos crecientes no presupuestados, vendor con conflicto de interés.

**Stakeholders relacionados**: Contraloría (SD-10), Junta Directiva (SD-1).

---

## Mapeo Driver → Meta

### G-1: Cumplimiento regulatorio nativo SBP/SEI/UAF al go-live

**Derivada de**: SD-7, SD-9, SD-14, SD-16, SD-1.

**Owner**: Cumplimiento (responsable) + Aldo Ríos / Innovación (rendición).

**Enunciado SMART**: Al go-live (T₀), el nuevo Core genera nativamente el 100% de los reportes SBP del inventario D04 [DOC-CB-001-C12] en formatos válidos para el SEI (XML/XSD), envía ROS a la UAF en tiempo real, y pasa las tres capas de validación SEI (estructura, aritmética, consistencia histórica) [DOC-CB-003-C26] en pre-producción durante al menos 3 ciclos mensuales consecutivos antes del corte.

**Por qué importa**: una interrupción de reportería expone al banco a sanciones SBP y a observaciones de Contraloría con impacto político.

**Métricas**:

- **Primaria**: % de reportes del inventario D04 generados nativamente y aceptados por el SEI = 100%.
- **Secundarias**: tiempo medio de envío al SEI (≤ 30 min antes de cada fecha límite), número de rechazos del SEI por trimestre (= 0 críticos), variaciones detectadas en consistencia histórica resueltas con explicación documentada.

**Baseline**: hoy, los reportes se generan desde Datapro / e-IBS con apoyo manual variable.

**Meta**: 100% nativo y aceptado por el SEI.

**Medición**: bitácora del SEI (número de radicación + resultado), reportes de Cumplimiento.

**Dependencias**: vendor con capacidad SEI demostrada en PoC; sandbox SBP disponible; inventario D04 cerrado y firmado por Cumplimiento.

**Riesgos**: vendor sub-estima esfuerzo de adaptación; cambios SBP durante el proyecto.

---

### G-2: TCO total a 7 años dentro del presupuesto aprobado (±10%)

**Derivada de**: SD-4, SD-1, SD-10.

**Owner**: Finanzas (responsable) + Gerencia General (rendición).

**Enunciado SMART**: El TCO contractual a 7 años (licenciamiento + mantenimiento + soporte + infraestructura + módulos opcionales + servicios profesionales de implementación) queda fijado al firmar el contrato dentro del rango ±10% del presupuesto aprobado por la JD, con cláusulas de límite a "true-ups" e incrementos anuales por inflación con tope.

**Por qué importa**: como entidad estatal, los costos extraordinarios no presupuestados son materia de observación de Contraloría y de cuestionamiento político.

**Métricas**: TCO contractual vs presupuesto; costos efectivos vs proyectados por trimestre; número de cambios contractuales que aumenten costo.

**Baseline**: presupuesto a aprobar por la JD (no público).

**Meta**: dentro del ±10%.

**Medición**: control presupuestario de Finanzas; auditoría anual de cumplimiento de cláusulas contractuales.

**Dependencias**: claridad del scope al RFP; vendor que acepta cláusulas de tope.

**Riesgos**: scope creep, dependencia de módulos opcionales no anticipados.

---

### G-3: Disponibilidad ≥ 99.95% mensual para canales digitales y pagos sostenida durante y después de migración

**Derivada de**: SD-8, SD-13, SD-15, SD-2.

**Owner**: Operaciones (responsable) + TI (apoyo).

**Enunciado SMART**: La disponibilidad mensual de Super App, Banca en Línea, ATMs y de las integraciones Yappy / ACH / Telered se mantiene ≥ 99.95% durante los 12 meses anteriores al corte, durante el período de migración y por al menos 12 meses posteriores al corte.

**Por qué importa**: protege la reputación del banco, la calificación AAA(pan) y el rol de Yappy en el ecosistema panameño de pagos.

**Métricas**: % uptime por canal y por mes; número de incidentes P1/P2; MTTR.

**Baseline**: nivel actual a confirmar con TI (objetivo ≥ 99.95%).

**Meta**: ≥ 99.95% mensual sostenido.

**Medición**: telemetría de Operaciones; reportes mensuales al Comité de Tecnología.

**Dependencias**: SLA contractual del vendor ≥ 99.95% con penalizaciones; topología activo-activo o activo-pasivo demostrada.

**Riesgos**: degradación durante el período de paralelo; falla de conmutación.

---

### G-4: Integración nativa con ecosistema panameño sin interrupciones durante migración

**Derivada de**: SD-5, SD-13, SD-2, SD-15.

**Owner**: TI (responsable) + Digital (apoyo).

**Enunciado SMART**: El nuevo Core integra Yappy, ACH Panamá, Telered (switch ATMs) y SWIFT (corresponsalías internacionales) demostrado en PoC; durante la migración, cero interrupciones de estas integraciones imputables al cambio.

**Por qué importa**: Yappy integra 55+ instituciones públicas; un corte impacta al ecosistema panameño.

**Métricas**: integración demostrada en PoC (binaria); número de interrupciones imputables al cambio (= 0); tiempo medio de paralelo por integración.

**Baseline**: integraciones operando actualmente vía middleware existente [DOC-CB-001-C21].

**Meta**: cero interrupciones.

**Medición**: tablero de incidentes durante migración; testing end-to-end pre-corte.

**Dependencias**: pre-validación de compatibilidad con cada partner; ambiente de paralelo en producción controlada.

**Riesgos**: cambios contractuales de Yappy/ACH/Telered durante el proyecto.

---

### G-5: Mandato social operativo al día 1 con cálculo automático del subsidio de Interés Preferencial

**Derivada de**: SD-11, SD-12, SD-15, SD-1.

**Owner**: Hipotecas + Créditos (responsables) + Cumplimiento (auditoría regulatoria).

**Enunciado SMART**: Al go-live, el 100% de los productos del mandato social — Interés Preferencial, FGA, Profimype, "Una Cuenta Para Todos", transferencias sociales, créditos verdes — están operativos y los cálculos del subsidio estatal son automáticos y auditables [DOC-CB-001-C13].

**Métricas**: % de productos sociales operativos; diferencias en cálculo de subsidio vs sistema legado (= 0 material).

**Baseline**: productos sociales operando hoy con diversos sistemas y procesos manuales.

**Meta**: 100% operativo con cálculo automático.

**Medición**: aceptación firmada por Hipotecas, Créditos y MEF; reportería MIVIOT generable nativamente.

**Dependencias**: vendor con parametrización demostrada en demo; migración validada contra sistema legado.

**Riesgos**: vendor estándar requiere desarrollo a medida para productos sociales (incompatible con Principio 20 PRIN v1.1).

---

### G-6: Modelo dual de provisiones NIIF 9 + Acuerdo 6-2000 automatizado

**Derivada de**: SD-14, SD-9, SD-12, SD-7.

**Owner**: Riesgos + Cumplimiento (responsables).

**Enunciado SMART**: Al go-live, el Core (o su entorno contable inmediato) ejecuta mensualmente y de forma automatizada los modelos NIIF 9 ECL en tres stages [DOC-CB-003-C14] y el Acuerdo 6-2000 con tabla A–E [DOC-CB-003-C18], registra el mayor y contabiliza la diferencia como reserva regulatoria en patrimonio sin pasar por resultados [DOC-CB-003-C17], con cero diferencias materiales contra una corrida paralela contra el legacy durante 3 meses consecutivos pre-corte.

**Métricas**: diferencias materiales contra legacy (= 0); tiempo de cálculo mensual; cobertura de contagio inter-crédito automatizado.

**Baseline**: hoy, doble corrida con apoyo manual y reconciliación.

**Meta**: cero diferencias materiales y proceso automatizado end-to-end.

**Medición**: reporte mensual de Riesgos; revisión de Auditoría Interna.

**Dependencias**: vendor con módulo de provisiones que ejecute ambos modelos simultáneamente; PD/LGD/EAD calibrados [DOC-CB-003-C16]; umbral SICR parametrizable [DOC-CB-003-C15].

**Riesgos**: vendor solo ofrece NIIF 9, no modelo regulatorio SBP.

---

### G-7: Soberanía de datos en Panamá validada legalmente

**Derivada de**: SD-7, SD-10, SD-1, SD-6.

**Owner**: Legal (responsable) + CISO (apoyo técnico).

**Enunciado SMART**: Antes del cierre del RFP, Legal emite dictamen firme sobre soberanía y residencia de datos personales, financieros y transaccionales en Panamá [DOC-CB-001-C10, DOC-CB-001-C11]; los vendors que no cumplan son eliminados del proceso.

**Métricas**: dictamen emitido (binaria); número de vendors finalistas que cumplen residencia.

**Baseline**: ausencia actual de dictamen formal.

**Meta**: dictamen firme + ≥ 2 vendors finalistas cumpliendo residencia.

**Medición**: documento legal firmado por Legal y respaldado por Contraloría.

**Dependencias**: claridad de directrices del MEF/Contraloría sobre cloud pública.

**Riesgos**: que la directriz emerja después del RFP y obligue a rediseño.

---

### G-8: Contratación pública aprobada sin observaciones de Contraloría

**Derivada de**: SD-10, SD-1, SD-2, SD-4.

**Owner**: Finanzas + Legal (responsables) + Aldo Ríos (rendición).

**Enunciado SMART**: El proceso de selección cumple Ley 22 de Contrataciones Públicas; el contrato firmado pasa auditoría de Contraloría sin observaciones materiales.

**Métricas**: observaciones de Contraloría (= 0 materiales); cumplimiento de pasos formales del proceso.

**Baseline**: proceso por definir.

**Meta**: cero observaciones materiales.

**Medición**: dictamen de Contraloría posterior a la firma.

**Dependencias**: vendors que pasen criterios de contratación pública [DOC-CB-001-C9].

**Riesgos**: descalificación de vendor preferido por incumplir requisitos formales.

---

### G-9: Migración con conciliación contable exacta y cero pérdida de datos

**Derivada de**: SD-5, SD-8, SD-14, SD-11, SD-12.

**Owner**: TI (responsable) + Riesgos + Auditoría Interna.

**Enunciado SMART**: La migración valida saldo-por-saldo (depósitos, cartera, hipotecas, garantías) contra el sistema legado, con diferencias = 0 al cierre del corte; las hipotecas con condiciones especiales antiguas (subsidios, moratorias COVID-19 [DOC-CB-001-C15]) preservan su trazabilidad histórica.

**Métricas**: diferencias de saldo (= 0); registros migrados / registros origen (= 100%).

**Baseline**: N/A (pre-migración).

**Meta**: cero diferencias y 100% de cobertura.

**Medición**: reporte de conciliación post-corte firmado por Auditoría Interna.

**Dependencias**: calidad y limpieza de datos legacy [DOC-CB-001-C16, DOC-CB-001-C17]; plan de migración con periodo de paralelo.

**Riesgos**: datos en hojas de cálculo / sistemas externos (Access, Excel) no detectados [DOC-CB-001-C20].

---

### G-10: Capacitación, gestión del cambio y comunicación al cliente

**Derivada de**: SD-2, SD-3, SD-8, SD-15, RRHH.

**Owner**: RRHH + Comunicaciones (responsables) + Aldo Ríos (rendición).

**Enunciado SMART**: 100% del personal de TI, Operaciones, Hipotecas, Créditos, Digital, Atención al Cliente y Cumplimiento capacitado en el nuevo Core en español antes del corte; plan de comunicación al cliente externo con hitos clave entregado.

**Métricas**: % de personal capacitado y certificado; NPS interno pre/post; reclamos del cliente externo durante migración.

**Baseline**: equipos actuales operando sobre Datapro / e-IBS.

**Meta**: 100% capacitado; sin caída significativa de NPS.

**Medición**: registros de RRHH; encuesta interna; reportes de Atención al Cliente.

**Dependencias**: vendor con plan formal de capacitación en español [DOC-CB-001-C29]; agenda de despliegue.

**Riesgos**: rotación de personal clave durante el proyecto; resistencia al cambio.

---

## Mapeo Meta → Resultado

### O-1: Cero hallazgos críticos en inspecciones SBP en 24 meses post go-live

**Metas que soporta**: G-1, G-6.

**Enunciado**: Las inspecciones in-situ de la SBP durante los 24 meses posteriores al go-live no producen hallazgos críticos relacionados con: reportería SEI, plan de cuentas, modelo de provisiones, contagio o garantías.

**KPI**: número de hallazgos críticos = 0; observaciones menores ≤ 3 por inspección.

**Fuente**: oficios de la SBP recibidos por Cumplimiento.

**Frecuencia**: por inspección (típicamente anual).

**Owner del reporte**: Cumplimiento.

**Valor de negocio**: protege la calificación AAA(pan), evita sanciones y restricciones operativas, sostiene reputación institucional ante Contraloría y Asamblea Nacional.

**Cronograma**:

- T₀ go-live → T+6m: estabilización; cualquier hallazgo se remedia en plazo SBP.
- T+6m → T+24m: cero hallazgos críticos sostenido.

**Beneficios por stakeholder**: JD (reputación), Cumplimiento (gestión del riesgo regulatorio), Gerencia General (sustento del programa).

**Indicadores adelantados**: pre-validación local que reproduce las tres capas SEI sin rechazo; cero rechazos del SEI en pre-producción.

**Indicadores rezagados**: oficios SBP cero hallazgos críticos.

---

### O-2: TCO total a 7 años dentro del ±10% del presupuesto, auditable por Contraloría

**Metas que soporta**: G-2, G-8.

**KPI**: TCO efectivo / TCO contractual; varianza acumulada.

**Frecuencia**: trimestral.

**Owner**: Finanzas.

**Valor**: financiero (control presupuestario), reputacional (sin cuestionamiento político).

**Cronograma**: medición continua del año 1 al 7; reporte trimestral a JD; auditoría anual de cláusulas contractuales.

**Indicadores adelantados**: número de cambios contractuales con impacto en TCO.

**Indicadores rezagados**: dictamen anual de Auditoría Interna.

---

### O-3: 99.95%+ uptime mensual sostenido por 12 meses consecutivos post go-live

**Metas que soporta**: G-3, G-4.

**KPI**: % uptime por canal y por mes; número de meses consecutivos ≥ 99.95%.

**Frecuencia**: diaria (datos), mensual (reporte).

**Owner**: Operaciones.

**Valor**: confianza del cliente, sostenimiento de la calificación AAA(pan), no afectación del ecosistema panameño de pagos.

**Cronograma**: medición continua; meta sostenida desde T₀ + 1 mes hasta T₀ + 12 meses.

**Indicadores adelantados**: pruebas de carga al 10x del promedio diario superadas; chaos testing aprobado.

**Indicadores rezagados**: reporte público de disponibilidad anual.

---

### O-4: Cero interrupciones de Yappy / ACH / ATMs imputables al cambio durante la migración

**Metas que soporta**: G-3, G-4.

**KPI**: número de incidentes P1 con causa raíz "migración Core".

**Frecuencia**: durante ventanas de corte y por 30 días post-corte.

**Owner**: TI + Operaciones.

**Valor**: confianza del ecosistema panameño en Caja de Ahorros como operador estable.

**Cronograma**: período de migración (típicamente 6–12 meses).

**Indicadores adelantados**: pruebas end-to-end de integración aprobadas pre-corte.

**Indicadores rezagados**: reporte de incidentes de Operaciones.

---

### O-5: 100% de productos sociales operativos al día 1 con cálculo automático del subsidio de Interés Preferencial

**Metas que soporta**: G-5, G-9.

**KPI**: número de productos sociales operativos / total; diferencias en cálculo de subsidio vs legado (= 0 material).

**Frecuencia**: validación pre-go-live + medición continua post.

**Owner**: Hipotecas + Créditos.

**Valor**: mandato social del Estado preservado [DOC-CB-001-C27]; reportería MIVIOT automática.

**Indicadores adelantados**: parametrización demostrada en demo del vendor sin código del vendor.

**Indicadores rezagados**: reporte mensual de cartera social.

---

### O-6: Modelo dual de provisiones automatizado con cero diferencias materiales contra legacy

**Metas que soporta**: G-6, G-9.

**KPI**: diferencia mensual NIIF 9 + Acuerdo 6-2000 (Core) vs legado; tiempo de cálculo mensual.

**Frecuencia**: mensual (paralelo pre-corte 3 meses; post-corte 12 meses).

**Owner**: Riesgos.

**Valor**: cumplimiento contable robusto, evita observaciones SBP sobre clasificación.

**Indicadores adelantados**: corrida paralela en pre-producción con diferencias ≤ tolerancia.

**Indicadores rezagados**: dictamen anual de auditor externo sobre provisiones.

---

### O-7: Dictamen legal de soberanía de datos emitido y vinculante antes del RFP

**Metas que soporta**: G-7.

**KPI**: dictamen emitido (binaria); fecha del dictamen anterior a la fecha del RFP.

**Owner**: Legal.

**Valor**: elimina riesgo de descalificación contractual posterior; alinea con MEF/Contraloría.

---

### O-8: Contratación pública aprobada por Contraloría sin observaciones materiales

**Metas que soporta**: G-8.

**KPI**: dictamen de Contraloría sin observaciones materiales.

**Owner**: Finanzas + Legal.

**Valor**: legitimidad pública del contrato; protección institucional.

---

### O-9: NPS de cliente ≥ +40 sostenido durante y después de la migración

**Metas que soporta**: G-3, G-5, G-10.

**KPI**: NPS mensual (panel representativo).

**Frecuencia**: mensual.

**Owner**: Atención al Cliente / Comunicaciones.

**Valor**: confianza del cliente final y de la marca "Banco de la Familia Panameña".

**Indicadores adelantados**: reclamos en redes sociales durante hitos; tiempo de respuesta de soporte.

**Indicadores rezagados**: NPS mensual.

---

### O-10: Calificación crediticia AAA(pan) con perspectiva estable sostenida

**Metas que soporta**: G-1, G-2, G-3, G-8.

**KPI**: calificación de Fitch / Pacific Credit Rating; perspectiva.

**Frecuencia**: revisión anual.

**Owner**: Gerencia de Finanzas + Junta Directiva.

**Valor**: costo de fondeo del banco; confianza del Estado en su brazo financiero.

---

## Matriz de Trazabilidad Completa

### Stakeholder → Driver → Meta → Resultado

| Stakeholder | Driver | Resumen | Meta | Resumen | Resultado | Resumen |
|-------------|--------|---------|------|---------|-----------|---------|
| Junta Directiva | SD-1 | Sostenibilidad y AAA(pan) | G-1 | Cumplimiento SBP nativo | O-1, O-10 | Cero hallazgos / AAA |
| Junta Directiva | SD-1 | Sostenibilidad y AAA(pan) | G-2 | TCO controlado | O-2, O-10 | Presupuesto / AAA |
| Gerencia General | SD-2 | Modernización sin disrupción | G-3 | Uptime 99.95% | O-3 | 99.95% sostenido |
| Gerencia General | SD-2 | Modernización sin disrupción | G-10 | Adopción | O-9 | NPS ≥ +40 |
| Aldo Ríos (Innovación) | SD-3 | Liderar la transformación | G-3, G-4, G-5 | Digital y mandato | O-3, O-4, O-5 | Uptime / pagos / social |
| Finanzas | SD-4 | TCO bajo control | G-2 | TCO ±10% | O-2 | Presupuesto |
| Finanzas | SD-4 | TCO bajo control | G-8 | Contratación pública | O-8 | Sin observaciones |
| TI | SD-5 | Integración limpia | G-4 | Integración nativa | O-4 | Cero interrupciones |
| TI | SD-5 | Integración limpia | G-9 | Migración exacta | O-5, O-6 | Productos / provisiones |
| CISO | SD-6 | Seguridad Zero Trust | G-1 | Cumplimiento SBP | O-1 | Cero hallazgos |
| Cumplimiento | SD-7 | SBP / UAF / FATF | G-1 | Cumplimiento nativo | O-1 | Cero hallazgos |
| Cumplimiento | SD-7 | SBP / UAF / FATF | G-6 | Provisiones duales | O-6 | Cero diferencias |
| Operaciones | SD-8 | Continuidad 24/7 | G-3 | Uptime 99.95% | O-3, O-9 | 99.95% / NPS |
| SBP | SD-9 | Reportería conforme | G-1 | Cumplimiento nativo | O-1 | Cero hallazgos |
| SBP | SD-9 | Reportería conforme | G-6 | Provisiones duales | O-6 | Cero diferencias |
| Contraloría | SD-10 | Auditoría de contratos | G-7 | Soberanía datos | O-7 | Dictamen legal |
| Contraloría | SD-10 | Auditoría de contratos | G-8 | Contratación pública | O-8 | Sin observaciones |
| Hipotecas | SD-11 | Cartera social | G-5 | Productos sociales | O-5 | 100% operativos |
| Hipotecas | SD-11 | Cartera social | G-9 | Migración exacta | O-5 | 100% operativos |
| Créditos | SD-12 | FGA + duales | G-5 | Productos sociales | O-5 | 100% operativos |
| Créditos | SD-12 | FGA + duales | G-6 | Provisiones duales | O-6 | Cero diferencias |
| Digital | SD-13 | Continuidad digital | G-4 | Integración nativa | O-4, O-9 | Cero cortes / NPS |
| Riesgos | SD-14 | Modelo dual + migración | G-6 | Provisiones duales | O-6 | Cero diferencias |
| Riesgos | SD-14 | Modelo dual + migración | G-9 | Migración exacta | O-5, O-6 | Productos / provisiones |
| Clientes | SD-15 | Sin interrupciones | G-3 | Uptime 99.95% | O-3, O-9 | 99.95% / NPS |
| UAF | SD-16 | ROS continuos | G-1 | Cumplimiento nativo | O-1 | Cero hallazgos |
| Asamblea Nacional | SD-17 | Transparencia | G-2, G-8 | TCO + contratación | O-2, O-8 | Presupuesto / sin observaciones |
| RRHH | (apoyo) | Capacitación | G-10 | Adopción | O-9 | NPS ≥ +40 |
| Legal | (apoyo SD-7) | Dictámenes y contratos | G-7, G-8 | Soberanía / contratación | O-7, O-8 | Dictamen / sin observaciones |

### Análisis de Conflictos

**Conflicto 1: Velocidad (Gerencia General, Innovación) vs Prudencia (Operaciones, Riesgos)**

- Gerencia General e Innovación quieren un cronograma agresivo (modernización rápida para no perder momento digital). Operaciones y Riesgos exigen periodos extensos de paralelo, pruebas exhaustivas y cortes pequeños para minimizar riesgo de interrupciones de Yappy / ACH / ATMs y errores contables.
- **Estrategia de resolución**: cronograma de migración por **bandos de productos** (no big-bang), con periodos de paralelo de ≥ 3 meses por bando y compuertas de go/no-go formales con voto de Operaciones y Riesgos. Innovación renuncia a fechas duras a cambio de hitos de visibilidad pública por bando completado.

**Conflicto 2: TCO bajo (Finanzas) vs Controles exhaustivos (Cumplimiento, CISO, Riesgos)**

- Finanzas presiona por TCO contenido (clave para Contraloría y Asamblea). Cumplimiento / CISO / Riesgos exigen módulos completos (AML real-time, NIIF 9 + 6-2000, segmentación de red, MFA, bóveda de secretos, pen-tests anuales) que son los más caros en muchas propuestas.
- **Estrategia**: clasificar controles en **obligatorios eliminatorios** (no negociables, no opcionales) vs **deseables priorizables**. Los eliminatorios entran en el RFP como cláusula sin opcionalidad y se costean en el TCO base. Los deseables compiten por presupuesto incremental con caso de negocio individual.

**Conflicto 3: Cloud público (Innovación, Gerencia General) vs Soberanía de datos (Cumplimiento, Legal, Contraloría)**

- Innovación favorecería Core SaaS en nube pública internacional por agilidad y costo. Cumplimiento / Legal / Contraloría exigen residencia de datos en Panamá [DOC-CB-001-C10].
- **Estrategia**: bloquear este debate **antes del RFP** con el dictamen legal vinculante (G-7). El RFP define la regla; los vendors se ajustan o se eliminan.

**Conflicto 4: Configurabilidad (TI, Hipotecas, Créditos) vs Controles de seguridad (CISO)**

- Negocio quiere parametrización amplia de productos sin tickets de TI. CISO exige separación de privilegios y auditoría de cambios.
- **Estrategia**: definir **perímetro de parametrización auditable** — campos que negocio puede cambiar sin riesgo de seguridad (tasas, plazos, fees) vs cambios que requieren flujo de gobernanza (nuevos productos, integraciones, esquemas contables).

**Conflicto 5: Productos sociales complejos (Hipotecas, Créditos) vs Cero customización de vendor (Finanzas, Innovación)**

- Hipotecas / Créditos requieren tratamientos contables específicos para Interés Preferencial, FGA, Profimype [DOC-CB-001-C13, DOC-CB-001-C14, DOC-CB-001-C18]. Finanzas / Innovación quieren evitar customización de vendor (incrementa TCO y vendor lock-in).
- **Estrategia**: el Principio 20 PRIN v1.1 ya define que los productos sociales **DEBEN soportarse mediante parametrización, no desarrollo a medida**. Vendor que no demuestre esto en demo queda eliminado.

### Sinergias

- **Cumplimiento + Riesgos + Auditoría Interna + SBP + Contraloría**: convergen en G-1 (cumplimiento regulatorio nativo) y G-6 (modelo dual de provisiones). Aprovechar como bloque para fortalecer criterios eliminatorios del RFP.
- **Operaciones + Digital + Clientes + Yappy/ACH/Telered**: convergen en G-3 (99.95% uptime) y G-4 (integración nativa). Diseñar como un equipo de "continuidad operacional" que valida hitos de migración.
- **Junta Directiva + Gerencia General + Finanzas + Asamblea Nacional**: convergen en G-2 (TCO controlado) y G-8 (contratación pública). Diseñar el RFP y los hitos de gobernanza con visibilidad pública preparada.
- **Innovación + TI + Digital + RRHH**: convergen en G-10 (capacitación y adopción) y G-3/G-4 (modernización con continuidad). Aprovechar como bloque para gestionar el cambio interno.

---

## Plan de Comunicación y Engagement

### Mensajes por Stakeholder

#### Junta Directiva

**Mensaje principal**: "El programa Core Banking moderniza la plataforma transaccional sin disrupción al cliente, dentro del presupuesto aprobado y con cumplimiento regulatorio robusto. Protege la calificación AAA(pan) y el mandato social del banco."

**Talking points**:

- Avance vs hitos y vs presupuesto (TCO).
- Riesgos críticos y mitigación.
- Decisiones que requieren la JD.

**Frecuencia**: mensual + decisiones de gate.

**Canal**: comité ejecutivo de tecnología; reportes ejecutivos.

#### Gerencia General

**Mensaje**: "Coordinamos el programa con foco en continuidad del negocio y entrega de la agenda digital sin frenarla."

**Frecuencia**: semanal (comité de programa).

#### Aldo Ríos / Innovación (líder del programa)

**Mensaje**: "Eres dueño del programa; mantienes el equipo, el backlog y la trazabilidad de decisiones."

**Frecuencia**: diaria (operación), semanal (gobernanza).

#### Cumplimiento + Riesgos + CISO

**Mensaje**: "Los controles obligatorios (SEI, NIIF 9 + 6-2000, AML/UAF, MFA, Zero Trust) son cláusulas eliminatorias del RFP."

**Frecuencia**: quincenal (gates regulatorios).

#### Operaciones + TI + Digital

**Mensaje**: "La migración es por bandos con paralelo; ningún canal se interrumpe sin tu firma de readiness."

**Frecuencia**: semanal (operación), por gate.

#### Finanzas + Legal

**Mensaje**: "El TCO contractual y la contratación pública son verificables; el dictamen de soberanía precede al RFP."

**Frecuencia**: por hito contractual.

#### Hipotecas + Créditos + áreas de negocio

**Mensaje**: "Los productos sociales se soportan por parametrización; ningún producto se pierde en la migración."

**Frecuencia**: quincenal (workshops + demos).

#### SBP + UAF + Contraloría + Asamblea Nacional

**Mensaje**: "Coordinamos hitos de cumplimiento y transparencia con anticipación; las pruebas con sandbox SEI ocurren antes del corte."

**Frecuencia**: por hito formal.

#### Clientes (externo)

**Mensaje**: "Estamos modernizando para servirte mejor; te avisaremos con anticipación si necesitamos ventanas de mantenimiento."

**Frecuencia**: por hito de migración relevante para cliente.

---

## Evaluación de Impacto del Cambio

| Stakeholder | Estado actual | Estado futuro | Magnitud | Riesgo de resistencia | Mitigación |
|-------------|--------------|---------------|----------|---------------------|-----------|
| TI (operación del Core) | Operación de Datapro / e-IBS [DOC-CB-001-C1] | Operación de nuevo Core con APIs publicadas, IaC, CI/CD | ALTA | MEDIO | Capacitación extensa, ramp-up con vendor, plan de retención de personal clave |
| Cumplimiento | Generación de reportes SBP con apoyo manual | Reportería nativa al SEI con workflow Preparador/Revisor/Firmante | ALTA | BAJO | Cumplimiento es champion (driver fuerte) |
| Riesgos | Doble corrida NIIF 9 / 6-2000 con apoyo manual | Modelo dual automatizado | ALTA | BAJO | Riesgos es champion |
| Hipotecas / Créditos | Sistemas y procesos heterogéneos | Core consolidado | ALTA | MEDIO | Parametrización demostrada en demo; co-diseño de migración |
| Operaciones | Operación 24/7 sobre legacy estable | Operación 24/7 sobre nuevo Core (curva de aprendizaje) | ALTA | MEDIO-ALTO | Periodo de paralelo extenso, soporte vendor reforzado |
| Clientes | Servicios actuales | Servicios actuales (vista externa, sin cambios visibles si va bien) | BAJA | BAJO | Comunicación proactiva, modo degradado |
| Auditoría Interna | Auditoría sobre legacy | Auditoría sobre nuevo Core + plan de cuentas SBP | MEDIA | BAJO | Acceso temprano a evidencia |

### Champions

- **Aldo Ríos / Innovación** — driver de liderazgo personal y estratégico.
- **Cumplimiento** — el SEI y el modelo dual les simplifican enormemente la operación regulatoria.
- **Riesgos** — automatización del modelo dual.
- **Junta Directiva + Gerencia General** — patrocinio estratégico.

### Fence-sitters (neutrales que necesitan convencimiento)

- **Hipotecas / Créditos** — necesitan ver demos con sus productos sociales reales antes de comprometerse.
- **RRHH** — necesita ver el plan de capacitación en español del vendor.
- **Legal** — necesita el dictamen de soberanía emitido antes de comprometerse.

### Resisters (escépticos)

- **Vendor incumbente (Datapro / e-IBS)** — pierde un contrato grande; estrategia: cláusula contractual de cooperación durante la transición; reconocimiento del esfuerzo histórico.
- **Personal técnico altamente especializado en el Core actual** — sienten amenaza profesional; estrategia: planes de re-capacitación y rol claro en el nuevo modelo.

---

## Registro de Riesgos relacionado con Stakeholders

### R-1: Pérdida de talento clave de TI durante el proyecto

**Stakeholders**: TI, RRHH, Gerencia General.

**Descripción**: el personal con conocimiento profundo del Core actual y de las integraciones (middleware, Yappy, ACH, Telered) puede salir voluntariamente o ser reasignado durante el proyecto.

**Impacto en metas**: G-4 (integración), G-9 (migración).

**Probabilidad**: MEDIA.

**Impacto**: ALTO.

**Mitigación**: plan de retención (bonos de proyecto, claridad de carrera post-migración), documentación de conocimiento crítico, contratos de consultoría con expertos del legacy si salen.

**Contingencia**: contratación de consultores especializados del vendor incumbente.

### R-2: Observación de Contraloría sobre proceso de contratación

**Stakeholders**: Contraloría, Finanzas, Legal, JD.

**Descripción**: el proceso de selección no cumple Ley 22 o el contrato firmado contiene cláusulas observables.

**Impacto en metas**: G-8.

**Probabilidad**: BAJA con buena preparación, ALTA sin ella.

**Impacto**: CRÍTICO.

**Mitigación**: asesoría legal externa especializada en contratación pública, revisión pre-firma, documentación exhaustiva del proceso.

**Contingencia**: re-licitar el módulo observado.

### R-3: Diferencia significativa en provisiones contra legacy

**Stakeholders**: Riesgos, Cumplimiento, SBP, Auditoría Interna.

**Descripción**: el modelo dual NIIF 9 + 6-2000 del nuevo Core produce cifras divergentes del legacy y se generan observaciones de la SBP.

**Impacto en metas**: G-6, G-1.

**Probabilidad**: MEDIA.

**Impacto**: ALTO.

**Mitigación**: corrida paralela de ≥ 3 meses pre-corte; conciliación documentada; validación con auditor externo antes del go-live.

**Contingencia**: ajuste del modelo, comunicación proactiva a SBP.

### R-4: Indisponibilidad pública de canales digitales durante migración

**Stakeholders**: Operaciones, Digital, Clientes, Asamblea Nacional (visibilidad política).

**Descripción**: un corte de Super App / Yappy / ATMs durante la migración escala como tema mediático y político.

**Impacto en metas**: G-3, G-4, G-9.

**Probabilidad**: MEDIA.

**Impacto**: CRÍTICO.

**Mitigación**: rolling deployment, plan de comunicación preparado, war-room durante ventanas críticas, rollback probado.

**Contingencia**: comunicación pública rápida, escalamiento a JD.

### R-5: Vendor finalista no soporta productos sociales del mandato del Estado

**Stakeholders**: Hipotecas, Créditos, MEF, MIVIOT, JD.

**Descripción**: el vendor seleccionado requiere customización por código del proveedor para Interés Preferencial / FGA / Profimype, contradiciendo el Principio 20 PRIN v1.1 [DOC-CB-001-C27].

**Impacto en metas**: G-5.

**Probabilidad**: MEDIA si la evaluación no es rigurosa.

**Impacto**: ALTO.

**Mitigación**: cláusula eliminatoria en RFP — productos sociales DEBEN parametrizarse, no codificarse; demo obligatoria con productos reales.

**Contingencia**: descalificar vendor; aceptar solo finalistas que cumplan.

### R-6: Disputa entre cloud público y soberanía de datos post-RFP

**Stakeholders**: Cumplimiento, Legal, Contraloría, Innovación.

**Descripción**: el vendor seleccionado propone arquitectura cloud sin presencia en Panamá y aparece un dictamen legal posterior que la prohíbe.

**Impacto en metas**: G-7, G-8.

**Probabilidad**: BAJA si el dictamen es pre-RFP.

**Impacto**: CRÍTICO si ocurre.

**Mitigación**: emitir el dictamen legal vinculante **antes del RFP** (meta G-7).

**Contingencia**: re-arquitectura o renegociación contractual.

### R-7: Cambios regulatorios SBP durante el proyecto

**Stakeholders**: Cumplimiento, Riesgos, vendor.

**Descripción**: la SBP emite nuevos Acuerdos o evoluciona el SEI hacia XBRL [DOC-CB-003-C29] durante el proyecto.

**Impacto en metas**: G-1.

**Probabilidad**: ALTA (la SBP tiene agenda activa).

**Impacto**: MEDIO.

**Mitigación**: cláusula contractual de "cumplimiento regulatorio continuo" sin cobros extraordinarios (Principio 7 PRIN v1.1); monitoreo activo de la SBP por Cumplimiento.

**Contingencia**: ajuste del scope, cronograma flexible.

---

## Gobernanza y Derechos de Decisión

### Matriz de Autoridad (RACI)

| Decisión | Responsable (R) | Aprobado (A) | Consultado (C) | Informado (I) |
|----------|----------------|--------------|----------------|---------------|
| Aprobación de presupuesto del programa | Finanzas | Junta Directiva | Gerencia General, Aldo Ríos | PMO, todas las áreas |
| Definición del alcance del RFP | Aldo Ríos / PMO | Gerencia General | Cumplimiento, TI, Riesgos, Negocio | JD, Contraloría |
| Dictamen de soberanía de datos | Legal | Junta Directiva | Cumplimiento, CISO | Contraloría, MEF |
| Criterios eliminatorios del RFP | Cumplimiento + TI | Comité de Tecnología | Riesgos, CISO, Negocio | JD |
| Short-list de vendors | Comité de evaluación | Gerencia General | Cumplimiento, Finanzas | JD, Contraloría |
| Selección final del vendor | Comité de evaluación | Junta Directiva | Cumplimiento, Legal, Finanzas | Contraloría, Asamblea (transparencia) |
| Firma del contrato | Legal + Gerencia General | Junta Directiva | Finanzas | Contraloría |
| Decisiones arquitectónicas (ADRs) | Lead técnico TI | Aldo Ríos / Comité Arquitectura | CISO, Riesgos, Negocio | JD (resúmenes) |
| Go/No-Go por bando de migración | Operaciones + TI | Aldo Ríos | Riesgos, Cumplimiento, Negocio | JD, Comunicaciones |
| Plan de comunicación al cliente | Comunicaciones / Marketing | Gerencia General | Aldo Ríos, Atención al Cliente | JD |
| Excepciones a principios (PRIN) | Solicitante | Comité de Arquitectura (no críticos) / JD (críticos) | Cumplimiento, CISO | Resto |

### Camino de Escalamiento

1. **Nivel 1 — Día a día**: PMO / Líder técnico → Aldo Ríos.
2. **Nivel 2 — Hitos**: Comité de Tecnología (semanal/quincenal).
3. **Nivel 3 — Decisiones críticas**: Gerencia General.
4. **Nivel 4 — Decisiones de gobernanza**: Junta Directiva.
5. **Nivel 5 — Decisiones regulatorias / fiscales**: SBP / Contraloría / Asamblea (por canal formal).

---

## Validación y Aprobación

### Revisión de Stakeholders

| Stakeholder | Fecha de revisión | Comentarios | Estado |
|-------------|-------------------|-------------|--------|
| Aldo Ríos — Innovación | Pendiente | — | PENDING |
| Gerencia General | Pendiente | — | PENDING |
| Cumplimiento | Pendiente | — | PENDING |
| Finanzas | Pendiente | — | PENDING |
| TI | Pendiente | — | PENDING |
| Operaciones | Pendiente | — | PENDING |
| CISO | Pendiente | — | PENDING |
| Riesgos | Pendiente | — | PENDING |
| Legal | Pendiente | — | PENDING |
| Junta Directiva | Pendiente | — | PENDING |

### Aprobación del Documento

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Patrocinador del programa (Gerencia General) | | | |
| Líder de programa (Aldo Ríos — Innovación) | | | |
| Gerencia de Tecnología (TI) | | | |
| Cumplimiento | | | |
| Junta Directiva (representante) | | | |

---

## Apéndices

### Apéndice A — Inputs documentales

- **PRIN**: `projects/000-global/ARC-000-PRIN-v1.1.md` — 21 principios de arquitectura, marco regulatorio refinado (Ley 20/1975, Acuerdos SBP, SEI, modelo dual NIIF 9 + Acuerdo 6-2000).
- **DOC-CB-001**: `projects/000-global/external/Relevamiento_CoreBanking_CajaDeAhorros_v2.docx` — Relevamiento confidencial del proyecto.
- **DOC-CB-002**: `projects/000-global/external/Relevamiento_Caja Ahorro_Pana.xlsx` — Cuestionario estructurado por área.
- **DOC-CB-003**: `projects/000-global/external/informacion_regulatoria.docx` — Brief regulatorio (Ley 20/1975, plan de cuentas SBP, NIIF 9, Acuerdos 6-2000 / 5-2011 / 3-2009 / 8-2010, SEI, fechas SBP).

### Apéndice B — Glosario

Ver glosario completo en `ARC-000-PRIN-v1.1.md` (Sección "Glosario").

---

## External References

> Esta sección proporciona trazabilidad desde el contenido generado hacia los documentos fuente.

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| DOC-CB-001 | Relevamiento_CoreBanking_CajaDeAhorros_v2.docx | Word | `projects/000-global/external/` | Relevamiento de necesidades confidencial para selección de Core Banking |
| DOC-CB-002 | Relevamiento_Caja Ahorro_Pana.xlsx | Excel | `projects/000-global/external/` | Cuestionario estructurado por área con 108 preguntas |
| DOC-CB-003 | informacion_regulatoria.docx | Word | `projects/000-global/external/` | Brief regulatorio SBP — diferenciación bancos estatales, NIIF 9, Acuerdos, SEI, fechas |

### Citations

Las citas DOC-CB-001-Cn y DOC-CB-003-Cn referidas en este documento están **definidas en `ARC-000-PRIN-v1.1.md` (Sección External References)**. Este STKE no las re-define; las usa por referencia para evitar duplicación. Citas específicas usadas en este documento:

| Citation ID | Doc ID | Uso en este STKE |
|-------------|--------|------------------|
| DOC-CB-001-C1 | DOC-CB-001 | Datapro / e-IBS como Core actual (SD-2, R-1) |
| DOC-CB-001-C2 | DOC-CB-001 | Reportería SBP como requisito no negociable (Resumen, SD-7) |
| DOC-CB-001-C3 | DOC-CB-001 | Métricas de escala (650,000 clientes, AAA(pan), 14.41% capital, cartera hipotecaria) (SD-1, SD-11, SD-15) |
| DOC-CB-001-C4 | DOC-CB-001 | Picos de planilla pública 5-10x (SD-8) |
| DOC-CB-001-C5 | DOC-CB-001 | Pagos sociales del Estado (SD-15) |
| DOC-CB-001-C6 | DOC-CB-001 | Agenda digital activa (SD-2, SD-3, SD-13) |
| DOC-CB-001-C7 | DOC-CB-001 | Yappy 55+ instituciones, 1.6M usuarios (SD-3, SD-13, G-4, R-4) |
| DOC-CB-001-C8 | DOC-CB-001 | AML real-time integrado al Core (SD-16) |
| DOC-CB-001-C9 | DOC-CB-001 | Contraloría puede excluir vendors (SD-10, G-8) |
| DOC-CB-001-C10 | DOC-CB-001 | Soberanía de datos como eliminatorio (G-7, R-6) |
| DOC-CB-001-C11 | DOC-CB-001 | Posición MEF/Contraloría sobre cloud (G-7) |
| DOC-CB-001-C12 | DOC-CB-001 | Inventario D04 de reportes SBP (G-1) |
| DOC-CB-001-C13 | DOC-CB-001 | Subsidio Interés Preferencial (SD-11, G-5, O-5) |
| DOC-CB-001-C14 | DOC-CB-001 | Créditos con garantía estatal FGA (SD-12, R-5) |
| DOC-CB-001-C15 | DOC-CB-001 | Reestructuraciones COVID-19 (SD-11, SD-14) |
| DOC-CB-001-C16 | DOC-CB-001 | Datos legados COBOL/mainframe (R-1, SD-14) |
| DOC-CB-001-C17 | DOC-CB-001 | Calidad de datos (G-9) |
| DOC-CB-001-C18 | DOC-CB-001 | Profimype y sistemas externos (SD-12, R-5) |
| DOC-CB-001-C19 | DOC-CB-001 | Sistemas auxiliares hipotecarios (SD-11) |
| DOC-CB-001-C20 | DOC-CB-001 | Datos en hojas de cálculo (R-1) |
| DOC-CB-001-C21 | DOC-CB-001 | Middleware/API Gateway existente (SD-5, SD-13, G-4) |
| DOC-CB-001-C22 | DOC-CB-001 | Programa "Una Cuenta Para Todos" (G-5) |
| DOC-CB-001-C23 | DOC-CB-001 | Caja Amiga inclusión financiera (Stakeholder list) |
| DOC-CB-001-C24 | DOC-CB-001 | Cinco comarcas indígenas (Stakeholder list) |
| DOC-CB-001-C26 | DOC-CB-001 | Control de pases sensible para banca estatal (SD-10) |
| DOC-CB-001-C27 | DOC-CB-001 | Mandato social del banco (R-5, Resumen) |
| DOC-CB-001-C28 | DOC-CB-001 | Créditos verdes (SD-12) |
| DOC-CB-001-C29 | DOC-CB-001 | Soporte local en español (G-10) |
| DOC-CB-003-C1 | DOC-CB-003 | Ley 20 de 1975 (Resumen, SD-1) |
| DOC-CB-003-C2 | DOC-CB-003 | Supervisión SBP coordinada (SD-7, SD-9) |
| DOC-CB-003-C5 | DOC-CB-003 | Reportes AML/UAF sin distinción (SD-7, SD-9, SD-16) |
| DOC-CB-003-C6 | DOC-CB-003 | Fiscalización Contraloría + Asamblea (SD-1, SD-10, SD-17) |
| DOC-CB-003-C7 | DOC-CB-003 | Plan de cuentas SBP no modificable (G-1) |
| DOC-CB-003-C9 | DOC-CB-003 | NIIF con adaptaciones regulatorias (SD-9) |
| DOC-CB-003-C10 | DOC-CB-003 | Modelo dual NIIF 9 + Acuerdo 6-2000 (Resumen, SD-12, G-6) |
| DOC-CB-003-C14 | DOC-CB-003 | Stages NIIF 9 (G-6, SD-12) |
| DOC-CB-003-C15 | DOC-CB-003 | Umbral SICR (G-6) |
| DOC-CB-003-C16 | DOC-CB-003 | PD/LGD/EAD series 5-7 años (SD-14, G-6) |
| DOC-CB-003-C17 | DOC-CB-003 | Reserva regulatoria en patrimonio (G-6, SD-12) |
| DOC-CB-003-C18 | DOC-CB-003 | Tabla A–E Acuerdo 6-2000 (SD-12, G-6, SD-9) |
| DOC-CB-003-C20 | DOC-CB-003 | Contagio inter-crédito (SD-9) |
| DOC-CB-003-C21 | DOC-CB-003 | Garantías y haircuts SBP (SD-9) |
| DOC-CB-003-C22 | DOC-CB-003 | Modificaciones 2008 / 2020 al Acuerdo 6-2000 (SD-11) |
| DOC-CB-003-C23 | DOC-CB-003 | SEI portal SBP (Resumen, SD-7) |
| DOC-CB-003-C24 | DOC-CB-003 | Roles SEI (SD-7) |
| DOC-CB-003-C26 | DOC-CB-003 | Validaciones SEI tres niveles (SD-7, G-1, O-1) |
| DOC-CB-003-C28 | DOC-CB-003 | Fechas límite SBP (SD-9) |
| DOC-CB-003-C29 | DOC-CB-003 | XBRL roadmap (SD-9, R-7) |

### Unreferenced Documents

| Filename | Source Location | Reason |
|----------|-----------------|--------|
| Relevamiento_Caja Ahorro_Pana.xlsx (DOC-CB-002) | `projects/000-global/external/` | Replica el contenido del Word (DOC-CB-001) por sesión de entrevista; no agrega afirmaciones independientes citables. Se conserva como insumo operativo del proyecto. |

---

**Generated by**: ArcKit `/arckit:stakeholders` command
**Generated on**: 2026-05-19
**ArcKit Version**: 5.0.1
**Project**: Caja de Ahorros — Evaluación y Selección de Core Banking (Project 001)
**Model**: Claude Opus 4.7 (1M context)
