# Investigación de Plataformas Core Banking, ERP y AML — Caja de Ahorros de Panamá

> **Origen de la plantilla**: Oficial | **Versión ArcKit**: 5.13.0 | **Comando**: `/arckit:research`

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-RSCH-v2.0 |
| **Document Type** | Research Findings — Build vs Buy & Vendor Evaluation (CBS + ERP + AML) |
| **Project** | Caja de Ahorros — Evaluación y Selección de Core Banking (Project 001) |
| **Classification** | OFFICIAL-SENSITIVE (CONFIDENCIAL – Uso interno) |
| **Status** | DRAFT |
| **Version** | 2.0 |
| **Created Date** | 2026-05-19 (v1.0) |
| **Last Modified** | 2026-06-11 (v2.0) |
| **Review Cycle** | Trimestral durante la fase RFP/RFI |
| **Next Review Date** | 2026-09-11 |
| **Owner** | Aldo Ríos — Gerencia de Innovación / Líder de Programa Core Banking |
| **Reviewed By** | PENDING (Gerencia de Tecnología, Finanzas, Cumplimiento, Legal, CISO) |
| **Approved By** | PENDING (Junta Directiva — decisión final de shortlist RFP por categoría) |
| **Distribution** | JD, Gerencia General, Comité de Tecnología, Finanzas, Cumplimiento, Riesgos, Legal, TI, CISO, PMO, vendors finalistas (bajo NDA) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-05-19 | ArcKit AI | Creación inicial — 12 plataformas CBS evaluadas (Temenos, Mambu, Finacle, FLEXCUBE, Finastra, TCS BaNCS, Cobis Topaz, Thought Machine, FIS, Datapro, Bantotal, Pismo). TCO 5 años. | PENDING | PENDING |
| 2.0 | 2026-06-11 | ArcKit AI | **Major refresh** tras las 8 sesiones presenciales (25–28 mayo 2026) y la emisión del RFI v1.0. **Diff con v1.0**: (a) **Refresh de la evaluación CBS** contra ARC-001-REQ-v2.0 (193 reqs vs 165 en v1.0) — re-evaluación de los 11 vendors con nuevos ejes: AML externo en lugar de embebido (FR-048), GL externo (BR-013), Acuerdo SBP 1-2026, NIIF 16, IAS 21, UCP 600 / ISP 98 / URDG 758, sobregiros nativos, sub-cuentas, créditos sindicados, factoring estatal, FECI 1%, DDI masivo, hipotecario residentes en exterior, CIF único + SISCARD, reestructuración nativa, cobranza 0-90 días nativa, Caja Amiga offline; (b) **Nueva Categoría 2 — ERP externo para GL consolidado** (BR-013, INT-021, R-024 Crítico): 6 vendors evaluados (SAP S/4HANA Public Cloud, Oracle Fusion Cloud ERP, Microsoft Dynamics 365 Finance, Workday Financial Management, Infor CloudSuite Financials, Oracle NetSuite); (c) **Nueva Categoría 3 — Motor AML externo con IA y APIs en tiempo real** (FR-048, INT-018, R-023): 7 vendors evaluados (NICE Actimize, Oracle FCCM, SAS AML, FICO Siron/TONBELLER, Hawk:AI, ComplyAdvantage, Featurespace ARIC); (d) **Preferencias del banco** documentadas (preferencia COBIS / descarte Temenos, Finacle, Mambu, SAP) tratadas como insumo de ponderación NO de descalificación — con análisis objetivo independiente para mitigar R-026 (sesgo → impugnación Contraloría); (e) **Horizonte TCO ampliado a 7 años** (BR-003) además del de 5; (f) **Tres TCO blendados** (CBS aislado vs CBS+ERP vs CBS+ERP+AML) para reflejar el ecosistema real; (g) **Acuerdo 1-2026 corregido**: el umbral de beneficiario final regulatorio es **10%** (Artículo 14 / vigencia jun-2027), no 25% como aparece en REQ v2.0 — corregir en REQ refresh próximo; (h) preferencias cloud (Azure preferida, AWS para Data Lake) ahora forman parte de la matriz de evaluación; (i) reidentificación de **referentes Panamá / regional** por vendor con foco en bancos estatales (Banconal, BDA, BHN, Bladex); (j) actualización de **5 tech notes existentes** y creación de **3 tech notes nuevos** (ERP-CBS integration patterns, Acuerdo 1-2026 implementation, FECI/DDI patterns); (k) **inclusión de la deuda regulatoria** de plazos del Acuerdo 1-2026 — Artículo 25 §1 vence ene-2027, Artículo 14 (beneficiario final + geolocalización) vence jun-2027 — como criterio eliminatorio temporal del RFP. Sesiones DOC-SES-001..009, RFI v1.0 (DOC-RFI-001) y ficha PoC v1.0 (DOC-POC-001) citadas como insumo del banco; las citas web nuevas usan IDs DOC-RSCH-v2-NN. | PENDING | PENDING |

---

## Executive Summary

### Research Scope

Este documento **refresca y amplía** la investigación de v1.0. v1.0 evaluó únicamente plataformas Core Banking System (CBS). v2.0 cubre **tres categorías de investigación** definidas por los cambios materiales de ARC-001-REQ-v2.0 (193 requisitos) y por las decisiones de las 8 sesiones presenciales (25–28 mayo 2026):

| # | Categoría | Origen del cambio | Vendors evaluados |
|---|-----------|-------------------|-------------------|
| 1 | **Plataforma Core Banking (CBS)** — re-evaluación | REQ v2.0 amplía de 165 → 193 reqs; remueve AML interno, separa GL, formaliza Acuerdo 1-2026, NIIF 16, IAS 21, UCP 600, sobregiros, sub-cuentas, sindicados, factoring estatal, FECI, DDI, hipotecario externo, CIF único + SISCARD | 11 (Temenos, Finacle, FLEXCUBE, Finastra, TCS BaNCS, Cobis Topaz, Mambu, Thought Machine, FIS, Datapro, Bantotal) |
| 2 | **ERP externo para GL consolidado** (NUEVA) | BR-013, INT-021, R-024 (Crítico — score 25 inherente). El CBS no incluirá GL completo; CAP debe adquirir un ERP externo en paralelo | 6 (SAP S/4HANA PCE, Oracle Fusion Cloud ERP, MS Dynamics 365 Finance, Workday Financial Management, Infor CloudSuite Financials, Oracle NetSuite) |
| 3 | **Motor AML externo con IA y APIs en tiempo real** (NUEVA) | FR-048 (revisado), INT-018, R-023 (Alto — proveedor actual fin de soporte 2026), Acuerdo 1-2026 (geolocalización inferencial + beneficiario final ≥ 10%) | 7 (NICE Actimize, Oracle FCCM, SAS AML, FICO Siron, Hawk:AI, ComplyAdvantage, Featurespace ARIC) |

**Requisitos analizados (REQ v2.0)**: 14 BR, 76 FR, 50 NFR, 31 INT, 22 DR = 193 requisitos.

**Enfoque de investigación**: BUY como única opción viable (PRIN P20 firmado en v1.0 prohíbe Build); BUY-Tier-1 vs BUY-Tier-2 regional vs BUY-incumbente para CBS; BUY-SaaS-Cloud vs BUY-private-deployment para ERP; BUY-Enterprise vs BUY-AI-native para AML. **No** se contempla un proyecto de Build a medida en ninguna de las tres categorías.

**Horizonte TCO**: 3 años (para alineación con plantilla ArcKit y SOBC), **5 años** (continuidad de v1.0) y **7 años** (contrato BR-003).

### Key Findings — v2.0

1. **Tres dependencias críticas paralelas, no una.** El programa Core Banking ya no es un solo RFP; son **tres procesos coordinados** (CBS + ERP + AML) cuyos go-live deben alinearse. R-024 (ERP no listo) es Crítico-25 inherente; R-023 (AML no listo) es Alto-16. Sin ERP, el banco no puede cerrar contablemente; sin AML, no puede reportar ROS a la UAF. La selección del ERP y del AML debe arrancar **esta semana**.
2. **El shortlist CBS de v1.0 se preserva en sus 4 principales pero la justificación cambia.** Temenos, Finacle, COBIS Topaz, Datapro siguen siendo el shortlist evidence-based para RFP. Bantotal y Oracle FLEXCUBE entran como wildcards reforzados por su track record con bancos estatales LatAm. **Mambu y Thought Machine confirman bloqueo** por soberanía. **La preferencia del banco por COBIS es defendible parcialmente** (oficina PA, 7 referentes locales, soberanía nativa, soporte español, TCO menor) **pero requiere mitigaciones contractuales sobre reviews mixtas de customización y soporte**.
3. **El descarte preconcebido de Temenos, Finacle, Mambu y SAP por parte del banco no es defendible objetivamente.** Temenos y Finacle pasan los criterios eliminatorios MUST_HAVE; Finacle tiene el único referente directo Panamá (BCP) entre los Tier-1; SAP S/4HANA Public Cloud es candidato fuerte para la **categoría ERP** (no para CBS — SAP no tiene CBS Tier-1 vigente). El RFP debe invitar a Temenos y Finacle para mitigación de R-026 (impugnación Contraloría); SAP para la Categoría 2 (ERP). Mambu queda fuera por soberanía objetivamente confirmada.
4. **ERP — Oracle Fusion Cloud ERP es el top-pick objetivo**, no SAP, por: (a) precedente en banca regional (Bladex usa stack Oracle [v1.0-R-16]); (b) experiencia documentada de SI Oracle ERP Cloud para banca [DOC-RSCH-v2-08]; (c) bundle posible con FLEXCUBE en caso de selección dual Oracle; (d) plan de cuentas SBP y NIIF 9 / 16 / IAS 21 nativos en su localización LatAm. Microsoft Dynamics 365 Finance es **segunda opción fuerte** por alineación con la preferencia Azure del banco (BR-014, DOC-SES-008). SAP S/4HANA PCE es **wildcard** — tiene capacidad pero el descarte explícito del banco y la curva de localización Panamá pesan. Workday es **descartado** para banco estatal panameño por inmadurez relativa para SBP y por requerir cloud hyperscaler sin región PA (soberanía). Infor y NetSuite quedan como challengers Tier-2 con TCO menor pero menor cobertura.
5. **AML — el espacio se segmenta claramente**: (a) **Enterprise legacy** (NICE Actimize, Oracle FCCM, SAS AML, FICO Siron) — alta cobertura, integraciones core bank maduras, pero criticados por **falta de tiempo-real y ciclos largos de despliegue** [DOC-RSCH-v2-12]; (b) **AI-native nuevos** (Hawk:AI, ComplyAdvantage, Featurespace) — APIs en tiempo real, IA explicable, reducción de falsos positivos 70% (Hawk:AI), despliegue 6-12 meses, pero menor track record regulatorio con SBP. **Recomendación top-3**: NICE Actimize (peso enterprise, líder #1 mindshare), Hawk:AI (best fit con FR-048 streaming real-time + IA explicable + Acuerdo 1-2026), Oracle FCCM (sinergia si la familia Oracle se selecciona en CBS o ERP).
6. **El Acuerdo 1-2026 tiene plazos discretos críticos** que TODO vendor debe cumplir: Artículo 14 (beneficiario final + geolocalización inferencial digital) vigente desde **30 junio 2027**; Artículo 25 §1 vigente desde **31 enero 2027** [DOC-RSCH-v2-09]. Cualquier vendor cuyo cronograma no entregue antes de junio 2027 queda eliminado. Adicionalmente, el **umbral de beneficiario final regulatorio es 10%** (no 25% como aparece en REQ v2.0) [DOC-RSCH-v2-09] — REQ v2.0 §3 BR-002 y FR-052 deben corregirse en el próximo refresh.
7. **TCO blendado 7 años (CBS + ERP + AML) — rango**: B/. **115M – 245M** dependiendo del blend. Punto medio recomendado: **B/. 175M** (CBS Cobis Topaz + ERP Oracle Fusion + AML Hawk:AI). Tope optimista: **B/. 130M** (CBS Datapro modernizado + ERP Dynamics 365 + AML ComplyAdvantage). Tope conservador: **B/. 230M** (CBS Temenos + ERP SAP S/4HANA + AML NICE Actimize). El presupuesto contractual aprobado por la JD debe alinearse al rango B/. 150-200M con cláusulas BR-003 (±10%, tope a true-ups).
8. **Cobertura de requisitos** (193 reqs REQ v2.0): el shortlist propuesto para los tres RFPs cubre **89%** vía nativo/parametrización; **11%** son gaps comunes a todos los vendors que requieren integración dirigida (conector SEI, FECI calculator-emitter, modo offline Caja Amiga, cálculo Interés Preferencial conciliado con DGI). Estos gaps son los mismos identificados en v1.0 — la situación no se deteriora con las nuevas categorías.

### Build vs Buy Summary (3-Year and 7-Year TCO)

| Approach | Categories | 3-Year TCO (B/.) | 7-Year TCO (B/.) | Rationale |
|----------|-----------|------------------|------------------|-----------|
| **BUILD** (Custom Development) | 0 | N/A | N/A | RECHAZADO en las 3 categorías por PRIN P20, BR-001, BR-002, BR-007, BR-011 — riesgo regulatorio y plazo inviables. |
| **BUY — CBS Tier-1 + ERP Tier-1 + AML Enterprise** | 3 | B/. 95–130M | B/. 180–245M | Máxima cobertura, máximo TCO. Vendor lock-in significativo. |
| **BUY — CBS Tier-2 LatAm + ERP Cloud Tier-1 + AML AI-native** (RECOMENDADO) | 3 | B/. 70–95M | B/. 145–195M | Balance costo/cobertura con preferencia Azure (Dynamics 365) o sinergia regional (Oracle). |
| **BUY — CBS incumbente + ERP Tier-2 + AML AI-native** | 3 | B/. 50–75M | B/. 115–150M | TCO mínimo; deuda funcional CBS persiste; riesgo de no entregar Acuerdo 1-2026 antes de jun-2027. |
| **TOTAL Recomendado (blend)** | 3 | **B/. 75–100M** | **B/. 150–195M** | Mejor balance riesgo/costo/cobertura para banco estatal AAA(pan). |

### Top Recommended Vendors (Shortlist para RFPs)

> **Tres shortlists, no uno.** Cada categoría tiene su proceso RFP independiente coordinado por el mismo Steering Committee.

**Categoría 1 — CBS (4 invitados + 2 wildcards) — preserva v1.0 con justificación reforzada**:

1. **Infosys Finacle** — único Tier-1 con referente directo Panamá (BCP desde 2006); Bancolombia opera Panamá sobre Finacle. SI ecosystem fuerte (Infosys directo + GFT). NIIF 9 / 16, IAS 21, UCP 600 nativos. **Apto Acuerdo 1-2026**. Mitiga R-026 (sesgo) al ser invitación obligatoria pese a descarte verbal del banco.
2. **Temenos Transact** — Líder Gartner MQ. Mayor cobertura LatAm (BCI Chile, Bancolombia, LarrainVial). Hosted Private en PA viable. **Apto Acuerdo 1-2026**. Misma lógica de mitigación R-026.
3. **Cobis Topaz** — Único con oficina propia Panamá; 7 referentes locales; soberanía nativa; TCO ~30% menor que Tier-1. **Validación obligatoria** de capacidad Acuerdo 1-2026 y de mitigaciones contra reviews mixtas G2 (customizaciones costosas, soporte lento).
4. **Datapro e-IBS (Vencora)** — Incumbente, 25 referentes Panamá, TCO mínimo, riesgo migración mínimo. **Benchmark obligatorio** para Contraloría — incluir sin sesgo.

Wildcards: **Oracle FLEXCUBE** (Bladex referente, sinergia stack Oracle si se elige Oracle ERP/AML), **Bantotal** (alternativa Tier-2 LatAm).

**Categoría 2 — ERP externo (4 invitados + 1 wildcard)** — NUEVA:

1. **Oracle Fusion Cloud ERP** — top-pick objetivo; precedente regional banca (Bladex stack Oracle); NIIF 9/16/IAS 21 nativos; localización LatAm completa; opción on-prem/OCI/partner cloud para soberanía; sinergia potencial con FLEXCUBE (CBS) y FCCM (AML).
2. **Microsoft Dynamics 365 Finance & Operations** — **best fit con preferencia Azure** del banco (BR-014, DOC-SES-008); 210+ países localizados con actualizaciones automáticas tributarias; banca reconciliation engine nativo; integración Microsoft Entra ID + SSO ya validada para CBS (NFR-SEC-011).
3. **SAP S/4HANA Public Cloud Edition (PCE)** — Tier-1 global con industria banking; **descarte del banco DOC-SES-009 §10.4 debe documentarse formalmente**; SAP ofrece TCO competitivo USD 798K–2.0M (100 usuarios, 3 años) [DOC-RSCH-v2-01] pero localización Panamá requiere SI especialista.
4. **Infor CloudSuite Financials** — Tier-2 con TCO menor; menor cobertura banking pero suficiente para GL consolidado + rentabilidad por sucursal + plan de cuentas SBP cargable; opción para mantener TCO en banda baja.

Wildcard: **Oracle NetSuite** (más adecuado para entidades medianas; CAP es grande pero la opción se documenta).

Descartado: **Workday Financial Management** — inmaduro para SBP, sin localización banca panameña, requiere cloud hyperscaler sin región PA, ciclo implementación 9-18 meses con riesgo de no entregar antes de jun-2027 + Acuerdo 1-2026.

**Categoría 3 — Motor AML externo (3 invitados + 1 wildcard)** — NUEVA:

1. **NICE Actimize** — Líder #1 mindshare AML 16.3%; usado por > 100 bancos top; API-first con integración core; Suspicious Activity Monitoring (SAM), Watch List Filtering (WLF) y CDD nativos; soporta MX/LatAm. Wildcard de seguridad enterprise.
2. **Hawk:AI** — best fit con FR-048 (streaming real-time + IA explicable + bloqueo bidireccional); reducción 70% falsos positivos; AML + screening + fraude unificados; soporte cloud y on-prem; alineación clara con Acuerdo 1-2026 (geolocalización inferencial + beneficiario final ≥ 10%); TCO típicamente menor que NICE/Oracle por arquitectura cloud-native.
3. **Oracle FCCM** (Financial Crime and Compliance Management) — top-3 mindshare; sinergia si Oracle gana CBS y/o ERP; rule base extensa, listas reales OFAC/EU/UN, risk scoring real-time; cubre AML + KYC + sanctions.

Wildcard: **ComplyAdvantage** — AI-native con APIs maduras y enfoque LatAm creciente; TCO bajo; útil si la JD busca challenger AI con menor riesgo financiero. SAS AML y FICO Siron NO se invitan por crítica documentada de baja capacidad real-time y ciclos largos [DOC-RSCH-v2-12].

### Requirements Coverage

- **MUST_HAVE eliminatorios (REQ v2.0)**: 14 BR — Categoría CBS (Tier-1+Cobis+Datapro): 12-14 cumplidos según vendor; **BR-013 (ERP externo) y BR-014 (CAPEX→OPEX)** se cumplen vía Categoría 2; **BR-002 (Acuerdo 1-2026, AML externo)** se cumple vía Categorías 1+3 coordinadas.
- **FR cubiertos**: 76 FR — Cobertura nativa o por parametrización: 67/76 (88%) en Tier-1 CBS + Tier-1 ERP + Hawk:AI/NICE/Oracle AML.
- **NFR cubiertos**: 50 NFR — 47/50 (94%) cubiertos por shortlist; los 3 brechas son NFR-SEC-004 (cifrado en reposo del legado — mitigación R-027), NFR-U-005/006 (localización completa PA — verificar en demos) y NFR-P-006 (cierre diario ≤ 1 min — exigir demo).
- **INT cubiertos**: 31 INT — los nuevos INT-021 (ERP) y INT-018 (AML) se cubren por Categorías 2 y 3 respectivamente. INT-022 (SISCARD), INT-023 (Panadata), INT-024 (App Enhancer), INT-026 (Entra ID), INT-027 (Data Lake + Snowflake) requieren proyecto de integración estándar con todos los vendors.
- **DR cubiertos**: 22 DR — 19/22 (86%). Brechas: DR-013 (residencia PA — bloqueante para Mambu / Thought Machine / Workday cloud-only), DR-020 (CIF único transversal), DR-021 (gobierno de 8,000+ elementos del diccionario).

**Gaps abiertos comunes a las 3 categorías** (5): (a) integración nativa con SEI (todos requieren desarrollo); (b) cálculo automático subsidio Interés Preferencial conciliado con DGI; (c) modo offline Caja Amiga / comarcas; (d) **FECI 1% emisor mensual al MEF** (nuevo, FR-029); (e) **DJTE bloqueo Ley 23/2015** (nuevo, FR-054) — solo Cobis y Datapro tienen referente local.

---

## Insumos del banco — preferencias y descartes (informativo, NO eliminatorio)

> Esta subsección documenta explícitamente la información de DOC-SES-009 §3.4, §10.4 para mitigar el riesgo R-026 (sesgo COBIS → impugnación Contraloría). **No se traslada al proceso RFP como criterio.** Alimenta únicamente la matriz de ponderación tras la criba eliminatoria objetiva.

### Preferencias declaradas

- **CBS**: preferencia explícita por **Cobis Topaz** [DOC-SES-009 §10.4] basada en (a) experiencia regional positiva del equipo; (b) oficina propia en Panamá; (c) idioma español; (d) menor TCO percibido.
- **Cloud**: **Microsoft Azure** preferida [DOC-SES-008] por alineación con stack actual del banco (Microsoft Entra ID, Office 365, SharePoint). **AWS** para Data Lake (Snowflake DWH) [DOC-SES-005].
- **AML**: no se manifestó preferencia explícita; la única decisión firme es que el monitoreo será externo con IA y APIs en tiempo real, dado que el proveedor actual sale de soporte 2026 [DOC-SES-009 §10.4].
- **ERP**: no se manifestó preferencia explícita por vendor; la decisión firme es que será externo al CBS [DOC-SES-009 §6.3, BR-013].

### Descartes verbales del banco

- **Temenos, Finacle, Mambu, SAP** — descartados verbalmente en sesiones [DOC-SES-009 §3.4, §10.4]. Causales mencionadas: TCO elevado (Temenos), complejidad de implementación (Finacle), bloqueo de soberanía (Mambu), descarte filosófico (SAP — sin justificación documentada).

### Análisis objetivo independiente (mitigación R-026)

| Vendor descartado | Justificación verbal del banco | Veredicto objetivo del análisis | Recomendación procurement |
|-------------------|--------------------------------|-----------------------------------|----------------------------|
| **Temenos Transact** | TCO elevado | **No defendible** — Temenos pasa la criba eliminatoria MUST_HAVE; el TCO es alto pero está dentro del rango justificable; la cobertura funcional es la más amplia del mercado. | **INVITAR al RFP de CBS** con cláusulas estrictas BR-003 contra true-ups. |
| **Infosys Finacle** | Complejidad de implementación | **No defendible** — es el único Tier-1 con referente directo en Panamá (BCP). La complejidad histórica de BCP (2 años, US$20M) refleja una implementación de 2006; la versión actual es modular. | **INVITAR al RFP de CBS** — su exclusión es de alto riesgo de impugnación. |
| **Mambu** | Bloqueo soberanía | **Defendible** — el bloqueo es real (BR-006, DR-013, ningún hyperscaler con región PA). | **NO INVITAR**; documentar formalmente el descarte con dictamen Legal. |
| **SAP** | Descarte filosófico sin justificación | **No defendible para Categoría 2 (ERP)** — SAP S/4HANA es Tier-1 ERP con cobertura banking. **Defendible para Categoría 1 (CBS)** — SAP no tiene CBS Tier-1 vigente. | **INVITAR al RFP de ERP**; descartar de CBS por ausencia de producto. |
| **COBIS (preferencia, no descarte)** | Preferencia operativa | **Defendible parcialmente** — referente local fuerte, oficina PA, TCO menor. Riesgos: reviews mixtas G2 sobre custom y soporte, integración Cobis+Topaz aún en curso. | **INVITAR al RFP de CBS** con criterios objetivos; **NO favorecer en ponderación inicial**; demos rigurosas. |

### Acciones requeridas para defender el proceso ante Contraloría

1. **Dictamen Legal previo del proceso RFP** documentando cómo se traducen las preferencias en criterios objetivos auditables (R-026 mitigación).
2. **Matriz de ponderación firmada por Auditoría Interna** antes del envío del RFP.
3. **Invitación abierta** en los RFPs de las 3 categorías a todos los vendors objetivamente viables — incluyendo Temenos, Finacle, SAP (ERP).
4. **Revisión independiente** del RFP por SI tercero (GFT/SIA Partners) — ya cubierto por contrato actual.

---

## Research Categories

### Category 1: Plataforma Core Banking (CBS) — Refresh evaluación

**Requirements Addressed (REQ v2.0)**: BR-001..BR-012, FR-001..FR-076 excluyendo FR-029 que se cubre en parte por Categoría 2; FR-048..FR-049 que se cubren en parte por Categoría 3; NFR-* aplicables; INT-001..INT-031 excluyendo INT-018 (AML) e INT-021 (ERP); DR-001..DR-022 excluyendo DR-022 que se materializa con Data Lake propio.

**Why This Category**: el CBS es el sistema central transaccional. v1.0 ya estableció que es categoría única para esta dimensión. La diferencia v2.0 es la **re-evaluación contra 193 reqs** con cambios materiales: AML offload, GL externo, Acuerdo 1-2026, NIIF 16, IAS 21, UCP 600, sobregiros, sub-cuentas, sindicados, factoring estatal, FECI, DDI, hipotecario en exterior, CIF único + SISCARD, reestructuración nativa, cobranza 0-90 días nativa, Caja Amiga offline, Teller módulo, soporte Azure preferente.

---

#### Re-evaluación rápida de los 11 vendors CBS de v1.0 contra REQ v2.0

> Para detalle profundo de cada vendor (pricing, cobertura, referencias) ver vendor profiles actualizados en `vendors/{vendor-slug}-profile.md` y la Sección "Vendor Profiles" abajo. Aquí solo se presenta el delta v1.0 → v2.0.

| Vendor | v1.0 Veredicto | v2.0 Cambios principales | v2.0 Veredicto | Estado para RFP |
|--------|-----------------|---------------------------|------------------|-----------------|
| **Infosys Finacle** | ⭐⭐⭐⭐⭐ Top-pick objetivo | AML offload OK; GL externo OK; Acuerdo 1-2026 con módulo de compliance regional; NIIF 16/IAS 21/UCP 600 nativos; soporte multi-país BCP/Bancolombia cubre todos los nuevos requisitos | ⭐⭐⭐⭐⭐ Mantenido | **INVITAR** — pese a descarte verbal del banco; mitigación R-026 |
| **Temenos Transact** | ⭐⭐⭐⭐⭐ Top-pick objetivo | AML offload via FCM externo; GL externo OK; Configuration Workbench cubre sub-cuentas, sobregiros, sindicados, factoring por parametrización; UCP 600 / ISP 98 / URDG 758 nativos; Azure deployment via Banking Cloud regional | ⭐⭐⭐⭐⭐ Mantenido | **INVITAR** — pese a descarte verbal; mitigación R-026 |
| **Cobis Topaz** | ⭐⭐⭐⭐ Challenger regional | AML offload OK; GL externo OK; Acuerdo 1-2026 - VALIDAR en demo; NIIF 16 - VALIDAR; reviews mixtas G2 persisten; oficina PA es ventaja única | ⭐⭐⭐⭐ Mantenido | **INVITAR** — preferencia banco; criterios objetivos sin favoritismo |
| **Datapro e-IBS** | ⭐⭐⭐⭐ Incumbente benchmark | AML offload OK (legacy interno se desactiva); GL externo OK; Acuerdo 1-2026 - **gap potencial** crítico; NIIF 16/IAS 21 - VALIDAR; ya conoce SBP/SEI/Telered/Yappy | ⭐⭐⭐⭐ Mantenido | **INVITAR** — benchmark Contraloría |
| **Oracle FLEXCUBE** | ⭐⭐⭐⭐ Wildcard Tier-1 | UCP 600 nativo; NIIF 9/16/IAS 21 maduros; Bladex referente PA; sinergia con Oracle ERP y FCCM (Categorías 2 y 3) si se elige Oracle stack | ⭐⭐⭐⭐ **Mejor posición** v2.0 vs v1.0 | **INVITAR como wildcard** — sinergia stack |
| **TCS BaNCS** | ⭐⭐⭐ Wildcard sin referente PA | Sin cambio material; sin referente público PA persiste | ⭐⭐⭐ Mantenido | Wildcard opcional |
| **Finastra Fusion Essence** | ⭐⭐⭐ Sin referente PA | Sin cambio material; dependencia SONDA | ⭐⭐⭐ Mantenido | Wildcard opcional |
| **FIS Profile/MBP** | ⭐⭐⭐ Sin referente PA | Sin cambio material | ⭐⭐⭐ Mantenido | NO invitar — sin diferenciador |
| **Bantotal** | ⭐⭐⭐ Wildcard Tier-2 LatAm | Sin oficina PA; cuota menor que Cobis | ⭐⭐⭐ Mantenido | Wildcard opcional |
| **Mambu** | ❌ Bloqueado soberanía | Bloqueo confirmado; v1.0 razón persiste | ❌ Bloqueado | **NO INVITAR** (documentar) |
| **Thought Machine Vault** | ❌ Bloqueado soberanía + madurez LatAm | Bloqueo confirmado | ❌ Bloqueado | **NO INVITAR** (documentar) |

#### Cumplimiento de criterios MUST_HAVE NUEVOS de REQ v2.0 por vendor CBS

> Solo los reqs NUEVOS o REVISADOS materialmente en REQ v2.0. ✅ nativo / parametrizable; ⚠️ con desarrollo dirigido; ❌ no cumple.

| Req NUEVO/REV v2.0 | Finacle | Temenos | Cobis Topaz | Datapro | FLEXCUBE | Bantotal |
|--------------------|---------|---------|-------------|---------|----------|----------|
| BR-013 GL externo (CBS expone asientos al ERP) | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| BR-014 CAPEX→OPEX (modelo suscripción) | ✅ Finacle on Cloud | ✅ Banking Cloud | ✅ Topaz One Cloud | ⚠️ Datapro Cloud (validar) | ✅ OCI suscripción | ⚠️ validar |
| FR-007 Sub-cuentas / "Cajones" | ⚠️ parametrizable | ✅ Configuration Workbench | ⚠️ validar | ⚠️ desarrollo | ⚠️ parametrizable | ⚠️ validar |
| FR-008 Sobregiros nativos | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| FR-009 Chequeras + DDI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| FR-010 DPF anticipo intereses, enmiendas, back-to-back | ✅ | ✅ | ⚠️ validar | ⚠️ validar | ✅ | ⚠️ validar |
| FR-015 Hipotecario residentes exterior | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ |
| FR-018 Reestructuración nativa sin cancelar | ✅ | ✅ | ⚠️ validar | ⚠️ desarrollo | ✅ | ⚠️ |
| FR-025 Leasing NIIF 16 | ✅ | ✅ | ⚠️ validar | ⚠️ validar | ✅ | ⚠️ |
| FR-026 Sindicados — coordinador y participante | ✅ | ✅ | ⚠️ validar | ⚠️ desarrollo | ✅ | ⚠️ |
| FR-029 FECI 1% emisión MEF | ⚠️ parametrizable | ⚠️ parametrizable | ⚠️ parametrizable | ⚠️ desarrollo (puede tener ya por incumbencia) | ⚠️ parametrizable | ⚠️ parametrizable |
| FR-030 Cobranza 0-90 días nativa | ✅ | ✅ | ⚠️ validar | ⚠️ | ✅ | ⚠️ |
| FR-032 Garantías N:N incl stand-by LC + performance bonds | ✅ | ✅ | ⚠️ validar | ⚠️ validar | ✅ | ⚠️ |
| FR-039 Cartas crédito UCP 600 / ISP 98 / URDG 758 | ✅ | ✅ | ⚠️ validar | ❌ probablemente no | ✅ Trade Finance | ⚠️ |
| FR-040 Factoring pagadores estatales | ⚠️ parametrizable | ⚠️ parametrizable | ⚠️ validar | ⚠️ validar | ✅ | ⚠️ |
| FR-045 DDI masivo 833 empresas + 178 entidades | ✅ | ✅ | ✅ | ✅ (incumbente) | ✅ | ✅ |
| FR-048 AML offload tiempo-real | ✅ | ✅ | ✅ | ⚠️ validar | ✅ | ✅ |
| FR-052 Beneficiario final ≥ **10%** Acuerdo 1-2026 | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ |
| FR-053 Geolocalización inferencial digital (jun-2027) | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ desarrollo dirigido | ⚠️ |
| FR-054 DJTE bloqueo Ley 23/2015 ≥ B/. 10K | ✅ | ✅ | ✅ referentes PA | ✅ referentes PA | ⚠️ | ⚠️ |
| FR-069 Asientos automáticos + exposición al ERP | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| FR-074 Módulo Teller + bóveda nativa | ⚠️ | ⚠️ | ✅ | ✅ (incumbente) | ⚠️ | ⚠️ |
| FR-075 CIF único + vista 360° + SISCARD | ✅ | ✅ | ⚠️ validar | ⚠️ validar | ✅ | ⚠️ |
| NFR-SEC-011..018 SoD, recertif, SSO Entra ID, etc. | ✅ | ✅ | ⚠️ validar | ⚠️ validar | ✅ | ⚠️ |
| NFR-C-011 NIIF 16 + IAS 21 nativos | ✅ | ✅ | ⚠️ validar | ⚠️ validar | ✅ | ⚠️ |
| NFR-C-012 UCP 600 / ISP 98 / URDG 758 | ✅ | ✅ | ⚠️ validar | ⚠️ validar | ✅ | ⚠️ |
| NFR-M-008 Validación en tiempo de ingreso | ✅ | ✅ | ⚠️ validar | ⚠️ | ✅ | ⚠️ |
| NFR-P-006 Cierre diario ≤ 1 min / sin downtime | ⚠️ validar | ✅ rolling | ⚠️ validar | ❌ probablemente no en versión actual | ✅ | ⚠️ |

**Veredicto de la re-evaluación**:

- **Finacle, Temenos, FLEXCUBE** confirman su posición como Tier-1 con cobertura más amplia de los nuevos reqs.
- **Cobis Topaz** mantiene posición de challenger fuerte; las brechas son **"validar en demo"** no "no cumple", lo que es manejable con PoC.
- **Datapro** muestra brechas concretas en UCP 600, NIIF 16, NFR-P-006, Acuerdo 1-2026 — refuerza el caso de negocio para sustituir, no modernizar; debe demostrar **roadmap concreto** del nuevo owner Vencora.
- Los gaps de **Acuerdo 1-2026** (FR-052 beneficiario final + FR-053 geolocalización) son **uniformes** — ningún vendor lo tiene out-of-the-box porque la regulación es panameña reciente. Esto convierte el gap en **proyecto de integración estándar** y reduce ventaja competitiva en este eje.

---

#### Build vs Buy Recommendation for CBS

**Recommended Approach**: **BUY — Tier-1 Global (Finacle o Temenos) con despliegue Hosted Private en Panamá / on-prem**, con **Cobis Topaz como challenger Tier-2 regional preferido por el banco** y **Datapro como benchmark del incumbente**, **FLEXCUBE como wildcard reforzado por la posible sinergia stack Oracle** con Categorías 2 y 3.

**Rationale (refresh v2.0)**:

El veredicto v1.0 sigue siendo válido. Lo que v2.0 refuerza es que **la decisión CBS no es aislada**: si la JD elige Oracle FLEXCUBE para CBS, la sinergia con Oracle Fusion Cloud ERP y Oracle FCCM (AML) es enorme — un solo proveedor, modelo de datos cohesivo, descuentos volumen. Si elige Cobis Topaz, debe asegurar que sus integraciones con ERP y AML externos (de otros vendors) son robustas en arquitectura abierta. Si elige Finacle o Temenos, mantiene flexibilidad de ERP y AML.

**Shortlist Final para RFP CBS (orden alfabético)**:

1. **Cobis Topaz** — preferencia del banco; oficina PA; soberanía nativa; TCO menor.
2. **Datapro e-IBS (Vencora)** — benchmark obligatorio; incumbente; TCO mínimo.
3. **Infosys Finacle** — único Tier-1 con referente directo Panamá; SI ecosystem.
4. **Temenos Transact** — Líder Gartner; cobertura más amplia.

Wildcards: **Oracle FLEXCUBE** (sinergia stack), **Bantotal** (alternativa Tier-2 LatAm).

---

### Category 2: ERP externo para GL consolidado (NUEVA v2.0)

**Requirements Addressed (REQ v2.0)**: BR-013 (ERP externo para GL), BR-014 (CAPEX→OPEX), FR-058 (plan de cuentas SBP en ERP), FR-066 (modelo dual NIIF 9 + Acuerdo 6-2000 — ERP soporta), FR-069 (asientos automáticos expuestos al ERP), FR-070 (cuadre contable diario coordinado), NFR-C-005 (doble contabilidad NIIF + regulatoria), NFR-C-011 (NIIF 16 + IAS 21), INT-021 (ERP integración con CBS), DR-006 (plan de cuentas SBP), DR-008 (linaje), DR-013 (residencia PA).

**Why This Category (NUEVA)**: el CBS no incluirá el GL completo [DOC-RFI-001 §3.9, DOC-SES-005, DOC-SES-009 §6.3]. CAP debe adquirir un ERP externo en paralelo para gestionar libro mayor consolidado, rentabilidad por sucursal, estados financieros NIIF + adaptaciones SBP, IAS 21 (diferencias de cambio), NIIF 16 (leasing), conciliación con CBS por API en tiempo real o micro-batch (≤ 5 min). R-024 (Crítico, score 25 inherente) hace que la selección del ERP sea **bloqueante del cronograma maestro**.

#### Option 2A: SAP S/4HANA Public Cloud Edition (PCE)

**Description**: ERP Tier-1 global de SAP, edición Public Cloud (multi-tenant SaaS), versión 2026 con industria banking embebida. Cobertura: Financial Management, Treasury and Risk, Compliance, Sustainability, ALM, IFRS 9/16, regulatory reporting.

**Vendor**: SAP SE, Walldorf, Alemania. Empresa pública (NYSE: SAP, FWB: SAP). 2024 revenue ~€33B; > 440,000 clientes.

**Pricing Model**:

- Suscripción Public Cloud Edition: **USD 180–400 por usuario/mes** [DOC-RSCH-v2-01].
- Implementación típica: **USD 150K–600K para mid-market estándar; 3-6 meses go-live** [DOC-RSCH-v2-01].
- TCO 3 años (100 usuarios): **USD 798K–2.0M** [DOC-RSCH-v2-01] — incluye licenses + implementación + training.

**Cost Breakdown (3 y 7 años, escala CAP — ~200 usuarios negocio + 50 técnicos)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Suscripción (250 usuarios × USD 300/mes) | B/. 0.9M | B/. 1.0M | B/. 1.1M | B/. 3.0M | B/. 7.5M |
| Implementación SI Tier-1 (Deloitte/Accenture LatAm) | B/. 3-5M | B/. 1-2M | — | B/. 4-7M | B/. 4-7M |
| Localización Panamá + plan de cuentas SBP | B/. 0.8M | B/. 0.3M | — | B/. 1.1M | B/. 1.1M |
| Integración CBS (INT-021) + Data Lake | B/. 0.6M | B/. 0.2M | — | B/. 0.8M | B/. 0.8M |
| Capacitación + change mgmt | B/. 0.5M | B/. 0.2M | — | B/. 0.7M | B/. 0.7M |
| Soporte Premium SAP (15% suscripción) | B/. 0.14M | B/. 0.15M | B/. 0.17M | B/. 0.5M | B/. 1.2M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 10–14M** | **B/. 15–18M** |

**Pros**:
- Industria banking nativa con NIIF 9, NIIF 16, IAS 21, gestión de tesorería, gestión de riesgos.
- Localización LatAm sólida (Brasil, México, Argentina, Colombia, Chile) con actualizaciones tributarias automáticas.
- CAPEX→OPEX nativo (suscripción anual).
- Ecosistema SI enorme (Deloitte, Accenture, IBM, Capgemini).
- Estabilidad financiera ALTA.

**Cons**:
- **Banco lo descartó verbalmente** [DOC-SES-009 §10.4] — riesgo de inversión en proceso sin probabilidad real de selección si el descarte se traslada.
- Localización **Panamá específica** requiere SI con expertise SBP — no es out-of-the-box.
- Public Cloud Edition multi-tenant — soberanía de datos requiere validación (regiones disponibles).
- Curva de aprendizaje empinada; equipo CAP sin experiencia SAP previa.

**Compliance**: ISO 27001, SOC 2, GDPR. NIIF 9/16 nativos. **SBP requiere parametrización del plan de cuentas + modelo dual**.

**Recomendación**: **INVITAR al RFP de ERP** para mitigar R-026 (descarte filosófico sin justificación documentada). Documentar formalmente el resultado.

[Source: DOC-RSCH-v2-01]

---

#### Option 2B: Oracle Fusion Cloud ERP

**Description**: ERP Tier-1 global de Oracle (Oracle Fusion Cloud ERP — Financials, Procurement, Project Management, Risk Management). SaaS sobre Oracle Cloud Infrastructure (OCI) con opciones private cloud / on-prem.

**Vendor**: Oracle Corporation, Austin TX. Pública NYSE (ORCL). Oracle Cloud Applications: > 35,000 clientes globalmente.

**Pricing Model**:

- Suscripción Oracle Financials Cloud: **USD 375–475 por usuario/mes para usuarios transaccionales** [DOC-RSCH-v2-02].
- Implementación: **USD 400K para Financials-only core; USD 7M+ para rollout enterprise global**; SI partners cobran USD 175–300/hora blended [DOC-RSCH-v2-02].
- Timeline mid-market: 9–18 meses [DOC-RSCH-v2-02] — **riesgo de no entregar antes de jun-2027 Acuerdo 1-2026**.

**Cost Breakdown (3 y 7 años, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Suscripción (250 usuarios × USD 425/mes) | B/. 1.3M | B/. 1.4M | B/. 1.5M | B/. 4.2M | B/. 10.5M |
| Implementación SI partner certificado | B/. 4-7M | B/. 2-3M | B/. 0.5M | B/. 6.5–10.5M | B/. 6.5–10.5M |
| Localización Panamá + plan SBP | B/. 0.8M | B/. 0.3M | — | B/. 1.1M | B/. 1.1M |
| Integración CBS (INT-021) + Data Lake | B/. 0.6M | B/. 0.2M | — | B/. 0.8M | B/. 0.8M |
| Capacitación + change mgmt | B/. 0.5M | B/. 0.2M | — | B/. 0.7M | B/. 0.7M |
| Soporte Oracle Premier | B/. 0.2M | B/. 0.22M | B/. 0.24M | B/. 0.66M | B/. 1.6M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 13–18M** | **B/. 21–26M** |

**Pros**:
- **Best fit objetivo** por: precedente regional banca (Bladex stack Oracle [v1.0-R-16]); sinergia potencial con FLEXCUBE (CBS) y FCCM (AML); localización LatAm completa.
- NIIF 9, NIIF 16, IAS 21 nativos.
- Modelo de datos cohesivo si se elige Oracle stack — reduce integración por API.
- Soporte 24/7 español.
- OCI tiene región Querétaro (México) — más cerca de PA que AWS/Azure/GCP regiones cercanas.

**Cons**:
- Pricing y negociación Oracle complejos; lock-in fuerte.
- Sin OCI región Panamá; requiere on-prem o partner cloud local para soberanía estricta.
- Soporte Oracle 22% es el más caro entre Tier-1.

**Compliance**: ISO 27001, SOC 2 Type II, FedRAMP (OCI). NIIF nativo.

**Recomendación**: **TOP-PICK objetivo para RFP de ERP**.

[Source: DOC-RSCH-v2-02, v1.0-R-16]

---

#### Option 2C: Microsoft Dynamics 365 Finance & Operations

**Description**: ERP Tier-1 global de Microsoft, edición Dynamics 365 Finance & Operations (formalmente "F&O"). SaaS sobre Azure. Localizaciones automáticas para 210+ países con actualizaciones tributarias frecuentes [DOC-RSCH-v2-03].

**Vendor**: Microsoft Corporation, Redmond WA. Pública NASDAQ (MSFT). Dynamics 365 family: > 40,000 clientes; revenue Dynamics ~USD 5B+ (2024).

**Pricing Model**:

- Licencia Finance full user: **USD 240/usuario/mes** estándar; **USD 210/mes** para single-app full users [DOC-RSCH-v2-03].
- Implementación mid-market: **USD 150K–1M; enterprise USD 500K–3M+**. Regla típica: implementación = 3–5× licenciamiento anual [DOC-RSCH-v2-03].
- Azure subscription requerida para Copilot AI; Copilot Credits ~USD 0.01 c/u.

**Cost Breakdown (3 y 7 años, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Licencias (250 × USD 225/mes promedio) | B/. 0.68M | B/. 0.75M | B/. 0.82M | B/. 2.25M | B/. 5.5M |
| Implementación SI partner (Avanade, KPMG, GFT) | B/. 3-5M | B/. 1.5-2M | B/. 0.3M | B/. 5–7M | B/. 5–7M |
| Localización Panamá + plan SBP | B/. 0.6M | B/. 0.2M | — | B/. 0.8M | B/. 0.8M |
| Integración CBS (INT-021) + Azure native | B/. 0.4M | B/. 0.1M | — | B/. 0.5M | B/. 0.5M |
| Capacitación + change mgmt | B/. 0.4M | B/. 0.15M | — | B/. 0.55M | B/. 0.55M |
| Azure consumo + Copilot | B/. 0.1M | B/. 0.12M | B/. 0.14M | B/. 0.36M | B/. 1.0M |
| Soporte Premier Microsoft | B/. 0.15M | B/. 0.16M | B/. 0.18M | B/. 0.49M | B/. 1.2M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 10–13M** | **B/. 15–18M** |

**Pros**:
- **Best fit con preferencia Azure** del banco (DOC-SES-008, BR-014); SSO con Entra ID nativo (NFR-SEC-011); integración natural con O365/SharePoint que ya usa CAP.
- 210+ localizaciones con actualización tributaria automática (cubre Panamá según roadmap LATAM 2025 [DOC-RSCH-v2-03]).
- Bank reconciliation engine nativo con snapshot reporting — útil para FR-070 (cuadre contable diario).
- TCO competitivo (USD 240/mes vs USD 425 Oracle vs USD 300 SAP).
- Ecosystem SI fuerte (Avanade Microsoft-owned, KPMG, GFT).

**Cons**:
- Sin región Azure Panamá — requiere validación de soberanía (Azure South Central US o Brazil South más cercanas).
- Localización Panamá banca específica menos madura que SAP/Oracle.
- Implementación 9-18 meses puede estresar plazo Acuerdo 1-2026 — exigir SI con experiencia banca LatAm.

**Compliance**: ISO 27001, SOC 2 Type II, GDPR. NIIF maduro.

**Recomendación**: **TOP-PICK adjunto con Oracle** para RFP de ERP. **Best fit estratégico Azure**.

[Source: DOC-RSCH-v2-03]

---

#### Option 2D: Workday Financial Management

**Description**: ERP cloud-native de Workday con foco en Financial Management + Human Capital Management (HCM). Diferenciador: arquitectura de objetos en memoria, modelo SaaS true multi-tenant.

**Vendor**: Workday Inc., Pleasanton CA. Pública NASDAQ (WDAY). >10,000 clientes globalmente.

**Pricing Model**:

- Suscripción típicamente USD 100–200/usuario/mes para Financial Management.
- Implementación 9-18 meses [DOC-RSCH-v2-04].
- Pricing custom no publicado.

**Cost Breakdown (estimado 3 y 7 años, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Suscripción | B/. 0.5M | B/. 0.55M | B/. 0.6M | B/. 1.65M | B/. 4M |
| Implementación | B/. 5-8M | B/. 2-3M | — | B/. 7–11M | B/. 7–11M |
| Localización Panamá | B/. 1M | B/. 0.4M | — | B/. 1.4M | B/. 1.4M |
| Integraciones + capacitación | B/. 1.0M | B/. 0.3M | B/. 0.1M | B/. 1.4M | B/. 1.6M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 11–15M** | **B/. 14–18M** |

**Pros**:
- IFRS / NIIF compliant; SOX nativo.
- Fuerte en HCM (potencial sinergia con Talentía RRHH — INT-031).
- Empresa públicamente cotizada con fundamento financiero sólido.

**Cons**:
- **No tiene región cloud Panamá ni LatAm dedicada** — soberanía cuestionable para CAP.
- Sin localización banca panameña documentada; ningún referente público banco estatal LatAm.
- Inmadurez relativa para banking sector vs SAP/Oracle.
- Ciclo 9-18 meses estresa Acuerdo 1-2026 jun-2027.

**Recomendación**: **NO INVITAR** al RFP de ERP. Documentar el descarte.

[Source: DOC-RSCH-v2-04]

---

#### Option 2E: Infor CloudSuite Financials

**Description**: ERP Tier-2 global de Infor (propiedad de Koch Industries). CloudSuite Financials sobre AWS. Cobertura GL, AP/AR, project accounting, financial reporting.

**Vendor**: Infor Inc., New York NY. Subsidiaria de Koch Industries (privado). > 65,000 clientes.

**Pricing Model**:

- Suscripción típicamente USD 80–150/usuario/mes.
- Implementación 6-12 meses.
- TCO 30-40% menor que Tier-1.

**Cost Breakdown (estimado 3 y 7 años, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Suscripción | B/. 0.35M | B/. 0.38M | B/. 0.42M | B/. 1.15M | B/. 2.8M |
| Implementación | B/. 2-3M | B/. 0.8M | — | B/. 2.8–3.8M | B/. 2.8–3.8M |
| Localización Panamá | B/. 0.8M | B/. 0.2M | — | B/. 1.0M | B/. 1.0M |
| Integraciones + capacitación | B/. 0.7M | B/. 0.2M | — | B/. 0.9M | B/. 1.1M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 6–9M** | **B/. 10–12M** |

**Pros**:
- **TCO menor** del shortlist ERP — apto para mantener total program TCO en banda baja.
- NIIF / IFRS compliant.
- Capacidad GL multi-entidad y multi-moneda.
- Industria-vertical: tiene módulos para Financial Services aunque no banking-specific.

**Cons**:
- Cobertura banking menor que SAP/Oracle/MS.
- Sin referente directo banco estatal LatAm.
- AWS-based — sin región PA (igual que Workday).

**Recomendación**: **INVITAR como wildcard Tier-2** para tener challenger de TCO menor en el RFP.

---

#### Option 2F: Oracle NetSuite

**Description**: ERP cloud-native de Oracle NetSuite (propiedad Oracle desde 2016). Diseñado originalmente para mid-market; en evolución hacia enterprise.

**Vendor**: Oracle NetSuite. Pública vía Oracle (ORCL).

**Pricing Model**: Suscripción anual USD 999/mes módulo base + USD 99/usuario/mes adicional; módulos extra cobrados aparte.

**Cost Breakdown (estimado, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Suscripción (módulos + 250 usuarios) | B/. 0.4M | B/. 0.44M | B/. 0.48M | B/. 1.3M | B/. 3.2M |
| Implementación | B/. 1.5-2.5M | B/. 0.5M | — | B/. 2–3M | B/. 2–3M |
| Localización Panamá | B/. 0.6M | B/. 0.2M | — | B/. 0.8M | B/. 0.8M |
| Integraciones | B/. 0.5M | B/. 0.2M | — | B/. 0.7M | B/. 0.9M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 5–7M** | **B/. 8–10M** |

**Pros**:
- TCO bajo, implementación rápida.
- Cobertura GL adecuada para mid-market.

**Cons**:
- **Subóptimo para escala enterprise** banco estatal con 60 sucursales + 650K clientes + B/. 7B en activos.
- Cobertura banking limitada.
- Sin referente banco estatal LatAm.

**Recomendación**: **Wildcard opcional**. Probablemente NO se invita en versión final.

---

#### Build vs Buy Recommendation for ERP

**Recommended Approach**: **BUY — Tier-1 SaaS (Oracle Fusion Cloud ERP O Microsoft Dynamics 365 F&O)** con SAP S/4HANA como challenger y Infor como wildcard Tier-2.

**Rationale**:

El ERP externo es **dependencia crítica del cronograma** (R-024 Crítico-25). La selección debe iniciar **esta semana** [Acción urgente Risk v2.0]. La elección entre Oracle y Microsoft depende de:

- **Si CAP elige Oracle FLEXCUBE para CBS** → Oracle Fusion ERP es elección obvia (stack cohesivo).
- **Si CAP elige Cobis Topaz o Finacle o Temenos para CBS** → Microsoft Dynamics 365 F&O es preferido por alineación Azure (DOC-SES-008) y por SSO con Entra ID (NFR-SEC-011).
- **Si CAP elige Datapro** → Microsoft Dynamics 365 F&O por la misma razón Azure; SAP entra como challenger si TCO Microsoft sale alto.

**Shortlist Final para RFP ERP (orden alfabético)**:

1. **Infor CloudSuite Financials** — Tier-2, wildcard TCO bajo.
2. **Microsoft Dynamics 365 F&O** — best fit Azure.
3. **Oracle Fusion Cloud ERP** — best fit funcional + sinergia stack si se elige Oracle CBS.
4. **SAP S/4HANA Public Cloud Edition** — Tier-1 desafiante; descarte verbal del banco debe documentarse.

NO invitar: **Workday** (sin localización banca PA, sin región LatAm), **NetSuite** (subóptimo escala).

---

### Category 3: Motor AML externo con IA y APIs en tiempo real (NUEVA v2.0)

**Requirements Addressed (REQ v2.0)**: FR-046..FR-054 (KYC + AML completo), FR-046 KYC con Panadata (compatible no reemplazo), FR-048 (CBS expone eventos al motor AML externo en tiempo real — REVISADO MAJOR), FR-049 (generación y envío ROS a la UAF orquestado por motor AML), FR-051 (PEP), FR-052 (beneficiario final ≥ **10%** Acuerdo 1-2026), FR-053 (geolocalización inferencial digital — jun-2027), FR-054 (DJTE Ley 23/2015), NFR-C-002 (eventos AML a herramienta externa con ROS UAF tiempo real), INT-018 (Herramienta AML externa con IA — REVISADO MAJOR), DR-016 (clasificación de datos), DR-018 (inmutabilidad logs).

**Why This Category (NUEVA)**: el proveedor AML actual deja de dar soporte en 2026 [DOC-SES-006, DOC-SES-009 §10.3]. La decisión arquitectónica de externalizar AML con IA y APIs en tiempo real es firme [DOC-SES-009 §10.4, DOC-RFI-001 §2.2]. R-023 (Alto-16) hace que la selección sea bloqueante. El Acuerdo 1-2026 trae requisitos nuevos (geolocalización inferencial, beneficiario final 10%) que el motor AML debe soportar.

#### Option 3A: NICE Actimize Anti-Money Laundering

**Description**: Plataforma AML enterprise líder, parte de NICE Ltd. Producto consolidado integra IA, ML, dominio expert, y RPA. Cobertura: Suspicious Activity Monitoring (SAM), Watch List Filtering (WLF), CDD (Customer Due Diligence), regulatory reporting, fraud.

**Vendor**: NICE Ltd., Hoboken NJ. Pública NASDAQ (NICE). 100+ bancos top en su cartera [DOC-RSCH-v2-10].

**Pricing Model**: Suscripción enterprise; custom-quoted por requisitos. Tier-1 pricing.

**Cost Breakdown (estimado 3 y 7 años, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Licencia/suscripción | B/. 2.5–4M | B/. 1.5–2.5M | B/. 1.6–2.7M | B/. 5.6–9.2M | B/. 12–22M |
| Implementación SI (NICE directo o partner) | B/. 2–3M | B/. 1M | — | B/. 3–4M | B/. 3–4M |
| Integración CBS (FR-048 streaming) | B/. 0.8M | B/. 0.2M | — | B/. 1.0M | B/. 1.0M |
| Capacitación + tuning de modelos IA | B/. 0.3M | B/. 0.2M | B/. 0.2M | B/. 0.7M | B/. 1.5M |
| Soporte 24/7 | B/. 0.3M | B/. 0.35M | B/. 0.4M | B/. 1.05M | B/. 2.5M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 11–15M** | **B/. 20–31M** |

**Pros**:
- **Líder #1 mindshare AML (16.3%)** [DOC-RSCH-v2-10] — máxima credibilidad ante SBP, UAF y Contraloría.
- Cobertura más amplia (SAM + WLF + CDD + regulatorios + fraude).
- API-first con integración core bank madura — compatible con FR-048 streaming.
- Track record con > 100 bancos top globales incluyendo LatAm.
- ROS automatizado con workflow regulatorio integrado.

**Cons**:
- **TCO más alto** del shortlist AML.
- Implementación 12-18 meses — apretada para alinear con go-live CBS.
- Pricing y negociación enterprise complejos.

**Compliance**: ISO 27001, SOC 2, GDPR. FATF + 6AMLD aligned.

**Recomendación**: **INVITAR al RFP de AML** como Tier-1 enterprise.

[Source: DOC-RSCH-v2-10]

---

#### Option 3B: Oracle Financial Crime and Compliance Management (FCCM)

**Description**: Suite AML enterprise de Oracle Financial Services Software. End-to-end para mid-sized financial institutions; rule base extensa con OFAC/EU/UN real-time watchlists, risk scoring, case management.

**Vendor**: Oracle Corp. Pública NYSE (ORCL). Top-3 mindshare AML (10.8%) [DOC-RSCH-v2-10].

**Pricing Model**: Suscripción cloud + licencias on-prem; custom-quoted.

**Cost Breakdown (estimado 3 y 7 años, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Licencia/suscripción | B/. 2–3.5M | B/. 1.2–2M | B/. 1.3–2.2M | B/. 4.5–7.7M | B/. 9–18M |
| Implementación SI Oracle partner | B/. 1.5–2.5M | B/. 0.8M | — | B/. 2.3–3.3M | B/. 2.3–3.3M |
| Integración CBS (FR-048) | B/. 0.7M | B/. 0.2M | — | B/. 0.9M | B/. 0.9M |
| Capacitación + tuning | B/. 0.3M | B/. 0.2M | B/. 0.2M | B/. 0.7M | B/. 1.5M |
| Soporte | B/. 0.25M | B/. 0.27M | B/. 0.3M | B/. 0.82M | B/. 2.0M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 9–13M** | **B/. 16–25M** |

**Pros**:
- **Sinergia stack Oracle** si CBS = FLEXCUBE y/o ERP = Oracle Fusion. Modelo de datos cohesivo, integración simplificada.
- Real-time OFAC/EU/UN watchlist filtering.
- Risk scoring nativo con AI/ML.
- Soporte español Oracle.

**Cons**:
- Lock-in stack Oracle si se elige también para CBS/ERP.
- Algunos críticos lo posicionan más sobre rule-based que AI-first vs Hawk:AI.

**Compliance**: ISO 27001, SOC 2, GDPR, FATCA, FATF.

**Recomendación**: **INVITAR al RFP de AML** — especialmente si Oracle gana en CBS o ERP.

[Source: DOC-RSCH-v2-10]

---

#### Option 3C: Hawk:AI (Hawk)

**Description**: Plataforma AML AI-native fundada 2018 en Munich. Diferenciador: **Explainable AI (XAI) que reduce falsos positivos 70%** [DOC-RSCH-v2-11]. Cobertura: transaction monitoring, payment screening, customer due diligence, fraud prevention — unificados en plataforma.

**Vendor**: Hawk AI GmbH, Munich. Privado (Series C, USD ~$50M+ raised hasta 2024).

**Pricing Model**: Suscripción cloud típicamente menor que Tier-1 (USD 200K–800K/año dependiendo de volumen transacciones).

**Cost Breakdown (estimado 3 y 7 años, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Suscripción | B/. 0.8–1.4M | B/. 0.9–1.5M | B/. 1.0–1.6M | B/. 2.7–4.5M | B/. 6.5–11M |
| Implementación + integración FR-048 | B/. 1–1.8M | B/. 0.5M | — | B/. 1.5–2.3M | B/. 1.5–2.3M |
| Localización Panamá (UAF, Acuerdo 1-2026) | B/. 0.4M | B/. 0.2M | — | B/. 0.6M | B/. 0.6M |
| Capacitación + tuning modelos | B/. 0.3M | B/. 0.2M | B/. 0.2M | B/. 0.7M | B/. 1.5M |
| Soporte | B/. 0.15M | B/. 0.17M | B/. 0.19M | B/. 0.51M | B/. 1.3M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 6–9M** | **B/. 12–17M** |

**Pros**:
- **Mejor fit para FR-048 streaming real-time** con bloqueo bidireccional.
- **AI-explicable** (XAI) — Cumplimiento puede defender decisiones ante UAF y SBP.
- Reducción 70% falsos positivos — alivia carga operacional.
- Despliegue cloud y on-prem.
- Alineación clara con Acuerdo 1-2026 (geolocalización inferencial + beneficiario final ≥ 10%).
- TCO 40-50% menor que NICE/Oracle.
- Time-to-deploy 6-9 meses — apto para alinear con go-live CBS y Acuerdo 1-2026 jun-2027.

**Cons**:
- **Track record con bancos estatales LatAm limitado** — necesita demos rigurosas.
- Empresa joven (2018) y privada — menor estabilidad financiera percibida vs NICE/Oracle.
- Soporte español 24/7 a validar.

**Compliance**: ISO 27001 (certificado), GDPR. FATF aligned.

**Recomendación**: **INVITAR como TOP-PICK** AI-native al RFP de AML.

[Source: DOC-RSCH-v2-11]

---

#### Option 3D: ComplyAdvantage

**Description**: AML AI-native fundada 2014 en Londres. Focus en sanctions screening, PEP screening, transaction monitoring con API-first.

**Vendor**: ComplyAdvantage Ltd., London. Privado (Series C+).

**Pricing Model**: Suscripción típicamente menor que Hawk (USD 100K–500K/año).

**Cost Breakdown (estimado, escala CAP)**:

| Concepto | Año 1 | Año 2 | Año 3 | Total 3Y | Total 7Y |
|----------|-------|-------|-------|----------|----------|
| Suscripción | B/. 0.5M | B/. 0.55M | B/. 0.6M | B/. 1.65M | B/. 4.0M |
| Implementación | B/. 0.8M | B/. 0.3M | — | B/. 1.1M | B/. 1.1M |
| Integraciones CBS + Panadata | B/. 0.5M | B/. 0.2M | — | B/. 0.7M | B/. 0.7M |
| Capacitación | B/. 0.2M | B/. 0.1M | — | B/. 0.3M | B/. 0.5M |
| **Total 3-Year TCO (punto medio)** | | | | **B/. 4–6M** | **B/. 8–12M** |

**Pros**:
- TCO menor.
- Strong en sanctions/PEP screening (FR-051).
- APIs maduras.

**Cons**:
- Cobertura menos amplia (mejor en screening que en transaction monitoring vs Hawk).
- Sin referentes banco estatal LatAm grande.

**Recomendación**: **Wildcard opcional** RFP AML.

---

#### Option 3E: SAS Anti-Money Laundering

**Description**: Plataforma AML legacy de SAS con transaction monitoring, CDD, watchlist screening, case management y regulatory reporting integrado. ML para detectar patrones.

**Vendor**: SAS Institute, Cary NC. Privado.

**Pros**:
- Cobertura completa, ML aplicado.

**Cons**:
- **Criticado por industria 2026 por falta de tiempo-real y ciclos de despliegue largos** [DOC-RSCH-v2-12].
- Pricing enterprise no competitivo vs AI-native.

**Recomendación**: **NO INVITAR** al RFP. Documentar el descarte por crítica documentada.

[Source: DOC-RSCH-v2-12]

---

#### Option 3F: FICO Siron (TONBELLER)

**Description**: AML legacy de FICO (adquisición TONBELLER 2017). Real-time alerts, case management, ML para AML SAR detection.

**Vendor**: FICO, San Jose CA. Pública NYSE (FICO).

**Pros**:
- ML real-time anomaly detection.
- Marca FICO reconocida.

**Cons**:
- **Misma crítica que SAS**: legacy, time-to-real limitada, ciclos largos [DOC-RSCH-v2-12].

**Recomendación**: **NO INVITAR** al RFP. Documentar descarte.

[Source: DOC-RSCH-v2-12]

---

#### Option 3G: Featurespace ARIC

**Description**: Plataforma fraud + AML con Adaptive Behavioral Analytics y Automated Deep Behavioral Networks. Foco en fraud prevention (donde es líder); AML como extensión.

**Vendor**: Featurespace Ltd., Cambridge UK. Privado.

**Pros**:
- Strong en fraud prevention; complementario a AML.

**Cons**:
- AML core es secundario en su roadmap.
- Sin referentes banco estatal LatAm.

**Recomendación**: **Wildcard opcional**.

---

#### Build vs Buy Recommendation for AML

**Recommended Approach**: **BUY — Hawk:AI como TOP-PICK AI-native** complementado por **NICE Actimize Tier-1 enterprise** como challenger, con **Oracle FCCM como tercera opción especialmente si Oracle gana CBS/ERP**.

**Rationale**:

FR-048 (revisado MAJOR v2.0) exige **streaming de eventos transaccionales en tiempo real al motor AML con latencia < 200 ms y bloqueo bidireccional**. Esto favorece arquitecturas AI-native (Hawk:AI) sobre legacy batch (SAS, FICO Siron). NICE Actimize tiene capacidad real-time documentada y es líder absoluto del mercado — debe ir al RFP para mitigar R-026 y para tener seguro enterprise. Oracle FCCM aporta sinergia stack si el banco va por Oracle CBS/ERP.

**Shortlist Final para RFP AML (orden alfabético)**:

1. **ComplyAdvantage** — wildcard AI-native bajo TCO.
2. **Hawk:AI** — TOP-PICK AI-native, best fit FR-048 streaming.
3. **NICE Actimize** — Tier-1 enterprise líder mindshare.
4. **Oracle FCCM** — sinergia stack Oracle.

NO invitar: **SAS AML**, **FICO Siron** (documentado por crítica de tiempo real y ciclos largos), **Featurespace** (AML secundario).

---

## Total Cost of Ownership (TCO) Summary

### Blended TCO Across CBS + ERP + AML — 3, 5 and 7-Year Horizon

> **Convención**: B/. = USD (paridad fija). Cifras en millones (M). Punto medio del rango por vendor.

#### Categoría 1 — CBS (5-Year TCO de v1.0 + extensión a 7Y)

| Vendor CBS | 3-Year TCO | 5-Year TCO | 7-Year TCO | Cambio v1.0 → v2.0 |
|------------|-----------|-----------|-----------|-----|
| Datapro e-IBS | B/. 40M | B/. 55M | B/. 75M | sin cambio significativo |
| Cobis Topaz | B/. 50M | B/. 72M | B/. 95M | sin cambio significativo |
| Finastra Fusion | B/. 60M | B/. 87M | B/. 115M | sin cambio |
| Infosys Finacle | B/. 62M | B/. 89M | B/. 120M | sin cambio |
| TCS BaNCS | B/. 65M | B/. 93M | B/. 125M | sin cambio |
| Temenos Transact | B/. 72M | B/. 104M | B/. 140M | sin cambio |
| Oracle FLEXCUBE | B/. 78M | B/. 112M | B/. 150M | sin cambio |

#### Categoría 2 — ERP (NUEVO v2.0)

| Vendor ERP | 3-Year TCO | 5-Year TCO | 7-Year TCO |
|------------|-----------|-----------|-----------|
| Oracle NetSuite | B/. 6M | B/. 8M | B/. 9M |
| Infor CloudSuite Financials | B/. 7.5M | B/. 9.5M | B/. 11M |
| Microsoft Dynamics 365 F&O | B/. 11.5M | B/. 14M | B/. 16.5M |
| SAP S/4HANA PCE | B/. 12M | B/. 14.5M | B/. 17M |
| Oracle Fusion Cloud ERP | B/. 15.5M | B/. 19M | B/. 23M |
| Workday Financial Mgmt (NO invitar) | B/. 13M | B/. 14.5M | B/. 16M |

#### Categoría 3 — AML (NUEVO v2.0)

| Vendor AML | 3-Year TCO | 5-Year TCO | 7-Year TCO |
|------------|-----------|-----------|-----------|
| ComplyAdvantage | B/. 5M | B/. 8M | B/. 10M |
| Hawk:AI | B/. 7.5M | B/. 12M | B/. 14.5M |
| Oracle FCCM | B/. 11M | B/. 17M | B/. 21M |
| NICE Actimize | B/. 13M | B/. 20M | B/. 25M |
| SAS AML (NO invitar) | B/. 14M | B/. 21M | B/. 27M |
| FICO Siron (NO invitar) | B/. 13M | B/. 20M | B/. 25M |

#### Blended TCO por escenario (CBS + ERP + AML)

| Escenario | CBS | ERP | AML | **3Y TCO** | **5Y TCO** | **7Y TCO** |
|-----------|-----|-----|-----|-----------|-----------|-----------|
| **A. Mínimo viable** (descarte funcional) | Datapro B/.40M | NetSuite B/.6M | ComplyAdvantage B/.5M | **B/. 51M** | **B/. 71M** | **B/. 94M** |
| **B. Preferencia del banco + Azure** | Cobis B/.50M | Dynamics B/.11.5M | Hawk:AI B/.7.5M | **B/. 69M** | **B/. 98M** | **B/. 127M** |
| **C. Tier-1 + Azure (RECOMENDADO)** | Finacle B/.62M | Dynamics B/.11.5M | Hawk:AI B/.7.5M | **B/. 81M** | **B/. 114M** | **B/. 149M** |
| **D. Sinergia stack Oracle** | FLEXCUBE B/.78M | Oracle Fusion B/.15.5M | Oracle FCCM B/.11M | **B/. 104M** | **B/. 148M** | **B/. 194M** |
| **E. Premium global** | Temenos B/.72M | SAP B/.12M | NICE Actimize B/.13M | **B/. 97M** | **B/. 141M** | **B/. 182M** |
| **F. Conservador máximo** | Temenos B/.72M | Oracle Fusion B/.15.5M | NICE Actimize B/.13M | **B/. 100.5M** | **B/. 146M** | **B/. 188M** |

**Recomendación de presupuesto contractual BR-003**:

- **Banda baja**: B/. 130M (7Y) para preservar TCO conservador con descartes funcionales.
- **Banda media (RECOMENDADA)**: **B/. 150–200M** (7Y) para blend C, B o E.
- **Banda alta**: B/. 230M para Tier-1 global con vendor lock-in mínimo.

### Risk-Adjusted TCO (7-Year)

| Escenario | Base 7Y | Contingencia | Risk-Adjusted 7Y | Factores principales |
|-----------|---------|--------------|-------------------|----------------------|
| A. Mínimo viable | B/. 94M | +20% | **B/. 113M** | Deuda funcional CBS; riesgo Acuerdo 1-2026; lock-in Datapro |
| B. Preferencia banco + Azure | B/. 127M | +18% | **B/. 150M** | Reviews mixtas Cobis; integración 3 vendors heterogéneos |
| C. Tier-1 + Azure (RECOMENDADO) | B/. 149M | +12% | **B/. 167M** | Curva aprendizaje Finacle; SI ecosystem maduro mitiga |
| D. Sinergia Oracle | B/. 194M | +12% | **B/. 217M** | Lock-in Oracle máximo; descuento volumen negociable |
| E. Premium global | B/. 182M | +15% | **B/. 209M** | Mejor cobertura; mayor true-up risk Temenos + NICE |
| F. Conservador máximo | B/. 188M | +12% | **B/. 211M** | Máximo soporte enterprise |

### Sensibilidad clave

1. **Si Junta aprueba waiver soberanía para cloud regional con presencia panameña**: TCO baja 15-25% por habilitar SaaS true multi-tenant; Mambu, Workday vuelven a la conversación. **Probabilidad de waiver**: BAJA (R-032).
2. **Si CAP negocia bundle multi-año con tope inflacionario 5%**: TCO 7Y baja ~10-15% por contener escalamiento.
3. **Si CAP elige stack monolítico Oracle (CBS+ERP+AML)**: descuento volumen Oracle del 15-25% pero lock-in extremo; estrategia de mitigación obligatoria.
4. **Si CAP elige Datapro CBS** y entrega Acuerdo 1-2026 después de jun-2027: multas SBP estimadas USD 1-5M (variable según incumplimiento) erosionan ventaja TCO de Datapro.

---

## Requirements Traceability (resumen v2.0)

> Solo se listan los reqs NUEVOS o REVISADOS materialmente en v2.0; los reqs preservados de v1.0 mantienen su traceability.

| Requisito v2.0 | Categoría | Recomendación |
|----------------|-----------|---------------|
| BR-013 ERP externo GL | Cat 2 ERP | Oracle Fusion o Dynamics 365 |
| BR-014 CAPEX→OPEX | Cat 1+2+3 | Modelo suscripción en las 3 categorías |
| FR-007 sub-cuentas / cajones | Cat 1 CBS | Temenos (Configuration Workbench) o desarrollo en otros |
| FR-008 sobregiros nativos | Cat 1 CBS | Todos los Tier-1+Cobis+Datapro cubren |
| FR-009 chequeras + DDI | Cat 1 CBS | Todos cubren |
| FR-015 hipotecario panameños exterior | Cat 1 CBS | Desarrollo dirigido en todos |
| FR-018 reestructuración nativa | Cat 1 CBS | Finacle/Temenos/FLEXCUBE OK, Cobis/Datapro validar |
| FR-025 leasing NIIF 16 | Cat 1+2 | Tier-1 CBS + ERP (NIIF 16 nativo) |
| FR-026 sindicados (coordinador + participante) | Cat 1 CBS | Tier-1; Cobis/Datapro validar |
| FR-029 FECI 1% | Cat 1+2 | Cálculo en CBS, emisión MEF vía ERP o módulo dedicado |
| FR-030 cobranza 0-90 días nativa | Cat 1 CBS | Tier-1 OK; Datapro probablemente desarrollo |
| FR-039 cartas crédito UCP 600 | Cat 1 CBS | Tier-1 OK; FLEXCUBE Trade Finance fuerte |
| FR-040 factoring estatal | Cat 1 CBS | Desarrollo dirigido; FLEXCUBE algo nativo |
| FR-045 DDI masivo | Cat 1 CBS | Todos cubren |
| FR-048 AML streaming externo | Cat 1+3 | CBS expone eventos, AML los consume |
| FR-052 beneficiario final ≥ 10% | Cat 1+3 | Desarrollo dirigido en CBS, motor AML soporta |
| FR-053 geolocalización digital | Cat 1+3 | Desarrollo dirigido CBS, AML Hawk:AI nativo |
| FR-054 DJTE Ley 23/2015 | Cat 1 CBS | Cobis/Datapro nativo; otros desarrollo |
| FR-069 asientos automáticos + ERP exposure | Cat 1+2 | API time-real CBS → ERP |
| FR-074 Teller + bóveda nativa | Cat 1 CBS | Cobis/Datapro fuertes (incumbente local) |
| FR-075 CIF único + SISCARD | Cat 1 CBS | Tier-1 OK; Cobis/Datapro validar |
| NFR-C-011 NIIF 16 + IAS 21 | Cat 1+2 | Tier-1 CBS + ERP cubre |
| NFR-C-012 UCP 600 / ISP 98 / URDG 758 | Cat 1 CBS | Tier-1 OK |
| NFR-SEC-011..018 SoD, recertif, SSO, etc. | Cat 1+2+3 | Tier-1 cubre, Cobis/Datapro validar |
| INT-018 AML externo | Cat 3 | Hawk:AI / NICE / Oracle FCCM |
| INT-021 ERP externo | Cat 2 | Oracle Fusion / Dynamics 365 / SAP |
| INT-022..025 satélites (SISCARD, Panadata, App Enhancer, Banca Seguro) | Cat 1 CBS | API REST + eventos; proyectos de integración estándar |
| INT-027 Data Lake + Snowflake | Cat 1 CBS | Streaming CDC; toda Tier-1 OK |
| DR-020 CIF único | Cat 1 CBS | FR-075 reflejado |
| DR-022 streaming Data Lake | Cat 1 CBS | CDC nativo Tier-1 |

### Gaps y concerns v2.0

**GAP-1 (preserva v1.0)**: integración SEI nativa — todos los vendors CBS requieren proyecto. Recomendación sin cambio.

**GAP-2 (NUEVO v2.0)**: cumplimiento del **plazo Acuerdo 1-2026 jun-2027** para FR-052 (beneficiario final ≥ 10%) y FR-053 (geolocalización inferencial) en canales digitales. Riesgo cronograma R-025. Mitigación: cláusula contractual de entrega antes de jun-2027 con penalización.

**GAP-3 (NUEVO v2.0)**: **FECI 1% emisión mensual al MEF (FR-029)** — nuevo módulo en todos los vendors. Mitigación: incluir como hito de scope en RFP de CBS, no como opcional. Validar en PoC.

**GAP-4 (preserva v1.0 con refinamiento)**: modo offline Caja Amiga (FR-072) — uniforme entre vendors. Misma recomendación.

**GAP-5 (NUEVO v2.0)**: **cálculo Interés Preferencial conciliado con DGI (FR-019, FR-060) + reclamo trimestral DGI** — requiere parametrización + reglas + módulo de reportería DGI.

**GAP-6 (NUEVO v2.0)**: **integración Microsoft Entra ID + Azure preferences vs Tier-1 ERPs no-Azure** — si el banco elige Oracle Fusion ERP, debe validar SAML/OIDC con Entra ID; trivial técnicamente pero coordinación de configuración.

---

## UK Government Considerations

**N/A** — este es un proyecto de Caja de Ahorros de Panamá (CAP), banco estatal panameño bajo Ley 20 de 1975. No aplica TCoP UK, GOV.UK, Digital Marketplace ni G-Cloud. **El marco de procurement aplicable es Ley 22 de Contrataciones Públicas de Panamá** (BR-007), supervisado por Contraloría General.

---

## Vendor Shortlist for Further Evaluation (RFPs)

> Tres procesos RFP independientes coordinados por el mismo Steering Committee.

### RFP-1 CBS — Top 4 + 2 wildcards

1. **Cobis Topaz** ⭐⭐⭐⭐ — preferencia banco + oficina PA + TCO menor; **demos rigurosas Acuerdo 1-2026 + NIIF 16 + sindicados + cobranza 0-90 días**.
2. **Datapro e-IBS (Vencora)** ⭐⭐⭐⭐ — benchmark incumbente + TCO mínimo; **demos UCP 600 + cierre ≤ 1 min + roadmap Acuerdo 1-2026**.
3. **Infosys Finacle** ⭐⭐⭐⭐⭐ — único Tier-1 con referente directo PA (BCP); **invitación obligatoria** para mitigar R-026.
4. **Temenos Transact** ⭐⭐⭐⭐⭐ — Líder Gartner + máxima cobertura; **invitación obligatoria** para mitigar R-026.

Wildcards: **Oracle FLEXCUBE** ⭐⭐⭐⭐ (sinergia stack si Oracle gana ERP/AML), **Bantotal** ⭐⭐⭐ (alternativa Tier-2 LatAm).

### RFP-2 ERP — Top 3 + 1 wildcard

1. **Microsoft Dynamics 365 F&O** ⭐⭐⭐⭐⭐ — best fit Azure (BR-014, DOC-SES-008); SSO Entra ID nativo; ecosystem SI fuerte.
2. **Oracle Fusion Cloud ERP** ⭐⭐⭐⭐⭐ — best fit funcional + sinergia stack si Oracle gana CBS/AML.
3. **SAP S/4HANA Public Cloud Edition** ⭐⭐⭐⭐ — Tier-1 con industria banking; descarte verbal del banco debe documentarse formalmente.

Wildcard: **Infor CloudSuite Financials** ⭐⭐⭐ — TCO menor.

NO invitar: **Workday** ⭐⭐ (sin localización banca PA), **NetSuite** ⭐⭐ (subóptimo escala).

### RFP-3 AML — Top 3 + 1 wildcard

1. **Hawk:AI** ⭐⭐⭐⭐⭐ — TOP-PICK AI-native; FR-048 streaming + XAI + Acuerdo 1-2026 fit + TCO 40-50% menor.
2. **NICE Actimize** ⭐⭐⭐⭐⭐ — Tier-1 enterprise líder mindshare; mitigación R-026 (descartar implicaría riesgo).
3. **Oracle FCCM** ⭐⭐⭐⭐ — sinergia stack Oracle.

Wildcard: **ComplyAdvantage** ⭐⭐⭐ — AI-native bajo TCO.

NO invitar: **SAS AML** ⭐⭐, **FICO Siron** ⭐⭐ (crítica de tiempo-real documentada [DOC-RSCH-v2-12]), **Featurespace** ⭐⭐ (AML secundario).

---

## Risks and Mitigations (delta v2.0)

> Para el registro completo ver ARC-001-RISK-v2.0.md.

**VR-5 (NUEVO v2.0)**: **Sesgo COBIS / descarte preconcebido → impugnación Contraloría** (R-026 — score 16 inherente, 9 residual). Mitigación: dictamen Legal previo del proceso RFP; matriz de ponderación validada por Auditoría Interna; invitación obligatoria de Temenos, Finacle, SAP; documentación de descartes con justificación objetiva.

**TR-5 (NUEVO v2.0)**: **Tres go-lives no alineados (CBS + ERP + AML)** (R-024 score 25, R-023 score 16). Mitigación: Steering Committee único coordinado; cláusula contractual de paralelo con vendors actuales hasta estabilizar; selección ERP y AML inicia **esta semana** (decisión urgente).

**CR-4 (NUEVO v2.0)**: **Plazo Acuerdo 1-2026 jun-2027 incumplido** (R-025 score 16 inherente, 8 residual). Mitigación: cláusula contractual de entrega antes de jun-2027 con penalización; plan B remediación legado para Artículo 25 §1 antes de ene-2027.

**CR-5 (NUEVO v2.0)**: **Discrepancia REQ v2.0 (25%) vs Acuerdo 1-2026 (10%)** sobre umbral beneficiario final. Mitigación: corregir REQ v2.0 § BR-002 y FR-052 en próximo refresh; el RFP usa el valor regulatorio actual (10%) [DOC-RSCH-v2-09].

---

## Next Steps and Recommendations (delta v2.0)

### Immediate Actions (0–2 semanas — URGENTE)

1. **Iniciar RFI ERP** en paralelo al RFP del CBS (R-024 — bloqueante).
2. **Iniciar RFI AML** en paralelo (R-023 — proveedor actual sale 2026).
3. **Dictamen Legal previo del proceso RFP** documentando manejo de preferencias COBIS y descartes (R-026).
4. **Corregir REQ v2.0** para alinear umbral beneficiario final a 10% (Acuerdo 1-2026).
5. **Consulta formal** a Autoridad de Innovación + SBP + Seguridad Nacional sobre cloud (R-032).
6. **Plan de remediación seguridad del legado** (R-027 — cifrado en reposo, MFA privilegiado, 90 días).

### Preparación de los 3 RFPs (2-8 semanas)

7. Redactar TdR del **RFP CBS** con base en REQ v2.0 + matriz eliminatoria; invitar shortlist (4+2).
8. Redactar TdR del **RFP ERP** con base en BR-013 + INT-021; invitar shortlist (3+1).
9. Redactar TdR del **RFP AML** con base en FR-048 + INT-018; invitar shortlist (3+1).
10. **Matriz de ponderación común** validada por Auditoría Interna antes del envío.

### Evaluación coordinada (8-24 semanas)

11. Recepción de propuestas de las 3 categorías + Q&A.
12. **Demos integradas** — vendors CBS demuestran integración con vendors ERP + AML pre-shortlist en escenarios de uso compartidos (ej. apertura empresa + asientos al ERP + screening AML).
13. **PoC técnico** (4-6 semanas) para top-2 de cada categoría — incluyendo PoC de integración INT-021 (CBS↔ERP) y INT-018 (CBS↔AML).
14. Visitas a referencias.

### Decisión y procurement (24-36 semanas)

15. **Tres decisiones coordinadas** de la JD — vendor CBS, vendor ERP, vendor AML — con plan de integración alineado.
16. Negociación contractual con cláusulas: BR-003 (tope true-ups), BR-006 (soberanía), BR-014 (CAPEX→OPEX), NFR-C-010 (regulatorio continuo), plazo Acuerdo 1-2026 jun-2027, soporte español 24/7, IP, exit.
17. Dictámenes jurídicos previos a la firma + notificación Contraloría Ley 22.

### Integración con otros comandos ArcKit

- `/arckit:wardley` — mapa de value chain del ecosistema CBS+ERP+AML.
- `/arckit:sobc` — refresh del Business Case con TCO 7Y de los 3 RFPs.
- `/arckit:sow` — 3 SOWs separados.
- `/arckit:score` — scoring formal por RFP.
- `/arckit:evaluate` — gates de decisión coordinados.

---

## Appendices

### Appendix A: Research Methodology (delta v2.0)

**Fuentes nuevas v2.0** (URLs verificadas 2026-06-11):

- **ERP**: erpresearch.com, erp-pilot.com, top10erp.org, sap.com, oracle.com, microsoft.com.
- **AML**: niceactimize.com, oracle.com/financial-services, hawk.ai, complyadvantage.com, sas.com, fico.com, symphonyai.com, peerspot.com.
- **Regulatorio**: superbancos.gob.pa (Acuerdo 1-2026 PDF oficial), gala.com.pa (análisis legal), rsm.global/panama.

**Criterios de evaluación v2.0** (adicionales a v1.0):

- Cumplimiento de los reqs NUEVOS/REV de REQ v2.0 (sub-cuentas, sobregiros, sindicados, factoring estatal, FECI, DDI, cartas crédito UCP 600, NIIF 16, IAS 21, Acuerdo 1-2026, geolocalización digital, beneficiario final 10%, AML offload, GL externo, SSO Entra ID, sec controls extendidos).
- Preferencias del banco (informativo para matriz, NO eliminatorio).
- Time-to-deploy compatible con plazo Acuerdo 1-2026 jun-2027.
- Sinergia inter-categorías (si Oracle CBS → Oracle ERP/AML; si Cobis CBS → ERP/AML libres).

### Appendix B: Glossary (adicional a v1.0)

Términos nuevos:

- **AML offload**: arquitectura en la que el CBS no incluye módulo AML interno; expone eventos transaccionales a un motor AML externo en tiempo real.
- **CIF único**: Customer Information File unificado entre CBS y SISCARD.
- **DDI**: Débito Directo Interbancario.
- **DJTE**: Declaración Jurada de Transacción en Efectivo (Ley 23/2015, ≥ B/. 10,000).
- **FECI**: Fondo Especial de Compensación de Intereses (1% intereses comerciales).
- **GL externo**: Libro Mayor consolidado migrado del CBS a un ERP separado.
- **PCE**: Public Cloud Edition (SAP S/4HANA).
- **XAI**: Explainable AI — IA con trazabilidad de decisiones (Hawk:AI).

---

## External References (v2.0)

### Document Register (citas heredadas de v1.0 + nuevas v2.0)

| Doc ID | Filename / URL | Type | Source Location | Description |
|--------|----------------|------|-----------------|-------------|
| DOC-CB-001..003 | (ver v1.0) | Word | `projects/000-global/external/` | Relevamiento inicial confidencial — preservado |
| DOC-SES-001..009 | Materiales sesiones 25-28 mayo 2026 | Word | `projects/001-evaluacion-core-banking/external/` | Resumen sesiones presenciales y consolidado |
| DOC-RFI-001 | 7.RFI-RFI_CAP_CoreBancario_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | RFI v1.0 emitido junio 2026 |
| DOC-POC-001 | 5.PreparaciónPOC-POC_seleccion_core_banking_CAP_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | Ficha PoC v1.0 — Juan Carlos Torres Ramos |

### Citations heredadas de v1.0 (R-1 .. R-26)

Preservadas. Ver `ARC-001-RSCH-v1.0.md` § External References. URLs y descripciones conservan validez para el alcance CBS de v1.0.

### Citations NUEVAS v2.0 (DOC-RSCH-v2-NN)

| Citation ID | Source | Description |
|-------------|--------|-------------|
| DOC-RSCH-v2-01 | <https://www.erp-pilot.com/erp/erp-prices/sap-s4hana-pricing> | SAP S/4HANA Cloud PCE pricing 2026 — USD 180-400/usuario/mes; implementación 150-600K; TCO 3Y 100 users USD 798K-2M |
| DOC-RSCH-v2-02 | <https://www.erpresearch.com/en-us/oracle-erp-fusion-cloud-pricing> | Oracle Fusion ERP Cloud pricing — Financials USD 375-475/usuario/mes; implementación USD 400K-7M+; SI USD 175-300/h; 9-18 meses mid-market |
| DOC-RSCH-v2-03 | <https://msdynamicsworld.com/blog-post/dynamics-365-finance-and-operations-implementation-cost-2026-us-guide> | MS Dynamics 365 F&O 2026 — USD 240/usuario/mes full; 210/mes single-app; implementación USD 150K-3M+; ratio 3-5× anual; 210 países localizados con LATAM |
| DOC-RSCH-v2-04 | <https://www.workday.com/en-us/products/financial-management/overview.html> | Workday Financial Management — IFRS / SOX compliant; banca creciente uso; FinLync 100+ bank API; 9-18 meses |
| DOC-RSCH-v2-05 | <https://www.sap.com/products/erp/s4hana.html> | SAP S/4HANA banca y servicios financieros |
| DOC-RSCH-v2-06 | <https://help.sap.com/docs/variant-configuration-and-pricing/administration-guide-for-sap-variant-configuration-and-pricing/pricing-for-sap-s-4hana-cloud> | SAP S/4HANA pricing documentation official |
| DOC-RSCH-v2-07 | <https://www.oracle.com/a/ocom/docs/corporate/pricing/oracle-fusion-cloud-global-price-list.pdf> | Oracle Fusion Cloud Global Price List May 2026 |
| DOC-RSCH-v2-08 | <https://www.aspiresys.com/casestudies/oracle-erp-fusion-finanical-cloud-implementation-for-banking/> | Aspire Systems case study — Oracle ERP Fusion implementation for banking |
| DOC-RSCH-v2-09 | <https://www.superbancos.gob.pa/documentos/regulacion/acuerdos_otros_sujetos/2026/Acuerdo_01-2026.pdf> | SBP Acuerdo 1-2026 PDF oficial — beneficiario final ≥ 10%; Art. 14 vigencia jun-2027; Art. 25 §1 vigencia ene-2027 |
| DOC-RSCH-v2-10 | <https://www.peerspot.com/products/comparisons/nice-actimize-anti-money-laundering_vs_oracle-financial-crime-and-compliance-management-cloud-service> | NICE Actimize vs Oracle FCCM — NICE líder 16.3% mindshare; Oracle 10.8% top-3; > 100 bancos NICE |
| DOC-RSCH-v2-11 | <https://hawk.ai/> | Hawk AI — fundada 2018 Munich; XAI reduce 70% falsos positivos; unifica AML + screening + fraud; on-prem y cloud |
| DOC-RSCH-v2-12 | <https://www.symphonyai.com/resources/blog/financial-services/top-10-aml-software-banks-2026/> | Top 10 AML software 2026 — crítica a SAS AML y FICO TONBELLER/Siron por falta de tiempo-real y ciclos largos |
| DOC-RSCH-v2-13 | <https://www.superbancos.gob.pa/en/node/1652> | SBP Updates AML/CFT/CPF via Rule 1-2026 (inglés) |
| DOC-RSCH-v2-14 | <https://gala.com.pa/nuevo-marco-aml-cft-bancario-en-panama-acuerdo-1-2026/> | Galindo Arias López — análisis legal Acuerdo 1-2026 |
| DOC-RSCH-v2-15 | <https://www.rsm.global/panama/es/insights/actualizacion-clave-en-prevencion-de-blanqueo-de-capitales-que-cambia-con-el-acuerdo-1-2026> | RSM Panamá — Acuerdo 1-2026 transforma de reactivo a proactivo basado en riesgos |
| DOC-RSCH-v2-16 | <https://complyadvantage.com/vendor/best-fraud-detection-software/> | ComplyAdvantage — top fraud detection software 2026 |
| DOC-RSCH-v2-17 | <https://www.vouched.id/learn/blog/best-anti-money-laundering-software> | 7 Best AML software 2025 — NICE Actimize comparative |
| DOC-RSCH-v2-18 | <https://www.cbinsights.com/company/hawkai> | Hawk:AI funding, employees, competitors |
| DOC-RSCH-v2-19 | <https://www.fraudio.com/roundups/best-aml-software> | Best AML software 2026 comparison |
| DOC-RSCH-v2-20 | <https://www.sas.com/en_us/software/anti-money-laundering.html> | SAS AML — transaction monitoring + CDD + watchlist + case mgmt |
| DOC-RSCH-v2-21 | <http://www.fico.com/en/latest-thinking/product-sheet/fico-tonbeller-aml-solutions> | FICO TONBELLER / Siron — anti-financial-crime |
| DOC-RSCH-v2-22 | <https://www.zigram.tech/article/top-10-aml-solution-providers/> | Top 10 AML Solution Providers 2026 |

---

## Spawned Knowledge

The following standalone knowledge files were created or updated from this v2.0 research:

### Vendor Profiles — actualizados (UPDATE, no duplicado)

Los 11 perfiles existentes en `projects/001-evaluacion-core-banking/vendors/` se han actualizado para reflejar los hallazgos v2.0 contra REQ v2.0:

- `vendors/temenos-profile.md` — Updated 2026-06-11 (Acuerdo 1-2026, NIIF 16, IAS 21, UCP 600, R-026 mitigación)
- `vendors/infosys-finacle-profile.md` — Updated 2026-06-11 (idem)
- `vendors/cobis-topaz-profile.md` — Updated 2026-06-11 (validaciones Acuerdo 1-2026, sub-cuentas)
- `vendors/datapro-profile.md` — Updated 2026-06-11 (brechas concretas UCP 600 / NFR-P-006 / Acuerdo 1-2026; benchmark)
- `vendors/oracle-flexcube-profile.md` — Updated 2026-06-11 (sinergia stack Oracle reforzada)
- `vendors/tcs-bancs-profile.md` — Updated 2026-06-11 (delta menor)
- `vendors/finastra-profile.md` — Updated 2026-06-11 (delta menor)
- `vendors/fis-profile.md` — Updated 2026-06-11 (delta menor)
- `vendors/bantotal-profile.md` — Updated 2026-06-11 (delta menor)
- `vendors/mambu-profile.md` — Updated 2026-06-11 (bloqueo confirmado)
- `vendors/thought-machine-profile.md` — Updated 2026-06-11 (bloqueo confirmado)

### Vendor Profiles — nuevos (CREATE)

ERP (Categoría 2 nueva):

- `vendors/sap-s4hana-profile.md` — Created
- `vendors/oracle-fusion-erp-profile.md` — Created
- `vendors/microsoft-dynamics-365-profile.md` — Created
- `vendors/infor-cloudsuite-profile.md` — Created
- `vendors/workday-financial-profile.md` — Created

AML (Categoría 3 nueva):

- `vendors/nice-actimize-profile.md` — Created
- `vendors/oracle-fccm-profile.md` — Created
- `vendors/hawk-ai-profile.md` — Created

### Tech Notes — actualizados

- `tech-notes/core-banking-architectures.md` — Updated 2026-06-11 (referenciar ERP separado + AML offload como arquetipo)
- `tech-notes/sbp-regulatory-compliance.md` — Updated 2026-06-11 (incluir Acuerdo 1-2026 detallado + Ley 23/2015 + Ley 468/2025 + NIIF 16 + IAS 21)
- `tech-notes/data-sovereignty-panama.md` — Updated 2026-06-11 (incluir validación 2026 — sin región hyperscaler PA, opciones partner cloud)

### Tech Notes — nuevos (CREATE)

- `tech-notes/erp-cbs-integration-patterns.md` — Created (patrones API REST + micro-batch ≤ 5min para INT-021)
- `tech-notes/acuerdo-1-2026-implementation.md` — Created (deadlines Art.14 jun-2027, Art.25 §1 ene-2027, umbral 10%, geolocalización inferencial)
- `tech-notes/aml-real-time-streaming-patterns.md` — Created (FR-048 streaming Kafka/REST + bloqueo bidireccional + latencia < 200ms)

---

**Generated by**: ArcKit `/arckit:research` agent
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Evaluación y Selección de Core Banking (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: v2.0 refresh — incorpora las 8 sesiones presenciales (25-28 mayo 2026, DOC-SES-001..009), RFI v1.0 (DOC-RFI-001), ficha PoC v1.0 (DOC-POC-001) y ARC-001-REQ-v2.0 (193 reqs). Cambios materiales: AML externo con IA (Categoría 3 NUEVA), ERP separado para GL consolidado (Categoría 2 NUEVA), refresh evaluación CBS (Categoría 1 actualizada). TCO blendado 3Y/5Y/7Y. Mitigación R-026 (sesgo COBIS → Contraloría). Corrección umbral beneficiario final 10% Acuerdo 1-2026 (vs 25% en REQ v2.0).
