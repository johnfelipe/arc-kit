# Statement of Work (SOW) — Reemplazo del Core Banking System (CBS) — Caja de Ahorros de Panamá

> **Documento legalmente vinculante para procurement bajo Ley 22 de Contrataciones Públicas de Panamá. Constituye el RFP formal para la categoría CBS.**

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-SOW-CBS-v1.0 |
| **Document Type** | Statement of Work (RFP — Core Banking System) |
| **Project** | Reemplazo del Core Banking + ERP + AML — Caja de Ahorros, Panamá (Project 001) |
| **RFP Track** | **CBS** — Core Banking System (1 de 3 RFPs coordinados) |
| **Classification** | OFFICIAL-SENSITIVE (CONFIDENCIAL – Uso interno hasta envío bajo NDA a vendors) |
| **Status** | DRAFT — pendiente firma de Auditoría Interna + Legal previo al envío |
| **Version** | 1.0 |
| **Created Date** | 2026-06-11 |
| **Last Modified** | 2026-06-11 |
| **Review Date** | 2026-07-11 |
| **Owner** | Aldo Ríos — Gerencia de Innovación / Líder del Programa |
| **Reviewed By** | PENDING — Auditoría Interna (validación del proceso), Legal (dictamen previo), Cumplimiento, Finanzas, CISO |
| **Approved By** | PENDING — Comité de Tecnología (emisión); Junta Directiva (presupuesto blendado del programa) |
| **Distribution** | Vendors invitados bajo NDA firmado; Junta Directiva; Comité de Tecnología; Comité de Evaluación; Auditoría Interna; Contraloría (información) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 (addendum) | 2026-06-11 (PM) | ArcKit AI | **Addendum post-revisión** — al detectarse que **10X Banking** y **TUUM** estaban ausentes sin memo justificativo (gap en mitigación R-026), se añaden los descartes formales en el Apéndice B §"Vendors no invitados con memo justificativo". Profiles asociados en `vendors/10x-banking-profile.md` y `vendors/tuum-profile.md`. Sin cambios al texto del RFP, eliminatorios, scope ni términos contractuales — sólo actualización del registro de descartes para defensibilidad ante Contraloría. | PENDING | PENDING |
| 1.0 | 2026-06-11 | ArcKit AI | Creación inicial del SOW formal para el RFP CBS. Construido sobre el RFI v1.0 emitido en junio de 2026 (DOC-RFI-001) — formaliza scope, requisitos, eliminatorios, ponderación, deliverables y términos contractuales. Integra los 15 eliminatorios + ponderación CBS del Marco de Evaluación (ARC-001-EVAL-v2.0); 193 requisitos categorizados de ARC-001-REQ-v2.0 (corrigendum aplicado); 37 riesgos mitigados de ARC-001-RISK-v2.0; shortlist y TCO de referencia de ARC-001-RSCH-v2.0; recomendación Opción 2 del SOBC v2.0. Contrato Hybrid (Fixed-price para licencias + implementación con tope ±10% / T&M para change requests). Ponderación 70% Técnico / 30% Costo. | PENDING | PENDING |

---

## 1. Resumen Ejecutivo

### 1.1 Identificación del Proceso

| Concepto | Detalle |
|----------|---------|
| **Comprador** | Caja de Ahorros (CAP) — banco estatal autónomo bajo Ley 20 de 1975 |
| **Proceso** | Procedimiento abierto bajo Ley 22 de Contrataciones Públicas |
| **Categoría** | Adquisición, implementación y soporte de Core Banking System |
| **Modalidad contractual** | Hybrid — Fixed-price para licencias + implementación + migración (con tope ±10% sobre presupuesto) + T&M para change requests post go-live |
| **Plazo del proceso** | RFP abierto 6 semanas; respuesta del vendor + 8 semanas demos/PoC + 4 semanas referencias + selección |
| **Valor estimado del contrato** | B/. 60–135M a 7 años (TCO CBS aislado — referencia RSCH v2.0); rango blendado del programa B/. 150–195M a 7 años |
| **Idioma** | Español (oferta y contratación); documentación técnica y funcional en español |

### 1.2 Objetivos del Programa

1. Reemplazar el Core Banking DataPro/eIBS con una plataforma moderna que cumpla los **193 requisitos** de ARC-001-REQ-v2.0 sin interrumpir la operación.
2. Cumplir nativamente el marco regulatorio panameño completo: SBP (Acuerdos 4-2013, 6-2000, 5-2011, 3-2009, 8-2010, **1-2026**), Resolución SBP-DJ-0014, Ley 23/2015 (DJTE), Ley 468/2025 (Interés Preferencial), Ley 52/2000 (cheques), NIIF 9, NIIF 16, IAS 21, UCP 600/ISP 98/URDG 758.
3. Habilitar el mandato social del Estado con parametrización (no desarrollo a medida) — Interés Preferencial, FGA, Profimype, Caja Amiga, transferencias sociales, créditos verdes.
4. Sostener la agenda digital activa (Super App, Yappy, A.N.D.R.E.A., Caja Amiga, Omnicaja) sin interrupción.
5. Integrar el CBS con un **ERP externo** (track separado) que asumirá el GL consolidado, y con un **motor AML externo con IA** (track separado).
6. Mantener disponibilidad ≥ 99.99% para servicios críticos en línea / ≥ 99.95% canales digitales durante toda la migración.

### 1.3 Resultados Esperados (Outcomes)

- Cero hallazgos críticos en inspecciones SBP en 24 meses post go-live.
- TCO contractual a 7 años dentro de ±10% del precio firmado.
- Cumplimiento del Acuerdo SBP 1-2026 (Resolución SBP-JD-0001-2026 del 16-ene-2026): **Art. 25 §1 vigencia 31-ene-2027**; **Art. 14 vigencia 30-jun-2027** (beneficiario final ≥ **10%** + geolocalización inferencial digital).
- Mandato social operativo desde día 1.
- Dictamen Contraloría sin observaciones materiales.

---

## 2. Scope of Work

### 2.1 Alcance del SOW (En scope)

El alcance del SOW CBS comprende:

1. **Software y licencias del CBS** — versión más reciente del producto cotizado, módulos requeridos para cubrir el catálogo funcional (sección 4), con derecho de actualización a versiones mayores durante toda la vida del contrato.

2. **Implementación end-to-end**:
   - Arquitectura de despliegue en territorio panameño (on-premise CAP, colocation certificado SBP o cloud privado regional con presencia panameña — definido por dictamen Legal previo).
   - Configuración del producto a las necesidades del banco mediante **parametrización** (sin desarrollo a medida del vendor — Principio 20 PRIN v1.1, BR-004).
   - **Integración** con: bus IBM MQ + API Gateway existentes (INT-013), Yappy (INT-001), ACH Panamá (INT-002), Telered (INT-003), SWIFT vía SCONNECT LAU/CSV (INT-004), SEI (INT-005), UAF (INT-006 — orquestado por el motor AML externo), MIVIOT (INT-007), MEF (INT-008), SIACAP (INT-009), APC (INT-010, INT-020), A.N.D.R.E.A. (INT-011), Super App (INT-012), SITECA (INT-014), BPMs Ultimus/Asicom-Finflow/Genexus (INT-015), FATCA/CRS (INT-016/17), motor AML externo (INT-018), **ERP externo** (INT-021), SISCARD (INT-022), Panadata (INT-023), App Enhancer (INT-024), Banca Seguro (INT-025), IAM corporativa / Microsoft Entra ID (INT-026), Data Lake AWS + Snowflake (INT-027), DGI (INT-028).
   - **Migración de datos** del legado DataPro/eIBS, incluyendo consolidación de Profimype, sistemas hipotecarios auxiliares, hojas Access/Excel; mapeo de los 8,000+ elementos del diccionario de datos heredado (DR-021) al nuevo modelo del CBS; validación saldo-por-saldo con diferencias = 0 al cierre del corte.
   - **Plan de migración por bandos** (no big-bang) con paralelo ≥ 3 meses por bando y compuertas go/no-go con voto de Operaciones y Riesgos.

3. **Documentación funcional y técnica completa en español** — guías de usuario por rol, manuales operativos, documentación de APIs (OpenAPI/AsyncAPI), runbooks de operación, plan de contingencia, plan de DR.

4. **Capacitación certificada en español** — currículum por rol; ~3,500 empleados a capacitar (TI, Operaciones, Hipotecas, Créditos, Digital, Atención al Cliente, Cumplimiento, Riesgos, Finanzas, Auditoría Interna); certificación con examen.

5. **Soporte L1/L2/L3 24/7/365 en español** con SLA contractual (cláusula 2 de la sección 9.1):
   - P1 (servicio crítico caído): respuesta ≤ 30 min, resolución ≤ 4 h.
   - P2 (degradación significativa): respuesta ≤ 2 h, resolución ≤ 24 h.
   - P3 (incidente menor): respuesta ≤ 8 h, resolución ≤ 5 días hábiles.

6. **Mantenimiento evolutivo** — adaptación del producto a nuevos Acuerdos SBP **sin cobros extraordinarios** (NFR-C-010); fix packs; actualizaciones de versión.

7. **Servicios profesionales** para fases de discovery + diseño + implementación + paralelo + go-live + estabilización.

8. **Soporte transicional** con el incumbente (DataPro/Vencora) durante la migración (cláusula 6 de la sección 9.1) — coordinación de equipos, transferencia de conocimiento, custodia de datos.

### 2.2 Fuera de Alcance del SOW CBS

- **ERP externo**: track separado — ver `ARC-001-SOW-ERP-v1.0.md`.
- **Motor AML externo con IA**: track separado — ver `ARC-001-SOW-AML-v1.0.md`.
- **SISCARD** (core de tarjetas): se mantiene, se integra — no se reemplaza en Fase 1.
- **Bus IBM MQ + API Gateway**: se preservan como capa de abstracción.
- **Super App, A.N.D.R.E.A., Omnicaja**: se mantienen e integran al nuevo CBS pero su desarrollo continúa paralelo.
- **XBRL completo**: Fase 2, alineado al roadmap SBP.
- **Reemplazo de BPMs** (Ultimus, Asicom-Finflow, Genexus): Fase 2 — el CBS recibe el crédito aprobado del BPM externo.
- **Reemplazo de Emerix** (sistema externo de cobranza > 90 días): Fase 2 — el CBS gestiona 0-90 días nativamente y notifica a Emerix en tiempo real.

### 2.3 Supuestos

1. El dictamen Legal sobre soberanía de datos estará cerrado antes de la firma del contrato.
2. La consulta a Autoridad de Innovación + SBP + Seguridad Nacional sobre modelo cloud habrá emitido respuesta antes de la selección final.
3. CAP continuará operando bajo Ley 20 de 1975 (esquema supervisorio coordinado) y bajo Ley 22 de Contrataciones Públicas durante toda la vida del contrato.
4. CAP completará la transición Activo-Pasivo → Activo-Activo (R-028) antes del go-live del CBS.
5. CAP ejecutará en paralelo el plan de remediación de seguridad del legado (R-027).
6. La selección del ERP externo y del motor AML externo se hará en paralelo a este RFP CBS con go-live coordinado.

### 2.4 Restricciones

1. **Soberanía de datos** (BR-006, DR-013): datos personales, financieros y transaccionales en territorio panameño.
2. **TCO con tope contractual** ±10% del precio firmado (BR-003).
3. **Plazos regulatorios**: vendor cuyo cronograma propuesto no entregue **Acuerdo 1-2026 Art. 14 antes del 30-jun-2027** queda descalificado (E-15 del EVAL v2.0).
4. **Ley 22 de Contrataciones Públicas**: proceso, contrato y modificaciones cumplen Ley 22; Contraloría visa el contrato.
5. **Idioma**: todo el proceso, documentación y soporte en español.
6. **PRIN v1.1 — Principios obligatorios**: P5 (Cumplimiento Regulatorio), P6 (Soberanía), P7 (Reportería SBP Nativa), P8 (Integridad Contable + Modelo Dual), P11 (APIs Abiertas), P20 (Parametrización vs Código), P21 (Soporte Español).

### 2.5 Dependencias

| Dependencia | Owner | Plazo |
|-------------|-------|-------|
| Dictamen Legal de soberanía de datos | Legal CAP | Pre-firma de contrato |
| Consulta gubernamental sobre cloud | Aldo Ríos + Legal | Pre-selección final |
| Selección y contratación del ERP externo | Finanzas + TI | Paralelo a este RFP |
| Selección y contratación del motor AML externo | Cumplimiento | Paralelo a este RFP |
| Transición Activo-Activo (35–40 km) | TI + Operaciones | Pre-go-live |
| Plan de remediación del legado (R-027) | CISO | Paralelo a este RFP |
| Validación del Marco EVAL por Auditoría Interna | Auditoría Interna | Pre-envío del RFP |

---

## 3. Marco Regulatorio Aplicable

| Marco | Ámbito |
|-------|--------|
| **Ley 20 de 1975** | Ley orgánica de la Caja de Ahorros |
| **Ley 22 de Contrataciones Públicas** | Proceso de compra, contrato y modificaciones |
| **Acuerdo SBP 4-2013** | Coeficientes de liquidez (LCR) |
| **Acuerdo SBP 6-2000** | Clasificación y provisiones de cartera |
| **Acuerdo SBP 5-2011** | Bienes adjudicados y activos fuera de uso |
| **Acuerdo SBP 3-2009** | Consolidación de grupo bancario |
| **Acuerdo SBP 8-2010** | Derivados |
| **Acuerdo SBP 1-2026** | AML/CFT/FPADM — Resolución SBP-JD-0001-2026 del 16-ene-2026; Art. 25 §1 vigencia 31-ene-2027; Art. 14 vigencia 30-jun-2027 (beneficiario final ≥ 10% + geolocalización inferencial digital) |
| **Resolución SBP-DJ-0014** | Formato y procedimiento de envío al SEI |
| **Ley 23 de 2015** | Prevención AML/FT + DJTE para transacciones ≥ B/. 10,000 |
| **Ley 468/2025** | Tasas de Interés Preferencial (vivienda social) |
| **Ley 52 de 2000** | Régimen de cheques |
| **Ley 81 de Panamá** | Protección de Datos Personales |
| **NIIF 9** | Instrumentos financieros y modelo ECL |
| **NIIF 16** | Arrendamientos financieros (leasing) |
| **IAS 21** | Diferencias de cambio de moneda extranjera |
| **UCP 600 / ISP 98 / URDG 758** | Cartas de crédito documentarias / stand-by / garantías |
| **FATCA / CRS** | Reportería fiscal internacional |

---

## 4. Requisitos del Producto

> **Referencia normativa**: la totalidad de los requisitos del CBS está documentada en `ARC-001-REQ-v2.0.md` (193 requisitos — 14 BR, 76 FR, 50 NFR, 31 INT, 22 DR). Este SOW incorpora REQ v2.0 por referencia y resume aquí los **MUST_HAVE críticos**.

### 4.1 Business Requirements (BR) — MUST_HAVE

| ID | Requisito | Vínculo a SOW |
|----|-----------|----------------|
| BR-001 | Reemplazo del Core preservando continuidad operacional | Sección 2.1, 7.3 |
| BR-002 | Cumplimiento regulatorio nativo SBP / UAF / SEI / Acuerdo 1-2026 | Sección 3, 4.5 |
| BR-003 | TCO controlado a 7 años con auditabilidad de Contraloría | Sección 8.3 |
| BR-004 | Soporte completo al mandato social del Estado mediante parametrización | Sección 4.2 |
| BR-005 | Modelo dual de provisiones NIIF 9 + Acuerdo 6-2000 automatizado | Sección 4.5 |
| BR-006 | Soberanía de datos en Panamá validada legalmente | Sección 2.4, 3 |
| BR-007 | Contratación pública aprobada por Contraloría sin observaciones | Sección 9.1 |
| BR-008 | Migración con conciliación contable exacta y cero pérdida de datos | Sección 4.6, 6 |
| BR-009 | Adopción del personal mediante capacitación en español | Sección 5.4 |
| BR-010 | Sostenimiento de la agenda digital activa sin interrupción | Sección 4.4 |
| BR-011 | Calificación AAA(pan) sostenida | Sección 7.7 |
| BR-012 | Inclusión financiera operativa en zonas rurales y comarcas | Sección 4.4 |
| BR-013 | Adquisición e integración con ERP externo (track separado) | Sección 4.7 |
| BR-014 | Transición CAPEX → OPEX (preferencia banco) | Sección 8.4 |

### 4.2 Functional Requirements (FR) — clusters MUST_HAVE

Listado abreviado; detalle completo en REQ v2.0 §FR. Categorías obligatorias del producto:

- **Bloque A — Cuentas y depósitos**: cuentas pasivas (Regular, Dorada, Platinum, Ahorro Navidad, Panamá Para Ti, Juvenil, Ahorro Fácil para Niños, Una Cuenta Para Todos, Caja Amiga), **sub-cuentas/cajones** (FR-007), **sobregiros nativos** (FR-008), **cheques de gerencia + chequeras + DDI** (FR-009, FR-011), depósitos a plazo con renovación + back-to-back + anticipo intereses (FR-010), multimoneda con IAS 21 (FR-012).
- **Bloque B — Créditos**: hipotecario Interés Preferencial con reclamo trimestral a DGI (FR-014), **hipotecario residentes en exterior** (FR-015), FGA (FR-016), Profimype (FR-017), **reestructuración nativa sin cancelación** (FR-018), cálculo automático de subsidio (FR-019), créditos especiales etiquetables (FR-020), autos (FR-021), prendarios (FR-022), líneas de crédito (FR-023), construcción con conversión a hipoteca (FR-024), leasing NIIF 16 (FR-025), **sindicados como coordinador Y participante** (FR-026), comerciales y macro-obras (FR-027), mancomunados (FR-028), **FECI 1%** (FR-029), **cobranza temprana 0-90 días nativa** + notificación tiempo real a externo > 90 días (FR-030), contagio APC (FR-031), garantías N:N + stand-by LC + performance bonds (FR-032).
- **Bloque C — Pagos + Comercio Exterior**: Yappy (FR-034), ACH (FR-035), Telered (FR-036), corresponsales Caja Amiga (FR-037), SWIFT + pagos cross-border no-SWIFT (FR-038, FR-041), Cartas de Crédito UCP 600/ISP 98/URDG 758 (FR-039), **factoring estatal con retención 10% y gastos por adelantado** (FR-040), planilla pública (FR-042), transferencias sociales (FR-043), SIACAP (FR-044), **DDI masivo 833 empresas + 178 entidades** (FR-045).
- **Bloque D — AML/KYC compliance operacional**: KYC con Panadata (FR-046), KYC simplificado (FR-047), **exposición de eventos al motor AML externo (no embebido)** (FR-048), ROS UAF orquestado por externo (FR-049), FATCA/CRS (FR-050), PEP (FR-051), **beneficiario final ≥ 10%** (FR-052), **geolocalización inferencial** (FR-053), **DJTE Ley 23/2015 ≥ B/. 10,000** (FR-054).
- **Bloque E — Reportería**: SEI nativo (FR-055), inventario D04 54+ reportes mensuales (FR-056), liquidez diaria + CAR + LCR (FR-057), plan de cuentas SBP (FR-058), MIVIOT (FR-059), MEF + DGI (FR-060), pre-validación local 3 capas SEI (FR-061), APC mensual (FR-062), notificaciones internas estructuradas (FR-063).
- **Bloque F — Contabilidad**: NIIF 9 ECL + Acuerdo 6-2000 dual (FR-064..066), garantías + haircuts (FR-067), reservas dinámicas (FR-068), **asientos transaccionales expuestos al ERP externo en API o micro-batch ≤ 5 min** (FR-069), cuadre diario (FR-070).
- **Bloque G — Canales**: APIs (FR-071), Caja Amiga offline (FR-072), datos para A.N.D.R.E.A. (FR-073), 60 sucursales + módulo Teller + bóveda nativa (FR-074), **CIF único + vista 360° con SISCARD** (FR-075), notificaciones (FR-076).

### 4.3 Non-Functional Requirements (NFR) — MUST_HAVE críticos

| ID | Requisito | Métrica |
|----|-----------|---------|
| NFR-P-001 | Saldo p95; Yappy p95; movimientos p95 | < 1.5s / < 3s / < 2s |
| NFR-P-002 | Throughput planilla | ≥ 5,000 TPS |
| NFR-P-005 | Latencia evento AML al motor externo | < 200 ms |
| NFR-P-006 | Cierre diario | ≤ 1 min |
| NFR-A-001 | SLA servicios críticos | ≥ 99.99% mensual |
| NFR-A-002 | SLA canales digitales | ≥ 99.95% mensual |
| NFR-A-004 | RTO/RPO críticos | RTO ≤ 15 min, RPO ≤ 1 min |
| NFR-A-005 | Topología | Activo-Activo o Activo-Pasivo con conmutación automática |
| NFR-A-007 | Mantenimiento | Sin downtime (rolling, blue-green, canary) |
| NFR-SEC-001..010 | Seguridad: MFA, mTLS, bóveda secretos, cifrado en tránsito + reposo, logs 7 años, pen-tests anuales, SAST/SCA, segmentación, listas restrictivas, firma digital SEI | Todos MUST |
| NFR-SEC-011 | SSO con Microsoft Entra ID + SAML/OAuth/OIDC/LDAP | MUST |
| NFR-SEC-013 | Segregación de Funciones (SoD) configurable | MUST |
| NFR-SEC-014 | Permisos a nivel módulo/pantalla/campo + enmascaramiento por rol | MUST |
| NFR-SEC-015 | Recertificación periódica automática | MUST |
| NFR-M-008 | Validación en tiempo de ingreso transversal | MUST |
| NFR-M-009 | Configuración de productos en minutos sin TI/vendor | MUST |
| NFR-U-005 | Localización Panamá (UTC-5, USD, DD/MM/AAAA) | MUST |

### 4.4 Integration Requirements (INT) — MUST_HAVE

Las 31 integraciones obligatorias están en REQ v2.0 §INT. **Integraciones críticas que pueden eliminar al vendor**:

- INT-018 (motor AML externo con bloqueo bidireccional < 200 ms) — eliminatorio E-14.
- INT-021 (ERP externo con asientos contables vía API o micro-batch ≤ 5 min) — eliminatorio E-13.
- INT-026 (Microsoft Entra ID con SAML/OAuth/OIDC/LDAP) — eliminatorio E-9.

### 4.5 Cumplimiento del Acuerdo SBP 1-2026 (eliminatorio temporal)

El vendor seleccionado DEBE entregar las capacidades para cumplir:

- **Art. 25 §1 — vigencia 31-ene-2027**: regla específica de identificación. CAP combinará con plan de remediación del legado para llegar a la vigencia.
- **Art. 14 — vigencia 30-jun-2027**: beneficiario final ≥ **10%** + geolocalización inferencial digital.

**Vendors cuyo cronograma propuesto no entregue Art. 14 antes del 30-jun-2027 quedan descalificados del proceso** (Eliminatorio E-15 del EVAL v2.0).

### 4.6 Migración de Datos

- **Saldo-por-saldo** validado contra el legado; diferencias = 0 al cierre del corte.
- **8,000+ elementos** del diccionario de datos heredado mapeados al nuevo modelo con propietarios formales.
- **Consolidación** de Profimype, sistemas hipotecarios auxiliares, hojas Access/Excel.
- **Preservación de trazabilidad histórica** para hipotecas con condiciones especiales antiguas (Interés Preferencial heredado, reestructuraciones COVID-19, FGA).
- **Plan por bandos** con paralelo ≥ 3 meses por bando.

### 4.7 Integración con ERP Externo (BR-013, INT-021, E-13)

- El CBS expone los **asientos contables transaccionales** vía API REST o archivos estándar al ERP externo en **tiempo real o micro-batch (≤ 5 min)**.
- **Plan de cuentas SBP** cargado idénticamente en CBS y ERP.
- **Cierres** (diario, mensual, anual) coordinados con CBS, Teller y ERP — diferencias = 0.
- **Continuidad GL paralela** durante 90 días post go-live como contingencia mientras el ERP estabiliza.

---

## 5. Deliverables

| # | Deliverable | Aceptación | Plazo (referencia) |
|---|-------------|------------|---------------------|
| D-01 | **Diseño Funcional Detallado (DFD)** por dominio | Firmado por Negocio + TI + Cumplimiento | T+3 meses post-firma |
| D-02 | **Diseño de Arquitectura (HLD + DLD)** | Aprobado por Comité de Arquitectura — validación contra los 21 principios PRIN v1.1 | T+4 meses post-firma |
| D-03 | **Plan de Migración por Bandos** con cronograma y plan de rollback | Aprobado por Steering Committee | T+5 meses post-firma |
| D-04 | **Configuración del producto** y catálogo de productos sociales parametrizados | Demos en vivo con datos reales con cero customización del vendor | Incremental por banda |
| D-05 | **Migración de datos** por banda con conciliación firmada por Auditoría Interna | Diferencias = 0 al cierre del corte | Por banda |
| D-06 | **Suite de integraciones** (31 INT) configuradas y probadas end-to-end | Pruebas E2E aprobadas | Pre-go-live por banda |
| D-07 | **Pruebas de rendimiento + escalabilidad + seguridad + DR** | Métricas cumplen NFR-P / NFR-S / NFR-A / NFR-SEC | Pre-go-live por banda |
| D-08 | **Documentación completa en español** — guías de usuario, técnica, runbooks | Aprobada por Operaciones y TI | Pre-go-live |
| D-09 | **Capacitación certificada en español** del personal del banco | 100% del personal clave certificado por examen | Pre-corte por banda |
| D-10 | **Pase a producción por banda** con paralelo ≥ 3 meses | Aprobado por go/no-go con voto Operaciones + Riesgos | Por banda |
| D-11 | **Reporte de cumplimiento Acuerdo 1-2026 Art. 14** | Funcionalidad operativa antes de 30-jun-2027 | 2027-Q2 |
| D-12 | **Estabilización + warranty** | 90 días post go-live full sin incidentes P1 críticos | Post go-live |
| D-13 | **Plan de soporte transicional** con incumbente | Firma del incumbente | Pre-firma del contrato |
| D-14 | **Reporte final del proyecto** + handover a Operaciones | Aprobado por JD | Post-estabilización |

---

## 6. Cronograma y Hitos Clave

> **Referencia indicativa**: el vendor propone cronograma detallado; el banco evalúa adherencia a hitos eliminatorios.

| Hito | Fecha objetivo (T = firma del contrato) |
|------|------------------------------------------|
| Cierre del RFP (entrega de propuestas) | 2026-10-15 |
| Demos extendidas + PoC ampliada (top-3 vendors) | 2026-11-01 – 2026-12-15 |
| Reuniones de referencia | 2026-12-15 – 2026-12-31 |
| Selección final por JD | 2027-01-31 |
| Firma del contrato (T₀) | 2027-03-31 |
| **Cumplimiento Acuerdo 1-2026 Art. 25 §1** (vía plan de remediación del legado) | **2027-01-31** |
| Diseño Funcional + HLD/DLD | T+3 / T+4 meses |
| Plan de migración por bandos firmado | T+5 meses |
| Implementación Banda 1 (cuentas + canales) | T+6 a T+12 meses |
| Implementación Banda 2 (crédito) | T+10 a T+18 meses |
| **Cumplimiento Acuerdo 1-2026 Art. 14** (CBS o plan de remediación) | **2027-06-30** |
| Implementación Banda 3 (comercial + sindicados + factoring + cartas de crédito) | T+16 a T+24 meses |
| Implementación Banda 4 (Caja Amiga + comarcas + segmentos especiales) | T+20 a T+28 meses |
| Go-live full + estabilización | T+24 a T+30 meses |
| Warranty + soporte productivo | T+30 meses → contrato 7 años total |

---

## 7. Vendor Qualifications (Criterios Eliminatorios — Pass/Fail)

> **Referencia normativa**: los 15 criterios eliminatorios completos están en `ARC-001-EVAL-v2.0.md` Parte I. Resumen aplicable al CBS:

| ID | Criterio | Aplica |
|----|----------|--------|
| E-1 | Soberanía de Datos en Territorio Panameño | ✓ |
| E-2 | Productos del Mandato Social Parametrizables (NO Codificados) | ✓ |
| E-3 | Modelo Dual NIIF 9 + Acuerdo 6-2000 Nativo | ✓ |
| E-4 | Reportería SBP Nativa (SEI + Inventario D04) | ✓ |
| E-5 | Soporte 24/7 en Español con SLA Medible | ✓ |
| E-6 | Cumplimiento Acuerdo SBP 1-2026 (AML/CFT/FPADM) | ✓ |
| E-7 | Integración con Ecosistema de Pagos Panameño Demostrada | ✓ |
| E-8 | Mínimo 3 Referencias LatAm Verificables en Producción ≥ 24 Meses | ✓ |
| E-9 | Certificaciones Obligatorias (ISO 27001, ISO 27017 si cloud, SOC 2 Tipo II) | ✓ |
| E-10 | Estabilidad Financiera y Continuidad del Vendor (ingresos globales ≥ USD 100M) | ✓ |
| E-11 | Aceptación de las 15 Cláusulas Contractuales Obligatorias | ✓ |
| E-12 | Idoneidad Jurídica Bajo Ley 22 | ✓ |
| **E-13** | **Capacidad de Integración con ERP Externo** | ✓ |
| **E-14** | **Capacidad de Offload AML Bidireccional** | ✓ |
| **E-15** | **Deliverable Acuerdo 1-2026 Art. 14 antes del 30-jun-2027** | ✓ |

**Cualquier fallo en cualquiera de los 15 eliminatorios descalifica al vendor.**

### 7.7 Compromisos sobre AAA(pan) y mandato social

El vendor declara conocer que CAP es banco estatal con calificación AAA(pan) y mandato social legalmente vinculante, y se compromete a:

- No degradar la calidad de servicio durante migración (NFR-A-001..003).
- Soportar los productos del mandato social mediante parametrización del banco, sin desarrollo a medida del vendor.
- Cumplir el plazo del Acuerdo 1-2026 Art. 14 antes del 30-jun-2027 con cláusula penal por incumplimiento (cláusula 10 de la sección 9.1).

---

## 8. Proposal Requirements (Estructura Obligatoria de la Propuesta)

El vendor entregará una propuesta en **3 sobres independientes** (separación administrativa estricta para defensibilidad ante Contraloría):

### 8.1 Sobre Administrativo

- Documentación legal de Panamá (idoneidad SBP/MICI, certificado de existencia, representación legal local registrada, paz y salvo fiscal, declaración jurada de cumplimiento Ley 22).
- Acuerdo de Confidencialidad (NDA) firmado.
- Certificaciones ISO 27001 + ISO 27017 (si cloud) + SOC 2 Tipo II vigentes.
- Estados financieros auditados últimos 3 años.
- **Aceptación firmada de las 15 cláusulas contractuales obligatorias** (E-11).
- Lista de las 3+ referencias LatAm verificables con contacto.

### 8.2 Sobre Técnico

- Resumen ejecutivo de la propuesta (máx 10 págs).
- Respuesta detallada a cada uno de los **15 criterios eliminatorios** con evidencia documental por criterio.
- Cobertura de los 193 requisitos del REQ v2.0 (tabla con respuesta por ID — nativo / configurable / desarrollo del banco / no cubierto).
- Arquitectura propuesta (HLD inicial) con diagramas y descripción de despliegue.
- **Cronograma detallado** con hitos críticos (incluyendo cumplimiento Acuerdo 1-2026 Art. 14 antes de 30-jun-2027).
- **Plan de migración** por bandos con detalle de paralelo y rollback.
- **Plan de integración** con ERP externo, motor AML externo, bus IBM MQ, ecosistema panameño.
- **Plan de capacitación** en español con currículum por rol.
- **Plan de soporte transicional** con incumbente.
- **Equipo propuesto** con CVs detallados, distinguiendo equipo on-site Panamá vs remoto regional.
- **Casos de éxito** documentados con detalle (mínimo 3 referencias LatAm en producción ≥ 24 meses).
- **Plan de gestión de riesgos** vinculado a RISK v2.0.
- **Hoja de ruta del producto** a 7 años (módulos opcionales no incluidos pero disponibles).

### 8.3 Sobre Económico

- **Precio total a 7 años con desglose CAPEX (años 1-3) y OPEX (años 4-7)**:
  - Licenciamiento (con número de transacciones / usuarios incluidos).
  - Implementación inicial (precio fijo).
  - Migración de datos (precio fijo).
  - Servicios profesionales (estimación + tarifa para T&M).
  - Soporte y mantenimiento anual (% de licencia + tope contractual).
  - Módulos opcionales (precio por módulo + condiciones).
- **Modelo de pricing** detallado: por usuario, por transacción, por entidad, por servidor, etc.
- **Cláusula de tope ±10%** y **tope a true-ups** anuales firmada.
- **Modelo CAPEX / OPEX**: alternativa OPEX si está disponible (preferencia banco BR-014).
- **TCO a 7 años** consolidado con análisis de sensibilidad (transacciones +/- 30%, inflación, FX).
- **Bonus / penalizaciones** por cumplimiento de hitos críticos.
- **Costos de salida** si CAP termina anticipadamente (cláusula 9).
- **Costos transicionales** con incumbente.

---

## 9. Términos Contractuales

### 9.1 Cláusulas Obligatorias (15 — el vendor acepta sin reservas)

1. **Residencia de datos en Panamá** (BR-006) — durante todo el ciclo de vida (procesamiento, almacenamiento, respaldo, archivo); auditoría trimestral.
2. **SLA con penalizaciones** — P1: 10% de la facturación mensual; P2: 5%; P3: 2%. Penalización acumulativa hasta 30%.
3. **TCO con tope ±10%** + tope a true-ups e incrementos por inflación.
4. **Cumplimiento regulatorio continuo** — el vendor adapta el producto a nuevos Acuerdos SBP sin cobros extraordinarios (NFR-C-010).
5. **Auditabilidad por Contraloría** — acceso a contratos, pases a producción, trazabilidad transaccional.
6. **Soporte transicional con incumbente** durante migración — coordinación de equipos firmada por ambas partes.
7. **Capacitación en español certificada** — currículum por rol; certificación con examen.
8. **Documentación funcional y técnica en español** — viva, accesible, actualizada.
9. **Salida ordenada** — portabilidad de datos en formatos estándar al término del contrato; código de la configuración entregable a CAP.
10. **Penalización por incumplimiento de plazos críticos** — Acuerdo 1-2026 Art. 14 (30-jun-2027): penalización de 15% del valor total del contrato por mes de retraso.
11. **Confidencialidad y datos personales** (Ley 81 de Panamá).
12. **Anticorrupción y cumplimiento de Ley 22**.
13. **(NUEVA v2.0)** **Integración con ERP externo** — SLA específico para asientos contables expuestos al ERP (latencia ≤ 5 min, idempotencia, conciliación automática).
14. **(NUEVA v2.0)** **Exposición de eventos al motor AML externo** — streaming < 200 ms y soporte para bloqueo bidireccional.
15. **(NUEVA v2.0)** **Coordinación inter-RFP** — el vendor seleccionado coordina su cronograma e implementación con los vendors ERP y AML; participa en sesiones de integración trimestrales.

### 9.2 Estructura de Pago (Hybrid — Fixed-price + T&M)

**Fixed-price** para los siguientes deliverables, con pago por hitos:

| Hito | % del precio fijo |
|------|--------------------|
| Firma del contrato | 10% (anticipo) |
| Aprobación Diseño Funcional + HLD/DLD | 10% |
| Plan de Migración firmado | 5% |
| Implementación Banda 1 + paralelo + go-live | 15% |
| Implementación Banda 2 + paralelo + go-live | 15% |
| Implementación Banda 3 + paralelo + go-live | 15% |
| Implementación Banda 4 + paralelo + go-live | 10% |
| Cumplimiento Acuerdo 1-2026 Art. 14 (jun-2027) | 5% |
| Go-live full + estabilización 90 días sin P1 críticos | 10% |
| Cierre del proyecto + handover firmado por Operaciones | 5% |
| **Total Fixed-price** | **100%** |

**T&M** para:

- Change requests post-firma > 5% del scope original — con tarifas firmadas en el contrato.
- Configuraciones de productos nuevos no contemplados.
- Servicios profesionales evolutivos años 4-7.

**Soporte anual recurrente** (años 1-7):

- Pago trimestral anticipado.
- Reducción contractual del 10% si SLA promedio anual cae bajo 99.9%.

### 9.3 Aceptación

**Criterios de aceptación por deliverable**:

- **D-01..D-03 (Diseño)**: aprobación firmada por el Comité de Arquitectura del banco.
- **D-04..D-07 (Implementación)**: pruebas E2E con dataset proporcionado por el banco; criterios funcionales y de rendimiento documentados; demo en vivo aprobada por Negocio + TI + Cumplimiento.
- **D-09 (Capacitación)**: 100% del personal clave certificado por examen.
- **D-10 (Pase a producción)**: go/no-go con voto explícito de Operaciones + Riesgos.
- **D-11 (Acuerdo 1-2026)**: validación regulatoria + dictamen de Cumplimiento.
- **D-12 (Warranty)**: 90 días consecutivos sin incidentes P1 críticos.

### 9.4 Gestión de Cambios

- Change requests con impacto técnico, presupuestario o de cronograma > 5% requieren:
  - Solicitud formal por CAP.
  - Análisis de impacto del vendor (≤ 10 días hábiles).
  - Aprobación del Comité de Tecnología (cambios < B/. 5M) o de la JD (≥ B/. 5M).
- Modificaciones contractuales pasan por dictamen de Contraloría.

### 9.5 Propiedad Intelectual

- **Software del vendor**: licencia perpetua para CAP durante la vida del contrato + 5 años de uso post-terminación si CAP decide migrar.
- **Configuraciones, parametrizaciones, customizaciones**: propiedad de CAP.
- **Código fuente del producto**: depósito en escrow con tercero independiente; condiciones de liberación: terminación del soporte del vendor, quiebra del vendor, incumplimiento material no remediado.
- **Datos de CAP**: propiedad exclusiva de CAP en todo momento.

### 9.6 Garantías y Soporte

- **Warranty** del producto: 18 meses post go-live full de cada banda — todos los defectos del producto se corrigen sin costo adicional.
- **Soporte** L1/L2/L3 24/7 en español durante toda la vida del contrato.
- **Actualizaciones de versión mayor**: incluidas durante la vida del contrato.

### 9.7 Cláusulas de Terminación

- **Por incumplimiento material no remediado** del vendor en 30 días hábiles: terminación con devolución del 100% del precio pagado de la etapa incumplida + penalización 15%.
- **Por incumplimiento de Acuerdo 1-2026 Art. 14** (30-jun-2027): terminación con penalización 15% acumulada por mes.
- **Por decisión de CAP** sin causa: terminación con pago de servicios profesionales prestados a la fecha + 30 días de aviso.
- **Por causa de fuerza mayor** (incluyendo decisión regulatoria de la SBP que prohíba el producto): terminación sin penalización para ninguna parte.

### 9.8 Auditoría

- Contraloría de la República puede auditar el contrato y la operación del vendor.
- Auditoría Interna del banco puede auditar trimestralmente.
- Pen-tests independientes anuales (cláusula NFR-SEC-006) — costo a cargo del vendor.

---

## 10. Evaluación de Propuestas

> **Referencia normativa**: el Marco de Evaluación completo está en `ARC-001-EVAL-v2.0.md`. Resumen aplicable al CBS:

### 10.1 Ponderación

- **70% Técnico / 30% Costo** (quality-first dado complejidad regulatoria y crítica).

### 10.2 Distribución del Score Técnico (sobre 70 pts)

- A — Encaje Funcional: 21 pts (30% × 70).
- B — Arquitectura Técnica & Integración: 14 pts (20% × 70).
- C — Cumplimiento Regulatorio: 10.5 pts (15% × 70).
- D — Referencias y Casos de Éxito: 7 pts (10% × 70).
- E — Presencia Regional y Soporte: 7 pts (10% × 70).
- Subtotal técnico: 59.5 pts → escalado a 70.

### 10.3 Distribución del Score Económico (sobre 30 pts)

- F.1 — TCO 7 años dentro de banda recomendada: 18 pts.
- F.2 — Pricing transparente con tope a true-ups e inflación: 6 pts.
- F.3 — Modelo CAPEX/OPEX adaptable: 3 pts.
- F.4 — Servicios profesionales incluidos: 2 pts.
- F.5 — Período de paralelo y plan de migración: 1 pt.
- Subtotal económico: 30 pts.

### 10.4 Umbrales

- **Apto para PoC**: ≥ 70/100 Y todos los 15 eliminatorios verdes.
- **Wildcard** (apto con plan de mitigación): 65-69/100 con plan firmado por gaps del Acuerdo 1-2026.
- **Rechazado**: < 65/100 O cualquier eliminatorio rojo.

### 10.5 Empate Técnico

Dos vendors dentro de ±3 pts → desempate por: (1) mayor C (Cumplimiento), (2) mayor D (Referencias banca pública), (3) mejor TCO, (4) mejor cronograma Art. 14.

---

## 11. Proceso de RFP — Instrucciones para el Vendor

### 11.1 Cronograma del Proceso

| Hito | Fecha |
|------|-------|
| Envío del RFP a vendors invitados (NDA firmado) | 2026-08-15 |
| Sesión informativa virtual | 2026-08-22 |
| Periodo de Q&A | 2026-08-15 – 2026-09-15 |
| Cierre del RFP — entrega de propuestas | 2026-10-15 (12:00 hora Panamá) |
| Apertura administrativa | 2026-10-16 – 2026-10-22 |
| Scoring técnico + económico | 2026-10-23 – 2026-11-15 |
| Demos extendidas + PoC ampliada (top-3) | 2026-11-15 – 2026-12-15 |
| Reuniones de referencia (top-3) | 2026-12-15 – 2026-12-31 |
| Recomendación del Comité de Tecnología | 2027-01-15 |
| Decisión final de la JD | 2027-01-31 |
| Adjudicación y negociación contractual | 2027-02-01 – 2027-03-15 |
| Dictamen de Contraloría | 2027-03-15 – 2027-03-30 |
| Firma del contrato | 2027-03-31 |

### 11.2 Formato de la Propuesta

- **Idioma**: español.
- **Formato**: PDF firmado digitalmente; archivos Excel/CSV donde aplique para tablas de cobertura.
- **Estructura**: 3 sobres separados (Administrativo, Técnico, Económico) — apertura por etapa.
- **Confidencialidad**: cada vendor firma NDA antes de recibir el RFP.

### 11.3 Q&A

- Las preguntas se envían por correo a la dirección oficial del proceso.
- Las respuestas se publican periódicamente a todos los vendors (anonimizadas).
- Las preguntas sobre el alcance se aceptan hasta 30 días antes del cierre.

### 11.4 Validez de la Propuesta

- 180 días desde el cierre del RFP.

### 11.5 Recursos de Impugnación

- Plazo: 15 días tras la notificación de no selección.
- Panel independiente: Auditoría Interna + Comité de Tecnología sin Chair.
- Consulta a Contraloría si procede.

---

## 12. Apéndices

### Apéndice A — Documentos de Referencia Suministrados al Vendor

| Doc | Descripción | Acceso |
|-----|-------------|--------|
| ARC-001-REQ-v2.0.md | 193 requisitos completos | Bajo NDA |
| ARC-001-EVAL-v2.0.md | Marco de Evaluación completo (15 eliminatorios + 6 categorías ponderadas) | Bajo NDA |
| ARC-000-PRIN-v1.1.md | 21 principios de arquitectura | Público para el RFP |
| DOC-RFI-001 | RFI v1.0 (junio 2026) — punto de partida | Ya enviado |
| DOC-POC-001 | Ficha técnica de PoC v1.0 | Bajo NDA |
| Anexos del RFI | Arquitectura tecnológica AS-IS + Matriz de transacciones | Bajo NDA |
| tech-notes/acuerdo-1-2026-implementation.md | Implementación de Acuerdo 1-2026 (umbral 10%, plazos) | Bajo NDA |

### Apéndice B — Vendors Invitados

Lista de vendors invitados con memo justificativo por cada decisión (defensibilidad ante Contraloría):

| Vendor | Razón de invitación |
|--------|---------------------|
| Infosys Finacle | Único Tier-1 con referente directo Panamá (BCP); cumple objetivamente los 15 eliminatorios |
| Temenos Transact | Líder Gartner MQ; mayor cobertura LatAm; cumple objetivamente los 15 eliminatorios |
| Cobis Topaz | Oficina propia Panamá + 7 referentes locales + soberanía nativa |
| Datapro / Vencora | Incumbente — benchmark obligatorio para defensibilidad ante Contraloría |
| Oracle FLEXCUBE (wildcard) | Bladex referente; sinergia stack Oracle si gana ERP/AML |
| Bantotal (wildcard) | Tier-2 LatAm; complementa diversidad de propuestas |

> **Vendors no invitados con memo justificativo en el audit trail** (mitigación R-026):
>
> - **Mambu** — no cumple E-1 (soberanía panameña) objetivamente. Modelo SaaS multi-cloud sin región Panamá; despliegue on-prem incompatible con su modelo de negocio. Profile: `vendors/mambu-profile.md`.
> - **Thought Machine** — no cumple E-1 (soberanía panameña) objetivamente. Profile: `vendors/thought-machine-profile.md`.
> - **SAP** — no opera Tier-1 CBS vigente para banca panameña; invitado al RFP-ERP en su lugar. Profile: `vendors/sap-s4hana-profile.md`.
> - **10X Banking** *(añadido por revisión post-EVAL v2.0)* — no cumple E-7 (sin integración con ecosistema panameño demostrada) ni E-8 (sin referencias en banca LatAm en producción ≥ 24 meses). Cliente referente concentrado en banca anglosajona y de Oceanía (Chase UK, Westpac). Profile: `vendors/10x-banking-profile.md`.
> - **TUUM** *(añadido por revisión post-EVAL v2.0)* — no cumple E-7 (sin integración con ecosistema panameño demostrada), E-8 (sin referencias en banca LatAm en producción ≥ 24 meses) ni cumplimiento marginal de E-10 (funding ~USD 75M Series A-B — capacidad financiera modesta frente a peer set Tier-1/Tier-2 establecidos para un banco AAA(pan) con contrato a 7 años). Profile: `vendors/tuum-profile.md`.
> - **Pismo (Visa)** *(añadido por revisión post-EVAL v2.0)* — no cumple E-1 (sin región Panamá en hyperscalers; modelo SaaS cloud-native estándar sin compromiso documentado de despliegue panameño on-prem o cloud privado regional al cierre del análisis) ni E-7 (sin integración panameña demostrada). Cumple objetivamente 10/15 eliminatorios — incluyendo E-8 con margen (referentes Itaú Unibanco, BTG Pactual, Banco Inter, **Caixa Econômica Federal — banco estatal Brasil análogo a CAP**) y E-10 (Visa-owned desde 2024, revenue ~USD 36B) — pero las dos brechas son eliminatorias bajo aplicación uniforme de los criterios. El Comité de Evaluación consideró invitación como wildcard con condicionante (cloud privado regional + homologación Yappy/ACH/Telered) y optó por **descarte limpio** para mantener disciplina del proceso. Reconsiderar en Fase 2 si Visa/Pismo desarrolla compromiso de despliegue panameño documentado. Profile: `vendors/pismo-profile.md`.

### Apéndice C — Glosario

Ver `ARC-001-REQ-v2.0.md` Apéndice B + glosario adicional del RFI v1.0 (DOC-RFI-001 §GLOSARIO).

### Apéndice D — Contactos Oficiales del Proceso

| Rol | Contacto |
|-----|----------|
| Líder del Programa | Aldo Ríos — Gerencia de Innovación |
| PMO | [PENDING] |
| Asesores externos del proceso | GFT Technologies SE + SIA Partners |
| Auditoría Interna | [PENDING] |
| Legal | [PENDING] |
| Contraloría (informativo) | [PENDING] |

---

## External References

| Doc ID | Descripción |
|--------|-------------|
| ARC-001-REQ-v2.0 | Requisitos del CBS (193 reqs) |
| ARC-001-RISK-v2.0 | Riesgos del programa (37 riesgos) |
| ARC-001-RSCH-v2.0 | Research de vendors (CBS shortlist + TCO referencia) |
| ARC-001-EVAL-v2.0 | Marco de Evaluación (15 eliminatorios + ponderación CBS) |
| ARC-001-SOBC-v2.0 | Business Case del programa (Opción 2 — Balanceada, TCO blendado B/. 175M) |
| ARC-001-STKE-v1.0 | Stakeholders y drivers |
| ARC-000-PRIN-v1.1 | 21 principios de arquitectura |
| DOC-RFI-001 | RFI v1.0 emitido jun-2026 |
| DOC-POC-001 | Ficha PoC v1.0 |
| DOC-SES-001..009 | Resúmenes de las 8 sesiones presenciales |

---

**Generated by**: ArcKit `/arckit:sow` command
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Reemplazo del Core Banking + ERP + AML (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: SOW formal para RFP CBS (1 de 3 RFPs coordinados) construido sobre RFI v1.0 + REQ v2.0 + RISK v2.0 + RSCH v2.0 + EVAL v2.0 + SOBC v2.0. Contrato Hybrid; ponderación 70% Técnico / 30% Costo; eliminatorios incluyen E-13 (integración ERP), E-14 (offload AML), E-15 (Acuerdo 1-2026 Art. 14 ≤ 30-jun-2027).
