# Requisitos del Proyecto — Evaluación y Selección de Core Banking — Caja de Ahorros de Panamá

> **Origen de la plantilla**: Oficial | **Versión ArcKit**: 5.13.0 | **Comando**: `/arckit:requirements`

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-REQ-v2.0 |
| **Document Type** | Business and Technical Requirements |
| **Project** | Caja de Ahorros — Evaluación y Selección de Core Banking (Project 001) |
| **Classification** | OFFICIAL-SENSITIVE (equivalente a "CONFIDENCIAL – Uso interno") |
| **Status** | DRAFT |
| **Version** | 2.0 |
| **Created Date** | 2026-05-19 |
| **Last Modified** | 2026-06-11 |
| **Review Date** | 2026-07-11 |
| **Owner** | Aldo Ríos — Gerencia de Innovación / Líder de Programa Core Banking |
| **Reviewed By** | [PENDING] |
| **Approved By** | [PENDING] |
| **Distribution** | Junta Directiva, Gerencia General, Comité de Tecnología, Cumplimiento, Riesgos, Auditoría Interna, TI, Operaciones, Finanzas, áreas de negocio (Hipotecas, Créditos, Digital), CISO, Legal, RRHH, PMO, vendors finalistas (bajo NDA) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-05-19 | ArcKit AI | Creación inicial mediante `/arckit:requirements`. Requisitos derivados de ARC-000-PRIN-v1.1 (21 principios), ARC-001-STKE-v1.0 (17 drivers, 10 metas, 10 resultados) y del relevamiento confidencial DOC-CB-001/002/003. Cobertura: 12 BR, 46 FR, 38 NFR, 20 INT, 19 DR. | PENDING | PENDING |
| 2.0 (corrigendum) | 2026-06-11 (PM) | ArcKit AI | **Corrigendum post-`/arckit:research`** sobre el Acuerdo SBP 1-2026 — al verificar contra el PDF oficial de la SBP (Resolución SBP-JD-0001-2026 del 16-ene-2026): (a) **umbral de beneficiario final corregido de ≥ 25% a ≥ 10%** — Panamá adopta un umbral más estricto que la UE y la FATF (que sí usan 25%); (b) **plazos discretos por artículo en lugar de "general jul-2025 / digitales jul-2027"**: Art. 25 §1 vigencia 31-ene-2027; Art. 14 (beneficiario final + geolocalización inferencial digital) vigencia 30-jun-2027; no hay un hito "general jul-2025" en el articulado oficial; (c) **geolocalización inferencial** (no sólo GPS — combina IP+ASN, dispositivo/UA, GPS y comportamiento) en lugar de "geolocalización digital" genérica. Correcciones aplicadas a BR-002 (Justificación + criterios), FR-009 (cuentas corrientes), FR-052 (beneficiario final), FR-053 (geolocalización) y Apéndice C — Cheat sheet. Fuente: PDF oficial SBP verificado por el sub-agente `arckit-research` y citado en `research/ARC-001-RSCH-v2.0.md` + `tech-notes/acuerdo-1-2026-implementation.md`. Sin cambios al conteo (193 requisitos) ni a la versión (sigue v2.0 — DRAFT del día). | PENDING | PENDING |
| 2.0 | 2026-06-11 | ArcKit AI | **Major refresh** tras las 8 sesiones presenciales (25–28 mayo 2026) entre CAP, GFT y SIA Partners y la emisión del RFI v1.0 (junio 2026). Cambios materiales que justifican el bump mayor: (a) **AML revertido a herramienta externa con IA y APIs** (anteriormente embebido en el Core; el proveedor actual sale de soporte en 2026); (b) **adquisición de ERP separado** como decisión estratégica — el nuevo CBS no incluirá GL completo (BR-013, INT-021); (c) incorporación del **Acuerdo SBP 1-2026** (Resolución SBP-JD-0001-2026 del 16-ene-2026; Art. 25 §1 vigencia 31-ene-2027; Art. 14 — beneficiario final ≥ **10%** + geolocalización inferencial digital — vigencia 30-jun-2027) — multas elevadas; (d) regulaciones adicionales formalizadas: **Ley 23/2015** (DJTE ≥ B/. 10,000), **Ley 468/2025** (Interés Preferencial), **Ley 52/2000** (cheques), **NIIF 16** (leasing), **IAS 21** (divisas), **UCP 600 / ISP 98 / URDG 758** (comercio exterior); (e) **FECI 1%** sobre intereses comerciales como retención automática; (f) inventario completo de **sistemas satélite** (SITECA, BPMs Ultimus/Asicom/Genexus, Emerix, Átomos, Talentía, BCG, ANDREA, Banca Seguro, App Enhancer, SISCARD, Panadata, Telered, Omnicaja); (g) **CIF único + vista 360°** como pilar arquitectónico (FR/DR refinados); (h) **catálogo funcional completo** por producto incorporado del RFI (cuentas con sub-cuentas/cajones, sobregiros nativos, cheques de gerencia/chequeras, DDI, cartas de crédito, factoring con pagadores estatales, líneas de crédito, leasing NIIF 16, préstamos de construcción, prendarios, autos, créditos sindicados como coordinador y participante, hipotecario para panameños en el exterior, reestructuración nativa, contagio APC); (i) **preferencias de despliegue explícitas** del banco — **Azure preferida** (stack actual), **AWS** para Data Lake/Snowflake, **on-premise** mientras no haya dictamen Innovación + Seguridad Nacional; (j) **preferencias y descartes de vendor** (COBIS preferido; Temenos, Finacle, Mambu, SAP descartados — informativo, no eliminatorio del RFP); (k) **CAPEX→OPEX** como dirección estratégica que afecta la elección de modelo de despliegue (BR-014); (l) requisitos de **seguridad ampliados**: SoD configurable, recertificación periódica de accesos, SSO con Microsoft Entra ID, SAML/OAuth/OIDC/LDAP, MFA por perfil y canal, enmascaramiento por rol; (m) **localización** explícita (UTC-5, USD, DD/MM/AAAA, español primario / inglés opcional); (n) **validación en tiempo de ingreso** como requisito transversal de calidad de datos (DOC-SES-006); (o) métricas actualizadas: **60 sucursales** (antes 54), almacenamiento 70–80 TB, 13,000 tarjetas activas, ~B/. 1,015M cartera personal, ~B/. 3,000M depósitos particulares, 833 empresas + 178 entidades gubernamentales para DDI, 8,000+ elementos del diccionario de datos, 54+ reportes regulatorios mensuales, 96% de datos provienen del Core actual. Nuevas citas DOC-SES-001..009 (sesiones presenciales), DOC-RFI-001 (RFI v1.0), DOC-POC-001 (ficha PoC v1.0). Cobertura: 14 BR, 76 FR, 50 NFR, 31 INT, 22 DR = **193 requisitos**. | PENDING | PENDING |

## Propósito del Documento

Define los requisitos de negocio, funcionales, no funcionales, de integración y de datos para la **evaluación, selección, contratación e implementación del nuevo Core Banking (CBS) de Caja de Ahorros de Panamá (CAP)**. Sirve como insumo central para:

- El **RFI** (ya emitido — DOC-RFI-001) y el **RFP** subsecuente, incluyendo criterios eliminatorios.
- Las **demos y la PoC** (cuyo caso de uso de referencia — crédito hipotecario para panameño residente en el exterior — está definido en DOC-POC-001).
- El **HLD / DLD** de la solución seleccionada.
- Las **revisiones de arquitectura** en cada gate.
- La **matriz de trazabilidad** con las metas del programa (STKE) y los principios (PRIN v1.1).

---

## Resumen Ejecutivo

### Contexto de Negocio

Caja de Ahorros es el banco del Estado panameño bajo Ley 20 de 1975 [DOC-CB-003-C1], con activos > B/. 6,911M, depósitos > B/. 5,630M (B/. ~3,000M de particulares [DOC-SES-009]), cartera > B/. 4,943M (B/. ~3,000M hipotecaria, B/. ~1,015M personal, B/. ~40M leasing, 13,000 tarjetas activas [DOC-SES-009]), más de 650,000 clientes, 60 sucursales [DOC-RFI-001], 140 ATMs, 100+ corresponsales Caja Amiga [DOC-SES-009], 51M+ transacciones digitales anuales y calificación AAA(pan) [DOC-CB-001-C3]. Su Core actual **DataPro/eIBS** [DOC-CB-001-C1, DOC-RFI-001] ha alcanzado fin de ciclo de vida útil: requerimientos de hasta 2 años, parametrización escasa, lenguaje obsoleto, costo elevado y relación deteriorada con el proveedor [DOC-SES-009 §3.3].

El reemplazo del Core es un programa **multi-año, de alto riesgo y alta visibilidad** — afecta a 650,000+ clientes, al ecosistema panameño de pagos (Yappy + 55 instituciones / 1.6M usuarios [DOC-CB-001-C7]) y al mandato social del Estado (Interés Preferencial, FGA, Profimype, transferencias sociales). La selección se rige por los 21 principios de arquitectura (ARC-000-PRIN-v1.1) y por las metas G-1..G-10 del análisis de stakeholders (ARC-001-STKE-v1.0).

Las **sesiones presenciales del 25–28 de mayo de 2026** (8 sesiones — Arquitectura, Estrategia/Negocio, Captación, Crédito, Datos, Regulatoria, Ciberseguridad, Infraestructura [DOC-SES-009 §1.1]) consolidaron requerimientos no negociables y formaron la base del RFI v1.0 emitido en junio.

### Objetivos

- Garantizar **cumplimiento regulatorio nativo** SBP / UAF / SEI / APC / NIIF 9 + Acuerdo 6-2000 / **Acuerdo 1-2026** desde el go-live [DOC-RFI-001 §2.1, DOC-SES-006].
- Sustentar la **agenda digital activa sin interrupciones** durante y después del cambio [DOC-CB-001-C6].
- Habilitar el **mandato social del Estado** mediante parametrización (no desarrollo a medida) [DOC-CB-001-C27].
- Mantener el **TCO contractual dentro del presupuesto aprobado por la Junta Directiva** con auditabilidad de Contraloría.
- **Migrar el GL a un ERP externo** y operar con CIF único + vista 360° del cliente [DOC-RFI-001 §2.2, §3.9, §3.10, DOC-SES-009 §6.3].
- **Eliminar AML embebido**: integrar herramienta AML externa con IA y APIs en tiempo real [DOC-SES-006, DOC-SES-009 §10.4].
- Migrar **sin pérdida de datos ni divergencias contables** contra el sistema legado.
- Preservar **disponibilidad 24/7** [DOC-SES-009 §10.2] y **calificación AAA(pan)** durante todo el ciclo.
- Habilitar la transición **CAPEX → OPEX** del presupuesto tecnológico [DOC-SES-008].

### Resultados Esperados

- Cero hallazgos críticos en inspecciones SBP en 24 meses post go-live (O-1 STKE).
- TCO a 7 años dentro del ±10% del presupuesto (O-2 STKE).
- Disponibilidad mensual ≥ 99.99% para servicios críticos en línea y ≥ 99.95% para canales digitales (O-3 STKE).
- Cero interrupciones de Yappy / ACH / Telered durante migración (O-4 STKE).
- 100% de productos sociales operativos con cálculo automático del subsidio de Interés Preferencial (O-5 STKE).
- Modelo dual NIIF 9 + Acuerdo 6-2000 automatizado con cero diferencias materiales contra legado (O-6 STKE).
- Dictamen legal de soberanía de datos vinculante antes del RFP (O-7 STKE).
- Contratación pública aprobada por Contraloría sin observaciones materiales (O-8 STKE).
- NPS ≥ +40 sostenido (O-9 STKE).
- AAA(pan) sostenido (O-10 STKE).

### Alcance del Proyecto

**En alcance**:

- Reemplazo del Core Banking transaccional **DataPro/eIBS** (cuentas, depósitos, créditos, hipotecas, contabilidad transaccional, reportería) [DOC-CB-001-C1, DOC-RFI-001].
- **Adquisición de un ERP externo** para el Libro Mayor (GL) consolidado, rentabilidad por sucursal y estados financieros [DOC-RFI-001 §3.9, DOC-SES-005, DOC-SES-009 §6.3] — selección del ERP es proyecto paralelo coordinado.
- Integraciones nativas con el ecosistema panameño: Yappy, ACH Panamá, Telered (ATM/POS), SWIFT (vía SCONNECT LAU/CSV), SEI, UAF, APC, MIVIOT, MEF, SIACAP, DGI (subsidio Interés Preferencial).
- Migración de datos de **DataPro/eIBS** y consolidación de **sistemas satélite**: SITECA (originación hipotecaria), BPMs Ultimus / Asicom-Finflow / Genexus (originación personal/consumo/auto), Emerix (cobros), Átomos (BI regulatorio), BCG (SWIFT), Banca Seguro (broker), Profimype, sistemas hipotecarios auxiliares, hojas Access/Excel [DOC-SES-001, DOC-SES-009 §3.2].
- Integración con **SISCARD** (core de tarjetas separado) para vista unificada [DOC-RFI-001 §3.10, DOC-SES-001].
- Integración con **App Enhancer** (gestor documental SaaS) y proyecto de expediente único digital [DOC-RFI-001 §2.2, DOC-SES-006].
- Integración con **Panadata** (KYC) y nueva herramienta AML externa con IA [DOC-SES-006, DOC-RFI-001 §3.10].
- Integración con **plataforma IAM** (proyecto en curso) y SSO con **Microsoft Entra ID (Azure AD)** [DOC-SES-007, DOC-RFI-001 §4.7].
- Modelo dual de provisiones NIIF 9 + Acuerdo 6-2000 [DOC-CB-003-C10].
- Plan de cuentas SBP estandarizado y reportería SEI nativa [DOC-CB-003-C7, DOC-CB-003-C23].
- Soporte a productos del mandato social y a la **alianza estratégica con el Estado para macro-obras (~B/. 3,000M)** [DOC-SES-003, DOC-SES-009 §3.2].
- **Hipotecario para panameños en el exterior** (nuevo segmento en desarrollo) [DOC-RFI-001 §3.2.1, DOC-SES-009 §3.2].
- Capacitación al personal en español y plan de gestión del cambio [DOC-CB-001-C29].

**Fuera de alcance** (para fases o iniciativas separadas):

- Reemplazo de la Super App, A.N.D.R.E.A. y del **bus IBM MQ** existente — se mantienen como capa de abstracción [DOC-CB-001-C21, DOC-SES-001].
- Reemplazo del **core de tarjetas SISCARD** — se integra, no se sustituye en Fase 1 [DOC-RFI-001 §2.2].
- Reemplazo del sistema de **Tesorería** independiente y de **licencia fiduciaria** con contabilidad independiente [DOC-SES-006] — evaluar en Fase 2.
- Reemplazo del sistema de **Cobranza externa** (Emerix evoluciona o se sustituye en Fase 2 una vez que el CBS gestione 0–90 días nativos).
- Desarrollo de nuevos canales digitales (cubierto por programas paralelos, incluyendo el proyecto **Omnicaja** de 24 meses [DOC-SES-001]).
- Implementación de XBRL completo (planificado en Fase 2, alineado al roadmap SBP) [DOC-CB-003-C29].
- Selección de la herramienta **AML externa** (proyecto paralelo coordinado, con go-live alineado al del CBS dado que el proveedor actual sale de soporte en 2026 [DOC-SES-006, DOC-SES-009 §10.3]).

---

## Stakeholders

> Consulte `ARC-001-STKE-v1.0.md` para análisis detallado de los 27 stakeholders (18 internos + 9 externos). Resumen de los stakeholders con autoridad sobre requisitos:

| Stakeholder | Rol | Organización | Nivel de involucramiento |
|-------------|-----|-------------|--------------------------|
| Junta Directiva | Autoridad final | Caja de Ahorros | Decisión de gates |
| Gerencia General | Patrocinador ejecutivo | Caja de Ahorros | Aprobación de hitos |
| Aldo Ríos | Líder de programa | Innovación | Dueño del documento |
| Gerencia de Tecnología (TI) | Dueño técnico | Caja de Ahorros | Definición técnica |
| Cumplimiento | Riesgo regulatorio | Caja de Ahorros | Compuertas regulatorias |
| Riesgos | Riesgo operacional / crediticio | Caja de Ahorros | Modelos NIIF 9 / 6-2000 |
| Operaciones | Continuidad del negocio | Caja de Ahorros | Disponibilidad / SLA |
| Finanzas | Control TCO / contratación | Caja de Ahorros | Presupuesto, CAPEX/OPEX |
| CISO | Seguridad | Caja de Ahorros | Controles obligatorios |
| Legal | Contratos y dictámenes | Caja de Ahorros | Soberanía / cláusulas |
| Hipotecas / Créditos / Digital | Áreas de negocio | Caja de Ahorros | Casos de uso |
| Datos / Calidad | Gobierno de datos | Caja de Ahorros | Validaciones, streaming |
| SBP | Regulador (supervisión coordinada) | Externo | Reportería / inspección |
| UAF | Receptor de ROS AML/FT | Externo | AML / KYC |
| Contraloría General | Auditor de contratos y sistemas | Externo | Ley 22 / IaC / pases |
| APC | Central de Riesgos | Externo | Reportería de cartera |
| DGI | Subsidio Interés Preferencial (Ley 468/2025) | Externo | Reclamo trimestral |

---

## Aclaraciones sobre el alcance solicitado

- **SINPE** es el sistema interbancario de Costa Rica. El ecosistema **panameño** equivalente es **ACH Panamá** (cámara), **Yappy** (P2P) y **Telered** (switch ATM/POS). SINPE solo aplica si hay corresponsalía con Costa Rica — INT-019 sigue como TBD.
- **SIACAP** (Sistema de Ahorro y Capitalización de Pensiones de servidores públicos): cubierto en INT-009.
- **AML / PLD**: a partir de v2.0, el banco confirma que el **monitoreo AML será una herramienta externa con IA y APIs** [DOC-SES-009 §10.4]. El CBS NO requiere módulo AML interno; sí debe **exponer eventos transaccionales en tiempo real** a la herramienta externa y bloquear transacciones bajo instrucción del motor AML (FR-022 revisado).
- **ERP / GL**: a partir de v2.0, se asume **adquisición de un ERP externo** (selección paralela) para el GL consolidado. El CBS sigue siendo responsable de los **asientos contables transaccionales** y de su exposición al ERP vía API (BR-013, INT-021).
- **Cores descartados vs preferido (informativo, no eliminatorio)**: el banco expresó preferencia por **COBIS** (experiencia regional positiva) y descarte explícito de **Temenos, Finacle, Mambu, SAP** [DOC-SES-009 §3.4, §10.4]. El RFP debe operar sobre criterios eliminatorios objetivos; estas preferencias no constituyen criterios de descalificación pero alimentan la matriz de ponderación.
- **Nube**: preferencia explícita por **Microsoft Azure** (stack actual del banco) [DOC-SES-008, DOC-SES-009 §9.3]. **AWS** se mantiene para el Data Lake y migración Snowflake del DWH [DOC-SES-005]. Cualquier despliegue cloud requiere dictamen previo de **Autoridad de Innovación + SBP + Seguridad Nacional** [DOC-SES-001, DOC-SES-008].

---

## Requisitos de Negocio (BR)

### BR-001: Reemplazo del Core Banking preservando continuidad operacional

**Descripción**: Reemplazar la plataforma transaccional **DataPro/eIBS** [DOC-CB-001-C1, DOC-RFI-001] por un nuevo CBS moderno, sin interrumpir canales digitales, ATMs, ni reportería regulatoria durante la migración.

**Criterios de éxito**: cero interrupciones imputables al cambio en Yappy / ACH / Telered; disponibilidad ≥ 99.95% mensual sostenida durante migración (≥ 99.99% post go-live para servicios críticos); migración por bandos con paralelo ≥ 3 meses por bando.

**Prioridad**: MUST_HAVE | **Stakeholder**: Gerencia General (SD-2), Junta Directiva (SD-1), Operaciones (SD-8). | **Trazabilidad**: G-3, G-4 (STKE) — PRIN P2, P3, P11, P12.

### BR-002: Cumplimiento regulatorio nativo SBP / UAF / SEI / Acuerdo 1-2026

**Descripción**: el nuevo CBS genera y envía nativamente al SEI el 100% de los reportes del inventario D04 [DOC-CB-001-C12], soporta Acuerdos SBP (4-2013, 6-2000, 5-2011, 3-2009, 8-2010, **1-2026**), Resolución SBP-DJ-0014, **Ley 23/2015** (DJTE), **Ley 468/2025** (Interés Preferencial), **Ley 52/2000** (cheques) [DOC-RFI-001 §2.1], y expone eventos transaccionales a la herramienta AML externa para envío de ROS a la UAF en tiempo real.

**Justificación**: el **Acuerdo SBP 1-2026** (Resolución SBP-JD-0001-2026 del 16-ene-2026) introduce multas elevadas, **geolocalización inferencial** de clientes digitales y validaciones de **beneficiario final ≥ 10%** (umbral más estricto que el 25% adoptado por la UE y la FATF) [DOC-SES-006, DOC-RFI-001 §2.1; PDF oficial SBP §Art. 14, §Art. 25 §1]. Plazos discretos por artículo: **Art. 25 §1 vigencia 31-ene-2027**; **Art. 14 vigencia 30-jun-2027** (beneficiario final + geolocalización inferencial digital). Las inspecciones SBP replican la clasificación A–E [DOC-CB-003-C18]; diferencias sistemáticas derivan en provisiones adicionales.

**Criterios de éxito**:

- 100% de reportes D04 generados nativamente y aceptados por el SEI.
- Tres ciclos mensuales consecutivos sin rechazos críticos en pre-producción o sandbox SBP.
- Geolocalización **inferencial** (no solo GPS — IP+ASN, dispositivo/UA, comportamiento) capturada y persistida para todos los registros de canales digitales antes de **30-jun-2027** (Art. 14).
- Workflow de **beneficiario final ≥ 10%** operativo desde el día 1 para personas jurídicas (Art. 14).
- Eventos AML expuestos a la herramienta externa con latencia < 200 ms (FR-022 revisado).

**Prioridad**: MUST_HAVE | **Stakeholder**: Cumplimiento (SD-7), SBP (SD-9), UAF (SD-16), Riesgos (SD-14). | **Trazabilidad**: G-1, G-6 — PRIN P4, P5, P7, P8.

### BR-003: TCO controlado a 7 años con auditabilidad de Contraloría

**Descripción**: TCO contractual a 7 años (licenciamiento + mantenimiento + soporte + infraestructura + módulos opcionales + servicios profesionales de implementación + **ERP externo** + **herramienta AML externa**) fijado al firmar el contrato dentro de ±10% del presupuesto JD, con cláusulas de tope a "true-ups" e incrementos anuales.

**Criterios de éxito**: TCO efectivo / contractual ±10%; cláusulas con tope a inflación y a módulos opcionales; auditoría anual sin observaciones materiales.

**Prioridad**: MUST_HAVE | **Stakeholder**: Finanzas (SD-4), Junta Directiva (SD-1), Contraloría (SD-10). | **Trazabilidad**: G-2, G-8.

### BR-004: Soporte completo al mandato social del Estado

**Descripción**: al go-live, 100% de los productos del mandato social operativos con **parametrización nativa** (no desarrollo a medida): Interés Preferencial (Ley 468/2025), FGA, Profimype, "Una Cuenta Para Todos", transferencias sociales (Beca Universal, 120 a los 65, Red de Oportunidades), créditos verdes, **Caja Amiga** (régimen simplificado).

**Criterios de éxito**: 100% operativo día 1; cálculo automático del subsidio Interés Preferencial sin diferencias contra legado; reclamo trimestral a DGI automatizado [DOC-RFI-001 §3.2.1]; parametrización demostrada en demo (sin código del vendor).

**Prioridad**: MUST_HAVE | **Stakeholder**: Hipotecas (SD-11), Créditos (SD-12), MIVIOT, MEF, DGI. | **Trazabilidad**: G-5 — PRIN P20.

### BR-005: Modelo dual de provisiones NIIF 9 + Acuerdo 6-2000 automatizado

**Descripción**: ejecución mensual automatizada de NIIF 9 ECL (3 stages) y Acuerdo 6-2000 (A–E); registro del mayor; diferencia como reserva regulatoria en patrimonio sin pasar por resultados [DOC-CB-003-C17]. Contagio inter-crédito + integración APC [DOC-CB-003-C20, DOC-RFI-001 §3.3].

**Criterios de éxito**: ejecución simultánea demostrada; corrida paralela ≥ 3 meses pre-corte con cero diferencias materiales; umbral SICR parametrizable; contagio automático con consumo de Central de Riesgos APC.

**Prioridad**: MUST_HAVE | **Stakeholder**: Riesgos (SD-14), Cumplimiento (SD-7), Créditos (SD-12), SBP (SD-9). | **Trazabilidad**: G-6 — PRIN P8.

### BR-006: Soberanía de datos en Panamá validada legalmente antes del RFP

**Descripción**: dictamen Legal firme y vinculante sobre residencia de datos personales, financieros, transaccionales y de seguridad nacional **antes del cierre del RFP**. Vendors que no cumplan son eliminados.

**Justificación**: la regulación panameña prohíbe almacenar datos sensibles fuera del país, especialmente fondos públicos y cuentas de organizaciones gubernamentales [DOC-SES-008, DOC-CB-001-C10]. La consulta formal a Autoridad de Innovación, SBP y Seguridad Nacional debe completarse pre-RFP.

**Criterios de éxito**: dictamen emitido; mapa de residencia por tipo de dato; cláusulas contractuales de residencia; auditoría trimestral.

**Prioridad**: MUST_HAVE | **Stakeholder**: Legal, Cumplimiento, Contraloría, CISO. | **Trazabilidad**: G-7 — PRIN P6.

### BR-007: Contratación pública aprobada por Contraloría sin observaciones materiales

**Descripción**: el proceso (RFI → RFP → contrato) cumple Ley 22 de Contrataciones Públicas; el contrato firmado pasa auditoría de Contraloría sin observaciones materiales.

**Criterios de éxito**: proceso documentado y firmado; cero observaciones materiales; dictamen jurídico previo a la firma.

**Prioridad**: MUST_HAVE | **Stakeholder**: Finanzas, Legal, Contraloría, JD. | **Trazabilidad**: G-8.

### BR-008: Migración con conciliación contable exacta y cero pérdida de datos

**Descripción**: la migración valida saldo-por-saldo (depósitos, cartera, hipotecas, garantías, contingentes) contra el legado, diferencias = 0 al cierre del corte. Hipotecas con condiciones especiales antiguas (subsidios, moratorias COVID-19) preservan trazabilidad histórica [DOC-CB-001-C15]. Consolida sistemas satélite (SITECA, BPMs, Profimype, Excel/Access [DOC-SES-009 §3.2]).

**Criterios de éxito**: diferencias = 0; 100% de registros migrados; Auditoría Interna firma reporte de conciliación post-corte; los 8,000+ elementos del diccionario actual [DOC-SES-009 §6.1, DOC-RFI-001 §4.6] tienen mapeo trazable al nuevo modelo de datos.

**Prioridad**: MUST_HAVE | **Stakeholder**: TI, Riesgos, Auditoría Interna, Operaciones. | **Trazabilidad**: G-9 — PRIN P8.

### BR-009: Adopción del personal mediante capacitación en español y gestión del cambio

**Descripción**: 100% del personal de TI, Operaciones, Hipotecas, Créditos, Digital, Atención al Cliente y Cumplimiento capacitado y certificado en español antes del corte.

**Criterios de éxito**: 100% certificado pre-corte; documentación funcional/técnica en español; soporte L1/L2/L3 24/7 en español verificado contractualmente.

**Prioridad**: MUST_HAVE | **Stakeholder**: RRHH, Aldo Ríos, Gerencia General, Operaciones. | **Trazabilidad**: G-10 — PRIN P21.

### BR-010: Sostenimiento de la agenda digital activa sin interrupción

**Descripción**: Super App, A.N.D.R.E.A. (premiada Fintech Américas 2025 [DOC-CB-001-C6]), Yappy y el proyecto **Omnicaja** (24 meses [DOC-SES-001]) DEBEN seguir operativos durante la migración.

**Criterios de éxito**: APIs versionadas con compatibilidad hacia atrás; bus IBM MQ + API Gateway preservados como capa de abstracción [DOC-CB-001-C21, DOC-RFI-001 §4.2]; cero lanzamientos digitales suspendidos por el proyecto Core.

**Prioridad**: MUST_HAVE | **Stakeholder**: Digital (SD-13), Aldo Ríos, TI. | **Trazabilidad**: G-3, G-4 — PRIN P11, P16.

### BR-011: Calificación AAA(pan) sostenida durante y después del proyecto

**Descripción**: AAA(pan) con perspectiva estable mantenida durante el ciclo y por ≥ 24 meses post go-live.

**Prioridad**: SHOULD_HAVE (resultado) | **Stakeholder**: JD, Gerencia General, Finanzas. | **Trazabilidad**: O-10.

### BR-012: Inclusión financiera operativa en zonas rurales y comarcas

**Descripción**: Red **Caja Amiga** (+100 puntos [DOC-SES-001]) y sucursales rurales operan sin pérdida de funcionalidad, con modo degradado / conciliación diferida.

**Prioridad**: MUST_HAVE | **Stakeholder**: Red Caja Amiga, Hipotecas, Operaciones. | **Trazabilidad**: PRIN P15.

### BR-013 (NEW v2.0): Adquisición e integración de ERP externo para el GL consolidado

**Descripción**: la transición a un nuevo CBS obliga a **adquirir un ERP externo** para gestionar el Libro Mayor (GL) consolidado, rentabilidad por sucursal y estados financieros, dado que los CBS modernos no incluyen GL completo [DOC-RFI-001 §3.9, DOC-SES-005, DOC-SES-009 §6.3].

**Justificación**: en DataPro/eIBS el GL forma parte del Core; al reemplazar el Core la funcionalidad de GL debe quedar en un sistema independiente (ERP) capaz de soportar plan de cuentas SBP, doble contabilidad NIIF / regulatoria, IAS 21 (diferencias de cambio), rentabilidad multi-dimensional y cierre coordinado.

**Criterios de éxito**:

- ERP seleccionado e implementado en paralelo, con go-live alineado al CBS.
- Asientos transaccionales generados por el CBS expuestos vía API al ERP en tiempo real o micro-batch (≤ 5 min).
- Plan de cuentas SBP cargado en CBS y ERP sin discrepancias.
- Doble contabilidad NIIF + regulatoria soportada sin doble ingreso de datos.
- Cierre diario, mensual y anual coordinado entre CBS, Teller y ERP sin diferencias.

**Prioridad**: MUST_HAVE | **Stakeholder**: Finanzas (SD-4), TI (SD-5), Riesgos, Contraloría. | **Trazabilidad**: G-9, G-1.

### BR-014 (NEW v2.0): Transición CAPEX → OPEX del presupuesto tecnológico

**Descripción**: el banco opera hoy con mayor CAPEX que OPEX; el objetivo estratégico es **aumentar OPEX y disminuir CAPEX** [DOC-SES-008 §9.4]. Esta orientación afecta el modelo de despliegue del CBS (cloud / SaaS preferido sobre on-premise siempre que la soberanía de datos lo permita) y la estructura del contrato (suscripción anual vs licencia perpetua).

**Justificación**: el cambio CAPEX→OPEX libera presupuesto de inversión para iniciativas adicionales y alinea el modelo financiero del banco al estándar de la industria. La soberanía de datos (BR-006) crea tensión que debe resolverse antes del RFP — el dictamen Legal puede habilitar cloud regional o privado en territorio panameño.

**Criterios de éxito**: modelo financiero del contrato seleccionado documentado y aprobado por Finanzas y JD; impacto presupuestario CAPEX/OPEX proyectado a 7 años en el TCO contractual.

**Prioridad**: SHOULD_HAVE | **Stakeholder**: Finanzas, JD, Gerencia General. | **Trazabilidad**: G-2.

---

## Requisitos Funcionales (FR)

### Personas

#### Persona 1: Cliente persona natural — "María"

35 años, sector público, ahorro + hipoteca Interés Preferencial + Yappy + planilla. Metas: Super App fluida, hipoteca con tasa preferencial automática, pagos puntuales. Dolores: caídas en fin de mes; demora aclaraciones.

#### Persona 2: Cliente sin historial — "Carlos"

28 años, "Una Cuenta Para Todos", primer producto bancario. Metas: apertura 100% digital, Yappy. Dolores: trámites complejos.

#### Persona 3: PYME — "Doña Elena"

Dueña de microempresa, Profimype. Metas: microcrédito, pagos electrónicos, reportería. Dolores: documentación duplicada.

#### Persona 4 (NEW v2.0): Cliente panameño residente en el exterior — "Juan Carlos"

34 años, ingeniero, residente en Miami desde 2016, ingresos del exterior, cuenta de ahorro con remesas regulares, busca crédito hipotecario para vivienda en Panamá [DOC-POC-001]. Persona del caso de uso de referencia de la PoC.

#### Persona 5: Asesor de sucursal

Atención presencial. Metas: abrir cuentas y créditos en minutos. Dolores: pantallas legacy, lentitud en cascada de productos.

#### Persona 6: Analista de Cumplimiento

Revisa alertas AML (en herramienta externa), prepara reportes SBP. Metas: trazabilidad de evidencia; envíos al SEI sin rechazos. Dolores: extracción manual.

#### Persona 7: Analista de Riesgos

Corre modelos NIIF 9 + 6-2000 y reservas dinámicas. Metas: cuadre mensual sin diferencias.

#### Persona 8: Operador del Core / Administrador TI

Operación 24/7, monitoreo, pases. Metas: cero incidentes y pases con doble aprobación auditable.

#### Persona 9 (NEW v2.0): Cajero / Teller

Operación de ventanilla. Metas: cuadre automático al cierre, gestión de bóveda sin Excel, monitoreo AML integrado [DOC-RFI-001 §3.7].

#### Persona 10 (NEW v2.0): Originador comercial (BPM)

Trabaja en Ultimus / Asicom-Finflow / Genexus. Meta: el CBS recibe el crédito aprobado y lo gestiona sin re-captura [DOC-RFI-001 §3.2, DOC-SES-004].

---

### Casos de Uso Críticos

UC-1..UC-6 de v1.0 se preservan (pago de planilla, apertura digital, originación hipotecaria, envío SEI, transferencia Yappy, cierre mensual dual). Se añaden:

#### UC-7 (NEW v2.0): Originación hipotecaria con codeudores + período de gracia + sub-cuentas de ahorro (PoC de referencia)

Actor: Asesor + Persona 4 (Juan Carlos). Escenario completo definido en DOC-POC-001 §2 — 13 módulos evaluados (M1..M13), 10 pasos secuenciales.

#### UC-8 (NEW v2.0): Reestructuración nativa de crédito

Actor: Persona 7 + cliente. El CBS modifica el crédito sin cancelarlo (extensión plazo, reducción tasa, capitalización intereses vencidos, gracia adicional) preservando trazabilidad histórica [DOC-RFI-001 §3.3].

#### UC-9 (NEW v2.0): Apertura de Carta de Crédito de Importación

Actor: cliente corporativo + Operaciones Comex. Solicitud → validación de línea → registro CBS → envío SWIFT → recepción de documentos → revisión de conformidad → pago/negociación → asiento contable [DOC-RFI-001 §3.5.1]. UCP 600.

#### UC-10 (NEW v2.0): Factoring con pagador estatal

Cesión, validación, abono al cedente con retención 10%, cobro a pagador, liquidación final [DOC-RFI-001 §3.5.2, DOC-SES-004].

#### UC-11 (NEW v2.0): Transacción en efectivo ≥ B/. 10,000 con DJTE

Persona 9 (Teller) ejecuta depósito en efectivo ≥ B/. 10,000; el CBS **bloquea** la transacción hasta completar la Declaración Jurada de Transacción en Efectivo conforme Ley 23/2015 [DOC-RFI-001 §3.7].

#### UC-12 (NEW v2.0): Préstamo de construcción con desembolso por tramos y conversión automática a hipoteca

Plan de desembolsos por hitos de avance; al concluir la obra, conversión automática a hipoteca estándar con constitución de garantía hipotecaria definitiva [DOC-RFI-001 §3.2.4].

#### UC-13 (NEW v2.0): Pago masivo de planilla con DDI hacia múltiples empleadores

CAP administra 833 empresas privadas y 178 entidades de gobierno con DDI activo [DOC-RFI-001 §3.2.2]. El CBS procesa archivos (Excel/TXT) en lote, aplica débitos automáticos, gestiona rechazos.

---

### Detalle de Requisitos Funcionales

#### Bloque A — Cuentas y depósitos

##### FR-001: Apertura de cuenta presencial

Cuenta de ahorro/corriente/inclusión con flujo guiado en español. Validación de cédula con dígito verificador, KYC, contrato en ≤ 5 min. **Prioridad**: MUST.

##### FR-002: Apertura digital con KYC simplificado ("Una Cuenta Para Todos")

100% digital, biometría/OCR, listas restrictivas en línea, ≥ 100 concurrentes sin degradación, límites prudenciales hasta KYC reforzado [DOC-CB-001-C22]. **Prioridad**: MUST.

##### FR-003: Consulta de saldo y movimientos multicanal

p95 < 1.5s; saldo coherente entre canales en tiempo real; **sin acceso directo a la BD** del Core desde canales (solo vía API) [PRIN P11, P12]. **Prioridad**: MUST.

##### FR-004: Transferencias internas y entre cuentas

Liquidación inmediata; asiento contable automático; ACID transaccional. **Prioridad**: MUST.

##### FR-005: Productos de inclusión financiera (cuentas bajo costo)

Parametrizables por usuarios de negocio sin código del vendor (PRIN P20). **Prioridad**: MUST.

##### FR-006 (REV v2.0): Catálogo completo de cuentas de ahorro

Variantes activas: Regular, Dorada, Platinum, Ahorro Navidad, Panamá Para Ti, Juvenil, Ahorro Fácil para Niños, Una Cuenta Para Todos, Caja Amiga (régimen simplificado) [DOC-RFI-001 §3.1.1, DOC-SES-002]. Apertura: sucursal, web, móvil. Intereses devengados diariamente sobre saldo promedio. Tasas parametrizables por tipo y saldo mínimo. **Prioridad**: MUST.

##### FR-007 (NEW v2.0): Sub-cuentas / "Cajones" de ahorro con objetivos

Sub-cuentas con objetivos de ahorro que reservan fondos sin afectar disponibilidad general; múltiples por CIF con saldos independientes; visualización de progreso [DOC-RFI-001 §3.1.1, DOC-POC-001 §2.3]. **Prioridad**: SHOULD.

##### FR-008 (NEW v2.0): Sobregiros nativos en cuenta corriente y de ahorro

Funcionalidad nativa: parametrización de límites por perfil, vínculo a línea de crédito preaprobada, bloqueo automático sin línea activa, cálculo de intereses sobre el sobregiro [DOC-RFI-001 §3.1.1, §3.1.2, DOC-SES-002]. **Prioridad**: MUST.

##### FR-009 (NEW v2.0): Cuentas corrientes con chequeras y DDI

Apertura para personas jurídicas con análisis de capas societarias y beneficiario final ≥ **10%** (Acuerdo 1-2026, Art. 14 — umbral panameño más estricto que el 25% UE/FATF). Gestión de **chequeras**: solicitud, emisión, entrega, bloqueo, rangos de números. Gestión de **DDI** (Débito Directo Interbancario): registro de mandatos y ejecución en ciclo [DOC-RFI-001 §3.1.2]. **Prioridad**: MUST.

##### FR-010 (REV v2.0): Depósitos a plazo fijo con renovación automática y back-to-back

Plazos 30 días–5 años. Tabla pizarra parametrizable por **plazo Y monto** (no solo por plazo). **No** existe cancelación anticipada (restricción regulatoria panameña) [DOC-RFI-001 §3.1.3, DOC-SES-002]. Renovación automática con notificación 30 días antes. **Anticipo periódico de intereses** sin cancelar el principal (deseable). **Enmiendas** (incremento de principal sin cancelar). **Back-to-back**: depósito como colateral con bloqueo y liberación automática. **Prioridad**: MUST.

##### FR-011 (NEW v2.0): Cheques de Gerencia

Solicitud, emisión, registro de serie, estado (emitido/en tránsito/compensado/rechazado), causales de rechazo (Ley 52/2000) [DOC-RFI-001 §3.1.4]. **Prioridad**: MUST.

##### FR-012 (NEW v2.0): Multimoneda y operaciones de cambio (Panamá dolarizado + USD/EUR)

Tabla parametrizable de divisas; spread comprador/vendedor; **revalorización automática** según IAS 21; cálculo de posición neta (larga/corta) con alerta ante límites regulatorios; integración con transferencias internacionales [DOC-RFI-001 §3.6, DOC-SES-003]. **Prioridad**: SHOULD.

#### Bloque B — Créditos y cartera (REV v2.0 — refinado contra RFI §3.2)

Atributos comunes: parametrización autónoma de tasas fijas/variables (tasa piso/techo), comisiones, pólizas, multas, moratorios, **FECI**, **IVA**. Cálculo automático del plan de pagos en sistemas **francés, alemán y escalonado**. Tipos de pago: **DDI, voluntario, cargo a cuenta y pago mixto**. Pagos escalonados para créditos comerciales. Automatización completa de asientos contables. Integración con módulo de garantías (N:N) [DOC-RFI-001 §3.2].

##### FR-013 (REV v2.0): Originación, gestión y cobro de créditos comerciales y personales

El CBS recibe el crédito aprobado por **BPMs externos** (Ultimus, Asicom-Finflow, Genexus) y administra el ciclo de vida posterior [DOC-RFI-001 §3.2, DOC-SES-004]. Workflow configurable de aprobación interna para créditos corporativos por comités. Mora detectada en tiempo real con contagio inter-crédito [DOC-CB-003-C20]. **Prioridad**: MUST.

##### FR-014 (REV v2.0): Hipotecas con Interés Preferencial (Ley 468/2025) y subsidio DGI

Hipotecas hasta 30 años, cartera ~B/. 3,000M [DOC-RFI-001 §3.2.1]. **CAP cobra la tasa plena; la DGI subsidia una porción** — el CBS gestiona el **reclamo trimestral del subsidio a la DGI** y su cancelación ante traslado o pago total. Codeudores solidarios con impacto en reporte APC. Reportería MIVIOT generable nativamente. Reestructuraciones COVID-19 preservan trazabilidad. **Prioridad**: MUST.

##### FR-015 (NEW v2.0): Hipotecario para panameños residentes en el exterior

Nuevo segmento en desarrollo. El CBS soporta cliente panameño residente fuera del país con fuente de ingresos del exterior, codeudores familiares, remesas como evidencia de capacidad de pago, cuenta de ahorro con cajón "Enganche" [DOC-RFI-001 §3.2.1, DOC-POC-001]. **Prioridad**: SHOULD.

##### FR-016: Créditos con garantía estatal (FGA)

Tratamiento contable diferenciado por tipo de garantía; provisión ajustada con haircuts SBP [DOC-CB-001-C14, DOC-CB-003-C21]. **Prioridad**: MUST.

##### FR-017: Profimype (microcréditos AMPYME)

Gestión nativa dentro del Core (eliminando hojas de cálculo) [DOC-CB-001-C18]. **Prioridad**: MUST.

##### FR-018 (REV v2.0): Reestructuración nativa de créditos

El CBS modifica el crédito **sin cancelarlo**: extensión de plazo, reducción de tasa, capitalización de intereses vencidos, período de gracia adicional. Período de gracia normativo: 6 meses para normalizar [DOC-RFI-001 §3.3, DOC-SES-004]. Workflow controlado con doble aprobación. Trazabilidad histórica preservada. **Diferencia con v1.0**: anteriormente CAP cerraba el préstamo y abría uno nuevo (mala práctica). **Prioridad**: MUST.

##### FR-019 (REV v2.0): Cálculo automático del subsidio Interés Preferencial + reclamo DGI

Diferencia vs cálculo legado = 0. Reportería MEF / MIVIOT / DGI automatizada y conciliable. **Prioridad**: MUST.

##### FR-020: Etiquetado de productos especiales (créditos verdes, Profimype, agropecuarios)

Parametrizables sin código; reportes filtrables [DOC-CB-001-C28]. **Prioridad**: SHOULD.

##### FR-021 (NEW v2.0): Préstamos de autos con garantía prendaria

Pago directo a la agencia (instrucción de pago a terceros); registro de chasis, placa, modelo, año, valor; cancelación automática de garantía al liquidar [DOC-RFI-001 §3.2.5]. **Prioridad**: MUST.

##### FR-022 (NEW v2.0): Préstamos prendarios con custodia

Bienes muebles (joyas, maquinaria) o garantías líquidas (depósitos) bajo custodia. Registro con avalúo, LTV, haircut; custodia y liberación [DOC-RFI-001 §3.2.6]. **Prioridad**: MUST.

##### FR-023 (NEW v2.0): Líneas de crédito revolvente y no revolvente

Cupo en tiempo real, bloqueo de disposiciones que excedan límite, renovaciones con alertas anticipadas, variantes (comercial / pre-factoring / sobregiro) [DOC-RFI-001 §3.2.7]. **Prioridad**: MUST.

##### FR-024 (NEW v2.0): Préstamos de construcción con desembolso por tramos

Desembolso por hitos de avance verificada; durante la construcción solo se pagan intereses; el principal se amortiza al concluir. **Conversión automática a hipoteca estándar** al finalizar con constitución de garantía hipotecaria definitiva [DOC-RFI-001 §3.2.4]. **Prioridad**: MUST.

##### FR-025 (NEW v2.0): Leasing financiero NIIF 16

Arrendamiento de bienes de capital con opción de compra. Reconocimiento del activo financiero según NIIF 16. Devengo y distribución capital/interés implícito. IVA sobre cuotas. Cartera actual ~B/. 40M [DOC-RFI-001 §3.2.8]. **Prioridad**: SHOULD.

##### FR-026 (NEW v2.0): Créditos sindicados — CAP como coordinador y como participante

CAP actúa como **coordinador** (distribuye pagos entre participantes) o como **banco participante** (registra su tramo). El CBS soporta ambos roles con estructura multi-participante [DOC-RFI-001 §3.2.3, DOC-SES-004]. **Prioridad**: MUST.

##### FR-027 (NEW v2.0): Créditos comerciales y macro-obras

Pagos escalonados adaptados al flujo de caja del proyecto, gracia al inicio, cronogramas flexibles no limitados a cuotas fijas. CAP financia macro-obras del Estado (~B/. 3,000M proyección [DOC-SES-003, DOC-SES-009 §3.2]). Audit trail completo de aprobaciones por comités. Actualmente 100% manual vía Power Apps; el CBS debe gestionarlo nativamente [DOC-RFI-001 §3.2.3]. **Prioridad**: MUST.

##### FR-028 (NEW v2.0): Créditos mancomunados

Dos o más personas comparten responsabilidad del pago. Soporte nativo (actualmente NO disponible en el legado) [DOC-SES-004, DOC-SES-009 §5.1]. **Prioridad**: SHOULD.

##### FR-029 (NEW v2.0): FECI — Retención automática del 1% sobre intereses comerciales

El CBS calcula automáticamente la retención del 1% sobre intereses comerciales y prepara la remisión mensual al MEF, o se integra con módulo FECI desacoplado [DOC-RFI-001 §3.2.3]. **Prioridad**: MUST.

##### FR-030 (REV v2.0): Cobranza temprana 0–90 días nativa en el CBS

Pre-mora (1–15 días antes): identificación automática y alertas proactivas al cliente y gestor. Mora temprana (1–90 días): seguimiento desde el CBS, planes de regularización, registro de gestiones, cálculo de moratorios. Mora tardía (90+ días): notificación en tiempo real a sistema externo de cobranza (Emerix evoluciona — eliminando desfase batch de 1 día) [DOC-RFI-001 §3.3, DOC-SES-004, DOC-SES-009 §5.4]. **Prioridad**: MUST.

##### FR-031: Contagio inter-crédito e integración con APC

Degradación automática de créditos sanos del mismo deudor cuando otro entra en D/E; integración APC [DOC-CB-003-C20]. **Prioridad**: MUST.

##### FR-032 (REV v2.0): Gestión de garantías N:N con módulo central

Una garantía puede respaldar múltiples préstamos y viceversa. Tipos: hipotecarias, prendarias, depósitos back-to-back, garantías bancarias emitidas (stand-by LC, performance bonds), codeudores/avales. Vinculación y liberación automática. Avalúos con vencimiento alertado. Haircuts SBP [DOC-RFI-001 §3.4, DOC-CB-003-C21]. **Prioridad**: MUST.

##### FR-033: Bienes adjudicados (Acuerdo 5-2011)

Registro y valoración con deterioro y plazos de realización. **Prioridad**: MUST.

#### Bloque C — Pagos, ecosistema panameño y comercio exterior

##### FR-034 (REV v2.0): Yappy P2P y comercios — integración nativa vía bus IBM MQ + API Gateway

Liquidación inmediata p95 < 3s end-to-end; idempotencia; sin doble débito/abono ante reintentos [DOC-CB-001-C7, DOC-RFI-001 §4.2]. **Prioridad**: MUST.

##### FR-035: ACH Panamá (Directo + Express)

Conciliación con cámara automatizada. **Prioridad**: MUST.

##### FR-036 (REV v2.0): Switch ATM/POS — integración API con Telered en tiempo real

Procesamiento ATM y POS terciarizado con **Telered**; el CBS recibe resultado en tiempo real vía API y actualiza saldo de inmediato; conciliación diaria automatizada con identificación de diferencias y gestión de disputas [DOC-RFI-001 §3.8]. **Prioridad**: MUST.

##### FR-037 (NEW v2.0): Corresponsales no bancarios (Caja Amiga, +100 puntos)

Pagos de servicios, cuotas de préstamos y tarjetas. Registro en tiempo real con liquidación automática e identificación del punto de origen. Modo degradado/offline con conciliación diferida (BR-012, FR-058) [DOC-RFI-001 §3.8, DOC-SES-009 §3.2]. **Prioridad**: MUST.

##### FR-038 (REV v2.0): SWIFT para corresponsalía internacional — integración SCONNECT LAU/CSV

Mensajes MT103, MT202 e ISO 20022 MX. Cuentas nostro/vostro con conciliación contra MT940/MT950. **Pagos cross-border no SWIFT** hacia economías relevantes (China, Japón, Brasil, UE) — capacidad para rails alternativos [DOC-RFI-001 §3.5.3, §4.2]. **Prioridad**: MUST.

##### FR-039 (NEW v2.0): Cartas de Crédito (Comercio Exterior)

Modalidades: importación (CAP emisor), exportación (CAP notificador/confirmador), stand-by (garantía). Marco: **UCP 600, ISP 98, URDG 758**. Ciclo: solicitud → validación línea → registro → SWIFT → recepción documentos → revisión conformidad → pago/negociación → asiento → cierre. Screening AML pre-ejecución [DOC-RFI-001 §3.5.1]. **Prioridad**: MUST.

##### FR-040 (NEW v2.0): Factoring con pagadores estatales y pre-factoring

Factoring con recurso propio, factoring con pagadores estatales (cartera estable de CAP), pre-factoring sobre líneas. Retención del 10% como garantía, gastos cobrados por adelantado, plazos de pago estimados, integración con módulo de garantías [DOC-RFI-001 §3.5.2, DOC-SES-004]. **Prioridad**: MUST.

##### FR-041 (NEW v2.0): Transferencias internacionales con políticas de retención y revisión

Enviadas: retención de fondos por 3 días hábiles para solicitudes en línea; verificación de perfil. Recibidas: acreditación automática hasta B/. 5,000; montos superiores requieren autorización adicional; antigüedad mínima de cuenta. Screening AML pre-ejecución [DOC-RFI-001 §3.5.3]. **Prioridad**: MUST.

##### FR-042: Pagos masivos de planilla del sector público

5–10× del promedio diario; ≥ 5,000 TPS; sin afectación a canales en línea [DOC-CB-001-C4]. **Prioridad**: MUST.

##### FR-043: Pagos de transferencias sociales del Estado

Beca Universal, 120 a los 65, Red de Oportunidades [DOC-CB-001-C5]. **Prioridad**: MUST.

##### FR-044 (REV v2.0): SIACAP — débitos de aportes a pensiones de servidores públicos

Débitos automáticos en la fecha SIACAP, reportería de aportes nativa, consulta de saldos. **Prioridad**: MUST.

##### FR-045 (NEW v2.0): DDI masivo para 833 empresas privadas + 178 entidades del Estado

Procesamiento de archivos de planilla (Excel/TXT) con aplicación masiva y gestión de rechazos. Mandatos de descuento directo con trazabilidad [DOC-RFI-001 §3.2.2]. **Prioridad**: MUST.

#### Bloque D — AML / KYC / Compliance operacional (REV v2.0 — AML reorientado a herramienta externa)

##### FR-046 (REV v2.0): KYC estándar y reforzado integrado con Panadata

Validación de documentos, listas (PEP, OFAC, ONU, SBP, internas), rating de cliente, re-KYC periódico. **Integración con Panadata** (proveedor KYC actual) para datos públicos centralizados [DOC-RFI-001 §3.10, DOC-SES-006]. **Prioridad**: MUST.

##### FR-047: KYC simplificado para "Una Cuenta Para Todos" y Caja Amiga

Reglas parametrizables por Cumplimiento sin código. **Prioridad**: MUST.

##### FR-048 (REV v2.0 — MAJOR CHANGE): Exposición de eventos AML a herramienta externa

> **Cambio v2.0**: el CBS **NO** incluirá módulo AML interno. El monitoreo AML/PLD se realizará con una herramienta externa con IA e integración por API en tiempo real [DOC-SES-006, DOC-SES-009 §10.4]. El CBS debe **exponer eventos transaccionales** a la herramienta externa con latencia < 200 ms y soportar **bloqueo de transacciones** bajo instrucción del motor AML.

Criterios:

- Stream de eventos transaccionales en tiempo real al motor AML externo (Kafka, eventos REST o equivalente).
- Capacidad de bloquear transacciones bajo instrucción del motor AML antes de la liquidación.
- Trazabilidad y evidencia auditable preservada en el CBS para Auditoría Interna.
- El proveedor AML actual deja de dar soporte en 2026; el go-live del nuevo AML debe alinearse con el del CBS.

**Prioridad**: MUST.

##### FR-049: Generación y envío de ROS a la UAF (orquestado por el motor AML externo)

El motor AML externo genera el ROS; el CBS provee los datos y persiste evidencia auditable (workflow, escalamiento, firma) [DOC-CB-003-C5]. **Prioridad**: MUST.

##### FR-050: FATCA y CRS nativos

Identificación de US persons (FATCA) y reportables CRS; reportería en formatos requeridos. **Prioridad**: MUST.

##### FR-051: Detección y manejo de PEP

Bases PEP actualizadas con periodicidad ≥ diaria; escalamiento a Cumplimiento sin bloqueo automático. **Prioridad**: MUST.

##### FR-052 (NEW v2.0): Beneficiario final ≥ 10% para personas jurídicas (Acuerdo 1-2026, Art. 14)

Análisis de capas societarias, identificación de beneficiarios finales con participación **≥ 10%** o control efectivo (umbral panameño más estricto que el 25% adoptado por UE/FATF), integración con Panadata para validación automática y alertas en tiempo real ante cambios en sociedades [DOC-RFI-001 §3.10, §3.1.2, DOC-SES-006; PDF oficial SBP Art. 14]. **Plazo**: vigencia 30-jun-2027 (Art. 14). **Prioridad**: MUST.

##### FR-053 (NEW v2.0): Geolocalización inferencial de clientes digitales (Acuerdo 1-2026, Art. 14 — vigencia 30-jun-2027)

**Geolocalización inferencial** (no se trata sólo de capturar GPS — combina múltiples señales: IP+ASN, dispositivo/UA, GPS si está disponible, comportamiento de sesión) para **inferir** la ubicación real del cliente digital y detectar anomalías o jurisdicciones sancionadas. Captura y persistencia en todos los canales digitales conforme Acuerdo 1-2026 Art. 14, **vigencia 30-jun-2027** [DOC-RFI-001 §2.1, §3.1.1, DOC-SES-006; PDF oficial SBP Art. 14]. **Prioridad**: MUST.

##### FR-054 (NEW v2.0): Declaración Jurada de Transacción en Efectivo (DJTE) ≥ B/. 10,000

El CBS **bloquea** la transacción en efectivo ≥ B/. 10,000 hasta completar la DJTE conforme **Ley 23/2015**. Aplica en ventanilla, cajeros, depósitos y todas las operaciones en efectivo [DOC-RFI-001 §3.7, DOC-SES-002]. **Prioridad**: MUST.

#### Bloque E — Reportería regulatoria SBP, MEF, MIVIOT, APC, DGI

##### FR-055 (REV v2.0): Integración nativa con el SEI (XML/XSD, workflow, firma digital)

XML válido contra XSD vigente; workflow auditable Preparador/Revisor/Firmante con doble validación pre-envío; firma digital con poderes; almacenamiento del número de radicación [DOC-CB-003-C23..C27]. **Prioridad**: MUST.

##### FR-056: Generación automatizada del inventario D04 — 54+ reportes mensuales

CAP genera ≥ 54 reportes regulatorios al SEI [DOC-CB-001-C12, DOC-SES-005]. 100% del inventario generable; documentación cruzada por Acuerdo SBP, frecuencia, formato, fuente. **Prioridad**: MUST.

##### FR-057: Posición de liquidez diaria (Acuerdo 4-2013) e indicadores prudenciales (CAR, LCR)

Generados y enviados antes del plazo SEI; CAR replicable contra cálculo legado (referencia 14.41% [DOC-CB-001-C3]); LCR conforme Acuerdo 4-2013. **Prioridad**: MUST.

##### FR-058: Plan de cuentas SBP estandarizado mapeado a operaciones

Grupos 1xx Activos / 2xx Pasivos / 3xx Patrimonio / 4xx Ingresos / 5xx Gastos / 6xx Contingentes; códigos SBP no modificables; cada operación mapeada [DOC-CB-003-C7, DOC-CB-003-C8]. **Prioridad**: MUST.

##### FR-059: Reportería MIVIOT (cartera hipotecaria social)

Generación nativa sobre la cartera hipotecaria social. **Prioridad**: MUST.

##### FR-060: Reportería MEF (subsidios estatales) y reclamo a DGI por Interés Preferencial

Subsidios asumidos por el Estado conciliables con registros contables; reclamo trimestral DGI por Interés Preferencial (Ley 468/2025) automatizado. **Prioridad**: MUST.

##### FR-061: Pre-validación local que reproduce las tres capas del SEI

Estructura / aritmética / consistencia histórica; variaciones > 15% generan alerta con explicación narrativa pre-envío [DOC-CB-003-C26]. **Prioridad**: MUST.

##### FR-062 (NEW v2.0): Reportería APC (Central de Riesgos)

Reporte mensual en lote de cartera al APC; consulta de deudores online durante originación; identificación de codeudores solidarios con impacto en historial APC [DOC-RFI-001 §3.2.2, §4.5]. **Prioridad**: MUST.

##### FR-063 (NEW v2.0): Notificaciones internas estructuradas para reportería regulatoria

Capacidad del CBS de generar notificaciones internas estructuradas (event-driven) consumibles por reportería regulatoria, incluyendo APC, SEI y herramientas analíticas [DOC-POC-001 §1.1 M13]. **Prioridad**: MUST.

#### Bloque F — Contabilidad y provisiones (REV v2.0 — coordinado con ERP externo)

##### FR-064 (REV v2.0): Modelo NIIF 9 ECL con stages 1/2/3 y PD/LGD/EAD

SPPI / modelo de negocio, stages 1/2/3 por segmento, PD/LGD/EAD calibrados con series ≥ 5–7 años, umbral SICR parametrizable [DOC-CB-003-C13..C16]. **Prioridad**: MUST.

##### FR-065: Acuerdo 6-2000 (clasificación A–E y provisiones 1/5/25/50/100%)

Clasificación con override por capacidad de pago con justificación auditada [DOC-CB-003-C18..C19]. **Prioridad**: MUST.

##### FR-066: Modelo dual — registro del mayor y reserva regulatoria en patrimonio

Cálculo simultáneo automatizado; trazabilidad completa de decisión por crédito [DOC-CB-003-C17]. **Prioridad**: MUST.

##### FR-067: Garantías y haircuts SBP; avalúos vigentes

Haircut configurable por tipo; alertas por avalúos vencidos [DOC-CB-003-C21]. **Prioridad**: MUST.

##### FR-068 (NEW v2.0): Reservas dinámicas con seguimiento temporal del cliente

Herramienta de seguimiento temporal del cliente (retrospectivo y proyectado) para cálculo de reservas dinámicas, eliminando el insumo manual actual [DOC-SES-006 §7.2]. **Prioridad**: SHOULD.

##### FR-069 (NEW v2.0): Asientos contables automáticos por evento del ciclo de vida + exposición al ERP

El CBS genera automáticamente asientos para devengo de intereses, cobros con distribución (principal/interés/seguros/cargos/FECI/IVA), provisiones, diferencias de cambio (IAS 21) y comisiones — y los **expone vía API o archivos estándar al ERP externo** en tiempo real o micro-batch (≤ 5 min) [DOC-RFI-001 §3.9, BR-013, INT-021]. **Prioridad**: MUST.

##### FR-070: Cuadre contable diario automatizado

Diferencias = 0 al cierre; asientos manuales con doble aprobación y rastro inmutable. **Prioridad**: MUST.

#### Bloque G — Canales y experiencia

##### FR-071: APIs para Super App y banca móvil

OpenAPI/AsyncAPI versionadas con compatibilidad hacia atrás; cero acceso directo a BD del Core [PRIN P11]. **Prioridad**: MUST.

##### FR-072: Red Caja Amiga con modo degradado / offline

Conciliación diferida con reglas anti-fraude probadas. **Prioridad**: MUST.

##### FR-073: Datos consultables vía API por A.N.D.R.E.A.

mTLS / tokens firmados; sin acceso a datos fuera del scope del cliente autenticado. **Prioridad**: MUST.

##### FR-074 (REV v2.0): Operación de 60 sucursales (ventanilla + plataforma) con módulo Teller

UI optimizada en español. **Módulo Teller nativo** o solución de caja integrada: cuadre por cajero con fondo fijo, gestión de bóveda (sustituyendo Excel actual), cuadre y cierre de sucursal, transportadora de valores [DOC-RFI-001 §3.7, DOC-SES-002]. **Prioridad**: MUST.

##### FR-075 (NEW v2.0): CIF único + vista 360° del cliente (incluye productos SISCARD)

CIF único como eje central. Vista unificada de datos personales/corporativos, productos activos (incluyendo tarjetas SISCARD), historial y relaciones. Segmentos: Masivo, Premium (Dorada/Platinum), Jubilados, Menores, Empresas, Cooperativas, Entidades del Estado, Régimen Simplificado [DOC-RFI-001 §3.10, DOC-SES-009 §3.4]. **Prioridad**: MUST.

##### FR-076 (NEW v2.0): Notificaciones automáticas a clientes por eventos críticos

Vencimientos de créditos y de pólizas, cambios en tasas o condiciones contractuales (obligación regulatoria) [DOC-SES-004]. **Prioridad**: SHOULD.

---

## Requisitos No Funcionales (NFR)

### Desempeño (NFR-P)

- **NFR-P-001**: Saldo p95 < 1.5s; transferencia Yappy p95 < 3s; movimientos p95 < 2s. **MUST**.
- **NFR-P-002**: Throughput de planilla pública ≥ 5,000 TPS. **MUST**.
- **NFR-P-003**: Apertura digital concurrente ≥ 100 sin degradación. **MUST**.
- **NFR-P-004**: Reportes SBP generados con holgura ≥ 1 día hábil antes del plazo SEI. **MUST**.
- **NFR-P-005 (REV v2.0)**: Latencia de exposición de eventos AML al motor externo < 200 ms (no debe demorar la transacción). **MUST**.
- **NFR-P-006 (NEW v2.0)**: Reducción de la ventana de cierre diario actual (5 min [DOC-SES-009 §9.2]) a **≤ 1 min** o procesamiento sin downtime; mantenimiento programado actual (1.5 h) reducido a ≤ 30 min/mes con rolling deployment. **MUST**.

### Seguridad (NFR-SEC)

- **NFR-SEC-001**: MFA obligatorio para acceso humano (PRIN P4). **MUST**.
- **NFR-SEC-002**: Autenticación servicio-a-servicio (mTLS, tokens firmados). **MUST**.
- **NFR-SEC-003**: Gestión de secretos en bóveda; nunca en código/config/repos. **MUST**.
- **NFR-SEC-004**: Cifrado en tránsito (TLS 1.2+) y en reposo (todos los almacenes — transaccional, analítico, respaldos, archivo). **MUST**. (Brecha actual: NO hay cifrado en reposo ni en tránsito interno [DOC-SES-007 §8.1].)
- **NFR-SEC-005**: Logs estructurados de autenticación/autorización con retención ≥ 7 años. **MUST**.
- **NFR-SEC-006**: Pen-tests independientes anuales con remediación obligatoria de hallazgos críticos/altos. **MUST**.
- **NFR-SEC-007**: SAST/SCA en pipeline CI/CD con bloqueo ante vulnerabilidades críticas/altas no remediadas. **MUST**.
- **NFR-SEC-008**: Segmentación de red; Core no accesible directamente desde Internet. **MUST**.
- **NFR-SEC-009**: Listas restrictivas (PEP, OFAC, ONU, internas, UAF) actualizadas al menos diariamente. **MUST**.
- **NFR-SEC-010**: Firma digital reconocida en Panamá para envío al SEI. **MUST**.
- **NFR-SEC-011 (NEW v2.0)**: **RBAC nativo** integrable con plataforma IAM del banco mediante **SAML 2.0, OAuth 2.0 / OIDC o LDAP/AD**. **SSO con Microsoft Entra ID (Azure AD)** [DOC-RFI-001 §4.7, DOC-SES-007]. **MUST**.
- **NFR-SEC-012 (NEW v2.0)**: **MFA por perfil y canal** (TOTP, biometría, certificados digitales). **MUST**.
- **NFR-SEC-013 (NEW v2.0)**: **Segregación de funciones (SoD)** — el CBS impide que un mismo usuario instruya y autorice la misma operación; reglas SoD configurables por el banco [DOC-RFI-001 §4.7]. **MUST**.
- **NFR-SEC-014 (NEW v2.0)**: Permisos a nivel de **módulo, pantalla, campo y operación** por rol; **enmascaramiento de campos sensibles** (saldo, cédula, tasa, número de cuenta) según rol [DOC-RFI-001 §4.7, DOC-SES-006]. **MUST**.
- **NFR-SEC-015 (NEW v2.0)**: **Recertificación periódica de accesos** — el CBS genera automáticamente listados de usuarios activos por rol/sucursal para revisión y aprobación por responsables de área (actualmente proceso manual 2 veces/año [DOC-SES-007]). **MUST**.
- **NFR-SEC-016 (NEW v2.0)**: Restricción de acceso por **sucursal, línea de negocio o cartera de clientes**; un usuario solo opera en ámbitos asignados. **MUST**.
- **NFR-SEC-017 (NEW v2.0)**: **Límites operativos individuales por usuario** (monto máximo por transacción, cupo diario, número de operaciones por tipo), independientes del límite general del producto. **MUST**.
- **NFR-SEC-018 (NEW v2.0)**: Control de sesión — tiempo máximo de inactividad configurable por perfil, bloqueo tras N intentos fallidos, flujo de desbloqueo con trazabilidad. **MUST**.

### Escalabilidad (NFR-S)

- **NFR-S-001**: Escalado horizontal sin reconfiguración manual (PRIN P1). **MUST**.
- **NFR-S-002**: Picos 10× del promedio diario absorbidos sin degradación [DOC-CB-001-C4]. **MUST**.
- **NFR-S-003**: Capacidad proyectada a 5 años con crecimiento 8–10% anual. **MUST**.

### Disponibilidad y Confiabilidad (NFR-A)

- **NFR-A-001**: SLA ≥ 99.99% mensual servicios críticos en línea (saldo, transferencias inmediatas, ATMs). **MUST**.
- **NFR-A-002**: SLA ≥ 99.95% canales digitales (Super App, banca en línea, Yappy, ACH). **MUST**.
- **NFR-A-003**: SLA ≥ 99.9% procesos batch. **MUST**.
- **NFR-A-004**: RTO/RPO — saldos/transferencias/ATMs/Yappy: RTO ≤ 15 min, RPO ≤ 1 min; canales digitales: RTO ≤ 30 min, RPO ≤ 5 min; batch: RTO ≤ 4 h, RPO ≤ 1 h. **MUST**.
- **NFR-A-005**: Topología activo-activo o activo-pasivo con conmutación automática (actualmente activo-pasivo, en transición a activo-activo entre dos sitios separados por 35–40 km [DOC-SES-008]). **MUST**.
- **NFR-A-006**: Ventanas de mantenimiento aprobadas por Negocio; bloqueos en cierre de mes, planilla pública, fin de año, festivos. **MUST**.
- **NFR-A-007**: Mantenimiento sin downtime — rolling, blue-green o canary obligatorio. **MUST**.

### Cumplimiento (NFR-C) — REV v2.0

- **NFR-C-001 (REV v2.0)**: Cumplimiento Ley 20/1975 + Acuerdos SBP (4-2013, 6-2000, 5-2011, 3-2009, 8-2010, **1-2026**), Resolución SBP-DJ-0014, **Ley 23/2015** (DJTE), **Ley 468/2025** (Interés Preferencial), **Ley 52/2000** (cheques) [DOC-RFI-001 §2.1]. **MUST**.
- **NFR-C-002 (REV v2.0)**: Exposición de eventos AML/FT a la herramienta externa, con envío de ROS a la UAF orquestado por el motor AML [DOC-CB-003-C5, DOC-SES-006]. **MUST**.
- **NFR-C-003**: FATCA y CRS soportados nativamente. **MUST**.
- **NFR-C-004**: Vendor con **ISO 27001** vigente; ISO 27002 implementados. CAP también busca certificar servicios bajo ISO 27001 [DOC-SES-007]. **MUST**.
- **NFR-C-005 (REV v2.0)**: Estados financieros NIIF + adaptaciones SBP. **Doble contabilidad NIIF (internacional) y plan de cuentas SBP (regulatoria)** soportada simultáneamente sin doble ingreso [DOC-RFI-001 §3.9, DOC-CB-003-C9]. **MUST**.
- **NFR-C-006**: Plan de cuentas SBP no modificable unilateralmente [DOC-CB-003-C7]. **MUST**.
- **NFR-C-007**: Retención de logs de auditoría ≥ 7 años (Código de Comercio + AML). **MUST**.
- **NFR-C-008**: Auditabilidad por Contraloría (contratos, pases, trazabilidad transaccional). **MUST**.
- **NFR-C-009**: Cumplimiento de Ley 22 de Contrataciones Públicas (proceso, contrato, modificaciones). **MUST**.
- **NFR-C-010**: Cláusula contractual de **cumplimiento regulatorio continuo** — vendor adapta el producto a nuevos Acuerdos SBP sin cobros extraordinarios (PRIN P7). **MUST**.
- **NFR-C-011 (NEW v2.0)**: **NIIF 16** (leasing) y **IAS 21** (diferencias de cambio) nativos [DOC-RFI-001 §3.2.8, §3.6]. **MUST**.
- **NFR-C-012 (NEW v2.0)**: **UCP 600, ISP 98, URDG 758** para cartas de crédito [DOC-RFI-001 §3.5.1]. **MUST**.

### Mantenibilidad y Evolutividad (NFR-M)

- **NFR-M-001**: Arquitectura modular por dominio. **MUST**.
- **NFR-M-002**: Parametrización sin código del vendor (productos, reglas, tasas, fees, límites) — usuarios de negocio (PRIN P20). **MUST**.
- **NFR-M-003**: Documentación viva en español. **MUST**.
- **NFR-M-004**: ADRs para decisiones significativas. **MUST**.
- **NFR-M-005**: Infraestructura como Código (IaC) versionada; sin cambios manuales en producción salvo break-glass auditado (PRIN P17). **MUST**.
- **NFR-M-006**: Cobertura de pruebas automatizadas con umbrales mínimos definidos. E2E sobre apertura, transferencia, desembolso hipotecario, planilla, cierre. **MUST**.
- **NFR-M-007**: Pipeline CI/CD auditable con SAST, SCA, code review, doble aprobación crítica, rollback probado, trazabilidad. **MUST**.
- **NFR-M-008 (NEW v2.0)**: **Validación en tiempo de ingreso** de reglas de negocio para prevenir registros mal formados en el origen (campos obligatorios, dominios, dependencias) [DOC-SES-006, DOC-RFI-001 §2.3, §3.10]. Aplica transversalmente a clientes, cuentas, créditos, garantías. **MUST**.
- **NFR-M-009 (NEW v2.0)**: Configuración de productos y cambios paramétricos en **minutos** sin dependencia del proveedor ni de TI [DOC-RFI-001 §2.3, DOC-SES-009 §10.2]. **MUST**.

### Usabilidad, Soporte y Localización (NFR-U)

- **NFR-U-001**: UI en español. **MUST**.
- **NFR-U-002**: Capacitación formal del vendor en español. **MUST**.
- **NFR-U-003**: Soporte L1/L2/L3 24/7 en español. **MUST**.
- **NFR-U-004**: Accesibilidad mínima WCAG 2.1 AA. **SHOULD**.
- **NFR-U-005 (NEW v2.0)**: **Localización Panamá** — UTC-5, moneda base USD, formato fecha DD/MM/AAAA, días inhábiles nacionales gestionados [DOC-RFI-001 §4.4, §4.7]. **MUST**.
- **NFR-U-006 (NEW v2.0)**: Idioma de interfaz por usuario (español primario; inglés opcional). **SHOULD**.

---

## Requisitos de Integración (INT) — REV v2.0

| ID | Sistema | Protocolo / Formato | Autenticación | Prioridad | Notas |
|----|---------|---------------------|---------------|-----------|-------|
| INT-001 | Yappy (P2P y comercios) | API REST + eventos vía API Gateway / bus IBM MQ | OAuth2 / mTLS | MUST | 55+ instituciones, 1.6M usuarios [DOC-CB-001-C7] |
| INT-002 | ACH Panamá (Directo / Express) | Cámara BNP | Conforme cámara | MUST | Liquidación y conciliación automatizada |
| INT-003 | Telered (switch ATM/POS + Tarjeta Clave) | API REST + ISO 8583 | mTLS / clave | MUST | 140 ATMs, POS, terciarizado [DOC-RFI-001 §3.8] |
| INT-004 | SWIFT (corresponsalía internacional) | SCONNECT LAU/CSV (mensajería SWIFT / ISO 20022 MX) | SWIFT certs | MUST | MT103, MT202, MT940/MT950; FR-038, FR-039, FR-041 |
| INT-005 | SBP — SEI | XML/XSD via portal seguro | Usuario jerárquico + firma digital | MUST | Preparador/Revisor/Firmante; XBRL roadmap |
| INT-006 (REV v2.0) | UAF (AML/FT, ROS) | Orquestado por motor AML externo | Conforme UAF | MUST | ROS generado por la herramienta AML externa con datos del CBS |
| INT-007 | MIVIOT (cartera hipotecaria social) | Reportes según procedimiento | TBD | MUST | Cartera Interés Preferencial |
| INT-008 | MEF (subsidios estatales) | Reportes según procedimiento | TBD | MUST | Subsidios |
| INT-009 | SIACAP (pensiones servidores públicos) | API / archivo SIACAP | TBD | MUST | Débitos de aportes; reportería |
| INT-010 | APC (Central de Riesgos) | API / archivo APC | TBD | MUST | Cartera mensual, consulta deudores, contagio |
| INT-011 | A.N.D.R.E.A. (asistente IA WhatsApp) | API REST | mTLS / tokens | MUST | Consulta datos del cliente |
| INT-012 | Super App / banca móvil interna | API REST / GraphQL | mTLS / OAuth2 | MUST | Versionado con compatibilidad |
| INT-013 (REV v2.0) | Bus IBM MQ + API Gateway | Mantener como capa de abstracción | mTLS / tokens | MUST | Algunos sistemas aún conectados punto a punto [DOC-SES-001] |
| INT-014 (REV v2.0) | SITECA (originación hipotecaria) | API / batch / file | TBD | MUST | El CBS recibe el crédito aprobado [DOC-SES-001, DOC-SES-009 §3.2] |
| INT-015 (REV v2.0) | BPMs externos: Ultimus, Asicom-Finflow, Genexus | API REST / eventos | mTLS / tokens | MUST | Originación personal/consumo/auto/comercial [DOC-RFI-001 §3.2, DOC-SES-009 §10.3] |
| INT-016 | FATCA (IRS) | Reporte conforme procedimiento | Conforme IRS | MUST | Anual |
| INT-017 | CRS (OCDE) | Reporte conforme procedimiento autoridad fiscal local | Conforme OCDE | MUST | Anual |
| INT-018 (REV v2.0) | **Herramienta AML externa con IA** | Stream de eventos + API REST + bloqueo bidireccional | mTLS / OAuth2 | MUST | **Reemplaza módulo AML interno**; proveedor por seleccionar; el actual sale de soporte en 2026 |
| INT-019 | SINPE (Costa Rica) — TBD | A definir | A definir | TBD | Solo si hay corresponsalía con Costa Rica |
| INT-020 | APC (Asociación Panameña de Crédito) | API según buró | TBD | MUST | Originación y reporte (consolidado con INT-010 — APC funciona como Central de Riesgos local) |
| INT-021 (NEW v2.0) | **ERP externo** (por seleccionar) | API REST + archivos estándar | mTLS / OAuth2 | MUST | Recibe asientos contables del CBS en tiempo real o micro-batch (≤ 5 min); GL consolidado [BR-013] |
| INT-022 (NEW v2.0) | **SISCARD** (core de tarjetas) | API REST / eventos | mTLS / tokens | MUST | Vista 360° del cliente; CIF compartido [DOC-RFI-001 §2.2, §3.10] |
| INT-023 (NEW v2.0) | **Panadata** (KYC) | API REST | mTLS / tokens | MUST | Validación automática y alertas en tiempo real sobre cambios societarios [DOC-SES-006, DOC-RFI-001 §3.10] |
| INT-024 (NEW v2.0) | **App Enhancer** (gestor documental SaaS) | API REST / eventos | mTLS / tokens | MUST | Expediente único digital; el CBS expone eventos para el expediente [DOC-RFI-001 §2.2] |
| INT-025 (NEW v2.0) | **Banca Seguro** (broker de seguros) | API REST | mTLS / tokens | MUST | Pólizas vinculadas a créditos (vida/desgravamen, incendio) [DOC-SES-001] |
| INT-026 (NEW v2.0) | **Plataforma IAM corporativa** (Microsoft Entra ID / SSO) | SAML 2.0, OAuth 2.0 / OIDC, LDAP/AD | Federado | MUST | Recertificación periódica de accesos [DOC-RFI-001 §4.7, DOC-SES-007] |
| INT-027 (NEW v2.0) | **Data Lake en AWS + Snowflake DWH** | Streaming (Kafka / CDC) + API REST | mTLS / tokens | MUST | Streaming desde el CBS hacia el Data Lake; 96% de fuentes de datos del banco provienen del Core [DOC-SES-005] |
| INT-028 (NEW v2.0) | **DGI** (subsidio Interés Preferencial — Ley 468/2025) | Procedimiento DGI | TBD | MUST | Reclamo trimestral del subsidio [DOC-RFI-001 §3.2.1] |
| INT-029 (NEW v2.0) | **Átomos** (BI regulatorio) | Batch / API | TBD | SHOULD | Mini-DWH para reportería SBP — evoluciona con migración Snowflake [DOC-SES-001, DOC-SES-005] |
| INT-030 (NEW v2.0) | **Emerix** (cobros — Fase 2) | API REST + eventos (en tiempo real, no batch) | mTLS / tokens | MUST | Notificación al sistema externo de cobranza en tiempo real (eliminando desfase batch de 1 día) [DOC-SES-009 §3.2, FR-030] |
| INT-031 (NEW v2.0) | **Talentía** (RRHH — SaaS) | API REST | mTLS / tokens | SHOULD | Para usuarios internos y planilla del banco |

---

## Requisitos de Datos (DR) — REV v2.0

- **DR-001**: Cliente persona natural identificado por cédula panameña con dígito verificador validado; persona jurídica por RUC [DOC-CB-001-C17]. **MUST**.
- **DR-002**: Cuentas mapeadas al plan SBP (tipo, estatus, titularidad, productos asociados). **MUST**.
- **DR-003**: Transacción genera asiento contable inmutable con timestamp, canal, usuario, resultado. **MUST**.
- **DR-004**: Hipotecas con campos para tipo de producto, subsidio estatal, garantías, reestructuraciones históricas, condiciones especiales COVID-19. **MUST**.
- **DR-005**: Créditos con campos para garantía, tasa, plan de pagos, modelo de provisión (NIIF 9 + 6-2000), etiquetas especiales. **MUST**.
- **DR-006**: Plan de cuentas SBP (1xx–6xx, no modificable) [DOC-CB-003-C7]. **MUST**.
- **DR-007**: Calidad de datos alineada a las tres validaciones del SEI (estructura, aritmética, consistencia histórica) [DOC-CB-003-C26]. **MUST**.
- **DR-008**: Linaje origen-destino documentado; transformaciones versionadas; análisis de impacto disponible. **MUST**.
- **DR-009**: Sistema de registro único por entidad; copias derivadas read-only etiquetadas. **MUST**.
- **DR-010**: MDM para datos maestros (cliente, producto, organización). **MUST**.
- **DR-011**: Retención — logs auditoría/seguridad/contables ≥ 7 años; logs aplicación 90 días + 1 año archivado; métricas 2 años agregadas + 5 años muestreadas; trazas 30 días en línea. **MUST**.
- **DR-012**: Cifrado en reposo en todos los almacenes. **MUST**.
- **DR-013**: Residencia de datos en Panamá [DOC-CB-001-C10]. **MUST**.
- **DR-014 (REV v2.0)**: Migración desde DataPro/eIBS y datos legados (COBOL, mainframe, archivos planos, hojas Access/Excel). 96% de fuentes de datos vienen del Core actual [DOC-SES-005]. **MUST**.
- **DR-015**: Consolidación de sistemas satélite (Profimype, sistemas hipotecarios auxiliares, hojas Access/Excel). **MUST**.
- **DR-016**: Clasificación de datos Public / Internal / Confidential / Restricted; controles diferenciados (PRIN P6). **MUST**.
- **DR-017**: Backup y DR conforme RTO/RPO; DR probado ≥ semestralmente. **MUST**.
- **DR-018**: Inmutabilidad de logs de auditoría (WORM o equivalente). **MUST**.
- **DR-019**: Datos históricos ≥ 5–7 años por segmento para calibrar PD/LGD/EAD [DOC-CB-003-C16]. **MUST**.
- **DR-020 (NEW v2.0)**: **CIF único** como entidad maestra del cliente, compartido entre CBS, SISCARD y herramientas externas (Panadata, AML, App Enhancer) con sincronización en tiempo real [DOC-RFI-001 §3.10]. **MUST**.
- **DR-021 (NEW v2.0)**: **Diccionario de datos del CBS** — el nuevo CBS debe documentar formalmente al menos los **8,000+ elementos** del diccionario actual [DOC-RFI-001 §4.6, DOC-SES-005, DOC-SES-009 §6.1] con propietarios y reglas de calidad. **MUST**.
- **DR-022 (NEW v2.0)**: **Streaming de datos** hacia el Data Lake (AWS) y Snowflake DWH en tiempo real o near-real-time (no solo batch) [DOC-RFI-001 §2.2, §4.5, DOC-SES-005, DOC-SES-009 §10.2]. **MUST**.

---

## Matriz de Trazabilidad de Requisitos (resumen)

| BR / Meta (STKE) | FR principales | NFR principales | INT | DR | PRIN |
|---|---|---|---|---|---|
| BR-001 / G-3, G-4 | FR-034, FR-035, FR-036, FR-042, FR-071 | NFR-P-001..006, NFR-A-001..007 | INT-001..003, INT-013 | DR-014, DR-017 | P2, P3, P11, P12 |
| BR-002 / G-1, G-6 | FR-046..054, FR-055..063, FR-064..067 | NFR-C-001..012, NFR-SEC-005, NFR-SEC-010 | INT-005, INT-006, INT-010, INT-018, INT-023 | DR-006, DR-007, DR-011, DR-019, DR-021 | P4, P5, P7, P8 |
| BR-003 / G-2 | — | NFR-C-009, NFR-C-010 | — | — | (gobernanza) |
| BR-004 / G-5 | FR-002, FR-005, FR-014..017, FR-019, FR-043, FR-072 | NFR-M-002 | INT-007, INT-008, INT-009, INT-028 | DR-004, DR-005 | P20 |
| BR-005 / G-6 | FR-064..067 | NFR-C-005, NFR-C-011 | INT-010, INT-020 | DR-005, DR-019 | P8 |
| BR-006 / G-7 | — | NFR-C-008 | — | DR-013 | P6 |
| BR-007 / G-8 | — | NFR-C-008, NFR-C-009 | — | — | P17, P19 |
| BR-008 / G-9 | FR-013, FR-014, FR-018, FR-024, FR-070 | NFR-M-006 | INT-013, INT-014, INT-022 | DR-014, DR-015, DR-021 | P8 |
| BR-009 / G-10 | FR-074 | NFR-U-001..006 | — | — | P21 |
| BR-010 / G-3, G-4 | FR-034, FR-071, FR-073, FR-075 | NFR-A-001, NFR-A-002, NFR-M-002 | INT-001, INT-011, INT-012, INT-013, INT-022 | DR-002, DR-003, DR-020 | P11, P12, P16 |
| BR-011 / O-10 | — (resultado) | — | — | — | (consecuencia) |
| BR-012 / P15 | FR-072 | NFR-A-002 | INT-001 | — | P15 |
| **BR-013 (NEW) / G-9** | FR-069, FR-058, FR-070 | NFR-C-005, NFR-C-011 | INT-021 | DR-006, DR-008 | P8 |
| **BR-014 (NEW) / G-2** | — | NFR-A-005 | — | DR-013, DR-017 | (modelo financiero) |

---

## Conflictos de Requisitos y Resoluciones

> Esta sección hace explícitos los conflictos derivados del análisis de stakeholders (STKE) y las decisiones tomadas durante las 8 sesiones presenciales.

### C-1: TCO bajo (BR-003) vs Controles obligatorios exhaustivos (NFR-SEC, NFR-C)

- **Stakeholders**: Finanzas vs Cumplimiento/CISO/Riesgos.
- **Resolución (Comprometer + Priorizar)**: clasificar como **obligatorios eliminatorios** y **deseables priorizables**. Obligatorios entran al RFP como cláusula sin opcionalidad; deseables compiten por presupuesto incremental con caso de negocio.
- **Ganador / Perdedor**: gana Cumplimiento/CISO/Riesgos en obligatorios; Finanzas obtiene predictibilidad del TCO base + control sobre extras.

### C-2: 99.99% sin downtime vs Mantenimiento SEI / parches críticos

- **Resolución (Innovar)**: rolling/blue-green/canary obligatorio (NFR-A-007); ventanas solo en franjas con bloqueo aprobado por Negocio. Parches críticos pueden quebrar SLA con justificación post-mortem.

### C-3: Cloud público vs Soberanía de datos (BR-006)

- **Resolución (Priorizar)**: bloquear el debate **antes del RFP** con el dictamen Legal vinculante. El RFP define la regla; vendors que no cumplan se eliminan. **Preferencia explícita por Azure** (stack actual) si el dictamen lo habilita en territorio panameño; AWS para Data Lake (no datos sensibles del CBS).

### C-4: Productos sociales vs Cero customización del vendor

- **Resolución (Priorizar via P20 + NFR-M-002)**: productos sociales DEBEN soportarse vía parametrización. Vendor que no demuestre en demo queda eliminado.

### C-5: Velocidad de modernización vs Cautela operacional

- **Resolución (Fase + Comprometer)**: migración por bandos (no big-bang), paralelo ≥ 3 meses por bando y compuertas go/no-go con voto de Operaciones y Riesgos.

### C-6: 99.99% (NFR-A-001) vs PRIN v1.1 P3 (99.95%)

- **Resolución (Tier)**: tier crítico 99.99% para servicios críticos en línea; 99.95% canales digitales generales (alineado PRIN); 99.9% batch. **Acción**: refresh de PRIN a v1.2 que formalice el tiering.

### C-7 (NEW v2.0): CAPEX→OPEX (BR-014) vs Soberanía (BR-006) — modelo de despliegue

- **Stakeholders**: Finanzas (prefiere OPEX/cloud) vs Cumplimiento/Legal/Contraloría (residencia local).
- **Resolución (Priorizar + Innovar)**: la soberanía gana en caso de conflicto. Para preservar la intención CAPEX→OPEX se exploran: (a) cloud regional con presencia panameña; (b) modelos híbridos (Core en premisas + servicios no-sensibles en cloud); (c) contrato de suscripción on-premise con costos OPEX-like.

### C-8 (NEW v2.0): AML embebido vs AML externo

- **Stakeholders**: Cumplimiento (continuidad operativa) vs Innovación + Datos (decisión final por motor con IA).
- **Resolución (Priorizar)**: AML externo confirmado [DOC-SES-009 §10.4]. El CBS NO incluye módulo AML interno. El RFI ya refleja esta decisión [DOC-RFI-001 §2.2]. La selección del motor AML externo se gestiona como proyecto paralelo coordinado con el go-live del CBS.

### C-9 (NEW v2.0): GL en el Core vs ERP externo

- **Stakeholders**: Finanzas (control contable robusto) vs Innovación + TI (Cores modernos no incluyen GL).
- **Resolución (Innovar)**: adquisición de ERP externo (BR-013). El CBS gestiona asientos transaccionales y los expone al ERP en tiempo real o micro-batch. La selección del ERP se gestiona como proyecto paralelo.

### C-10 (NEW v2.0): Preferencia por COBIS / descarte de Temenos, Finacle, Mambu, SAP vs Proceso RFP objetivo

- **Stakeholders**: áreas de negocio (preferencia operativa expresada en sesiones) vs Contraloría + Legal (proceso objetivo y auditable).
- **Resolución (Priorizar)**: el RFP debe operar sobre criterios eliminatorios objetivos. Las preferencias del banco alimentan la **matriz de ponderación** sin convertirse en criterios de descalificación. La preferencia por Azure como nube destino del CBS sí puede materializarse en ponderación favorable a vendors con arquitectura nativa Azure (DOC-RFI-001 §4.7 ya menciona Microsoft Entra ID).

---

## Apéndices

### Apéndice A — Documentos fuente

- `projects/000-global/ARC-000-PRIN-v1.1.md` (21 principios; PRIN v1.1).
- `projects/001-evaluacion-core-banking/ARC-001-STKE-v1.0.md` (27 stakeholders, 17 drivers, 10 metas, 10 resultados).
- `projects/000-global/external/Relevamiento_CoreBanking_CajaDeAhorros_v2.docx` (DOC-CB-001).
- `projects/000-global/external/Relevamiento_Caja Ahorro_Pana.xlsx` (DOC-CB-002).
- `projects/000-global/external/informacion_regulatoria.docx` (DOC-CB-003).
- `projects/001-evaluacion-core-banking/external/1.Material...Día1-SesióndeArquitecturayTecnología-ResumenDía1-...docx` (DOC-SES-001).
- `projects/001-evaluacion-core-banking/external/1.Material...Día2-SesióndeCaptación-ResumenDía2-...docx` (DOC-SES-002).
- `projects/001-evaluacion-core-banking/external/1.Material...Día2-SesióndeEstrategiayNegocio-ResumenDía2-...docx` (DOC-SES-003).
- `projects/001-evaluacion-core-banking/external/1.Material...Día3-SesióndeCrédito-Día3-Sesióndecrédito-Evaluación...docx` (DOC-SES-004).
- `projects/001-evaluacion-core-banking/external/1.Material...Día3-SesióndeDatos-Día3-Sesióndedatos-Evaluaciónd...docx` (DOC-SES-005).
- `projects/001-evaluacion-core-banking/external/1.Material...Día3-SesiónRegulatoria-Día3-SesiónRegulatoria-Evaluació...docx` (DOC-SES-006).
- `projects/001-evaluacion-core-banking/external/1.Material...Día4-SesióndeCiberseguridad-DÍA4-SesióndeCiberseguridad-Eva...docx` (DOC-SES-007).
- `projects/001-evaluacion-core-banking/external/1.Material...Día4-SesióndeInfraestructura-DÍA4-SesióndeInfraestructura-Ev...docx` (DOC-SES-008).
- `projects/001-evaluacion-core-banking/external/1.Material...ResumendeNotasAndreina_Sesionescon_27085f.docx` (DOC-SES-009 — Resumen Consolidado).
- `projects/001-evaluacion-core-banking/external/7.RFI-RFI_CAP_CoreBancario_v1.docx` (DOC-RFI-001 — RFI v1.0).
- `projects/001-evaluacion-core-banking/external/5.PreparaciónPOC-POC_seleccion_core_banking_CAP_v1.docx` (DOC-POC-001 — Ficha técnica PoC v1.0).

### Apéndice B — Glosario (adicional a v1.0)

Términos nuevos en v2.0 (definiciones tomadas del RFI):

- **APC** — Asociación Panameña de Crédito. Central de Riesgos privada local; reporta cartera mensual en lote.
- **App Enhancer** — Gestor documental SaaS utilizado por CAP; integración punto a punto hoy, eventos vía CBS en v2.0.
- **BPM** — Business Process Management. Sistemas de originación: Ultimus, Asicom-Finflow, Genexus.
- **CIF** — Customer Information File. Expediente único del cliente.
- **DDI** — Descuento / Débito Directo Interbancario. Pago de préstamos vía planilla del empleador.
- **DJTE** — Declaración Jurada de Transacción en Efectivo (Ley 23/2015, ≥ B/. 10,000).
- **FECI** — Fondo Especial de Compensación de Intereses. Retención del 1% sobre intereses comerciales remitida al MEF.
- **GL** — General Ledger. Libro Mayor Contable (migra a ERP externo en v2.0).
- **IAM** — Identity and Access Management.
- **IBM MQ** — Middleware de mensajería (Linux) usado como bus de integración.
- **NIIF 16** — Norma de leasing financiero.
- **IAS 21** — Norma de diferencias de cambio en moneda extranjera.
- **Panadata** — Proveedor KYC actual de CAP; valida datos públicos y emite alertas en tiempo real.
- **SCONNECT LAU/CSV** — Solución de integración SWIFT que utiliza CAP.
- **SISCARD** — Core de tarjetas de crédito de CAP (separado del Core bancario).
- **SITECA** — Sistema de originación hipotecaria de CAP.
- **SoD** — Segregation of Duties (Segregación de Funciones).
- **UCP 600** — Reglas internacionales para cartas de crédito documentarias.
- **ISP 98** — International Standby Practices (cartas de crédito stand-by).
- **URDG 758** — Uniform Rules for Demand Guarantees.

### Apéndice C — Diferencias clave entre v1.0 y v2.0 (cheat sheet)

| Tema | v1.0 | v2.0 |
|------|------|------|
| AML | Módulo interno en el Core, real-time (FR-022) | **Herramienta AML externa con IA y APIs**; el CBS expone eventos y soporta bloqueo (FR-048, INT-018) |
| GL / Contabilidad | Asumido dentro del CBS | **ERP externo** + CBS expone asientos (BR-013, FR-069, INT-021) |
| Sucursales | 54 | **60** |
| Acuerdo SBP | 4-2013, 6-2000, 5-2011, 3-2009, 8-2010, Res. DJ-0014 | **+ 1-2026** (Resolución SBP-JD-0001-2026 del 16-ene-2026; multas elevadas; geolocalización **inferencial** digital; **beneficiario final ≥ 10%** — umbral más estricto que el 25% UE/FATF; **Art. 25 §1** vigencia 31-ene-2027; **Art. 14** vigencia 30-jun-2027) |
| Leyes | (implícitas) | **+ Ley 23/2015 (DJTE), Ley 468/2025 (Interés Preferencial), Ley 52/2000 (cheques)** |
| Normas contables internacionales | NIIF 9 | **+ NIIF 16 (leasing), IAS 21 (divisas)** |
| Comercio exterior | SWIFT MT103/MT202 (FR-016) | **+ Cartas de crédito (UCP 600, ISP 98, URDG 758), factoring estatal, transferencias internacionales con políticas explícitas, pagos cross-border no-SWIFT** (FR-039..041) |
| Sistemas satélite | Profimype, hipotecarios auxiliares (genéricos) | **Inventario completo**: SITECA, BPMs (Ultimus/Asicom-Finflow/Genexus), Emerix, Átomos, Talentía, BCG, ANDREA, Banca Seguro, App Enhancer, SISCARD, Panadata (INT-014, INT-015, INT-022..025, INT-029..031) |
| Cobranza | (en BPM externos) | **Cobranza temprana 0–90 días NATIVA en el CBS**; notificación en tiempo real al externo > 90 días (FR-030) |
| Reestructuración | "Workflow controlado con doble aprobación" | **Reestructuración nativa que modifica el crédito sin cancelarlo** (FR-018) |
| Originación | Originación BPM con BPMs externos (genérico) | BPMs explícitos: **Ultimus, Asicom-Finflow, Genexus**; el CBS recibe el crédito aprobado (FR-013, INT-015) |
| Sobregiros | (no cubierto) | **Nativos en cuenta corriente y de ahorro** (FR-008) |
| Cheques de gerencia / chequeras | (no cubierto) | **Nativos** (FR-009, FR-011) |
| Sub-cuentas / Cajones | (no cubierto) | **Deseables** (FR-007) |
| Leasing | "Si aplica" (FR-041) | **NIIF 16 explícito** (FR-025) |
| Créditos sindicados | (no cubierto) | CAP como **coordinador y participante** (FR-026) |
| Macro-obras del Estado | (mención genérica) | **Alianza estratégica ~B/. 3,000M** (FR-027) |
| Hipotecario panameños en el exterior | (no cubierto) | **Nuevo segmento + caso de uso PoC** (FR-015) |
| Créditos mancomunados | (no cubierto) | **Soporte nativo** (FR-028) |
| Préstamos prendarios, líneas de crédito, construcción, autos | (parcialmente) | **Completos con NIIF/SBP** (FR-021..024) |
| FECI | (no cubierto) | **Retención automática 1%** (FR-029) |
| Garantías | (genéricas) | **N:N + módulo central + stand-by LC, performance bonds** (FR-032) |
| Teller / bóveda | (no cubierto explícitamente) | **Módulo Teller + bóveda nativa (reemplazo del Excel actual)** (FR-074) |
| CIF / vista 360° | Implícito | **Pilar arquitectónico — CIF único cross CBS + SISCARD** (FR-075, DR-020) |
| Seguridad / accesos | MFA + ISO 27001 | **+ SoD, recertificación periódica, SSO Entra ID, SAML/OAuth/OIDC/LDAP, MFA por canal, enmascaramiento por rol, límites por usuario** (NFR-SEC-011..018) |
| Validación de datos | (genérica) | **Validación en tiempo de ingreso transversal** (NFR-M-008) |
| Localización | "Español" | **UTC-5, USD, DD/MM/AAAA, días inhábiles PA, ES primario / EN opcional** (NFR-U-005..006) |
| Streaming / Data Lake | (no cubierto) | **Streaming nativo al Data Lake AWS + Snowflake** (DR-022, INT-027) |
| Diccionario de datos | (no cubierto) | **8,000+ elementos documentados con propietarios** (DR-021) |
| Vendor preference | (neutral) | **COBIS preferido; Temenos, Finacle, Mambu, SAP descartados** (informativo en matriz de ponderación) |
| Cloud preference | (genérica) | **Azure preferido; AWS para Data Lake** |
| CAPEX/OPEX | (no cubierto) | **Transición OPEX como objetivo estratégico** (BR-014) |
| Disponibilidad | 5 min downtime aceptable | **≤ 1 min o sin downtime** (NFR-P-006) |

---

## External References

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| DOC-CB-001 | Relevamiento_CoreBanking_CajaDeAhorros_v2.docx | Word | `projects/000-global/external/` | Relevamiento confidencial |
| DOC-CB-002 | Relevamiento_Caja Ahorro_Pana.xlsx | Excel | `projects/000-global/external/` | Cuestionario estructurado |
| DOC-CB-003 | informacion_regulatoria.docx | Word | `projects/000-global/external/` | Brief regulatorio SBP |
| DOC-SES-001 | 1.Material…Día1-Arquitectura-ResumenDía1-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 1 — Arquitectura y Tecnología |
| DOC-SES-002 | 1.Material…Día2-Captación-ResumenDía2-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 2 — Captación y Ventanilla |
| DOC-SES-003 | 1.Material…Día2-EstrategiayNegocio-ResumenDía2-…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 2 — Estrategia y Negocio |
| DOC-SES-004 | 1.Material…Día3-Crédito-Evaluación…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 3 — Crédito |
| DOC-SES-005 | 1.Material…Día3-Datos-Evaluación…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 3 — Datos |
| DOC-SES-006 | 1.Material…Día3-Regulatoria-Evaluación…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 3 — Regulatoria |
| DOC-SES-007 | 1.Material…Día4-Ciberseguridad-Evaluación…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 4 — Ciberseguridad |
| DOC-SES-008 | 1.Material…Día4-Infraestructura-Evaluación…docx | Word | `projects/001-evaluacion-core-banking/external/` | Día 4 — Infraestructura |
| DOC-SES-009 | 1.Material…ResumendeNotasAndreina…docx | Word | `projects/001-evaluacion-core-banking/external/` | **Resumen Consolidado** de las 8 sesiones (notas Andreina) |
| DOC-RFI-001 | 7.RFI-RFI_CAP_CoreBancario_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | **RFI v1.0** (junio 2026) — solicitud formal de información a vendors |
| DOC-POC-001 | 5.PreparaciónPOC-POC_seleccion_core_banking_CAP_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | **Ficha técnica PoC v1.0** — caso de uso de referencia crédito hipotecario con codeudores y subsidio |

### Citations principales nuevas (v2.0)

| Citation ID | Doc | Uso principal |
|---|---|---|
| DOC-SES-001 | Día 1 Arquitectura | DataPro/IBS 7.1, BPMs, IBM MQ, módulo de clientes, Omnicaja, soberanía de datos |
| DOC-SES-002 | Día 2 Captación | Sobregiros, sub-cuentas, depósitos a plazo, bóveda en Excel, DJTE, segmentos |
| DOC-SES-003 | Día 2 Estrategia/Negocio | Cartera personal B/. 1,015M, macro-obras B/. 3,000M, descalce de cartera, productos digitales activos |
| DOC-SES-004 | Día 3 Crédito | Factoring estatal, créditos sindicados, mancomunados, reestructuración, cobranza temprana |
| DOC-SES-005 | Día 3 Datos | 96% datos del Core, 54+ reportes, ERP externo, Data Lake AWS, Snowflake |
| DOC-SES-006 | Día 3 Regulatoria | Acuerdo 1-2026, beneficiario final, AML externo, validación en tiempo de ingreso |
| DOC-SES-007 | Día 4 Ciberseguridad | Sin cifrado, sin MFA, RBAC nativo deseado, IAM en curso, ISO 27001 objetivo |
| DOC-SES-008 | Día 4 Infraestructura | Activo-Pasivo en transición Activo-Activo (35–40 km), Azure preferida, CAPEX→OPEX |
| DOC-SES-009 | Resumen Consolidado | Preferencias vendor (COBIS / descartes), inventario satélite, requisitos no negociables |
| DOC-RFI-001 | RFI v1.0 | Catálogo funcional completo por producto, marco regulatorio, módulos SM/RBAC |
| DOC-POC-001 | Ficha PoC v1.0 | Caso de uso de referencia (Juan Carlos Torres Ramos), 13 módulos M1..M13 |

### Unreferenced Documents

| Filename | Source Location | Reason |
|----------|-----------------|--------|
| Día 1–4 SRT (transcripciones automáticas) | `projects/001-evaluacion-core-banking/external/` | Redundantes con los Resúmenes; no añaden afirmaciones independientes citables. |
| KickOff_CBS_Selection_CAP_vf.pptx, Presentacion-SesionKick-Off.pptx | `projects/001-evaluacion-core-banking/external/` | Material de presentación inicial; insumos cubiertos por DOC-SES-009. |
| Plan_SoftwareSelectionCajadeAhorro_*.xlsx | `projects/001-evaluacion-core-banking/external/` | Cronograma del proyecto; insumo de `/arckit:plan`, no de REQ. |
| 4.Selección...-Pre-seleccióndeCBSdeCAP.xlsx, Ratingdepre-selección..., Criteriosparapre-selección..., Evaluacion_CBS_CAP_conIA, criterios01062026_evaluado_v2.xlsx, referencias_criterios_deseables.pdf, referencias_evaluacion_core.pdf | `projects/001-evaluacion-core-banking/external/` | Insumos de `/arckit:evaluate` y `/arckit:score`; no requisitos. |
| 6.Cuestionarioymatrizdeponderación-* | `projects/001-evaluacion-core-banking/external/` | Cuestionario del RFI consolidado en DOC-RFI-001 y matriz de ponderación; insumo de `/arckit:evaluate`. |
| 5.PreparaciónPOC-Matriz_Evaluacion_PoC_CAP_v1.xlsx, POCv1_borrador.docx | `projects/001-evaluacion-core-banking/external/` | Insumo de `/arckit:evaluate` (criterios PoC); el escenario de referencia está en DOC-POC-001. |
| 7.RFI-Anexos-ArquitecturaTecnológica.pdf, Matrízdetransacciones*.xlsx | `projects/001-evaluacion-core-banking/external/` | Anexos del RFI ya referenciados a través de DOC-RFI-001. |
| ProcedimientoFactoring4.pdf, ProcedimientoOriginacióndePréstamos*.pdf, ProcedimientoMantenimientodePréstamo*.pdf, ResumenProcedimientoCartasdeCrédito.docx, ResumenProcedimientoManejodeTransf*.docx, ResumenProcedimientodeCobranzasSim*.docx | `projects/001-evaluacion-core-banking/external/` | Procedimientos AS-IS; insumos de HLD/DLD y mapeo de procesos detallados, no de REQ a este nivel. |
| Matrizdeproductos-Captación.xlsx, Productos_Comerciales2(1).xlsx, MapadeAplicacionesdeCajadeAhorro*.xlsx, OrganigramaTe*.pdf, Informeejecutivooperacionespréstamos.docx | `projects/001-evaluacion-core-banking/external/` | Catálogos detallados y diagramas AS-IS; insumos de `/arckit:data-model`, `/arckit:diagram` y HLD/DLD. |
| RequerimientosSeguridadOperativa.pdf | `projects/001-evaluacion-core-banking/external/` | Insumo principal de `/arckit:secure` y `/arckit:dpia`; los requerimientos de seguridad genéricos están reflejados en NFR-SEC. |

---

**Generated by**: ArcKit `/arckit:requirements` command
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Evaluación y Selección de Core Banking (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: v2.0 refresh — incorpora las 8 sesiones presenciales de evaluación (25–28 mayo 2026, DOC-SES-001..009), el RFI v1.0 (DOC-RFI-001) y la ficha técnica de PoC v1.0 (DOC-POC-001). Cobertura ampliada de 143 → 193 requisitos. Cambios materiales: AML externo, ERP separado, Acuerdo 1-2026, catálogo funcional completo, sistemas satélite específicos, vendor/cloud preferences, CAPEX→OPEX.
