# Marco de Evaluación de Vendors — Caja de Ahorros de Panamá (CBS + ERP + AML)

> **Origen de la plantilla**: Oficial | **Versión ArcKit**: 5.13.0 | **Comando**: `/arckit:evaluate`

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-EVAL-v2.0 |
| **Document Type** | Vendor Evaluation Framework (multi-track CBS + ERP + AML) |
| **Project** | Caja de Ahorros — Evaluación y Selección de Core Banking (Project 001) |
| **Classification** | OFFICIAL-SENSITIVE (CONFIDENCIAL – Uso interno) |
| **Status** | DRAFT |
| **Version** | 2.0 |
| **Created Date** | 2026-05-19 (v1.0) |
| **Last Modified** | 2026-06-11 (v2.0) |
| **Review Cycle** | Antes de cada gate del RFP; mensual durante la fase de evaluación de ofertas |
| **Next Review Date** | 2026-07-11 |
| **Owner** | Aldo Ríos — Gerencia de Innovación / Líder de Programa |
| **Reviewed By** | PENDING — Auditoría Interna (validación auditable de criterios y pesos), Legal, Cumplimiento, Finanzas, CISO |
| **Approved By** | PENDING — Comité de Tecnología (criterios y pesos), Junta Directiva (apertura del RFP) |
| **Distribution** | Junta Directiva, Gerencia General, Comité de Tecnología, Comité de Evaluación, PMO, Auditoría Interna, Contraloría (información), vendors invitados (bajo NDA) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-05-19 | ArcKit AI | Creación inicial — 12 criterios eliminatorios + 6 categorías ponderadas (Encaje Funcional 30, Arquitectura Técnica 20, Cumplimiento Regulatorio 15, Referencias 10, Presencia Regional 10, Propuesta Comercial 15). Aplicable solo a CBS. Trazabilidad criterios → drivers → BR → riesgos. | PENDING | PENDING |
| 2.0 (addendum) | 2026-06-11 (PM) | ArcKit AI | **Addendum post-revisión** — al detectarse durante revisión de la carpeta de vendor profiles que **10X Banking** y **TUUM** estaban ausentes sin memo justificativo (gap en mitigación R-026), se añaden los descartes formales en la sección IV.3 §"Vendors CBS no invitados" con razón objetiva basada en E-7 + E-8 (10X) y E-7 + E-8 + E-10 marginal (TUUM). Profiles creados: `vendors/10x-banking-profile.md` y `vendors/tuum-profile.md`. Actualización paralela aplicada a `ARC-001-SOW-CBS-v1.0.md` §Apéndice B. Sin cambios al conteo de eliminatorios, ponderación ni shortlist invitado. | PENDING | PENDING |
| 2.0 | 2026-06-11 | ArcKit AI | **Major refresh** — el programa ya no es un único RFP CBS sino **tres procesos coordinados** (CBS + ERP + AML) tras la decisión arquitectónica de v2.0 (BR-013 ERP separado, FR-048 AML externo). Cambios materiales: (a) **multi-track framework** — un único Marco con **tres matrices de ponderación** (una por categoría) y un único Comité de Evaluación con sub-paneles; (b) **3 eliminatorios nuevos**: E-13 (capacidad de integración con ERP externo — aplica a CBS), E-14 (capacidad de offload AML transaccional bidireccional — aplica a CBS), E-15 (deliverable Acuerdo 1-2026 Art. 14 — beneficiario final ≥ 10% + geolocalización inferencial — antes de 30-jun-2027); (c) **E-6 reemplazado**: pasa de Acuerdo 11-2018 (ciberseguridad) a **Acuerdo SBP 1-2026** (AML/CFT/FPADM) por ser el regulatorio más reciente con plazos discretos (Art. 25 §1 vigencia 31-ene-2027; Art. 14 vigencia 30-jun-2027) y ser específicamente requerido por REQ v2.0 (BR-002, FR-052, FR-053); (d) **E-11 ampliado**: las 12 cláusulas contractuales obligatorias se amplían a 15 — añade cláusula de integración con ERP externo, cláusula de exposición de eventos al motor AML externo y cláusula de coordinación de los tres RFPs; (e) **ponderaciones diferenciadas por categoría**: CBS preserva las 6 categorías v1.0 con pesos refinados; ERP introduce ponderación distinta (Encaje Funcional Contable 30, Arquitectura/Integración 25, Cumplimiento NIIF+IAS 15, Referencias Banca 10, Cloud/Localización 10, Propuesta Comercial 10); AML introduce ponderación distinta (Encaje Funcional AML 30, IA/Tiempo Real/APIs 25, Cumplimiento 1-2026 + UAF 15, Referencias LatAm 10, Despliegue/Integración 10, Propuesta Comercial 10); (f) **mitigación explícita de R-026** (sesgo COBIS / impugnación Contraloría): cada criterio ponderado tiene una **definición operativa auditable** (tabla de niveles 0-5 con evidencia requerida), el peso de cada criterio se justifica con BR/NFR específico y la **matriz de ponderación se valida formalmente por Auditoría Interna antes del envío del RFP**; (g) **preferencias y descartes del banco** (COBIS preferido; Temenos/Finacle/Mambu/SAP descartados — DOC-SES-009 §3.4, §10.4) son **insumo informativo** de la ponderación pero **NO se traducen en criterios eliminatorios**; las decisiones de invitación al RFP se documentan formalmente para cada vendor — incluyendo los descartados — para sostener el proceso ante Contraloría; (h) **shortlist objetiva por categoría** integrada desde ARC-001-RSCH-v2.0: CBS — Finacle, Temenos, Cobis Topaz, Datapro (incumbente como benchmark) + wildcards Oracle FLEXCUBE, Bantotal; ERP — Oracle Fusion, MS Dynamics 365 F&O, SAP S/4HANA, Infor + wildcard NetSuite; AML — NICE Actimize, Hawk:AI, Oracle FCCM + wildcards ComplyAdvantage, Featurespace; (i) **proceso multi-track coordinado**: tres RFPs paralelos con un mismo Steering Committee y un mismo cronograma de gates; (j) actualización del Apéndice A (trazabilidad) con los **15 eliminatorios** (era 12) y los **6 criterios ponderados ahora replicados por las 3 categorías** = 18 criterios totales. Nuevas citas: ARC-001-REQ-v2.0 (193 reqs), ARC-001-RISK-v2.0 (37 riesgos), ARC-001-RSCH-v2.0 (3 categorías), DOC-SES-001..009, DOC-RFI-001, DOC-POC-001, tech-notes/acuerdo-1-2026-implementation.md. | PENDING | PENDING |

---

## Resumen Ejecutivo

### Diseño del Framework

Este Marco de Evaluación organiza la selección de proveedores en **tres procesos coordinados** (tres RFPs paralelos) bajo un único Steering Committee y un único Comité de Evaluación con sub-paneles:

| RFP | Categoría | Por qué separado | Eliminatorios comunes / específicos |
|-----|-----------|------------------|--------------------------------------|
| **RFP CBS** | Core Banking System | El reemplazo del Core es el eje del programa | E-1..E-15 (todos los 15 aplican; E-13 + E-14 son específicos CBS) |
| **RFP ERP** | ERP externo para GL consolidado | El CBS no incluirá GL completo (BR-013) | E-1, E-3, E-4, E-5, E-9, E-10, E-11, E-12, E-15 (9 eliminatorios) |
| **RFP AML** | Motor AML externo con IA y APIs en tiempo real | AML extracted del CBS (FR-048 revisado) | E-1, E-5, E-6, E-9, E-10, E-11, E-12, E-15 (8 eliminatorios) |

### Distribución de Pesos (Parte II) — diferenciada por categoría

**CBS** (100 pts, preserva v1.0 con peso refinado):

- Encaje Funcional (FR/BR REQ v2.0): **30**
- Arquitectura Técnica & Integración: **20**
- Cumplimiento Regulatorio (SBP + Acuerdo 1-2026 + NIIF): **15**
- Referencias y Casos de Éxito (LatAm + banca pública): **10**
- Presencia Regional y Soporte (español 24/7): **10**
- Propuesta Comercial (TCO 7 años, ±10%): **15**

**ERP** (100 pts, ponderación específica para GL contable):

- Encaje Funcional Contable (Plan SBP, GL, doble contabilidad NIIF + reg): **30**
- Arquitectura/Integración (API CBS + AML + Data Lake): **25**
- Cumplimiento NIIF 9 + 16 + IAS 21 + SBP: **15**
- Referencias Banca (LatAm preferible): **10**
- Cloud/Localización (Azure pref / soberanía): **10**
- Propuesta Comercial (TCO 7 años): **10**

**AML** (100 pts, ponderación específica para IA y tiempo real):

- Encaje Funcional AML (FR-048..FR-054): **30**
- IA / Tiempo Real / APIs (latencia < 200ms, bloqueo bidireccional, IA explicable): **25**
- Cumplimiento Acuerdo 1-2026 + UAF + KYC (10% beneficiario final, geolocalización inferencial): **15**
- Referencias LatAm (banca pública preferible): **10**
- Despliegue/Integración (cloud + on-prem + APIs + Panadata): **10**
- Propuesta Comercial (TCO 7 años): **10**

### Umbrales de Decisión

- **Aprobar para PoC**: ≥ 70/100 en su categoría Y todos los eliminatorios verdes.
- **Apto wildcard**: 65-69/100 con plan de mitigación documentado para gaps Acuerdo 1-2026.
- **Rechazado**: < 65/100 O cualquier eliminatorio rojo.
- **Empate técnico**: dos vendors dentro de ±3 puntos → desempate por (1) Cumplimiento Regulatorio, (2) Referencias en banca pública, (3) TCO.

### Trazabilidad

Cada criterio se vincula a: stakeholder driver (STKE), Business Requirement (REQ v2.0), riesgo (RISK v2.0), y principio (PRIN v1.1). Apéndice A contiene la matriz completa de 15 eliminatorios + 18 criterios ponderados (6 por categoría × 3 categorías) cruzada contra estos artefactos.

### Mitigación R-026 (sesgo COBIS / impugnación Contraloría)

Este es el cambio más importante v2.0. Para sostener el proceso ante Contraloría:

1. **Definición operativa auditable**: cada criterio ponderado tiene una tabla de niveles 0-5 con evidencia requerida (no juicio subjetivo).
2. **Justificación de peso**: cada peso de criterio cita el BR/NFR/PRIN que lo justifica.
3. **Validación previa por Auditoría Interna**: el Comité de Evaluación firma los criterios y pesos **antes** de invitar a los vendors.
4. **Apertura inclusiva**: TODOS los vendors objetivamente aptos son invitados al RFP, incluyendo Temenos, Finacle, SAP y otros descartados verbalmente en sesiones. Los descartes documentados se hacen sólo por incumplir eliminatorios objetivos.
5. **Decisión registrada por vendor**: cada decisión de invitar/no invitar tiene un memo documentado con la razón objetiva, almacenado en el audit trail.
6. **Dictamen Legal previo**: Legal valida el proceso de evaluación antes de envío de RFP (acción P0.3 de RISK v2.0).

---

## Parte I — Criterios Eliminatorios (Pass/Fail)

> Aplican según la matriz de categorías (Resumen Ejecutivo). Un fallo en cualquiera de los eliminatorios aplicables descalifica al vendor del RFP correspondiente.

### E-1: Soberanía de Datos en Territorio Panameño

**Aplica a**: CBS + ERP + AML.

**Requerimiento**: el vendor presenta un modelo de despliegue verificable donde los datos personales, financieros y transaccionales residen en territorio panameño durante todo el ciclo de vida (procesamiento, almacenamiento, respaldo, archivo). Aceptables: on-premise CAP, colocation panameño certificado SBP, cloud regional con presencia física en Panamá. NO aceptable: cloud público internacional sin garantía contractual de residencia local con auditabilidad.

**Evidencia requerida**: arquitectura de despliegue propuesta + cláusula contractual de residencia + acuerdo de auditoría trimestral + dictamen del vendor sobre cumplimiento Ley 23/2015 (DJTE) y restricciones panameñas de exportación de datos.

**Vinculación**: BR-006, DR-013, R-006, R-018, PRIN P6.

### E-2: Productos del Mandato Social Parametrizables (NO Codificados)

**Aplica a**: CBS.

**Requerimiento**: el vendor demuestra en demo que los productos del mandato social — Interés Preferencial (Ley 468/2025), FGA, Profimype, "Una Cuenta Para Todos", transferencias sociales (Beca Universal, 120 a los 65, Red de Oportunidades), créditos verdes, Caja Amiga — se configuran mediante **parametrización por usuario de negocio**, sin código del vendor ni desarrollo a medida.

**Evidencia**: demo en vivo creando un producto Interés Preferencial nuevo desde cero en < 60 minutos con un usuario de negocio (no de TI). Cálculo automático del subsidio DGI (FR-019) demostrado contra valores de referencia del banco con diferencia = 0.

**Vinculación**: BR-004, FR-007, FR-014, FR-017, FR-019, R-005, PRIN P20.

### E-3: Modelo Dual NIIF 9 ECL + Acuerdo SBP 6-2000 Nativo

**Aplica a**: CBS + ERP.

**Requerimiento**: ejecución mensual automatizada simultánea de NIIF 9 ECL (3 stages, PD/LGD/EAD parametrizables) y Acuerdo 6-2000 (clasificación A–E, provisiones 1/5/25/50/100%); registro del mayor en P&L, diferencia como reserva regulatoria en patrimonio (sin pasar por resultados) [DOC-CB-003-C17]. Umbral SICR parametrizable. Contagio inter-crédito (FR-031) integrado con APC.

**Evidencia**: demo con dataset proporcionado por CAP (≥ 100 créditos con perfiles diversos). Resultado debe ser replicable y conciliable contra cálculo legado con diferencia < 0.5% material.

**Vinculación**: BR-005, FR-064, FR-065, FR-066, FR-031, R-003, R-005, PRIN P8.

### E-4: Reportería SBP Nativa (SEI + Inventario D04)

**Aplica a**: CBS + ERP (compartido — ERP genera reportes contables consolidados).

**Requerimiento**: generación nativa del 100% del inventario D04 [DOC-CB-001-C12] en XML válido contra los esquemas XSD vigentes del SEI. Workflow Preparador/Revisor/Firmante con firma digital reconocida en Panamá. Pre-validación local que reproduce las 3 capas del SEI (estructura, aritmética, consistencia histórica) [DOC-CB-003-C26]. Plan de cuentas SBP cargado sin modificación de códigos.

**Evidencia**: demostración de generación end-to-end del balance mensual y de la posición de liquidez diaria contra los XSD oficiales SBP. Almacenamiento del número de radicación devuelto por el SEI [DOC-CB-003-C27].

**Vinculación**: BR-002, FR-055, FR-056, FR-057, FR-058, FR-061, R-015, PRIN P5, P7.

### E-5: Soporte 24/7 en Español con SLA Medible

**Aplica a**: CBS + ERP + AML.

**Requerimiento**: soporte L1/L2/L3 24/7/365 en español con personal hispanohablante. SLA contractual: incidentes P1 respuesta ≤ 30 min, resolución ≤ 4 h; P2 respuesta ≤ 2 h, resolución ≤ 24 h; P3 ≤ 8 h / 5 días hábiles. Penalizaciones contractuales por incumplimiento documentadas.

**Evidencia**: contrato con cláusula explícita; equipo nombrado en la propuesta; oficina regional con horario panameño cubierto.

**Vinculación**: BR-009, NFR-U-001..003, R-001, R-020, PRIN P21.

### E-6 (REV v2.0): Cumplimiento Acuerdo SBP 1-2026 (AML/CFT/FPADM)

**Aplica a**: CBS + AML.

**Requerimiento**: el vendor demuestra capacidades nativas o vía hoja de ruta firmada (con cláusula penal) para:

1. **Beneficiario final ≥ 10%** (FR-052) — umbral panameño más estricto que el 25% UE/FATF — con análisis de capas societarias automatizable.
2. **Geolocalización inferencial** (FR-053) — combinando múltiples señales (IP+ASN, dispositivo/UA, GPS si disponible, comportamiento de sesión) para inferir ubicación real.
3. **Risk-based KYC** con niveles de debida diligencia escalables.
4. **Workflow de ROS a UAF** automatizable.

**Plazos eliminatorios temporales** (Resolución SBP-JD-0001-2026 del 16-ene-2026): Art. 25 §1 vigencia **31-ene-2027**; Art. 14 vigencia **30-jun-2027**. Cualquier vendor cuyo cronograma propuesto no entregue capacidades Art. 14 antes del 30-jun-2027 queda eliminado del RFP.

**Evidencia**: hoja de ruta con hitos antes de 30-jun-2027 + cláusula penal por incumplimiento + demo de capa de capas societarias + demo de geolocalización inferencial.

**Vinculación**: BR-002, FR-052, FR-053, NFR-C-001, R-007, R-025, PRIN P5, P7.

### E-7: Integración con Ecosistema de Pagos Panameño Demostrada

**Aplica a**: CBS.

**Requerimiento**: integración demostrada con Yappy (FR-034 / INT-001), ACH Panamá (FR-035 / INT-002), Telered (FR-036 / INT-003), SWIFT vía SCONNECT LAU/CSV (FR-038 / INT-004) y APC (FR-062 / INT-010, INT-020). Para vendors sin integraciones panameñas ya operativas, presentar caso de implementación equivalente en LatAm con vista de gobierno de integración.

**Evidencia**: lista de clientes panameños con estas integraciones operativas, O carta de intención de los partners de integración (Yappy, Telered, ACH) que confirme apertura de proceso de homologación.

**Vinculación**: BR-001, BR-010, FR-034..038, R-013, PRIN P2, P11.

### E-8: Mínimo 3 Referencias LatAm Verificables en Producción ≥ 24 Meses

**Aplica a**: CBS + ERP + AML.

**Requerimiento**: al menos 3 clientes en producción en LatAm (preferible Centroamérica/Caribe) en operación continua ≥ 24 meses, con la solución comparable a la propuesta para CAP. Para ERP y AML el horizonte mínimo es 12 meses dado que las categorías son más recientes en el banco. Acceso a llamada de referencia con cada cliente durante la fase de evaluación.

**Evidencia**: tres referencias por categoría con nombre del banco, contacto, fecha de go-live, alcance.

**Vinculación**: BR-001, BR-007, NFR-C-004.

### E-9: Certificaciones Obligatorias Vigentes

**Aplica a**: CBS + ERP + AML.

**Requerimiento**: ISO 27001 (vigente, alcance que cubra la solución ofertada al banco); ISO 27017 (cloud) si la oferta incluye cloud; SOC 2 Tipo II reciente para servicios cloud; PCI-DSS si maneja datos de tarjeta.

**Evidencia**: certificados con fecha y alcance; reporte SOC 2 más reciente bajo NDA.

**Vinculación**: NFR-C-004, NFR-SEC-001..010.

### E-10: Estabilidad Financiera y Continuidad del Vendor

**Aplica a**: CBS + ERP + AML.

**Requerimiento**: estados financieros auditados de los últimos 3 años; ingresos anuales globales ≥ USD 100M (CBS / ERP / AML enterprise) o ≥ USD 30M para AML AI-native challengers; plan de continuidad si el vendor cambia de manos.

**Evidencia**: documentación financiera auditada + cláusula de continuidad en el contrato.

**Vinculación**: BR-003, R-008.

### E-11 (REV v2.0): Aceptación de las 15 Cláusulas Contractuales Obligatorias

**Aplica a**: CBS + ERP + AML.

**Requerimiento**: el vendor acepta sin reservas las siguientes 15 cláusulas obligatorias (12 de v1.0 + 3 nuevas v2.0):

1. Residencia de datos en Panamá (BR-006).
2. SLA con penalizaciones (E-5).
3. TCO con tope a true-ups y a incrementos por inflación (BR-003).
4. Cumplimiento regulatorio continuo (NFR-C-010): el vendor adapta el producto a nuevos Acuerdos SBP sin cobros extraordinarios.
5. Auditabilidad por Contraloría (NFR-C-008).
6. Soporte transicional con incumbente durante migración.
7. Capacitación en español certificada.
8. Documentación funcional y técnica en español.
9. Salida ordenada — portabilidad de datos en formatos estándar al término del contrato.
10. Penalización por incumplimiento de plazos críticos (Acuerdo 1-2026).
11. Confidencialidad y manejo de datos personales (Ley 81 de Protección de Datos Personales de Panamá).
12. Cláusula anticorrupción y de cumplimiento de Ley 22.
13. **(NUEVA v2.0)** Para CBS: cláusula de **integración con ERP externo** con SLA específico para los asientos contables expuestos al ERP (latencia ≤ 5 min, idempotencia, conciliación automática).
14. **(NUEVA v2.0)** Para CBS: cláusula de **exposición de eventos al motor AML externo** con streaming < 200 ms y soporte para bloqueo bidireccional bajo instrucción del motor AML.
15. **(NUEVA v2.0)** Para los tres: cláusula de **coordinación inter-RFP** — el vendor seleccionado se compromete a coordinar su cronograma e implementación con los vendors de las otras dos categorías y participa en las sesiones de integración trimestrales.

**Evidencia**: aceptación firmada de las 15 cláusulas en la propuesta. Cualquier reserva material descalifica.

**Vinculación**: todos los BR, R-008, R-011, R-024, R-023, R-007.

### E-12: Idoneidad Jurídica Bajo Ley 22

**Aplica a**: CBS + ERP + AML.

**Requerimiento**: el vendor cumple los requisitos de contratación pública de Panamá (Ley 22 de Contrataciones Públicas): no estar inhabilitado, presentar declaración jurada de cumplimiento, paz y salvo fiscal, idoneidad técnica certificada por SBP/MICI.

**Evidencia**: documentación legal de Panamá; representación legal local registrada.

**Vinculación**: BR-007, R-002, PRIN P17, P19.

### E-13 (NEW v2.0): Capacidad de Integración con ERP Externo (CBS)

**Aplica a**: CBS.

**Requerimiento**: el CBS expone los asientos contables generados por cada evento del ciclo de vida (devengo, cobro, distribución capital/interés/seguros/cargos/FECI/IVA, provisiones, diferencias de cambio) vía API REST o archivos estándar al ERP externo en **tiempo real o micro-batch (≤ 5 min)**. Capacidad demostrada de exponer eventos sin duplicar la fuente de verdad contable transaccional. Plan de cuentas SBP cargado en CBS y disponible para sincronización con ERP.

**Evidencia**: demo de exposición de asientos contables a un consumidor externo simulado + documentación de la API + caso de uso con un ERP de referencia.

**Vinculación**: BR-013, FR-069, INT-021, R-024.

### E-14 (NEW v2.0): Capacidad de Offload AML Bidireccional (CBS)

**Aplica a**: CBS.

**Requerimiento**: el CBS expone eventos transaccionales al motor AML externo con **latencia < 200 ms** (NFR-P-005) y **soporta el bloqueo bidireccional** — el CBS detiene la transacción bajo instrucción del motor AML antes de la liquidación. Sin dependencia de módulo AML interno; el CBS NO debe imponer un AML embebido como pre-requisito de operación.

**Evidencia**: demo de stream de eventos a un consumidor AML simulado + demo de bloqueo bidireccional + arquitectura de la integración.

**Vinculación**: FR-048, INT-018, R-023, NFR-P-005.

### E-15 (NEW v2.0): Deliverable Acuerdo 1-2026 Art. 14 antes del 30-jun-2027

**Aplica a**: CBS + ERP + AML.

**Requerimiento**: el cronograma propuesto entrega las capacidades necesarias para cumplir el **Acuerdo SBP 1-2026 Art. 14** (beneficiario final ≥ 10% + geolocalización inferencial digital) **antes del 30 de junio de 2027**. Si la fecha objetivo del go-live de la solución es posterior, el vendor presenta un plan de remediación intermedio (capa de compliance externa, módulo adaptador, parche al CBS legado) firmado con compromiso contractual.

**Evidencia**: cronograma detallado con hitos pre-jun-2027 + plan de remediación intermedio si aplica.

**Vinculación**: BR-002, FR-052, FR-053, R-025.

### Resumen de Criterios Eliminatorios

| ID | Criterio | CBS | ERP | AML | Riesgo principal |
|----|----------|-----|-----|-----|------------------|
| E-1 | Soberanía de datos | ✓ | ✓ | ✓ | R-006 |
| E-2 | Mandato social parametrizable | ✓ | — | — | R-005 |
| E-3 | Modelo dual NIIF 9 + 6-2000 | ✓ | ✓ | — | R-003 |
| E-4 | Reportería SBP nativa | ✓ | ✓ | — | R-015 |
| E-5 | Soporte 24/7 español | ✓ | ✓ | ✓ | R-020 |
| E-6 (REV) | Acuerdo 1-2026 AML/CFT | ✓ | — | ✓ | R-025, R-023 |
| E-7 | Ecosistema panameño demostrado | ✓ | — | — | R-013 |
| E-8 | Mín 3 referencias LatAm | ✓ | ✓ | ✓ | R-008 |
| E-9 | Certificaciones | ✓ | ✓ | ✓ | NFR-C-004 |
| E-10 | Estabilidad financiera | ✓ | ✓ | ✓ | R-008 |
| E-11 (REV) | 15 cláusulas contractuales | ✓ | ✓ | ✓ | R-008, R-011 |
| E-12 | Ley 22 contratación | ✓ | ✓ | ✓ | R-002 |
| **E-13 (NEW)** | Integración con ERP externo | ✓ | — | — | R-024 |
| **E-14 (NEW)** | Offload AML bidireccional | ✓ | — | — | R-023 |
| **E-15 (NEW)** | Acuerdo 1-2026 Art. 14 ≤ 30-jun-2027 | ✓ | ✓ | ✓ | R-025 |

---

## Parte II — Criterios Ponderados (100 puntos por categoría)

### Escala de Scoring (aplicada a cada subcriterio)

| Nivel | Score | Definición operativa |
|-------|-------|----------------------|
| 5 | Excelente | Capacidad nativa demostrada con evidencia documental + referencias en producción comparable a CAP en LatAm |
| 4 | Bueno | Capacidad nativa con experiencia en banca de tamaño y complejidad similar |
| 3 | Adecuado | Capacidad disponible con configuración estándar; track record adecuado |
| 2 | Marginal | Capacidad disponible con desarrollo adicional o limitación significativa |
| 1 | Pobre | Capacidad parcial; gaps significativos |
| 0 | Ausente | Capacidad no demostrada |

> Cada subcriterio se calcula como: **score (0-5) × peso del subcriterio**.

### II.A — Marco Ponderado para CBS (100 pts)

#### Categoría A — Encaje Funcional (30 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| A.1 Cuentas pasivas — sub-cuentas/cajones, sobregiros nativos, depósitos con renovación y anticipo intereses (FR-006..010) | 6 | Demo en vivo |
| A.2 Catálogo de créditos — hipotecario Interés Preferencial, FGA, Profimype, comerciales, sindicados (CAP coord + part), factoring estatal, leasing NIIF 16, construcción, autos, prendarios, líneas (FR-013..029) | 8 | Demo + reportería |
| A.3 Reestructuración nativa sin cierre + cobranza temprana 0-90 días nativa (FR-018, FR-030) | 3 | Demo |
| A.4 Comercio exterior — Cartas de Crédito UCP 600 / ISP 98 / URDG 758, SWIFT, transferencias internacionales con políticas (FR-038..041) | 3 | Demo + casos |
| A.5 Multimoneda + revalorización IAS 21 (FR-012) | 2 | Demo |
| A.6 AML/KYC orientado a externo + beneficiario final ≥ 10% + geolocalización inferencial + FATCA/CRS/PEP (FR-046..054) | 4 | Demo + arquitectura |
| A.7 Reportería SBP nativa SEI + APC + MIVIOT + MEF + DGI (FR-055..063) | 2 | Demo |
| A.8 Cierre contable diario + automatización de asientos (FR-070, FR-069) | 2 | Demo |

#### Categoría B — Arquitectura Técnica & Integración (20 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| B.1 APIs abiertas (OpenAPI/AsyncAPI) + bus IBM MQ compatible (INT-001..013, NFR-M-001) | 4 | Documentación API + casos |
| B.2 CIF único + vista 360° + integración con SISCARD (FR-075, INT-022) | 3 | Arquitectura |
| B.3 Disponibilidad ≥ 99.99% crítico / 99.95% digital + topología activo-activo + RTO/RPO (NFR-A-001..005) | 3 | Diseño + casos |
| B.4 Performance saldo p95 < 1.5s, Yappy < 3s, planilla ≥ 5,000 TPS, AML stream < 200 ms (NFR-P-001..005) | 3 | Benchmarks |
| B.5 Streaming hacia Data Lake AWS + Snowflake (DR-022, INT-027) | 2 | Arquitectura |
| B.6 Mantenibilidad — parametrización sin código del vendor, IaC, CI/CD auditable (NFR-M-002, M-005, M-007) | 2 | Demo |
| B.7 Cloud preferida Azure / on-premise con soberanía (BR-014) | 2 | Arquitectura |
| B.8 Validación en tiempo de ingreso (NFR-M-008) + diccionario de datos formal de 8,000+ elementos (DR-021) | 1 | Demo |

#### Categoría C — Cumplimiento Regulatorio (15 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| C.1 Plan de cuentas SBP no modificable + NIIF 9 + 16 + IAS 21 + Resolución SBP-DJ-0014 (NFR-C-005, C-006, C-011) | 4 | Demo + reportes |
| C.2 Modelo dual NIIF 9 ECL + Acuerdo 6-2000 automatizado (BR-005) | 4 | Demo |
| C.3 Reportería SBP / UAF / APC / MIVIOT / DGI nativa (FR-055..063) | 3 | Demo |
| C.4 Acuerdo 1-2026 — beneficiario final ≥ 10% + geolocalización inferencial entregables antes de 30-jun-2027 (Art. 14) (FR-052, FR-053) | 2 | Hoja de ruta |
| C.5 Ley 22 + Contraloría + idoneidad jurídica (BR-007) | 1 | Documentación legal |
| C.6 Cláusula de cumplimiento continuo (NFR-C-010) | 1 | Contrato |

#### Categoría D — Referencias y Casos de Éxito (10 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| D.1 Banca pública / estatal LatAm en producción ≥ 24 meses | 4 | Llamada de referencia |
| D.2 Banca panameña / centroamericana con SBP / regulador equivalente | 3 | Referencias |
| D.3 Implementación exitosa de tamaño similar (≥ 500K clientes, ≥ B/. 5,000M activos) | 2 | Caso documentado |
| D.4 Reviews independientes (Gartner, Forrester, Celent, peer-reviewed) | 1 | Reportes |

#### Categoría E — Presencia Regional y Soporte (10 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| E.1 Oficina propia en Panamá o presencia panameña de SI especialista | 4 | Verificación física |
| E.2 Soporte 24/7 en español con personal hispanohablante con SLA | 3 | Contrato |
| E.3 Capacitación formal en español certificada | 2 | Plan |
| E.4 Documentación funcional y técnica en español | 1 | Muestra |

#### Categoría F — Propuesta Comercial (15 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| F.1 TCO 7 años dentro del rango B/. 60–135M (CBS aislado) y cláusula ±10% (BR-003) | 6 | Cotización |
| F.2 Pricing model transparente con tope a true-ups e inflación | 4 | Contrato |
| F.3 Modelo CAPEX/OPEX adaptable a las preferencias del banco (BR-014) | 2 | Propuesta |
| F.4 Servicios profesionales de implementación incluidos | 2 | SOW |
| F.5 Período de paralelo y plan de migración por bandos (BR-001) | 1 | Plan |

### II.B — Marco Ponderado para ERP (100 pts)

#### Categoría A — Encaje Funcional Contable (30 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| A.1 Plan de cuentas SBP (1xx–6xx, no modificable) cargado nativamente | 6 | Demo |
| A.2 Doble contabilidad NIIF + adaptaciones SBP simultánea sin doble ingreso | 6 | Demo |
| A.3 Asientos transaccionales recibidos vía API del CBS + libro mayor consolidado | 5 | Demo de integración |
| A.4 Rentabilidad por sucursal + dimensiones múltiples + analítica | 4 | Demo + reportes |
| A.5 Cierres (diario, mensual, anual) coordinados con CBS, Teller y ERP | 4 | Procedimiento + demo |
| A.6 Estados financieros consolidados (Acuerdo 3-2009) | 3 | Demo |
| A.7 Cuentas por pagar + presupuesto + gestión financiera completa | 2 | Demo |

#### Categoría B — Arquitectura / Integración (25 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| B.1 APIs REST + archivos estándar para integración con CBS (INT-021) | 6 | Documentación + caso |
| B.2 Integración con bus IBM MQ del banco | 4 | Arquitectura |
| B.3 Compatibilidad con plan de remediación si CBS no está listo (continuidad GL paralela 90 días) | 4 | Plan |
| B.4 Disponibilidad ≥ 99.95% mensual + RTO/RPO alineados al CBS | 3 | SLA |
| B.5 Streaming hacia Data Lake AWS + Snowflake | 3 | Arquitectura |
| B.6 Multimoneda + revalorización IAS 21 automatizada | 2 | Demo |
| B.7 Cloud preferida Azure / on-premise con soberanía | 2 | Arquitectura |
| B.8 Auditoría inmutable de asientos (WORM o equivalente) | 1 | Diseño |

#### Categoría C — Cumplimiento NIIF + IAS + SBP (15 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| C.1 NIIF 9 + 16 + IAS 21 nativos (sin desarrollo) | 6 | Demo |
| C.2 Resolución SBP-DJ-0014 (formato SEI) — generación nativa de insumos | 4 | Demo |
| C.3 Auditabilidad por Contraloría + cláusula cumplimiento continuo | 3 | Contrato |
| C.4 Plazos Acuerdo 1-2026 cumplidos en lo aplicable al ERP | 2 | Hoja de ruta |

#### Categoría D — Referencias Banca (10 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| D.1 Banca / institución financiera LatAm en producción ≥ 12 meses | 5 | Referencias |
| D.2 Implementación bancaria de tamaño y complejidad similar | 3 | Caso |
| D.3 Reviews independientes (Gartner, etc.) | 2 | Reportes |

#### Categoría E — Cloud / Localización (10 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| E.1 Azure preferida + presencia panameña o LatAm regional | 5 | Arquitectura |
| E.2 Soberanía de datos verificable (E-1 cumplida con margen) | 3 | Acuerdo |
| E.3 Localización Panamá: UTC-5, USD, DD/MM/AAAA, calendario de festivos nacionales | 2 | Configuración |

#### Categoría F — Propuesta Comercial (10 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| F.1 TCO 7 años dentro del rango B/. 21–58M (ERP aislado) + cláusula ±10% | 4 | Cotización |
| F.2 Pricing transparente con tope a inflación + módulos opcionales | 3 | Contrato |
| F.3 Modelo CAPEX/OPEX adaptable | 2 | Propuesta |
| F.4 Servicios profesionales de implementación incluidos | 1 | SOW |

### II.C — Marco Ponderado para AML (100 pts)

#### Categoría A — Encaje Funcional AML (30 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| A.1 Recepción de eventos transaccionales en streaming desde CBS (FR-048) | 6 | Demo + arquitectura |
| A.2 Bloqueo bidireccional bajo instrucción del motor antes de la liquidación (FR-048, E-14) | 5 | Demo |
| A.3 KYC con integración Panadata + listas restrictivas (PEP, OFAC, ONU, SBP) (FR-046, FR-051) | 4 | Demo + integración |
| A.4 Beneficiario final ≥ 10% con análisis de capas societarias automatizado (FR-052) | 4 | Demo |
| A.5 Geolocalización inferencial digital (FR-053) | 3 | Demo |
| A.6 ROS a la UAF orquestado con datos del CBS (FR-049) | 3 | Demo + workflow |
| A.7 FATCA / CRS reportería nativa (FR-050) | 2 | Demo |
| A.8 Workflow de PEP sin bloqueo automático ilegítimo + DJTE Ley 23/2015 (FR-051, FR-054) | 3 | Demo |

#### Categoría B — IA / Tiempo Real / APIs (25 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| B.1 Latencia transaccional añadida por evaluación AML < 200 ms (NFR-P-005) | 6 | Benchmark |
| B.2 IA explicable (XAI) con reducción medible de falsos positivos | 6 | Reportes + casos |
| B.3 APIs REST + streaming + soporte de bus de eventos | 4 | Documentación API |
| B.4 Sandbox + simulador para PoC | 3 | Acceso |
| B.5 Modelo de risk scoring centralizado (no rule-only) | 3 | Arquitectura |
| B.6 Auditabilidad de decisiones + trazabilidad de evidencia | 3 | Demo |

#### Categoría C — Cumplimiento Acuerdo 1-2026 + UAF + KYC (15 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| C.1 Cumplimiento Art. 14 + Art. 25 §1 antes de jun-2027 / ene-2027 | 6 | Hoja de ruta + cláusula penal |
| C.2 Risk-based KYC con niveles configurables | 4 | Demo |
| C.3 Integración con Panadata (KYC actual) | 3 | Arquitectura |
| C.4 Capacidad de generar evidencia auditable inmutable (WORM o equiv.) | 2 | Demo |

#### Categoría D — Referencias LatAm (10 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| D.1 Banco LatAm en producción con regulador equivalente a SBP ≥ 12 meses | 5 | Referencias |
| D.2 Caso de banca pública o estatal | 3 | Caso |
| D.3 Reviews independientes (Gartner MQ, Celent, peer-reviewed) | 2 | Reportes |

#### Categoría E — Despliegue / Integración (10 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| E.1 Cloud regional / on-premise viable en Panamá | 5 | Arquitectura |
| E.2 Integración con Microsoft Entra ID / IAM corporativa (NFR-SEC-011) | 3 | Demo |
| E.3 Plazo de implementación ≤ 12 meses con plan de paralelo con motor actual | 2 | Cronograma |

#### Categoría F — Propuesta Comercial (10 pts)

| Subcriterio | Peso | Evidencia |
|-------------|------|-----------|
| F.1 TCO 7 años dentro del rango B/. 13–25M (AML aislado) + cláusula ±10% | 4 | Cotización |
| F.2 Pricing transparente con tope a true-ups | 3 | Contrato |
| F.3 Modelo de licenciamiento adaptable (por transacción / por usuario / suscripción) | 2 | Propuesta |
| F.4 Servicios profesionales de implementación | 1 | SOW |

### Resumen de Pesos Ponderados por Categoría

| Categoría → | CBS | ERP | AML |
|-------------|-----|-----|-----|
| A — Encaje Funcional | 30 | 30 | 30 |
| B — Arquitectura / IA / Integración | 20 | 25 | 25 |
| C — Cumplimiento Regulatorio | 15 | 15 | 15 |
| D — Referencias | 10 | 10 | 10 |
| E — Presencia Regional / Cloud / Despliegue | 10 | 10 | 10 |
| F — Propuesta Comercial | 15 | 10 | 10 |
| **Total** | **100** | **100** | **100** |

---

## Parte III — Proceso de Evaluación

### III.1 Composición del Comité de Evaluación

Un único Comité con sub-paneles por categoría — gobierna las tres evaluaciones en paralelo:

**Steering Committee del Programa (decisión final por gate)**:

- Aldo Ríos — Líder del Programa (Innovación) — Chair.
- Gerencia de Tecnología (TI) — voto técnico.
- Cumplimiento — voto regulatorio.
- Finanzas — voto comercial.
- Legal — voto jurídico.
- Riesgos — voto de riesgo operacional/crediticio.

**Sub-panel CBS** (evaluación detallada CBS):

- Líder técnico CBS (TI senior arquitecto), Hipotecas, Créditos, Operaciones, Cumplimiento (representante), Datos / Calidad.

**Sub-panel ERP** (evaluación detallada ERP):

- CFO / Finanzas (lead), Contabilidad, Riesgos, TI senior arquitecto, Auditoría Interna.

**Sub-panel AML** (evaluación detallada AML):

- Cumplimiento (lead), CISO, TI senior arquitecto, Operaciones, Legal (representante).

**Validación independiente del proceso**:

- Auditoría Interna — valida criterios, pesos y proceso ANTES del envío del RFP (mitiga R-026).
- Contraloría informada — recibe el Marco de Evaluación con anticipación; opcionalmente delegado en sesiones clave.

### III.2 Etapas de la Evaluación

| Etapa | Duración | Actividad | Salida |
|-------|----------|-----------|--------|
| **Pre-RFP** | 4 semanas | Validación de criterios y pesos por Auditoría Interna; dictamen Legal; aprobación de Comité de Tecnología | Marco aprobado |
| **RFP emitido** | 6 semanas (vendor) | Vendors responden el RFP por categoría | Propuestas recibidas |
| **Apertura administrativa** | 1 semana | Verificación de E-1..E-15 (eliminatorios) por sub-paneles | Lista de aptos por categoría |
| **Scoring ponderado** | 3 semanas | Sub-paneles puntúan A..F sobre 100 con evidencia documental | Scores individuales |
| **Demos + PoC** | 8 semanas | Top-3 por categoría hacen demos extendidas y PoC del caso de uso de referencia (DOC-POC-001 ampliado per R-031) | Resultado de PoC |
| **Reuniones de referencia** | 2 semanas | Llamadas de referencia con clientes en producción de los top-3 | Notas de referencia |
| **Síntesis y deliberación** | 2 semanas | Sub-paneles sintetizan; Steering Committee delibera | Recomendación |
| **Decisión final** | 1 semana | Comité de Tecnología recomienda; JD decide | Selección formal |
| **Adjudicación y contratación** | 8 semanas | Legal + Finanzas negocian; Contraloría visa | Contratos firmados |

### III.3 Metodología de Scoring

1. Cada miembro del sub-panel puntúa **individualmente** cada subcriterio con la escala 0-5.
2. La puntuación final de un subcriterio es la **media de los miembros**, redondeada a 0.5.
3. Score de la categoría = Σ (score × peso) / 5 (para normalizar a peso).
4. Score total = Σ scores de categorías (max 100).
5. Cada score debe tener **justificación documentada** con cita de evidencia presentada por el vendor (página, sección, demo, referencia). Sin evidencia, score = 0.
6. Discrepancias > 1 punto entre miembros se discuten en sesión hasta consenso o se documentan como voto dividido.

### III.4 Empates y Desempate

Empate técnico: dos vendors dentro de ±3 puntos al cierre del scoring. Criterios de desempate por orden:

1. Mayor score en Categoría C (Cumplimiento Regulatorio).
2. Mayor score en D (Referencias en banca pública).
3. Mejor TCO 7 años con cláusula ±10%.
4. Mejor capacidad demostrada de entregar Acuerdo 1-2026 Art. 14 antes de 30-jun-2027.

### III.5 Gestión de Conflicto de Interés

Cada miembro del Comité firma declaración de conflicto de interés antes de evaluar. Conflictos materiales (parentesco, participación accionaria, empleo previo en los últimos 24 meses con el vendor) → recusación obligatoria. Auditoría Interna recibe el registro.

### III.6 Audit Trail Documental

Mantener registrado, accesible por Contraloría:

- Marco de Evaluación firmado (este documento).
- Lista de vendors invitados con memo justificativo por cada decisión de invitar/no invitar.
- Propuestas completas de los vendors (bajo NDA con respaldo).
- Scores individuales y consolidados por sub-panel con justificación.
- Resultados de PoC con evaluación de cada módulo.
- Notas de llamadas de referencia.
- Memos de deliberación del Comité de Tecnología.
- Acta de decisión de la JD.
- Documentos legales del contrato firmado.

### III.7 Comunicación a Vendors

Posterior a la decisión:

- Vendor seleccionado por categoría: notificación oficial + invitación a fase de contratación.
- Vendors no seleccionados: notificación con feedback consolidado (sin scores individuales) y agradecimiento.
- Vendors descalificados por eliminatorios: notificación con cita del eliminatorio fallido.

### III.8 Recursos de Impugnación

Cualquier vendor puede solicitar revisión en los 15 días siguientes a la notificación de no selección. La solicitud se atiende por un panel independiente (Auditoría Interna + Comité de Tecnología sin Chair) con consulta a Contraloría si procede. Decisión final irrevocable.

---

## Parte IV — Matriz de Comparación (a completar al cierre del RFP)

### IV.1 Resultado de Parte I (Criterios Eliminatorios)

#### IV.1.A — CBS

| Vendor | E-1 | E-2 | E-3 | E-4 | E-5 | E-6 | E-7 | E-8 | E-9 | E-10 | E-11 | E-12 | E-13 | E-14 | E-15 | Status |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|------|------|--------|
| Infosys Finacle | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente apertura |
| Temenos Transact | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente apertura |
| Cobis Topaz | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente apertura |
| Datapro e-IBS (Vencora) | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente apertura |
| Oracle FLEXCUBE (wildcard) | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente apertura |
| Bantotal (wildcard) | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente apertura |

#### IV.1.B — ERP

| Vendor | E-1 | E-3 | E-4 | E-5 | E-8 | E-9 | E-10 | E-11 | E-12 | E-15 | Status |
|--------|-----|-----|-----|-----|-----|-----|------|------|------|------|--------|
| Oracle Fusion Cloud ERP | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |
| MS Dynamics 365 F&O | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |
| SAP S/4HANA PCE | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |
| Infor CloudSuite Financials | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |
| Oracle NetSuite (wildcard) | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |

#### IV.1.C — AML

| Vendor | E-1 | E-5 | E-6 | E-8 | E-9 | E-10 | E-11 | E-12 | E-15 | Status |
|--------|-----|-----|-----|-----|-----|------|------|------|------|--------|
| NICE Actimize | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |
| Hawk:AI | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |
| Oracle FCCM | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |
| ComplyAdvantage (wildcard) | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |
| Featurespace ARIC (wildcard) | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | [PEND] | Pendiente |

### IV.2 Resultado de Parte II (Criterios Ponderados — 100 pts por categoría)

[A completarse al cierre del RFP — tabla por categoría con scores por subcriterio, totalizando por A..F y score final.]

### IV.3 Proyección de Resultados (informativa — desde RSCH v2.0)

> **NO oficial — proyección basada en análisis objetivo de RSCH v2.0 para orientar al Comité.** El scoring real se hará tras recepción de propuestas, demos y PoC.

#### CBS

| Vendor | Proyección Total | Comentario |
|--------|------------------|------------|
| Infosys Finacle | ~84/100 | Único Tier-1 con referencia directa Panamá (BCP) — fortaleza decisiva |
| Temenos Transact | ~83/100 | Líder Gartner, mayor cobertura LatAm; debe documentarse capacidad SBP nativa |
| Cobis Topaz | ~78/100 | Oficina PA, 7 referentes locales, soberanía nativa, TCO 30% menor; pendiente reviews mixtas G2 |
| Datapro e-IBS | ~72/100 | Incumbente, mínimo riesgo migración, TCO mínimo; deuda funcional persiste — benchmark obligatorio |
| Oracle FLEXCUBE (wildcard) | ~75/100 | Bladex referente, sinergia stack Oracle si gana ERP/AML |
| Bantotal (wildcard) | ~70/100 | Tier-2 LatAm; menor cobertura banca pública |

**Vendors CBS no invitados** (memo justificativo en `vendors/{slug}-profile.md`, audit trail R-026):

| Vendor no invitado | Razón objetiva del descarte |
|--------------------|------------------------------|
| Mambu | No cumple E-1 (soberanía panameña) — SaaS multi-cloud sin región Panamá; modelo on-prem incompatible con su negocio |
| Thought Machine | No cumple E-1 (soberanía panameña) objetivamente |
| **10X Banking** *(añadido post-revisión)* | No cumple E-7 (sin integración con ecosistema panameño) ni E-8 (sin referencias en banca LatAm en producción ≥ 24 meses) — referentes en banca anglosajona / Oceanía (Chase UK, Westpac) |
| **TUUM** *(añadido post-revisión)* | No cumple E-7 (sin integración panameña) ni E-8 (sin referencias LatAm) + cumplimiento marginal de E-10 (funding ~USD 75M modesto para contrato 7 años a banco AAA(pan)) |
| **Pismo (Visa)** *(añadido post-revisión)* | No cumple E-1 (sin región Panamá en hyperscalers; modelo SaaS cloud-native estándar sin compromiso documentado de despliegue panameño on-prem o cloud privado regional al cierre del análisis) ni E-7 (sin integración con ecosistema panameño demostrada — Yappy/ACH/Telered/SEI/APC). Cumple objetivamente 10/15 eliminatorios (incluyendo E-8 con referentes Itaú/BTG/Banco Inter/Caixa Econômica Federal en Brasil; E-10 con margen por respaldo Visa) — pero las dos brechas son eliminatorias bajo aplicación uniforme. Ver `vendors/pismo-profile.md` para análisis completo (incluye razón de descarte del Comité de Evaluación y constancia de que el análisis técnico había recomendado evaluar invitación como wildcard). |
| SAP | No opera Tier-1 CBS vigente — invitado al RFP-ERP |

#### ERP

| Vendor | Proyección Total | Comentario |
|--------|------------------|------------|
| MS Dynamics 365 F&O | ~82/100 | Best fit con preferencia Azure del banco; Entra ID SSO ya validado |
| Oracle Fusion Cloud ERP | ~80/100 | Top-pick objetivo: NIIF nativos, precedente Bladex, sinergia con FLEXCUBE/FCCM |
| SAP S/4HANA PCE | ~76/100 | Tier-1 global; descartado verbalmente por banco — documentar invitación formalmente |
| Infor CloudSuite Financials | ~70/100 | TCO menor pero menor cobertura banking |
| Oracle NetSuite (wildcard) | ~65/100 | Más adecuado a entidades medianas |

#### AML

| Vendor | Proyección Total | Comentario |
|--------|------------------|------------|
| Hawk:AI | ~85/100 | Best fit FR-048 (streaming + bloqueo + IA explicable + Acuerdo 1-2026); TCO 40-50% menor que enterprise |
| NICE Actimize | ~82/100 | Líder #1 mindshare AML 16.3%; 100+ bancos top; mitigación enterprise |
| Oracle FCCM | ~78/100 | Sinergia stack Oracle si CBS o ERP es Oracle |
| ComplyAdvantage (wildcard) | ~74/100 | AI-native challenger; menos track record SBP |
| Featurespace ARIC (wildcard) | ~70/100 | AI-native especializado fraude + AML |

---

## Apéndice A — Trazabilidad Criterios ↔ Drivers ↔ BR ↔ Riesgos ↔ Principios

| Criterio | Categoría | Stakeholder Driver | BR / FR | Riesgo | Principio |
|----------|-----------|---------------------|---------|--------|-----------|
| E-1 Soberanía | CBS+ERP+AML | SD-7, SD-10 | BR-006, DR-013 | R-006, R-018 | P6 |
| E-2 Mandato social | CBS | SD-11, SD-12 | BR-004, FR-007, FR-014, FR-017 | R-005 | P20 |
| E-3 Modelo dual | CBS+ERP | SD-14, SD-7 | BR-005, FR-064..066 | R-003 | P8 |
| E-4 Reportería SBP | CBS+ERP | SD-7, SD-9 | BR-002, FR-055..063 | R-015 | P5, P7 |
| E-5 Soporte español | CBS+ERP+AML | SD-3, SD-8 | BR-009, NFR-U-001..003 | R-001, R-020 | P21 |
| **E-6 (REV) Acuerdo 1-2026** | CBS+AML | SD-7, SD-16 | BR-002, FR-052, FR-053, NFR-C-001 | **R-025**, R-023 | P5, P7 |
| E-7 Ecosistema PA | CBS | SD-5, SD-13 | BR-001, BR-010, FR-034..038 | R-013 | P2, P11 |
| E-8 Referencias LatAm | CBS+ERP+AML | SD-1 | BR-001, BR-007 | R-008 | — |
| E-9 Certificaciones | CBS+ERP+AML | SD-6 | NFR-C-004 | NFR-SEC-001..010 | P4 |
| E-10 Estabilidad financiera | CBS+ERP+AML | SD-4, SD-1 | BR-003 | R-008 | — |
| E-11 (REV) 15 cláusulas | CBS+ERP+AML | SD-4, SD-7, SD-10 | múltiples BR | R-008, R-011, R-023, R-024 | P17, P19 |
| E-12 Ley 22 | CBS+ERP+AML | SD-4, SD-10 | BR-007 | R-002 | P17, P19 |
| **E-13 (NEW) Integración ERP** | CBS | SD-4, SD-5 | BR-013, FR-069, INT-021 | **R-024** | P8 |
| **E-14 (NEW) Offload AML** | CBS | SD-7 | FR-048, INT-018 | **R-023** | P4, P5 |
| **E-15 (NEW) Acuerdo 1-2026 ≤ jun-2027** | CBS+ERP+AML | SD-7 | BR-002, FR-052, FR-053 | **R-025** | P5, P7 |
| **Ponderado A — Encaje Funcional** | C/E/A (3 versiones) | SD-2, SD-11, SD-12, SD-13 | BR-001, BR-004, BR-010, FR-* | R-005 | P20 |
| **Ponderado B — Arquitectura/Integración/IA** | C/E/A (3 versiones) | SD-5, SD-6 | NFR-A-*, NFR-P-*, NFR-M-*, NFR-S-* | R-013, R-024, R-023, R-028, R-029 | P1, P2, P11, P16, P17 |
| **Ponderado C — Cumplimiento** | C/E/A (3 versiones) | SD-7, SD-9, SD-16 | BR-002, BR-005, NFR-C-* | R-015, R-025, R-007 | P5, P7, P8 |
| **Ponderado D — Referencias** | C/E/A (3 versiones) | SD-1, SD-4 | BR-001 | R-008 | — |
| **Ponderado E — Presencia/Cloud** | C/E/A (3 versiones) | SD-3, SD-8 | NFR-U-*, BR-014 | R-020, R-032, R-034 | P21 |
| **Ponderado F — Comercial** | C/E/A (3 versiones) | SD-4 | BR-003 | R-011, R-010 | — |

---

## Apéndice B — Plantilla de Hoja de Scoring Individual

(Una por evaluador, una por vendor, una por categoría)

```text
Evaluador: ____________________
Vendor: ______________________
Categoría: [ ] CBS  [ ] ERP  [ ] AML
Fecha: _______________________

PARTE I — Eliminatorios (marcar pass/fail con cita de evidencia)
E-1 Soberanía:                [ ] PASS  [ ] FAIL  Evidencia: __________
E-2 Mandato social:           [ ] PASS  [ ] FAIL  Evidencia: __________
... (E-3 a E-15 según aplique)

→ Si algún FAIL: VENDOR DESCALIFICADO. No continuar a Parte II.

PARTE II — Ponderado (score 0-5 por subcriterio con cita)
A.1 ...:                      Score: _/5  Evidencia: __________
A.2 ...:                      Score: _/5  Evidencia: __________
... (continúa por toda la categoría)

Score total: ___/100

Justificación del score total: __________________
Recomendación: [ ] Recomendado  [ ] Considerable  [ ] No Recomendado
Conflicto de interés declarado: [ ] No  [ ] Sí — detalle: __________

Firma evaluador: ____________________
```

---

## Aprobación del Documento

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Owner del Marco | Aldo Ríos — Gerencia de Innovación | [PENDING] | [PENDING] |
| Auditoría Interna (validación de proceso) | [PENDING] | [PENDING] | [PENDING] |
| Legal (dictamen previo de RFP) | [PENDING] | [PENDING] | [PENDING] |
| Cumplimiento | [PENDING] | [PENDING] | [PENDING] |
| Finanzas | [PENDING] | [PENDING] | [PENDING] |
| CISO | [PENDING] | [PENDING] | [PENDING] |
| Comité de Tecnología | [PENDING] | [PENDING] | [PENDING] |
| Junta Directiva (apertura del RFP) | [PENDING] | [PENDING] | [PENDING] |

---

## Próximos Pasos

1. **Esta semana**: validar este Marco con Auditoría Interna (mitigación R-026) + dictamen Legal (P0.3 RISK v2.0).
2. **Próximas 2 semanas**: aprobación por Comité de Tecnología; lista final de vendors invitados por categoría documentada con memo justificativo (incluyendo los descartados verbalmente — Temenos, Finacle, SAP, etc. — con documentación de invitación o no-invitación basada en eliminatorios objetivos).
3. **Próximas 4 semanas**: emisión de los tres RFPs (CBS — refresh del RFI existente DOC-RFI-001; ERP — nuevo; AML — nuevo). Coordinar con `/arckit:sow` para los SOWs formales.
4. **Próximas 6 semanas**: fase de respuestas de los vendors.
5. **Próximas 12 semanas**: scoring + demos + PoC ampliada (R-031 — sindicados, factoring estatal, DDI masivo además del caso PoC v1.0).
6. **Próximas 18 semanas**: deliberación, recomendación al Comité de Tecnología y decisión final de la JD.
7. **Refresh trimestral del Marco** o ad-hoc tras eventos críticos (nuevos Acuerdos SBP, cambios en RSCH).

---

## External References

### Document Register

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| ARC-001-REQ-v2.0 | ARC-001-REQ-v2.0.md | Markdown | `projects/001-evaluacion-core-banking/` | 193 requisitos refrescados v2.0 con corrigendum Acuerdo 1-2026 |
| ARC-001-RISK-v2.0 | ARC-001-RISK-v2.0.md | Markdown | `projects/001-evaluacion-core-banking/` | 37 riesgos refrescados v2.0 con corrigendum |
| ARC-001-RSCH-v2.0 | research/ARC-001-RSCH-v2.0.md | Markdown | `projects/001-evaluacion-core-banking/research/` | Research de 3 categorías de vendors (CBS, ERP, AML) |
| ARC-001-STKE-v1.0 | ARC-001-STKE-v1.0.md | Markdown | `projects/001-evaluacion-core-banking/` | 27 stakeholders, 17 drivers, 10 metas |
| ARC-000-PRIN-v1.1 | ARC-000-PRIN-v1.1.md | Markdown | `projects/000-global/` | 21 principios |
| DOC-RFI-001 | 7.RFI-RFI_CAP_CoreBancario_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | RFI v1.0 emitido jun-2026 |
| DOC-POC-001 | 5.PreparaciónPOC-POC_seleccion_core_banking_CAP_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | Ficha PoC v1.0 |
| DOC-SES-001..009 | Resúmenes de las 8 sesiones presenciales | Word | `projects/001-evaluacion-core-banking/external/` | Insumos de las sesiones 25–28 mayo 2026 |
| tech-notes/acuerdo-1-2026-implementation.md | Tech Note | Markdown | `projects/001-evaluacion-core-banking/tech-notes/` | Implementación de Acuerdo 1-2026 (umbral 10%, plazos) |

### Citas principales nuevas (v2.0)

| Citation ID | Doc | Uso principal |
|---|---|---|
| ARC-001-REQ-v2.0 | REQ | Eliminatorios derivados de BR-013, BR-014, FR-048, FR-052, FR-053; ponderaciones derivadas de FR/NFR específicos |
| ARC-001-RISK-v2.0 | RISK | Mitigaciones explícitas de R-024 (ERP), R-023 (AML), R-025 (Acuerdo 1-2026), R-026 (sesgo COBIS) en el diseño del Marco |
| ARC-001-RSCH-v2.0 | RSCH | Shortlists por categoría + proyección de resultados informativos + presupuestos TCO 7 años por categoría |
| DOC-SES-009 | Resumen consolidado | Preferencias del banco (COBIS / descartes) tratadas como insumo de ponderación, no eliminatorio |

---

**Generated by**: ArcKit `/arckit:evaluate` command
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Evaluación y Selección de Core Banking (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: v2.0 refresh — refleja la decisión arquitectónica de v2.0 (CBS + ERP + AML como tres procesos coordinados), introduce 3 eliminatorios nuevos (E-13 integración ERP, E-14 offload AML, E-15 Acuerdo 1-2026 ≤ 30-jun-2027) y refresca E-6 a Acuerdo 1-2026; añade ponderaciones diferenciadas por categoría; integra el shortlist objetivo desde RSCH v2.0; documenta explícitamente la mitigación de R-026 (sesgo COBIS) mediante validación de Auditoría Interna y memo justificativo por decisión de invitación.
