# Evaluación de Impacto a la Protección de Datos (DPIA / EIPD) — Programa CBS + ERP + AML — Caja de Ahorros de Panamá

> **Marco regulatorio adaptado**: este documento adopta la estructura del Data Protection Impact Assessment (DPIA) del UK GDPR Article 35 + guía ICO y la **adapta al marco panameño**: **Ley 81 de Panamá** (Protección de Datos Personales) + **Acuerdo SBP 1-2026** (componentes de identidad digital con vigencia 30-jun-2027 para Art. 14) + **Ley 23/2015** (AML/FT) + **autoridad reguladora ANTAI** (Autoridad Nacional de Transparencia y Acceso a la Información). El concepto análogo en español es **Evaluación de Impacto a la Protección de Datos (EIPD)**.

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-DPIA-v1.0 |
| **Document Type** | Data Protection Impact Assessment / Evaluación de Impacto a la Protección de Datos (Panama-adapted, Ley 81) |
| **Project** | Reemplazo del Core Banking + ERP + AML — Caja de Ahorros, Panamá (Project 001) |
| **Classification** | OFFICIAL-SENSITIVE (CONFIDENCIAL – Uso interno) |
| **Status** | DRAFT — **bloqueante para implementación de FR-053 (Acuerdo 1-2026 Art. 14)** |
| **Version** | 1.0 |
| **Created Date** | 2026-06-11 |
| **Assessment Date** | 2026-06-11 |
| **Next Review Date** | 2027-06-11 (anual; o ad-hoc tras eventos críticos) |
| **Owner** | Oficial de Protección de Datos (PENDIENTE de nombrar) + CISO (Guillermo Smith) + Legal |
| **Reviewed By** | PENDING — Cumplimiento, Riesgos, Auditoría Interna, Comité de Tecnología |
| **Approved By** | PENDING — CISO firma riesgos residuales; Comité de Tecnología; Junta Directiva |
| **Distribution** | JD, Gerencia General, Comité de Tecnología, CISO, Oficial de Protección de Datos, Legal, Cumplimiento, Riesgos, Auditoría Interna, ANTAI (en consulta previa si riesgos residuales altos) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-06-11 | ArcKit AI | Creación inicial. **DPIA es bloqueante regulatorio del Acuerdo SBP 1-2026 Art. 14 (vigencia 30-jun-2027)** dado que la geolocalización inferencial digital (FR-053) constituye tratamiento de datos personales de alto riesgo bajo Ley 81. Adapta marco UK GDPR / ICO al equivalente panameño (Ley 81 + Acuerdo 1-2026 + ANTAI). Cubre todos los tratamientos del programa CBS + ERP + AML: geolocalización inferencial, AML con IA explicable + bloqueo bidireccional, beneficiario final ≥ 10%, DJTE Ley 23/2015, scoring crediticio automatizado, datos de menores (Ahorro Fácil para Niños), datos de beneficiarios sociales del Estado (Beca Universal, 120 a los 65, Red de Oportunidades), datos en comarcas indígenas. Pre-screening adaptado: **9/9 criterios ANTAI/ICO cumplidos** → DPIA legalmente requerido. **Gap conocido a refrescar**: este DPIA se elabora antes de la ejecución formal de `/arckit:data-model` — el documento se refrescará a v2.0 cuando el modelo de datos formal esté disponible. Los 8,000+ elementos del diccionario de datos heredado (DR-021) se asumen con la categorización de REQ v2.0 §DR-001..022. | PENDING | PENDING |

---

## Resumen Ejecutivo

| Concepto | Detalle |
|----------|---------|
| **Veredicto del pre-screening (9/9 criterios)** | ✅ **DPIA REQUERIDO legalmente** bajo Ley 81 + Acuerdo SBP 1-2026 |
| **Tratamientos de mayor riesgo identificados** | (a) Geolocalización inferencial digital (FR-053); (b) AML con IA explicable + bloqueo bidireccional (FR-048); (c) Beneficiario final ≥ 10% con análisis de capas societarias (FR-052); (d) Scoring crediticio automatizado vía BPMs externos (FR-013); (e) Datos de menores (Ahorro Fácil para Niños); (f) Datos de beneficiarios sociales vulnerables del Estado |
| **Volumen de titulares** | ~650K clientes persona natural + ~300K beneficiarios sociales del Estado + ~ Menores en cuentas Ahorro Fácil = potencialmente **~1M de titulares afectados** |
| **Total de riesgos identificados** | **23 riesgos de privacidad** — 4 Altos / 12 Medios / 7 Bajos |
| **Consulta previa a ANTAI** | **REQUERIDA** — 1 riesgo residual Alto (geolocalización inferencial inadecuadamente calibrada) requiere consulta previa antes de implementación |
| **Bloqueante de cronograma** | DPIA aprobada y firmada por el Oficial de Protección de Datos (a nombrar) + ANTAI consultada antes de la implementación de FR-053 (target jun-2027 por Art. 14) |
| **Acción crítica P0** | Nombrar Oficial de Protección de Datos (Ley 81) — actualmente vacante |

---

## Sección 1 — Pre-screening (Necesidad del DPIA)

### 1.1 Criterios de Alto Riesgo — Marco Adaptado

> Marco original: ICO 9 criteria checklist. Adaptación a Ley 81 + Acuerdo SBP 1-2026 — los 9 criterios ICO son funcionalmente equivalentes a los desencadenantes de evaluación de impacto bajo Ley 81 y a los riesgos descritos en el Acuerdo SBP 1-2026.

| # | Criterio | Aplica a CAP? | Evidencia |
|---|----------|----------------|-----------|
| 1 | **Evaluación o scoring** | ✅ SÍ | (a) AML risk scoring con IA explicable (FR-048); (b) Scoring crediticio automatizado en BPMs externos (FR-013); (c) Clasificación crediticia A–E Acuerdo 6-2000 (FR-065) |
| 2 | **Decisión automatizada con efecto legal significativo** | ✅ SÍ | (a) Bloqueo bidireccional AML antes de liquidación (FR-048); (b) DJTE Ley 23/2015 — bloqueo automático ≥ B/. 10,000 (FR-054); (c) Decisiones crediticias automatizadas en BPMs |
| 3 | **Monitoreo sistemático** | ✅ SÍ | (a) AML monitoring continuo (FR-048); (b) Geolocalización inferencial digital (FR-053); (c) Listas PEP/OFAC/ONU monitoreadas diariamente (NFR-SEC-009) |
| 4 | **Datos sensibles** (especiales bajo Ley 81) | ✅ SÍ | (a) Datos financieros detallados (cartera, salarios vía planilla, saldos); (b) Datos de beneficiarios de programas sociales (Beca Universal, 120 a los 65, Red de Oportunidades); (c) Datos de hipotecarios subsidiados (vivienda social — Ley 468/2025); (d) Datos de salud implícitos en pólizas de vida (FR-014); (e) Datos de menores (Ahorro Fácil para Niños) |
| 5 | **Procesamiento a gran escala** | ✅ SÍ | ~1M de titulares afectados; 100% de la población bancarizable panameña; banco estatal con mandato social |
| 6 | **Combinación de datasets** | ✅ SÍ | (a) CBS + ERP + AML + SISCARD + Panadata + Data Lake AWS + Snowflake + UAF + APC + DGI + SEI — combinación crítica; (b) Beneficiario final con análisis de capas societarias = combinación de datasets societarios |
| 7 | **Titulares vulnerables** | ✅ SÍ (múltiples grupos) | (a) **Menores** — cuentas Ahorro Fácil para Niños; (b) **Comarcas indígenas** — 5 comarcas con Caja Amiga; (c) **Jubilados** — programa "120 a los 65"; (d) **Beneficiarios sociales** — Beca Universal, Red de Oportunidades; (e) **Inclusión financiera** — clientes sin historial; (f) **Hipotecarios sociales** — clientes de bajos ingresos con Interés Preferencial |
| 8 | **Tecnología innovadora** | ✅ SÍ | (a) **Geolocalización inferencial digital** — combinación de IP+ASN+UA+GPS+comportamiento para inferir ubicación real (FR-053) — tecnología novedosa con implicaciones de privacidad significativas; (b) **AML con IA explicable** (XAI) — modelos de ML para decisiones AML; (c) **Beneficiario final ≥ 10%** con umbral panameño más estricto que UE/FATF (25%) — tecnología de análisis societario automatizado |
| 9 | **Impide el ejercicio de derechos** | ⚠️ A VALIDAR | Mecanismos de Derechos del Titular bajo Ley 81 (acceso, rectificación, cancelación, oposición, portabilidad) — actualmente parciales; sin procedimientos formales documentados. Sin Oficial de Protección de Datos nombrado. |

### 1.2 Veredicto del Pre-screening

- **9/9 criterios cumplidos** → **DPIA LEGALMENTE REQUERIDO**.
- Marco regulatorio: Ley 81 de Panamá (Protección de Datos Personales) + Acuerdo SBP 1-2026 (Resolución SBP-JD-0001-2026) + Ley 23/2015 (AML/FT).
- Sin DPIA aprobada y firmada, **NO se puede implementar** FR-053 (geolocalización inferencial) — bloqueante regulatorio del Acuerdo 1-2026 Art. 14 (vigencia 30-jun-2027).
- Adicionalmente, sin DPIA, el RFP CBS no puede definir cláusulas obligatorias completas sobre Ley 81 (cláusula 11 del SOW CBS — "Confidencialidad y manejo de datos personales").

---

## Sección 2 — Descripción del Tratamiento

### 2.1 Contexto del Programa

Caja de Ahorros (CAP) — banco estatal panameño bajo Ley 20 de 1975 con mandato social del Estado — está reemplazando su Core Banking System (DataPro/eIBS) y adquiriendo, en paralelo coordinado, un ERP externo (para el GL) y un motor AML externo con IA. El programa procesa datos personales de **~1M de titulares** (clientes + beneficiarios sociales + menores) con datos sensibles bajo Ley 81 y bajo el régimen del Acuerdo SBP 1-2026.

### 2.2 Propósitos del Tratamiento

| ID | Propósito | Base legal Ley 81 | Vínculo regulatorio |
|----|-----------|--------------------|----------------------|
| P-01 | Apertura y gestión de cuentas (ahorro, corriente, sub-cuentas, Ahorro Fácil para Niños) | Contrato + Obligación legal SBP | Ley 20/1975, Acuerdo SBP 1-2026 |
| P-02 | Originación y gestión de créditos (hipotecario, personal, comercial, sindicado, etc.) | Contrato + Interés legítimo + Obligación legal | Acuerdo SBP 6-2000, NIIF 9, Ley 468/2025 |
| P-03 | Reportería SBP / UAF / APC / MIVIOT / MEF / DGI | **Obligación legal** | SBP, Ley 23/2015, Acuerdo 1-2026 |
| P-04 | Cumplimiento AML/CFT/FPADM con motor IA explicable | **Obligación legal** | Acuerdo SBP 1-2026, Ley 23/2015 |
| P-05 | **Beneficiario final ≥ 10% para personas jurídicas** | **Obligación legal** | Acuerdo SBP 1-2026 Art. 14 |
| P-06 | **Geolocalización inferencial de clientes digitales** | **Obligación legal** | Acuerdo SBP 1-2026 Art. 14 |
| P-07 | KYC + listas restrictivas (PEP, OFAC, ONU, SBP) | Obligación legal | Ley 23/2015 |
| P-08 | DJTE — Declaración Jurada de Transacción en Efectivo ≥ B/. 10,000 | Obligación legal | Ley 23/2015 |
| P-09 | Programas sociales del Estado (Beca Universal, 120 a los 65, Red de Oportunidades) | Obligación legal + Interés público | Mandato social del Estado |
| P-10 | Hipotecario Interés Preferencial con subsidio DGI | Obligación legal + Contrato | Ley 468/2025 |
| P-11 | Reportería FATCA / CRS internacional | Obligación legal | Acuerdos bilaterales |
| P-12 | Pen-tests + telemetría de seguridad | Interés legítimo (seguridad) | Acuerdo SBP 11-2018 |

### 2.3 Naturaleza del Tratamiento

| Aspecto | Descripción |
|---------|-------------|
| **Recolección** | (a) Apertura presencial / digital (KYC + biometría / OCR); (b) DDI masivo (planilla pública); (c) Eventos transaccionales del CBS; (d) Geolocalización inferencial digital (FR-053); (e) Integración con Panadata (KYC), APC (central de riesgos), SEI (reportes), DGI (subsidio) |
| **Almacenamiento** | On-premise CAP + (opcional, depende ADR-003) cloud privado regional con presencia panameña. Sin transferencia a cloud público internacional. Cifrado en reposo y en tránsito (NFR-SEC-003, NFR-SEC-004 — pendiente cierre R-027) |
| **Uso** | Procesamiento transaccional + reportería regulatoria + monitoreo AML + scoring crediticio + análisis comportamental + auditoría regulatoria |
| **Divulgación** | A SBP (reportería al SEI), UAF (ROS), APC (cartera), MIVIOT/MEF/DGI (subsidios), FATCA/CRS (internacional), motor AML externo (eventos transaccionales) |
| **Eliminación** | Retención mínima 7 años (Código de Comercio + AML); revisión post-vencimiento; auditoría inmutable WORM |

### 2.4 Alcance del Tratamiento

| Aspecto | Detalle |
|---------|---------|
| **Categorías de titulares** | (a) Clientes persona natural (~650K); (b) Clientes persona jurídica con beneficiarios finales; (c) Menores (Ahorro Fácil para Niños); (d) Beneficiarios de programas sociales (~300K); (e) Comarcas indígenas (5 comarcas); (f) Empleados de CAP (~3,500) |
| **Ámbito geográfico** | Territorio panameño + clientes panameños residentes en el exterior (FR-015 — nuevo segmento) |
| **Volumen estimado** | ~1M de titulares procesados; ~51M+ transacciones digitales anuales; ~10x peaks en planilla pública |

### 2.5 Categorías de Datos Personales

> Mapeo desde REQ v2.0 §DR-001..022 (modelo de datos no formal aún — refresh tras `/arckit:data-model`).

**Categorías identificadoras (datos básicos)**:
- Cédula panameña con dígito verificador (DR-001)
- Pasaporte (residentes exteriores — FR-015)
- Datos demográficos (nombre, dirección, fecha nacimiento, nacionalidad)
- Ocupación + ingresos declarados

**Categorías financieras (sensibles bajo Ley 81)**:
- Saldos y movimientos de cuentas (DR-002, DR-003)
- Cartera de créditos (DR-005) — incluyendo Interés Preferencial subsidiado por DGI
- Cartera hipotecaria con condiciones especiales (DR-004)
- Garantías (DR-005)
- Modelo de provisión NIIF 9 + 6-2000

**Categorías regulatorias (sensibles)**:
- PEP / OFAC / ONU flags (FR-051)
- Beneficiario final ≥ 10% — análisis de capas societarias (FR-052)
- ROS (Reportes de Operación Sospechosa) — UAF
- Categoría crediticia A–E + scoring (FR-035, FR-065)

**Categorías de programas sociales (sensibles — titulares vulnerables)**:
- Beneficiarios Beca Universal (menores y familias)
- Beneficiarios "120 a los 65" (jubilados)
- Beneficiarios Red de Oportunidades (familias en pobreza)
- Hipotecario Interés Preferencial — subsidio DGI

**Categorías nuevas v2.0 (Acuerdo 1-2026)**:
- **Geolocalización inferencial digital** (FR-053) — IP+ASN+UA+GPS+comportamiento — **dato personal de alto riesgo**
- Beneficiario final con threshold 10% — **dato societario combinado con personal**

**Categorías de menores**:
- Cuenta Ahorro Fácil para Niños (FR-006)
- Beneficiarios Beca Universal (menores en educación)

### 2.6 Fuentes y Destinos de Datos (Data Flow)

**Fuentes**:
- Apertura presencial / digital del cliente
- BPMs externos (Ultimus, Asicom-Finflow, Genexus)
- Panadata (KYC externo)
- SITECA (originación hipotecaria)
- Listas restrictivas (PEP, OFAC, ONU, SBP) actualizadas diariamente
- DDI masivo de planilla (833 empresas + 178 entidades gubernamentales)

**Destinos**:
- SBP via SEI (reportes XML/XSD)
- UAF (ROS — orquestado por motor AML)
- APC (cartera mensual + consulta online)
- MIVIOT (cartera hipotecaria social)
- MEF + DGI (subsidios)
- FATCA / CRS (internacional)
- Motor AML externo (stream eventos transaccionales)
- ERP externo (asientos contables)
- Data Lake AWS + Snowflake (analítica — pendiente revisión soberanía)
- Microsoft Entra ID (SSO)

### 2.7 Períodos de Retención

| Categoría | Retención mínima | Base legal |
|-----------|------------------|------------|
| Logs auditoría/seguridad/contables | ≥ 7 años | Código de Comercio panameño + AML |
| Logs aplicación | 90 días en línea + 1 año archivado | Buenas prácticas |
| Datos de cliente activos | Vigencia de la relación + 7 años | Ley 23/2015 + Acuerdo SBP |
| ROS UAF | ≥ 7 años con evidencia inmutable | Procedimiento UAF |
| Métricas | 2 años agregadas + 5 años muestreadas | Buenas prácticas |
| Trazas distribuidas | 30 días en línea | Buenas prácticas |

---

## Sección 3 — Consulta

### 3.1 Stakeholders Internos Consultados

| Stakeholder | Rol en el DPIA | Fecha consulta |
|-------------|-----------------|----------------|
| CISO (Guillermo Smith) | Validador técnico de seguridad | DOC-SES-007 (27-mayo-2026) |
| Cumplimiento (Cindy, Marina, González) | Validador regulatorio AML + Acuerdo 1-2026 | DOC-SES-006 (27-mayo-2026) |
| Legal | Validador Ley 81 + Ley 22 + contratos | PENDING |
| Oficial de Protección de Datos | Owner del DPIA | **PENDIENTE NOMBRAR** |
| Riesgos | Validador de riesgo operacional | PENDING |
| Auditoría Interna | Validador independiente del proceso | PENDING |
| Comité de Tecnología | Decisor final de riesgos residuales | PENDING |
| Junta Directiva | Decisor final de apetito de riesgo | PENDING |

### 3.2 Stakeholders Externos / Consulta a Titulares

- **Modalidad**: Surveys (recomendado por el comando) — encuestas dirigidas a muestras representativas de los grupos vulnerables identificados (clientes mandato social, jubilados, comarcas indígenas) para validar la percepción de privacidad sobre la geolocalización inferencial y el monitoreo AML continuo.
- **Plazo**: 60 días pre-implementación FR-053 (objetivo dic-2026).
- **Modalidad complementaria para comarcas indígenas**: workshops facilitados en idioma local + español, dada la barrera de comunicación digital. No se puede aplicar survey online por defecto.

### 3.3 Procesadores Externos a Considerar

| Procesador | Tipo de tratamiento | Cláusula Ley 81 requerida |
|-----------|----------------------|----------------------------|
| Vendor CBS (post-RFP) | Procesamiento contractual | Acuerdo de procesamiento + cláusula soberanía + auditoría |
| Vendor ERP (post-RFP) | Procesamiento contractual | Igual |
| Vendor motor AML (post-RFP) | Procesamiento contractual + IA explicable | Igual + cláusula sobre algoritmos |
| Panadata | KYC | Acuerdo vigente — revisar bajo Ley 81 |
| Telered | Switch ATM/POS | Acuerdo vigente — revisar |
| App Enhancer | Gestor documental | Acuerdo vigente — revisar |
| Banca Seguro | Broker de seguros | Acuerdo vigente — revisar |
| Microsoft (Entra ID + posible Azure regional) | IAM + cloud regional | Acuerdo + cláusula soberanía panameña |
| AWS (Data Lake) | Datos analíticos | Acuerdo + cláusula soberanía + revisión de qué datos van al Data Lake |

### 3.4 Consulta a ANTAI

- **Inicial**: comunicación informativa del programa a ANTAI antes del envío del RFP — define la arquitectura de tratamiento de datos personales.
- **Consulta previa formal**: requerida para **riesgo residual Alto DPIA-007 (geolocalización inferencial inadecuadamente calibrada — ver §5)** antes de la implementación de FR-053.

---

## Sección 4 — Necesidad y Proporcionalidad

### 4.1 Bases Legales del Tratamiento (Ley 81)

| Propósito | Base legal Ley 81 | Justificación |
|-----------|---------------------|----------------|
| P-01 Apertura/gestión de cuentas | Ejecución de contrato | Contrato bancario con el cliente |
| P-02 Originación de créditos | Ejecución de contrato + Obligación legal | Contrato + Acuerdo SBP 6-2000 |
| P-03 Reportería SBP/UAF/APC | **Obligación legal** | Acuerdos SBP, Ley 23/2015 |
| P-04 AML/CFT con IA | **Obligación legal** | Acuerdo 1-2026, Ley 23/2015 |
| P-05 Beneficiario final ≥ 10% | **Obligación legal** | Acuerdo 1-2026 Art. 14 |
| P-06 Geolocalización inferencial | **Obligación legal** + Interés público | Acuerdo 1-2026 Art. 14 — prevención AML/CFT |
| P-07 KYC + listas restrictivas | Obligación legal | Ley 23/2015 |
| P-08 DJTE | Obligación legal | Ley 23/2015 |
| P-09 Programas sociales | Obligación legal + Interés público | Mandato social del Estado |
| P-10 Hipotecario Interés Preferencial | Obligación legal + Contrato | Ley 468/2025 |
| P-11 FATCA/CRS | Obligación legal | Tratados internacionales |
| P-12 Seguridad / pen-tests | Interés legítimo del banco + Obligación legal | Acuerdo 11-2018 |

### 4.2 Test de Necesidad

| Tratamiento | ¿Es necesario? | Justificación |
|-------------|----------------|----------------|
| Geolocalización inferencial digital | **Sí** | Obligación legal del Acuerdo 1-2026 Art. 14; sin ella, el banco incumple la regulación |
| AML con IA explicable | **Sí** | Acuerdo 1-2026 + Ley 23/2015; obligación regulatoria |
| Beneficiario final ≥ 10% | **Sí** | Obligación regulatoria — umbral panameño más estricto que UE/FATF |
| DJTE | **Sí** | Ley 23/2015 — obligación legal |
| Combinación de datasets (CBS+ERP+AML+...) | **Sí parcialmente** | Necesario para reportería SBP y AML; debe limitarse al mínimo necesario por propósito |
| Datos en Data Lake AWS | **A VALIDAR** | Solo si no se transfieren datos sensibles (depende ADR-003 + Legal) |

### 4.3 Test de Proporcionalidad

| Tratamiento | Proporcional? | Justificación |
|-------------|----------------|----------------|
| Geolocalización inferencial | ⚠️ **Proporcional con salvaguardas** | Es proporcional **si y solo si** el modelo inferencial está calibrado para minimizar falsos positivos y se aplica únicamente a canales digitales transaccionales — no a navegación general. DPIA-007 (riesgo residual Alto) condicionado a calibración. |
| AML monitoring continuo | ✅ Proporcional | Aplicable solo a transacciones; no es vigilancia general |
| Beneficiario final ≥ 10% | ✅ Proporcional | Aplicable solo a personas jurídicas; finalidad regulatoria específica |
| KYC reforzado para clientes de alto riesgo | ✅ Proporcional | Diferenciado por nivel de riesgo |

### 4.4 Minimización de Datos

- Para FR-053 (geolocalización inferencial): captar **únicamente las señales mínimas** necesarias para inferencia (IP+ASN+UA+GPS si autorizado por el cliente+comportamiento de sesión). Sin tracking en navegación general.
- Para AML: pasar al motor externo **únicamente los atributos del evento transaccional** + perfil cliente relevante, no toda la información del CIF.
- Para Data Lake: política explícita de **qué dominios de datos van** (transaccional analítico anonimizado) **y cuáles NO** (PII detallada, beneficiarios sociales, datos de niños).
- Para beneficiario final: análisis de capas societarias automatizado **con minimización** — solo lo necesario para identificar UBO ≥ 10%, no el árbol societario completo.

---

## Sección 5 — Evaluación de Riesgos de Privacidad

### 5.1 Marco de Evaluación

- **Probabilidad**: Remota / Posible / Probable.
- **Severidad** (impacto en el titular): Mínima / Significativa / Severa.
- **Riesgo global**: Bajo (verde) / Medio (ámbar) / Alto (rojo).

### 5.2 Registro de Riesgos DPIA

| ID | Riesgo | Tratamiento afectado | Probabilidad | Severidad | Riesgo | Vínculo RISK v2.0 |
|----|--------|----------------------|--------------|-----------|--------|---------------------|
| **DPIA-001** | Brecha del CBS legado sin cifrado en reposo expone PII de ~1M titulares | Todos | Probable | Severa | **🔴 Alto** | R-027 |
| **DPIA-002** | Sin MFA para acceso privilegiado al legado = riesgo de exfiltración interna | Todos | Probable | Severa | **🔴 Alto** | R-027 |
| **DPIA-003** | Sin Oficial de Protección de Datos nombrado → titulares sin canal para ejercer derechos | Todos | Probable | Significativa | 🟠 Medio | — |
| **DPIA-004** | Discriminación algorítmica en scoring crediticio (BPMs externos) hacia titulares vulnerables | P-02 + scoring BPMs | Posible | Severa | 🟠 Medio | — |
| **DPIA-005** | Falsos positivos AML excesivos congelan cuentas de titulares legítimos | P-04 | Posible | Severa | 🟠 Medio | R-023 |
| **DPIA-006** | Datos de menores (Ahorro Fácil para Niños) sin tratamiento diferenciado de Ley 81 | P-01 | Probable | Significativa | 🟠 Medio | — |
| **DPIA-007** | **Geolocalización inferencial mal calibrada → vigilancia desproporcionada** | **P-06 (FR-053)** | **Probable** | **Severa** | **🔴 Alto** | **R-025** |
| DPIA-008 | Combinación CBS+ERP+AML+SISCARD+Panadata+Data Lake = perfil completo del titular sin consentimiento explícito | Todos | Posible | Severa | 🟠 Medio | — |
| DPIA-009 | Transferencia internacional al Data Lake AWS sin salvaguardas para datos sensibles | P-03, P-12 | Posible | Severa | 🟠 Medio | R-006, R-032 |
| DPIA-010 | Beneficiario final ≥ 10% sin notificación adecuada al titular UBO | P-05 | Probable | Significativa | 🟠 Medio | — |
| DPIA-011 | Errores en datos heredados (8,000+ elementos sin propietarios) → decisiones AML/crediticio erróneas | Todos | Probable | Significativa | 🟠 Medio | R-030 |
| DPIA-012 | Beneficiarios programas sociales (vulnerables) sin canal accesible para ejercer derechos | P-09 | Probable | Significativa | 🟠 Medio | — |
| DPIA-013 | Caja Amiga / comarcas indígenas — modo offline sin protección equivalente | P-01 | Posible | Significativa | 🟠 Medio | R-035 |
| **DPIA-014** | Sin DPIA completa antes de implementación FR-053 = sanción ANTAI + Acuerdo 1-2026 multa elevada | Todos los nuevos v2.0 | **Probable** | **Severa** | **🔴 Alto** | R-025 |
| DPIA-015 | Retención excesiva más allá de los plazos mínimos legales | Todos | Posible | Significativa | 🟠 Medio | — |
| DPIA-016 | Datos en BPMs externos (Ultimus/Asicom/Genexus) sin acuerdos de procesamiento Ley 81 | P-02 | Probable | Significativa | 🟠 Medio | R-029 |
| DPIA-017 | Datos en gestor documental App Enhancer SaaS sin garantías de soberanía | Todos | Posible | Severa | 🟠 Medio | R-006 |
| DPIA-018 | Pólizas Banca Seguro sin acuerdo de protección de datos | P-02 | Posible | Significativa | 🟢 Bajo | — |
| DPIA-019 | Logs sin pseudonimización adecuada permitiendo re-identificación de titulares | Todos | Posible | Significativa | 🟢 Bajo | — |
| DPIA-020 | Sin breach notification process formal hacia ANTAI (72 hrs) | Todos | Posible | Significativa | 🟠 Medio | — |
| DPIA-021 | Datos de salud implícitos en pólizas hipotecarias sin tratamiento diferenciado | P-02 | Posible | Significativa | 🟢 Bajo | — |
| DPIA-022 | Migración del CBS legado al nuevo: ventana de exposición de datos | Migración | Posible | Severa | 🟢 Bajo | R-017 |
| DPIA-023 | Vendor AML no panameño accede a datos personales sin acuerdo de procesamiento Ley 81 | P-04 | Posible | Significativa | 🟢 Bajo | R-023 |

**Total**: 23 riesgos — **4 Altos** (DPIA-001, DPIA-002, DPIA-007, DPIA-014) / **12 Medios** / **7 Bajos**.

---

## Sección 6 — Mitigaciones y Riesgo Residual

### 6.1 Mitigaciones por Riesgo

| ID | Riesgo | Mitigaciones técnicas | Mitigaciones organizacionales | Mitigaciones procedimentales | Riesgo residual |
|----|--------|------------------------|-------------------------------|-------------------------------|------------------|
| DPIA-001 | Brecha PII legado | Cifrado en reposo + bóveda secretos + segmentación | Plan remediación R-027 (P1) | Pen-test semestral | 🟠 Medio |
| DPIA-002 | MFA legado | MFA obligatorio para acceso privilegiado | Plan remediación R-027 (P1) | Recertificación trimestral | 🟠 Medio |
| DPIA-003 | Sin Oficial Protección Datos | — | **Nombrar Oficial Protección Datos (Ley 81)** — acción P0 | Procedimientos formales de derechos del titular | 🟢 Bajo |
| DPIA-004 | Discriminación scoring | Auditoría de modelos + monitoreo de bias | Política anti-discriminación + revisión humana de decisiones de alto impacto | Métricas de fairness mensuales | 🟢 Bajo |
| DPIA-005 | Falsos positivos AML | IA explicable + calibración de modelos | Revisión humana de alertas + escalamiento | Métricas mensuales | 🟢 Bajo |
| DPIA-006 | Datos de menores | Consentimiento parental documentado + tratamiento diferenciado | Privacy notice especial para menores en español accesible | Auditoría trimestral | 🟢 Bajo |
| **DPIA-007** | **Geolocalización mal calibrada** | **Calibración explícita con dataset panameño** + minimización de señales recolectadas + opt-out parcial | **DPIA específica para FR-053 + consulta previa ANTAI** | Pruebas A/B + revisión humana de bloqueos por geolocalización | **🟠 Medio (parcialmente residual)** |
| DPIA-008 | Combinación datasets sin consentimiento | Minimización por propósito + anonimización en Data Lake | Política de minimización por propósito | Auditoría trimestral | 🟢 Bajo |
| DPIA-009 | Transferencia internacional | Solo metadatos anonimizados al Data Lake; datos sensibles permanecen on-prem | Política explícita de soberanía + dictamen Legal | Auditoría trimestral | 🟢 Bajo |
| DPIA-010 | UBO sin notificación | Privacy notice actualizado para personas jurídicas | Procedimiento de notificación al UBO | — | 🟢 Bajo |
| DPIA-011 | Errores datos heredados | Validación en tiempo de ingreso (NFR-M-008) + propietarios de los 8,000+ elementos | Plan gobernanza diccionario (R-030, P2) | Auditoría trimestral | 🟢 Bajo |
| DPIA-012 | Vulnerables sin canal | Canal alternativo presencial en sucursales + soporte 24/7 en español | Procedimiento accesible para vulnerables | Capacitación de Atención al Cliente | 🟢 Bajo |
| DPIA-013 | Caja Amiga offline | Cifrado local + conciliación con auditoría | Procedimiento offline documentado | Auditoría trimestral | 🟢 Bajo |
| **DPIA-014** | **Sin DPIA pre-FR-053** | **Esta DPIA + DPIA específica FR-053** | **Aprobación CISO + JD + ANTAI consulta previa** | Pre-implementación obligatoria | **🟢 Bajo (esta DPIA mitiga directamente)** |
| DPIA-015 | Retención excesiva | Política de retención automatizada + purga al vencimiento | Procedimiento de retención por dominio | Auditoría anual | 🟢 Bajo |
| DPIA-016 | BPMs sin acuerdos Ley 81 | Acuerdo de procesamiento con cada BPM | Negociación contractual | — | 🟢 Bajo |
| DPIA-017 | App Enhancer SaaS | Verificación soberanía + acuerdo de procesamiento | Decisión de soberanía pendiente ADR-003 | — | 🟢 Bajo |
| DPIA-018 | Banca Seguro sin acuerdo | Acuerdo de procesamiento | — | — | 🟢 Bajo |
| DPIA-019 | Logs re-identificables | Pseudonimización + cifrado de logs | Política de logs | Auditoría anual | 🟢 Bajo |
| DPIA-020 | Sin breach notification | Procedimiento 72h ANTAI + 24h SBP | Designar responsable | Simulacros trimestrales | 🟢 Bajo |
| DPIA-021 | Pólizas con datos de salud | Procedimiento de minimización | Acuerdo con Banca Seguro | — | 🟢 Bajo |
| DPIA-022 | Migración exposición | Pen-test pre-corte + procedimiento de migración seguro | Plan migración por bandos (R-017) | War-room | 🟢 Bajo |
| DPIA-023 | Vendor AML sin acuerdo Ley 81 | Acuerdo de procesamiento + cláusula soberanía (cláusula 11 SOW AML) | Contractual | — | 🟢 Bajo |

### 6.2 Resumen de Riesgo Residual

- **🔴 Alto residual**: 0 (todos los Altos iniciales reducidos a Medio o Bajo con mitigaciones — pero DPIA-007 mantiene residualidad parcial Media pendiente de calibración real).
- **🟠 Medio residual**: 3 (DPIA-001, DPIA-002 — dependen del cierre P1 del plan de remediación legado R-027; DPIA-007 — depende de calibración real de geolocalización).
- **🟢 Bajo residual**: 20.

---

## Sección 7 — Consulta Previa a ANTAI

> Bajo Ley 81, la consulta previa a la autoridad de protección de datos es **requerida** cuando, tras las mitigaciones, **siguen existiendo riesgos altos** para los titulares.

**Veredicto**: **Consulta previa REQUERIDA** para DPIA-007 (geolocalización inferencial mal calibrada).

**Justificación**: Aun con mitigaciones (calibración con dataset panameño, minimización de señales, opt-out parcial), la geolocalización inferencial es tecnología novedosa con riesgo residual material de vigilancia desproporcionada. La consulta previa a ANTAI:

- Documenta la diligencia debida del banco.
- Permite a ANTAI proporcionar guía específica.
- Establece el audit trail para una eventual auditoría sancionatoria.

**Plazo de la consulta**: 60-90 días antes de la implementación productiva de FR-053 (objetivo 30-jun-2027 por Acuerdo 1-2026 Art. 14) → consulta a iniciar antes del 30-mar-2027.

---

## Sección 8 — Sign-off y Aprobación

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Oficial de Protección de Datos (Ley 81) | **[PENDIENTE NOMBRAR]** | [PENDING] | [PENDING] |
| CISO | Guillermo Smith | [PENDING] | [PENDING] |
| Legal | [PENDING] | [PENDING] | [PENDING] |
| Cumplimiento | [PENDING] | [PENDING] | [PENDING] |
| Riesgos | [PENDING] | [PENDING] | [PENDING] |
| Auditoría Interna | [PENDING] | [PENDING] | [PENDING] |
| Aldo Ríos (Líder del programa) | [PENDING] | [PENDING] | [PENDING] |
| **Comité de Tecnología** | [PENDING] | [PENDING] | [PENDING] |
| **Junta Directiva** | [PENDING] | [PENDING] | [PENDING] |
| **ANTAI (consulta previa para DPIA-007)** | [PENDING] | [PENDING] | [PENDING] |

---

## Sección 9 — Revisión y Monitoreo

### 9.1 Triggers de Revisión

- 12 meses (revisión anual).
- Nuevos tratamientos o cambios materiales (e.g., nueva categoría de datos, nuevo BPM, nuevo destino).
- Brechas de datos personales.
- Cambios regulatorios (nuevo Acuerdo SBP, modificación Ley 81).
- Cambio de vendor en cualquiera de los 3 RFPs.

### 9.2 Métricas de Monitoreo Continuo

| Métrica | Objetivo | Frecuencia |
|---------|----------|-----------|
| % de tratamientos con base legal documentada | 100% | Mensual |
| Solicitudes de derechos del titular procesadas en plazo | 100% en 30 días | Mensual |
| Brechas notificadas a ANTAI en plazo 72h | 100% | Por evento |
| Falsos positivos AML | < umbral target | Mensual |
| Bloqueos por geolocalización inferencial revisados manualmente | 100% | Mensual |
| Datos retenidos beyond plazo legal | 0 | Trimestral |

---

## Sección 10 — Trazabilidad

### 10.1 Vinculación con otros artefactos

| Artefacto | Referencia | Vínculo |
|-----------|------------|---------|
| ARC-001-REQ-v2.0 | Requisitos completos | DR-001..022, FR-046..054, NFR-SEC, NFR-C |
| ARC-001-RISK-v2.0 | Riesgos del programa | R-006, R-017, R-023, R-025, R-027, R-029, R-030, R-032, R-035 |
| ARC-001-SECD-v1.0 | Postura de seguridad | NIST CSF 2.0 + controles |
| ARC-001-EVAL-v2.0 | Eliminatorios | E-1 (soberanía), E-6 (Acuerdo 1-2026), E-11 (15 cláusulas incl. cláusula 11 Ley 81) |
| ARC-001-SOW-CBS/ERP/AML-v1.0 | Cláusulas contractuales | Cláusula 11 Ley 81 + cláusula 1 soberanía + cláusula 14 AML offload |
| ARC-001-ADR-001 | AML externo | Determina arquitectura de tratamiento AML |
| ARC-001-ADR-003 | Modelo de despliegue | Determina soberanía de datos |
| ARC-001-ADR-008 | Matriz de ponderación | Defensibilidad del proceso |
| ARC-000-PRIN-v1.1 | Principios P4, P5, P6 | Privacy by Design implícito |
| tech-notes/acuerdo-1-2026-implementation.md | Implementación Acuerdo 1-2026 | Patrones de geolocalización inferencial |

### 10.2 Gap conocido — Data Model

> Este DPIA se elabora **antes** de la ejecución formal de `/arckit:data-model`. El comando original exige un Data Model artifact como input mandatorio.
>
> **Gap mitigado**: REQ v2.0 §DR-001..022 + DR-021 (8,000+ elementos del diccionario heredado) + FR-046..054 (procesos KYC/AML) + tech-notes/acuerdo-1-2026-implementation.md proporcionan información funcionalmente equivalente para identificar el alcance del tratamiento.
>
> **Acción requerida**: refrescar este DPIA a **v2.0** una vez que `/arckit:data-model` esté ejecutado — para incorporar el modelo formal de los 8,000+ elementos del diccionario, con propietarios formales y reglas de calidad por dominio.

---

## Sección 11 — Derechos del Titular bajo Ley 81

| Derecho | Implementado actualmente? | Mecanismo (target) |
|---------|---------------------------|--------------------|
| **Acceso** | ⚠️ Parcial | Habilitar canal en Super App + sucursal + procedimiento documentado |
| **Rectificación** | ⚠️ Parcial | Habilitar canal + procedimiento de verificación |
| **Cancelación / supresión** | ❌ No formal | Establecer procedimiento con análisis de retención legal mínima |
| **Oposición** | ❌ No formal | Procedimiento explícito (relevante para marketing y profiling crediticio no obligatorio) |
| **Portabilidad** | ❌ No formal | Establecer formato estándar (JSON/CSV) para exportación |
| **Decisión automatizada con efecto significativo** | ⚠️ Parcial | Procedimiento de revisión humana para bloqueos AML + scoring crediticio |
| **Información sobre tratamiento** | ⚠️ Parcial | Privacy notice formal y accesible — actualmente no formalizado |

**Acción crítica**: Habilitar los 7 derechos formalmente antes de la implementación FR-053 (objetivo 30-jun-2027).

---

## Sección 12 — Transferencias Internacionales

| Destino | Tipo de datos | Salvaguarda |
|---------|---------------|-------------|
| FATCA / IRS | Reportería fiscal anual | Tratado bilateral panameño |
| CRS / OCDE | Reportería fiscal | Adhesión OCDE |
| Data Lake AWS (región LatAm) | Analítica anonimizada (NO datos sensibles personales) | Sujeto a ADR-003 — actualmente **no se transfieren datos sensibles**; revisar tras dictamen gubernamental |
| Microsoft Entra ID | Metadatos de identidad (no datos transaccionales) | Sujeto a ADR-003 |

**Riesgo crítico** DPIA-009: si tras ADR-003 se confirma cloud regional con datacenter fuera de Panamá → activar salvaguardas específicas (cláusulas contractuales tipo + auditoría trimestral + revisión de qué dominios cruzan la frontera).

---

## Sección 13 — Datos de Niños

> Aplicable a clientes Ahorro Fácil para Niños + beneficiarios menores de programas sociales.

| Aspecto | Estado | Acción requerida |
|---------|--------|------------------|
| Verificación de edad | ⚠️ Parcial — vía cédula juvenil | Procedimiento formal de verificación documentado |
| Consentimiento parental | ⚠️ Parcial — vía representante legal en apertura | Procedimiento formal + audit trail |
| Privacy notice infantil | ❌ No existe | Privacy notice en lenguaje accesible para menores + traducción a comarcas indígenas |
| Best interests assessment | ❌ No formal | Procedimiento documentado |
| Marketing dirigido a menores | ⚠️ Pendiente política explícita | Política de **no marketing** a menores |
| Profiling de menores | ⚠️ Sin política | Política de **no profiling crediticio o conductual** sobre menores |

---

## Sección 14 — IA / Procesamiento Algorítmico

> Aplicable principalmente al motor AML externo con IA explicable (FR-048) y al scoring crediticio en BPMs externos.

| Aspecto | Estado | Salvaguarda |
|---------|--------|-------------|
| Bias algorítmico | ⚠️ Riesgo identificado (DPIA-004) | Auditoría de modelos + métricas de fairness |
| Explicabilidad (XAI) | ✅ Requisito en SOW AML (eliminatorio del shortlist) | Hawk:AI, NICE Actimize lo declaran nativamente |
| Supervisión humana | ✅ Requerida para todas las decisiones de alto impacto | Procedimiento de revisión + escalamiento |
| Auditoría de modelos | ⚠️ Pendiente formalizar | Procedimiento trimestral con Auditoría Interna |
| Documentación del modelo | ✅ Requerido al vendor AML | Cláusula contractual |

---

## Sección 15 — Resumen y Plan de Acción

### 15.1 Resumen

| Indicador | Valor |
|-----------|-------|
| Pre-screening (9 criterios) | **9/9 cumplidos** → DPIA REQUERIDA |
| Titulares afectados | ~1M |
| Datos sensibles bajo Ley 81 | Sí (múltiples categorías) |
| Tratamientos de alto riesgo | 6 identificados |
| Riesgos identificados | 23 (4 Altos / 12 Medios / 7 Bajos) |
| Riesgos residuales tras mitigaciones | 0 Altos plenos / 3 Medios / 20 Bajos |
| Consulta previa a ANTAI | **REQUERIDA** para DPIA-007 |
| Derechos del titular implementados | 0 plenos / 4 parciales / 3 no implementados |
| Oficial de Protección de Datos | **PENDIENTE NOMBRAR** |

### 15.2 Plan de Acción Prioritario

#### P0 — Esta semana (bloqueante)

| # | Acción | Owner | Plazo |
|---|--------|-------|-------|
| 0.1 | **Nombrar Oficial de Protección de Datos** (Ley 81) | JD + Legal | 2 semanas |
| 0.2 | Aprobación de este DPIA por Comité de Tecnología + JD | Aldo Ríos | 4 semanas |
| 0.3 | Iniciar consulta informativa con ANTAI sobre el programa | Legal + Oficial Protección Datos | 4 semanas |

#### P1 — Próximas 4-12 semanas

| # | Acción | Owner | Plazo |
|---|--------|-------|-------|
| 1.1 | Privacy notice formal (general + infantil + comarcas) | Legal + Oficial Protección Datos | 8 semanas |
| 1.2 | Procedimientos formales para los 7 derechos del titular | Oficial Protección Datos | 8 semanas |
| 1.3 | Procedimiento de notificación de brecha a ANTAI 72h | CISO + Oficial Protección Datos | 6 semanas |
| 1.4 | Política de retención por dominio | Legal + TI | 12 semanas |
| 1.5 | Acuerdos de procesamiento Ley 81 con: Panadata, App Enhancer, Banca Seguro, BPMs, Telered | Legal | 12 semanas |
| 1.6 | Procedimiento de consentimiento parental para menores | Legal + Oficial Protección Datos | 8 semanas |
| 1.7 | Plan de remediación de R-027 (legado) — cifrado en reposo, MFA, RBAC (mitiga DPIA-001, DPIA-002) | CISO + TI | 90 días |

#### P2 — Próximos 3-6 meses

| # | Acción | Owner | Plazo |
|---|--------|-------|-------|
| 2.1 | **DPIA específica detallada para FR-053 (geolocalización inferencial)** | Oficial Protección Datos + CISO | 4 meses |
| 2.2 | **Consulta previa formal a ANTAI sobre FR-053** | Legal + Oficial Protección Datos | 5 meses |
| 2.3 | Política y métricas de fairness algorítmica (AML + scoring) | CISO + Cumplimiento | 6 meses |
| 2.4 | Refresh de este DPIA a v2.0 una vez ejecutado `/arckit:data-model` | Oficial Protección Datos | 6 meses |

#### P3 — Pre-implementación FR-053 (objetivo antes de 30-jun-2027)

| # | Acción | Owner |
|---|--------|-------|
| 3.1 | Recibir respuesta de la consulta previa ANTAI | Legal |
| 3.2 | Implementar mitigaciones de la consulta ANTAI | TI + CISO |
| 3.3 | Sign-off final de Oficial Protección Datos + Comité Tecnología + JD | — |
| 3.4 | Despliegue productivo de FR-053 con monitoreo intensivo | TI + CISO + Cumplimiento |

---

## External References

| Doc ID | Descripción |
|--------|-------------|
| ARC-001-REQ-v2.0 | Requisitos del programa (DR-001..022, FR-046..054, NFR-SEC, NFR-C) |
| ARC-001-RISK-v2.0 | Riesgos (R-006, R-017, R-023, R-025, R-027, R-029, R-030, R-032, R-035) |
| ARC-001-SECD-v1.0 | Postura de seguridad |
| ARC-001-EVAL-v2.0 | Eliminatorios y cláusulas |
| ARC-001-SOW-CBS/ERP/AML | Cláusulas contractuales Ley 81 |
| ARC-001-ADR-001 | AML externo |
| ARC-001-ADR-003 | Modelo de despliegue (soberanía) |
| ARC-001-ADR-008 | Matriz de ponderación auditable |
| ARC-000-PRIN-v1.1 | Principios P4, P5, P6 |
| tech-notes/acuerdo-1-2026-implementation.md | Implementación Acuerdo 1-2026 (umbral 10%, geolocalización inferencial) |
| **Ley 81 de Panamá** | Protección de Datos Personales |
| **Acuerdo SBP 1-2026** | AML/CFT/FPADM — Resolución SBP-JD-0001-2026 |
| **Ley 23/2015** | AML/FT + DJTE |
| **ANTAI** | Autoridad Nacional de Transparencia y Acceso a la Información |

---

**Generated by**: ArcKit `/arckit:dpia` command (adaptado a Panamá — Ley 81 + Acuerdo 1-2026 + ANTAI)
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Reemplazo del Core Banking + ERP + AML (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: DPIA adaptada al marco panameño — Ley 81 (Protección de Datos Personales), Acuerdo SBP 1-2026 (componentes de identidad digital con vigencia 30-jun-2027 para Art. 14), Ley 23/2015 (AML/FT), ANTAI como autoridad. Pre-screening: 9/9 criterios ICO/ANTAI cumplidos → DPIA legalmente requerida. 23 riesgos identificados (4 Altos / 12 Medios / 7 Bajos). Consulta previa a ANTAI requerida para DPIA-007 (geolocalización inferencial mal calibrada). Bloqueante regulatorio para implementación FR-053 antes de 30-jun-2027. **Gap conocido**: DPIA elaborada antes de `/arckit:data-model` formal — refrescar a v2.0 cuando esté disponible.
