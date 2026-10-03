# Statement of Work (SOW) — ERP Externo para Libro Mayor Consolidado — Caja de Ahorros de Panamá

> **Documento legalmente vinculante para procurement bajo Ley 22 de Contrataciones Públicas de Panamá. Constituye el RFP formal para la categoría ERP.**

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-SOW-ERP-v1.0 |
| **Document Type** | Statement of Work (RFP — Enterprise Resource Planning para GL bancario) |
| **Project** | Reemplazo del Core Banking + ERP + AML — Caja de Ahorros, Panamá (Project 001) |
| **RFP Track** | **ERP** — Enterprise Resource Planning (2 de 3 RFPs coordinados) |
| **Classification** | OFFICIAL-SENSITIVE |
| **Status** | DRAFT |
| **Version** | 1.0 |
| **Created Date** | 2026-06-11 |
| **Last Modified** | 2026-06-11 |
| **Review Date** | 2026-07-11 |
| **Owner** | CFO + Aldo Ríos — Gerencia de Innovación |
| **Reviewed By** | PENDING — Auditoría Interna, Legal, Finanzas, Contabilidad, Riesgos, TI |
| **Approved By** | PENDING — Comité de Tecnología; Junta Directiva |
| **Distribution** | Vendors invitados bajo NDA; JD; Comité de Tecnología; Comité de Evaluación; Auditoría Interna; Contraloría (informativo) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-06-11 | ArcKit AI | Creación inicial del SOW para el RFP ERP. Track NUEVO en el programa — emerge de la decisión arquitectónica de v2.0 (BR-013 — el CBS no incluirá GL completo). Integra los 9 eliminatorios aplicables a ERP del EVAL v2.0 (E-1, E-3, E-4, E-5, E-8, E-9, E-10, E-11, E-12, E-15) y la ponderación específica ERP (Encaje Funcional Contable 30 + Arquitectura/Integración 25 + Cumplimiento NIIF+IAS+SBP 15 + Referencias Banca 10 + Cloud/Localización 10 + Comercial 10). Contrato Hybrid; ponderación 70% Técnico / 30% Costo. Shortlist desde RSCH v2.0: Oracle Fusion Cloud ERP, Microsoft Dynamics 365 F&O, SAP S/4HANA PCE, Infor CloudSuite Financials (+ wildcard Oracle NetSuite). | PENDING | PENDING |

---

## 1. Resumen Ejecutivo

### 1.1 Identificación del Proceso

| Concepto | Detalle |
|----------|---------|
| **Comprador** | Caja de Ahorros (CAP) — banco estatal panameño bajo Ley 20 de 1975 |
| **Proceso** | Procedimiento abierto bajo Ley 22 de Contrataciones Públicas |
| **Categoría** | Adquisición e implementación de Enterprise Resource Planning (ERP) para el Libro Mayor (GL) consolidado del banco |
| **Modalidad contractual** | Hybrid — Fixed-price para licencias + implementación con tope ±10% / T&M para change requests post go-live |
| **Plazo del proceso** | RFP abierto 6 semanas; respuesta + 4 semanas demos + 2 semanas referencias + selección |
| **Valor estimado del contrato** | B/. 21–58M a 7 años (TCO ERP aislado — referencia RSCH v2.0); ~B/. 40M en el TCO blendado recomendado del programa |
| **Idioma** | Español |

### 1.2 Por qué un ERP separado

La decisión arquitectónica formalizada en ARC-001-REQ-v2.0 (BR-013) establece que el **nuevo Core Banking System no incluirá GL completo** [DOC-RFI-001 §3.9, DOC-SES-005, DOC-SES-009 §6.3]. La transición a un nuevo CBS obliga a:

1. Adquirir un ERP externo que asuma el GL consolidado.
2. Integrar el CBS con el ERP vía API REST o archivos estándar en tiempo real o micro-batch ≤ 5 min (FR-069, INT-021).
3. Soportar **doble contabilidad** NIIF + adaptaciones SBP simultánea sin doble ingreso (NFR-C-005).
4. Mantener el **plan de cuentas SBP** (1xx–6xx, no modificable) cargado en ambos sistemas con sincronización.

El RFP ERP corre **en paralelo coordinado** al RFP CBS bajo el mismo Steering Committee. **R-024 (ERP no listo al go-live del CBS = cierre contable inviable)** es el riesgo Crítico inherente del programa (score 25) que este SOW mitiga.

### 1.3 Objetivos del SOW ERP

1. Reemplazar el GL embebido en DataPro/eIBS con un ERP financiero profesional.
2. Cumplir nativamente NIIF 9, **NIIF 16** (leasing — nuevo en v2.0), **IAS 21** (diferencias de cambio), plan de cuentas SBP, Resolución SBP-DJ-0014 (formato SEI).
3. Integrar con el nuevo CBS y con el motor AML externo vía API.
4. Habilitar rentabilidad por sucursal + cierres coordinados (diario, mensual, anual) + estados financieros consolidados.
5. Coordinar implementación con el cronograma del CBS y del AML (cláusula 15 — coordinación inter-RFP).

---

## 2. Scope of Work

### 2.1 Alcance del SOW (En scope)

1. **Software y licencias del ERP** — módulos requeridos: GL, AP (cuentas por pagar), AR (cuentas por cobrar), gestión financiera, presupuesto, cierre, rentabilidad por sucursal/línea de negocio, conciliaciones automatizadas, consolidación.

2. **Implementación end-to-end**:
   - Despliegue en territorio panameño (on-premise CAP, colocation o cloud regional con presencia local — definido por dictamen Legal).
   - Configuración del **plan de cuentas SBP** sin modificación de códigos.
   - Configuración de **doble contabilidad** NIIF + adaptaciones regulatorias SBP.
   - Integración con el nuevo CBS para asientos transaccionales (FR-069, INT-021) — tiempo real o micro-batch ≤ 5 min.
   - Integración con el motor AML externo para eventos contables relevantes a AML.
   - Integración con el bus IBM MQ existente.
   - Integración con SEI vía generación de insumos para reportes regulatorios consolidados.
   - Integración con el Data Lake AWS + Snowflake (FR-022, streaming de eventos contables).
   - Integración con Microsoft Entra ID (SSO).

3. **Migración del GL del legado** — transición del GL embebido en DataPro/eIBS al ERP externo; corrida paralela ≥ 90 días pre-corte; cero diferencias materiales en cuadre de cuentas; preservación de trazabilidad histórica.

4. **Plan de contingencia GL paralelo durante 90 días post go-live del CBS** — si el CBS va a producción antes que el ERP esté completamente estabilizado, mantener GL paralelo en DataPro como respaldo.

5. **Documentación funcional y técnica completa en español**.

6. **Capacitación certificada en español** — para Contabilidad, Finanzas, Riesgos, Auditoría Interna, TI (~150 personas).

7. **Soporte L1/L2/L3 24/7 en español** con SLA contractual.

8. **Mantenimiento evolutivo** — adaptación a nuevos Acuerdos SBP, NIIF y normas internacionales sin cobros extraordinarios.

9. **Servicios profesionales** para fases de discovery + diseño + implementación + paralelo + go-live + estabilización.

### 2.2 Fuera de Alcance del SOW ERP

- **CBS**: track separado — ver `ARC-001-SOW-CBS-v1.0.md`.
- **Motor AML externo**: track separado — ver `ARC-001-SOW-AML-v1.0.md`.
- **Asientos transaccionales** del CBS: los genera el CBS y los expone al ERP vía API (responsabilidad del SOW CBS).
- **Tesorería**: evaluable en Fase 2.
- **RRHH (planilla)**: Talentía (SaaS) actual se mantiene; integración con ERP solo para asientos de planilla.

### 2.3 Supuestos

1. El RFP CBS estará abierto en paralelo y se coordinará con la selección del ERP.
2. El dictamen Legal de soberanía habrá emitido respuesta antes de la firma.
3. El vendor del CBS se compromete a exponer asientos vía API (cláusula contractual 13 del SOW CBS).

### 2.4 Restricciones

1. **Soberanía de datos** en Panamá (BR-006).
2. **TCO con tope ±10%** (BR-003).
3. **Plazos regulatorios**: aunque el ERP tiene menor exposición directa al Acuerdo 1-2026, debe estar operativo antes del go-live del CBS para no materializar R-024.
4. **Ley 22**: proceso, contrato y modificaciones cumplen.
5. **Idioma**: español.

### 2.5 Dependencias

| Dependencia | Owner | Plazo |
|-------------|-------|-------|
| Selección del CBS y su API de exposición de asientos | RFP CBS | Pre-firma ERP |
| Dictamen Legal de soberanía | Legal CAP | Pre-firma de contrato |
| Plan de cuentas SBP cargado al ERP | CAP + Vendor ERP | Fase de discovery |

---

## 3. Marco Regulatorio Aplicable

| Marco | Ámbito |
|-------|--------|
| **Ley 20 de 1975** | Ley orgánica de CAP |
| **Ley 22 de Contrataciones Públicas** | Proceso |
| **NIIF 9** | Instrumentos financieros y ECL |
| **NIIF 16** | Leasing financiero |
| **IAS 21** | Diferencias de cambio |
| **Plan de cuentas SBP** | 1xx–6xx, no modificable |
| **Resolución SBP-DJ-0014** | Formato SEI |
| **Acuerdo SBP 3-2009** | Consolidación de grupo bancario |
| **Acuerdo SBP 5-2011** | Bienes adjudicados |
| **Acuerdo SBP 6-2000** | Provisiones |
| **Acuerdo SBP 1-2026** | AML/CFT — relevante para flujos contables expuestos a la herramienta AML externa |
| **Ley 81 de Panamá** | Protección de datos personales |

---

## 4. Requisitos del Producto

### 4.1 Business Requirements (BR) — MUST_HAVE

| ID | Requisito | Vínculo |
|----|-----------|---------|
| BR-013 | Adquisición e integración del ERP externo para el GL consolidado | Eje del SOW |
| BR-003 | TCO controlado a 7 años con tope ±10% | Sección 9 |
| BR-006 | Soberanía de datos en Panamá | Sección 3 |
| BR-007 | Contratación pública sin observaciones Contraloría | Sección 9 |
| BR-008 | Migración del GL con conciliación exacta | Sección 4.3 |
| BR-009 | Capacitación en español | Sección 5.4 |
| BR-014 | Modelo CAPEX→OPEX deseable | Sección 8.4 |

### 4.2 Functional Requirements (FR) — MUST_HAVE

| ID | Requisito |
|----|-----------|
| FR-058 | Plan de cuentas SBP (1xx–6xx) cargado nativamente sin modificación |
| FR-069 | Recepción de asientos contables del CBS vía API o archivos estándar en tiempo real o micro-batch ≤ 5 min |
| FR-070 | Cuadre contable diario automatizado; diferencias = 0 al cierre del día |
| FR-064..066 | Modelo dual NIIF 9 + Acuerdo 6-2000 — el ERP soporta la doble contabilidad simultánea |

**Capacidades funcionales requeridas (FRC — Functional Requirements del ERP)**:

- **FRC-1**: Plan de cuentas SBP no modificable + asignación de cuenta válida a cada operación del CBS.
- **FRC-2**: Doble contabilidad NIIF + adaptaciones SBP simultánea (NFR-C-005) sin doble ingreso.
- **FRC-3**: Recepción de asientos transaccionales del CBS vía API REST o archivos estándar (REST/JSON, GraphQL, SFTP/CSV, Kafka, etc.) en tiempo real o micro-batch ≤ 5 min.
- **FRC-4**: Rentabilidad por sucursal + por línea de negocio + por producto + por segmento de cliente. Dimensiones múltiples configurables sin desarrollo.
- **FRC-5**: Cierres (diario, mensual, anual) coordinados con CBS, Teller y ERP; diferencias = 0 al cierre.
- **FRC-6**: Estados financieros consolidados conforme Acuerdo 3-2009.
- **FRC-7**: Cuentas por pagar (AP) + cuentas por cobrar (AR) + gestión financiera + presupuesto.
- **FRC-8**: NIIF 16 (leasing) nativo — reconocimiento de activo financiero, devengado, distribución capital/interés implícito.
- **FRC-9**: IAS 21 (diferencias de cambio) — revalorización automática de activos y pasivos en moneda extranjera; cálculo de posición neta.
- **FRC-10**: Generación de **insumos para los 54+ reportes SEI** que CAP envía mensualmente — formatos compatibles con la pre-validación local del CBS.
- **FRC-11**: Auditoría inmutable de asientos (WORM o equivalente — DR-018).
- **FRC-12**: Conciliación bancaria automatizada con bancos corresponsales.
- **FRC-13**: Streaming de eventos contables hacia Data Lake AWS + Snowflake (DR-022, INT-027).
- **FRC-14**: Workflow de aprobación de asientos manuales con doble aprobación auditable.
- **FRC-15**: Localización Panamá (UTC-5, USD, DD/MM/AAAA, calendario de festivos nacionales).

### 4.3 Non-Functional Requirements (NFR) — MUST_HAVE

| ID | Métrica |
|----|---------|
| NFR-A-002 | Disponibilidad ≥ 99.95% mensual |
| NFR-A-004 | RTO ≤ 30 min, RPO ≤ 5 min para operaciones de GL |
| NFR-SEC-001..010 | Seguridad: MFA, mTLS, cifrado en tránsito + reposo, logs 7 años, pen-tests, SAST/SCA, segmentación |
| NFR-SEC-011 | SSO con Microsoft Entra ID + SAML/OAuth/OIDC/LDAP |
| NFR-SEC-013 | SoD configurable (separación de quien instruye vs quien autoriza un asiento) |
| NFR-SEC-014 | Permisos a nivel campo + enmascaramiento por rol |
| NFR-SEC-015 | Recertificación periódica automática |
| NFR-C-005 | Doble contabilidad NIIF + adaptaciones SBP |
| NFR-C-006 | Plan de cuentas SBP no modificable |
| NFR-C-007 | Retención logs ≥ 7 años |
| NFR-C-011 | NIIF 16 (leasing) + IAS 21 (divisas) nativos |
| NFR-U-005 | Localización Panamá completa |

### 4.4 Integration Requirements (INT) — MUST_HAVE

| ID | Sistema |
|----|---------|
| INT-021 | CBS — vía API REST o archivos estándar para asientos contables |
| INT-013 | Bus IBM MQ + API Gateway |
| INT-005 | SEI — generación de insumos de reportes consolidados |
| INT-026 | Microsoft Entra ID (SSO) |
| INT-027 | Data Lake AWS + Snowflake (streaming) |
| INT-018 | Motor AML externo — eventos contables relevantes |

### 4.5 Plan de Migración del GL

- **Corrida paralela ≥ 90 días pre-corte** con DataPro como benchmark.
- Diferencias en saldos contables al cierre del corte: **= 0 materiales**.
- Trazabilidad histórica preservada para movimientos antiguos.
- **Plan de contingencia GL paralelo durante 90 días post go-live del CBS** (continuidad mientras estabiliza).
- Auditoría Interna firma reporte de conciliación post-corte.

---

## 5. Deliverables

| # | Deliverable | Aceptación | Plazo (referencia, T = firma) |
|---|-------------|------------|--------------------------------|
| D-01 | Diseño Funcional Detallado (DFD) por dominio | Aprobado por CFO + Contabilidad | T+2 meses |
| D-02 | Diseño de Arquitectura (HLD + DLD) | Aprobado por Comité de Arquitectura | T+3 meses |
| D-03 | Plan de cuentas SBP cargado + estructura de dimensiones | Validado por Contabilidad | T+3 meses |
| D-04 | Plan de Migración del GL con cronograma + plan de rollback | Aprobado por Steering Committee | T+4 meses |
| D-05 | Integración con CBS demostrada con asientos en tiempo real / micro-batch ≤ 5 min | Pruebas E2E aprobadas | T+8 meses |
| D-06 | Configuración doble contabilidad NIIF + SBP | Aprobado por Cumplimiento + Riesgos | T+10 meses |
| D-07 | Corrida paralela ≥ 90 días pre-corte | Conciliación diferencias = 0 | T+12-15 meses |
| D-08 | Pruebas de rendimiento + seguridad + DR | Métricas cumplen NFR | T+15 meses |
| D-09 | Documentación completa en español | Aprobada por Operaciones + TI | T+16 meses |
| D-10 | Capacitación certificada en español | 100% del personal clave certificado | T+18 meses |
| D-11 | Go-live coordinado con CBS | Aprobado go/no-go por CFO + Auditoría Interna | T+18 meses |
| D-12 | Estabilización + warranty (90 días) | Sin incidentes P1 críticos | T+21 meses |
| D-13 | Reporte final + handover a Finanzas | Aprobado por JD | T+22 meses |

---

## 6. Cronograma y Hitos Clave

| Hito | Fecha objetivo |
|------|-----------------|
| RFP emitido | 2026-08-15 |
| Cierre del RFP | 2026-11-15 |
| Demos + PoC (top-3) | 2026-11-16 – 2026-12-31 |
| Selección final por JD | 2027-01-31 |
| Firma del contrato | 2027-03-31 |
| **Cumplimiento Acuerdo 1-2026 Art. 25 §1** | **2027-01-31** (vía remediación del legado) |
| Diseño + HLD/DLD | T+3 meses |
| Plan de Migración firmado | T+4 meses |
| Implementación + integración con CBS | T+5 a T+12 meses |
| Corrida paralela ≥ 90 días pre-corte | T+12 a T+15 meses |
| **Go-live coordinado con CBS** | **2028-Q1** (alineado con Banda 2 del CBS) |
| Estabilización + warranty | 2028-Q1 a Q2 |
| Operación productiva → contrato 7 años | T+21 meses → T+84 meses |

---

## 7. Vendor Qualifications (Eliminatorios Pass/Fail)

| ID | Criterio | Aplica |
|----|----------|--------|
| E-1 | Soberanía de Datos en Territorio Panameño | ✓ |
| E-3 | Modelo Dual NIIF 9 + Acuerdo 6-2000 Nativo (ERP soporta doble contabilidad) | ✓ |
| E-4 | Reportería SBP Nativa (generación de insumos para SEI) | ✓ |
| E-5 | Soporte 24/7 en Español con SLA Medible | ✓ |
| E-8 | Mínimo 3 Referencias LatAm Verificables en Producción ≥ 12 Meses (ERP banking) | ✓ |
| E-9 | Certificaciones Obligatorias (ISO 27001, ISO 27017 si cloud, SOC 2 Tipo II) | ✓ |
| E-10 | Estabilidad Financiera y Continuidad del Vendor (ingresos globales ≥ USD 100M) | ✓ |
| E-11 | Aceptación de las 15 Cláusulas Contractuales Obligatorias | ✓ |
| E-12 | Idoneidad Jurídica Bajo Ley 22 | ✓ |
| E-15 | Deliverable Acuerdo 1-2026 Art. 14 antes del 30-jun-2027 (en lo aplicable al ERP) | ✓ |

**Cualquier fallo en cualquiera de los 10 eliminatorios descalifica al vendor.**

---

## 8. Proposal Requirements (Estructura Obligatoria)

3 sobres independientes (Administrativo, Técnico, Económico).

### 8.1 Sobre Administrativo

- Documentación legal (idoneidad SBP/MICI, paz y salvo fiscal, declaración jurada Ley 22, representación local).
- NDA firmado.
- Certificaciones ISO 27001 + ISO 27017 (si cloud) + SOC 2 Tipo II.
- Estados financieros auditados últimos 3 años.
- Aceptación firmada de las 15 cláusulas contractuales.
- Lista de referencias LatAm verificables.

### 8.2 Sobre Técnico

- Resumen ejecutivo (máx 8 págs).
- Respuesta a cada uno de los 10 eliminatorios con evidencia documental.
- Cobertura de los 15 FRC y de los NFR/INT relevantes — tabla por ID (nativo / configurable / desarrollo / no cubierto).
- Arquitectura HLD propuesta con detalle de integración con CBS.
- Cronograma con hitos críticos.
- Plan de migración del GL con corrida paralela.
- Plan de integración con CBS, motor AML, bus IBM MQ, Data Lake, Entra ID.
- Plan de capacitación en español.
- Equipo propuesto + CVs.
- Casos de éxito (≥ 3 referencias LatAm ERP banking ≥ 12 meses).
- Plan de gestión de riesgos.

### 8.3 Sobre Económico

- Precio total a 7 años con desglose CAPEX (años 1-3) / OPEX (años 4-7):
  - Licenciamiento (con usuarios incluidos).
  - Implementación inicial (precio fijo).
  - Migración del GL.
  - Servicios profesionales.
  - Soporte y mantenimiento anual.
  - Módulos opcionales.
- Modelo de pricing detallado.
- Cláusula de tope ±10% firmada.
- Modelo CAPEX/OPEX (preferencia banco BR-014).
- TCO a 7 años con sensibilidad.
- Costos de salida.

---

## 9. Términos Contractuales

### 9.1 Cláusulas Obligatorias (las 15 del SOW CBS — el vendor ERP acepta también)

1. Residencia de datos en Panamá.
2. SLA con penalizaciones.
3. TCO con tope ±10%.
4. Cumplimiento regulatorio continuo.
5. Auditabilidad por Contraloría.
6. Coordinación con el CBS (no aplica DataPro como incumbente — el ERP es nuevo).
7. Capacitación en español certificada.
8. Documentación en español.
9. Salida ordenada — portabilidad de datos.
10. Penalización por incumplimiento de plazos críticos (cumplimiento normas contables).
11. Confidencialidad y datos personales (Ley 81).
12. Anticorrupción y Ley 22.
13. Integración con CBS con SLA específico (latencia ≤ 5 min, idempotencia, conciliación automática).
14. Exposición de eventos a la herramienta AML externa.
15. **Coordinación inter-RFP** con vendor CBS + vendor AML; sesiones trimestrales de integración.

### 9.2 Estructura de Pago (Hybrid)

| Hito | % del precio fijo |
|------|--------------------|
| Firma del contrato | 10% |
| Diseño + HLD/DLD aprobados | 10% |
| Plan de cuentas SBP + estructura cargada | 5% |
| Integración con CBS demostrada | 15% |
| Doble contabilidad NIIF + SBP configurada | 10% |
| Corrida paralela ≥ 90 días con diferencias = 0 | 15% |
| Pruebas de rendimiento + seguridad aprobadas | 10% |
| Capacitación certificada 100% personal | 5% |
| Go-live coordinado con CBS | 10% |
| Estabilización 90 días sin P1 críticos | 5% |
| Cierre del proyecto + handover | 5% |
| **Total Fixed-price** | **100%** |

**T&M** para change requests > 5% del scope original — tarifas firmadas.

**Soporte anual recurrente** (años 1-7) con SLA y reducción contractual del 10% si SLA promedio < 99.9%.

### 9.3 Aceptación

- D-01..D-04 (Diseño y plan): aprobación firmada por Comité de Arquitectura + CFO.
- D-05..D-07 (Implementación + paralelo): pruebas E2E con dataset proporcionado por el banco; demo en vivo aprobada por Finanzas + Auditoría Interna.
- D-10 (Capacitación): 100% del personal clave certificado por examen.
- D-11 (Pase a producción): go/no-go con voto explícito de CFO + Auditoría Interna.
- D-12 (Warranty): 90 días consecutivos sin incidentes P1 críticos.

### 9.4 Gestión de Cambios

Igual al SOW CBS — change requests > 5% requieren análisis de impacto + aprobación Comité de Tecnología (< B/. 5M) o JD (≥ B/. 5M).

### 9.5 Propiedad Intelectual

- Software del vendor: licencia perpetua durante la vida del contrato + 5 años de uso post-terminación.
- Configuraciones: propiedad de CAP.
- Código fuente: escrow.
- Datos: propiedad exclusiva de CAP.

### 9.6 Garantías y Soporte

- Warranty: 12 meses post go-live.
- Soporte L1/L2/L3 24/7 en español durante toda la vida del contrato.
- Actualizaciones de versión mayor incluidas.

### 9.7 Cláusulas de Terminación

- Igual al SOW CBS.
- Adicional: **terminación por descoordinación con CBS** — si el vendor ERP causa retrasos materialmente atribuibles que impidan el go-live coordinado con el CBS (validado por Steering Committee), penalización 15% del valor del contrato.

### 9.8 Auditoría

- Contraloría puede auditar.
- Auditoría Interna trimestralmente.
- Pen-tests anuales a cargo del vendor.

---

## 10. Evaluación de Propuestas

### 10.1 Ponderación

- **70% Técnico / 30% Costo**.

### 10.2 Distribución del Score Técnico (sobre 70 pts)

- A — Encaje Funcional Contable: 21 pts (30% × 70).
- B — Arquitectura/Integración con CBS: 17.5 pts (25% × 70).
- C — Cumplimiento NIIF+IAS+SBP: 10.5 pts (15% × 70).
- D — Referencias Banca: 7 pts (10% × 70).
- E — Cloud/Localización: 7 pts (10% × 70).
- Subtotal técnico: 63 pts → escalado a 70.

### 10.3 Distribución del Score Económico (sobre 30 pts)

- F.1 — TCO 7 años en banda B/. 21–58M con cláusula ±10%: 12 pts (40% × 30).
- F.2 — Pricing transparente: 9 pts (30% × 30).
- F.3 — Modelo CAPEX/OPEX adaptable: 6 pts (20% × 30).
- F.4 — Servicios profesionales: 3 pts (10% × 30).
- Subtotal económico: 30 pts.

### 10.4 Umbrales

- Apto para PoC: ≥ 70/100 + todos eliminatorios verdes.
- Wildcard: 65-69/100 con plan de mitigación firmado.
- Rechazado: < 65/100 O cualquier eliminatorio rojo.

### 10.5 Empate Técnico

- Desempate: (1) mayor C (Cumplimiento), (2) mayor capacidad de integración con CBS (B), (3) mejor TCO, (4) mejor cronograma de integración.

---

## 11. Proceso de RFP — Instrucciones para el Vendor

### 11.1 Cronograma

| Hito | Fecha |
|------|-------|
| Envío del RFP a vendors invitados (NDA firmado) | 2026-08-15 |
| Sesión informativa | 2026-08-22 |
| Q&A | 2026-08-15 – 2026-09-30 |
| Cierre del RFP | 2026-11-15 |
| Apertura administrativa | 2026-11-16 – 2026-11-22 |
| Scoring | 2026-11-23 – 2026-12-15 |
| Demos + PoC (top-3) | 2026-12-15 – 2027-01-15 |
| Reuniones de referencia | 2027-01-15 – 2027-01-31 |
| Recomendación Comité de Tecnología | 2027-02-05 |
| Decisión final JD | 2027-02-15 |
| Adjudicación + negociación | 2027-02-16 – 2027-03-15 |
| Contraloría dictamen | 2027-03-15 – 2027-03-30 |
| Firma del contrato | 2027-03-31 |

### 11.2 Formato

- Español; PDF firmado digitalmente.
- 3 sobres separados.
- Validez 180 días.

---

## 12. Apéndices

### Apéndice A — Vendors Invitados

| Vendor | Razón de invitación |
|--------|---------------------|
| Microsoft Dynamics 365 F&O | Best fit con preferencia Azure del banco (BR-014); Entra ID SSO nativo |
| Oracle Fusion Cloud ERP | Precedente Bladex banca; NIIF 9/16 + IAS 21 nativos; sinergia con FLEXCUBE/FCCM si Oracle gana CBS/AML |
| SAP S/4HANA Public Cloud Edition | Tier-1 global banking; cobertura máxima — pese a descarte verbal del banco se invita objetivamente para mitigar R-026 |
| Infor CloudSuite Financials | Tier-2 con TCO menor + alternativa de competencia |
| Oracle NetSuite (wildcard) | Cloud-native; alternativa de TCO bajo |

> **Vendor no invitado**: Workday Financial Management — no cumple E-1 (soberanía objetiva) ni E-15 (timeline para Acuerdo 1-2026). Memo justificativo en audit trail.

### Apéndice B — Documentos Suministrados

| Doc | Acceso |
|-----|--------|
| ARC-001-REQ-v2.0.md (FRC, NFR, INT relevantes) | Bajo NDA |
| ARC-001-EVAL-v2.0.md (eliminatorios + ponderación ERP) | Bajo NDA |
| ARC-000-PRIN-v1.1.md | Público |
| ARC-001-RSCH-v2.0.md (TCO referencia ERP) | Bajo NDA |
| tech-notes/erp-cbs-integration-patterns.md | Bajo NDA |

### Apéndice C — Contactos

| Rol | Contacto |
|-----|----------|
| Líder del SOW ERP | CFO + Aldo Ríos |
| PMO | [PENDING] |
| Asesores externos | GFT + SIA Partners |
| Auditoría Interna | [PENDING] |
| Legal | [PENDING] |

---

## External References

| Doc ID | Descripción |
|--------|-------------|
| ARC-001-REQ-v2.0 | Requisitos del programa (193 reqs, incluye FRC del ERP) |
| ARC-001-RISK-v2.0 | Riesgos del programa (R-024 ERP Crítico) |
| ARC-001-RSCH-v2.0 | Research de vendors (ERP shortlist + TCO) |
| ARC-001-EVAL-v2.0 | Marco de Evaluación (eliminatorios + ponderación ERP) |
| ARC-001-SOBC-v2.0 | Business Case del programa |
| ARC-000-PRIN-v1.1 | 21 principios |
| ARC-001-SOW-CBS-v1.0 | SOW track CBS (coordinación inter-RFP) |
| ARC-001-SOW-AML-v1.0 | SOW track AML (coordinación inter-RFP) |
| tech-notes/erp-cbs-integration-patterns.md | Patrones de integración ERP-CBS |

---

**Generated by**: ArcKit `/arckit:sow` command
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Reemplazo del Core Banking + ERP + AML (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: SOW formal para RFP ERP (2 de 3 RFPs coordinados). Track NUEVO en el programa post-v2.0 — emerge de BR-013 (el CBS no incluirá GL completo). Contrato Hybrid; ponderación 70% Técnico / 30% Costo; 10 eliminatorios; shortlist Dynamics 365 + Oracle Fusion + SAP S/4HANA + Infor + NetSuite (wildcard).
