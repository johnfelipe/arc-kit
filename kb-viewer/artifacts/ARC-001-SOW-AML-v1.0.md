# Statement of Work (SOW) — Motor AML Externo con IA y APIs en Tiempo Real — Caja de Ahorros de Panamá

> **Documento legalmente vinculante para procurement bajo Ley 22 de Contrataciones Públicas de Panamá. Constituye el RFP formal para la categoría AML.**

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-SOW-AML-v1.0 |
| **Document Type** | Statement of Work (RFP — Motor AML/CFT externo con IA en tiempo real) |
| **Project** | Reemplazo del Core Banking + ERP + AML — Caja de Ahorros, Panamá (Project 001) |
| **RFP Track** | **AML** — Anti-Money Laundering (3 de 3 RFPs coordinados) |
| **Classification** | OFFICIAL-SENSITIVE |
| **Status** | DRAFT |
| **Version** | 1.0 |
| **Created Date** | 2026-06-11 |
| **Last Modified** | 2026-06-11 |
| **Review Date** | 2026-07-11 |
| **Owner** | Cumplimiento + Aldo Ríos — Gerencia de Innovación |
| **Reviewed By** | PENDING — Auditoría Interna, Legal, CISO, TI, Cumplimiento, Riesgos |
| **Approved By** | PENDING — Comité de Tecnología; Junta Directiva |
| **Distribution** | Vendors invitados bajo NDA; JD; Comité de Tecnología; Comité de Evaluación; Auditoría Interna; UAF (informativo); SBP (informativo) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-06-11 | ArcKit AI | Creación inicial del SOW formal para el RFP AML. Track NUEVO en el programa — emerge de la decisión arquitectónica de v2.0 (FR-048 revisado — el monitoreo AML ya NO se embeberá en el CBS sino que será un motor externo con IA). **Urgencia adicional**: el proveedor AML actual sale de soporte en 2026 (R-023 Alto — score 16 inherente). Integra los 8 eliminatorios aplicables a AML del EVAL v2.0 (E-1, E-5, E-6, E-8, E-9, E-10, E-11, E-12, E-15) y la ponderación específica AML (Encaje Funcional AML 30 + IA/Tiempo Real/APIs 25 + Cumplimiento Acuerdo 1-2026 + UAF + KYC 15 + Referencias LatAm 10 + Despliegue/Integración 10 + Comercial 10). Contrato Hybrid; ponderación 70% Técnico / 30% Costo. Shortlist desde RSCH v2.0: NICE Actimize, Hawk:AI, Oracle FCCM (+ wildcards ComplyAdvantage, Featurespace ARIC). | PENDING | PENDING |

---

## 1. Resumen Ejecutivo

### 1.1 Identificación del Proceso

| Concepto | Detalle |
|----------|---------|
| **Comprador** | Caja de Ahorros (CAP) — banco estatal panameño bajo Ley 20 de 1975 |
| **Proceso** | Procedimiento abierto bajo Ley 22 de Contrataciones Públicas |
| **Categoría** | Adquisición e implementación de Motor AML/CFT externo con IA, integración por APIs en tiempo real, ROS a UAF, KYC con Panadata, cumplimiento Acuerdo SBP 1-2026 |
| **Modalidad contractual** | Hybrid — Fixed-price para licencias + implementación con tope ±10% / T&M para change requests post go-live |
| **Plazo del proceso** | RFP abierto 6 semanas; respuesta + 4 semanas demos + 2 semanas referencias + selección |
| **Valor estimado del contrato** | B/. 13–25M a 7 años (TCO AML aislado — referencia RSCH v2.0); ~B/. 19M en el TCO blendado recomendado del programa |
| **Idioma** | Español |

### 1.2 Por qué un motor AML externo

El RFI v1.0 emitido en junio 2026 [DOC-RFI-001 §2.2] y las sesiones presenciales [DOC-SES-006, DOC-SES-009 §10.4] establecen que el monitoreo AML/PLD **NO se embebe en el CBS** sino que se externaliza:

1. El proveedor actual (basado en monitoreo batch con desfase 1 día) **deja de dar soporte en 2026** [DOC-SES-006]. Sin reemplazo, el banco queda sin AML y en falta con UAF y SBP.
2. El nuevo monitoreo será un **motor externo con IA explicable** e integración por APIs en tiempo real para procesar eventos del CBS con latencia < 200 ms y soportar **bloqueo bidireccional** (FR-048).
3. El nuevo motor debe cumplir el **Acuerdo SBP 1-2026** (Resolución SBP-JD-0001-2026 del 16-ene-2026) con sus plazos discretos: **Art. 25 §1 vigencia 31-ene-2027**; **Art. 14 vigencia 30-jun-2027** (beneficiario final ≥ **10%** + geolocalización inferencial digital).
4. El motor se integra con Panadata (KYC actual) y con SISCARD (visión 360° del cliente).

El RFP AML corre **en paralelo coordinado** al RFP CBS y al RFP ERP. **R-023 (AML externo no listo) Alto inherente** es el riesgo mitigado por este SOW.

### 1.3 Objetivos del SOW AML

1. Reemplazar el sistema AML actual antes del fin de soporte 2026.
2. Cumplir el Acuerdo SBP 1-2026 en plazos discretos.
3. Recibir eventos transaccionales del CBS en streaming en tiempo real con latencia < 200 ms.
4. Bloqueo bidireccional: el motor instruye al CBS para detener una transacción antes de la liquidación.
5. Reducir falsos positivos significativamente (objetivo: ≥ 50% reducción frente al sistema actual) mediante IA explicable.
6. Generar ROS a la UAF con orquestación del workflow.
7. Soportar análisis de **beneficiario final ≥ 10%** con integración a Panadata.
8. Soportar **geolocalización inferencial** (no solo GPS — combinando IP+ASN, dispositivo/UA, comportamiento).

---

## 2. Scope of Work

### 2.1 Alcance del SOW (En scope)

1. **Software y licencias del motor AML** — módulos: monitoreo transaccional con IA, KYC, sanctions screening (OFAC, ONU, listas internas, SBP), beneficiario final, geolocalización inferencial, risk scoring centralizado, workflow de ROS, generación de evidencia auditable.

2. **Implementación end-to-end**:
   - Despliegue en territorio panameño (on-premise CAP o cloud regional con presencia panameña — definido por dictamen Legal).
   - Configuración del motor para los productos del banco (cuentas, créditos, transferencias, cartas de crédito, factoring).
   - Integración con el **CBS** mediante streaming de eventos (Kafka, REST, o equivalente) con latencia < 200 ms.
   - **Bloqueo bidireccional**: el motor envía instrucción al CBS para detener una transacción antes de la liquidación.
   - Integración con **Panadata** (KYC actual del banco).
   - Integración con el **bus IBM MQ** existente para eventos legacy.
   - Integración con **Microsoft Entra ID** (SSO).
   - Integración con el **Data Lake AWS + Snowflake** para enriquecimiento analítico.
   - Integración con la **UAF** para envío automatizado de ROS.

3. **Migración del sistema AML actual** — extracción de configuración de reglas existentes; mapeo a nuevas reglas IA; corrida paralela ≥ 60 días; preservación de evidencia histórica para inspecciones SBP.

4. **Documentación funcional y técnica completa en español**.

5. **Capacitación certificada en español** — para Cumplimiento, Riesgos, TI, Operaciones (~200 personas).

6. **Soporte L1/L2/L3 24/7 en español** con SLA contractual.

7. **Mantenimiento evolutivo** — adaptación a nuevos Acuerdos SBP y reglas regulatorias sin cobros extraordinarios; actualización continua de modelos IA con nuevas tipologías de fraude/AML.

8. **Servicios profesionales** para discovery + diseño + implementación + paralelo + go-live + estabilización + tuning de modelos IA.

9. **Calibración de modelos IA** — durante los primeros 12 meses post go-live para reducir falsos positivos al objetivo establecido.

### 2.2 Fuera de Alcance del SOW AML

- **CBS**: track separado — ver `ARC-001-SOW-CBS-v1.0.md`. El CBS expone eventos al motor AML.
- **ERP**: track separado — ver `ARC-001-SOW-ERP-v1.0.md`. El ERP expone eventos contables relevantes a AML.
- **Panadata**: contrato KYC existente con el banco — se integra, no se reemplaza en Fase 1.
- **Investigación forense post-evento**: cubierto por procesos de Cumplimiento + SBP/UAF — fuera del SOW.

### 2.3 Supuestos

1. El proveedor AML actual extiende soporte transicional 12 meses post-decisión.
2. El RFP CBS estará en paralelo y el vendor CBS expone eventos vía streaming.
3. El dictamen Legal de soberanía habrá emitido respuesta antes de la firma.

### 2.4 Restricciones

1. **Soberanía de datos** (BR-006).
2. **TCO con tope ±10%** (BR-003).
3. **Plazos regulatorios**: vendor cuyo cronograma no entregue Acuerdo 1-2026 Art. 14 antes del 30-jun-2027 queda descalificado (E-15).
4. **Plazos del proyecto**: el motor AML DEBE estar operativo **antes del fin de soporte del proveedor actual** — alineado al go-live del CBS.
5. **Ley 22**.
6. **Idioma**: español.

### 2.5 Dependencias

| Dependencia | Owner | Plazo |
|-------------|-------|-------|
| Vendor CBS expone eventos vía streaming | RFP CBS | Pre-go-live AML |
| Dictamen Legal de soberanía | Legal CAP | Pre-firma de contrato |
| Continuidad de Panadata | Contrato KYC actual | Vida del contrato AML |
| Extensión soporte AML actual 12 meses | Negociación CAP-proveedor actual | Pre-firma de contrato AML |

---

## 3. Marco Regulatorio Aplicable

| Marco | Ámbito |
|-------|--------|
| **Ley 20 de 1975** | Ley orgánica de CAP |
| **Ley 22 de Contrataciones Públicas** | Proceso |
| **Acuerdo SBP 1-2026** | AML/CFT/FPADM (Resolución SBP-JD-0001-2026); Art. 25 §1 vigencia 31-ene-2027; Art. 14 vigencia 30-jun-2027 (beneficiario final ≥ 10% + geolocalización inferencial digital) |
| **Ley 23 de 2015** | Prevención AML/FT + DJTE ≥ B/. 10,000 |
| **Procedimiento UAF** | ROS / RAS según procedimiento UAF vigente |
| **FATCA / CRS** | Identificación de US persons / reportables CRS |
| **Ley 81 de Panamá** | Protección de datos personales |
| **FATF Recommendations** | Mejores prácticas internacionales |

---

## 4. Requisitos del Producto

### 4.1 Business Requirements (BR) — MUST_HAVE

| ID | Requisito |
|----|-----------|
| BR-002 | Cumplimiento regulatorio nativo SBP / UAF / SEI / Acuerdo 1-2026 |
| BR-006 | Soberanía de datos |
| BR-007 | Contratación pública sin observaciones |
| BR-003 | TCO con tope ±10% |
| BR-009 | Capacitación en español |

### 4.2 Functional Requirements (FR) — MUST_HAVE

| ID | Requisito |
|----|-----------|
| FR-048 (REV v2.0) | Recepción de eventos transaccionales en streaming desde CBS; bloqueo bidireccional; latencia < 200 ms |
| FR-049 | Generación y envío de ROS a la UAF orquestado por el motor con datos del CBS |
| FR-050 | FATCA / CRS reportería nativa |
| FR-051 | Detección y manejo de PEP — bases actualizadas ≥ diario |
| FR-052 | Beneficiario final ≥ **10%** para personas jurídicas — análisis automatizado de capas societarias con Panadata |
| FR-053 | Geolocalización inferencial (no solo GPS — combinación IP+ASN, dispositivo/UA, comportamiento) |
| FR-054 | DJTE ≥ B/. 10,000 — instrucción al CBS para bloqueo hasta completar declaración |
| FR-046 | KYC con integración a Panadata + listas restrictivas (PEP, OFAC, ONU, SBP, internas) |
| FR-047 | KYC simplificado para "Una Cuenta Para Todos" y Caja Amiga con reglas parametrizables |

**Capacidades funcionales del motor AML (FRC-AML)**:

- **FRC-A1**: Recepción de **streams** de eventos transaccionales del CBS en tiempo real (Kafka, REST, eventos webhook, o equivalente) con throughput ≥ 5,000 TPS.
- **FRC-A2**: Procesamiento con **IA explicable** (XAI) — reducción de falsos positivos ≥ 50% frente al sistema actual con explicación auditable de cada decisión.
- **FRC-A3**: **Bloqueo bidireccional** — el motor envía instrucción al CBS (allow / hold / block) con latencia total < 200 ms (NFR-P-005).
- **FRC-A4**: **Risk scoring centralizado** — no rule-only; modelos calibrados por segmento, producto, canal, geografía.
- **FRC-A5**: **Beneficiario final ≥ 10%** con análisis de capas societarias automatizado e integración con Panadata.
- **FRC-A6**: **Geolocalización inferencial** — captura y combinación de IP+ASN, dispositivo/UA, GPS si disponible, comportamiento de sesión; persistencia como atributo del evento.
- **FRC-A7**: **Workflow de ROS** automatizado con escalamiento y aprobación documentada; firma digital; envío a la UAF conforme procedimiento vigente.
- **FRC-A8**: **Auditabilidad inmutable** de decisiones — WORM o equivalente (DR-018); evidencia disponible para Auditoría Interna y SBP en inspección.
- **FRC-A9**: **Listas restrictivas** integradas (PEP, OFAC, ONU, SBP, internas, UAF) con actualización ≥ diaria.
- **FRC-A10**: **Sandbox + simulador** para pruebas y backtesting.
- **FRC-A11**: **APIs REST** documentadas (OpenAPI) + soporte de eventos asincrónicos (AsyncAPI).
- **FRC-A12**: **Configuración por usuario de negocio** de reglas, umbrales, listas, escalamiento — sin código del vendor.
- **FRC-A13**: **Dashboards en español** para Cumplimiento.
- **FRC-A14**: **DJTE Ley 23/2015** — soporte para bloqueo automático de transacciones ≥ B/. 10,000 hasta completar la Declaración Jurada.

### 4.3 Non-Functional Requirements (NFR) — MUST_HAVE

| ID | Métrica |
|----|---------|
| NFR-P-005 | Latencia transaccional añadida por evaluación AML < 200 ms |
| NFR-A-002 | Disponibilidad ≥ 99.95% mensual |
| NFR-A-004 | RTO ≤ 15 min, RPO ≤ 1 min |
| NFR-A-005 | Topología activo-activo o activo-pasivo |
| NFR-SEC-001..010 | Seguridad completa |
| NFR-SEC-011 | SSO Entra ID + SAML/OAuth/OIDC/LDAP |
| NFR-SEC-013 | SoD (separación analista vs supervisor de ROS) |
| NFR-SEC-014 | Permisos a nivel campo + enmascaramiento |
| NFR-SEC-015 | Recertificación periódica automática |
| NFR-C-001 | Cumplimiento Acuerdo 1-2026 + Ley 23/2015 + FATCA + CRS |
| NFR-C-002 | Reportería UAF AML/FT |

### 4.4 Integration Requirements (INT) — MUST_HAVE

| ID | Sistema |
|----|---------|
| INT-018 | CBS — streaming + bloqueo bidireccional |
| INT-006 | UAF — envío de ROS orquestado |
| INT-023 | Panadata (KYC actual) |
| INT-022 | SISCARD (vista 360° del cliente, incluyendo tarjetas) |
| INT-013 | Bus IBM MQ + API Gateway |
| INT-026 | Microsoft Entra ID (SSO) |
| INT-027 | Data Lake AWS + Snowflake |
| INT-016 | FATCA — IRS |
| INT-017 | CRS — OCDE |

### 4.5 Cumplimiento del Acuerdo SBP 1-2026

El vendor seleccionado DEBE entregar:

- **Art. 25 §1 — vigencia 31-ene-2027**: regla específica de identificación en producción al menos en paralelo con el sistema actual.
- **Art. 14 — vigencia 30-jun-2027**: beneficiario final ≥ **10%** + geolocalización inferencial digital — nativo en el motor y en producción.

**Vendors cuyo cronograma propuesto no entregue Art. 14 antes del 30-jun-2027 quedan descalificados** (E-15).

### 4.6 Migración del Sistema AML Actual

- **Corrida paralela ≥ 60 días pre-corte** con el sistema actual.
- Reducción de falsos positivos demostrada antes del corte.
- Preservación de evidencia histórica para inspecciones SBP del último año.
- **Extensión del soporte del proveedor actual 12 meses post-decisión** (cláusula negociada por CAP separadamente).

---

## 5. Deliverables

| # | Deliverable | Aceptación | Plazo (T = firma) |
|---|-------------|------------|---------------------|
| D-01 | Diseño Funcional Detallado (DFD) | Aprobado por Cumplimiento + CISO + TI | T+2 meses |
| D-02 | Diseño de Arquitectura (HLD + DLD) | Aprobado por Comité de Arquitectura | T+3 meses |
| D-03 | Plan de Migración del AML actual | Aprobado por Steering Committee | T+3 meses |
| D-04 | Integración con CBS demostrada (streaming + bloqueo bidireccional < 200 ms) | Pruebas E2E con dataset proporcionado por el banco | T+6 meses |
| D-05 | Configuración de reglas + modelos IA + integración Panadata | Aprobado por Cumplimiento | T+8 meses |
| D-06 | Workflow de ROS a UAF probado | Aprobado por Cumplimiento + UAF (informativo) | T+10 meses |
| D-07 | Beneficiario final ≥ 10% + geolocalización inferencial demostrados | Aprobado por Cumplimiento | T+10 meses |
| D-08 | Corrida paralela ≥ 60 días pre-corte con sistema actual | Reducción de falsos positivos ≥ 50% demostrada | T+11-12 meses |
| D-09 | Pruebas de rendimiento + seguridad + DR | Métricas cumplen NFR | T+12 meses |
| D-10 | Documentación completa en español | Aprobada por Operaciones + TI | T+13 meses |
| D-11 | Capacitación certificada en español | 100% del personal clave certificado | T+14 meses |
| D-12 | Go-live coordinado | Aprobado go/no-go por Cumplimiento + CISO + JD | T+14 meses |
| D-13 | **Cumplimiento Acuerdo 1-2026 Art. 14** | Funcionalidad operativa antes de 30-jun-2027 | 2027-Q2 |
| D-14 | Calibración de modelos IA (12 meses) | Reducción acumulada de falsos positivos | T+14 a T+26 meses |
| D-15 | Estabilización + warranty (90 días) | Sin incidentes P1 críticos | T+17 meses |
| D-16 | Reporte final + handover a Cumplimiento | Aprobado por JD | T+18 meses |

---

## 6. Cronograma y Hitos Clave

| Hito | Fecha objetivo |
|------|-----------------|
| RFP emitido | 2026-08-15 |
| Cierre del RFP | 2026-11-15 |
| Demos + PoC (top-3) | 2026-11-16 – 2026-12-31 |
| Selección final por JD | 2027-01-31 |
| Firma del contrato | 2027-03-31 |
| **Cumplimiento Acuerdo 1-2026 Art. 25 §1** | **2027-01-31** (vía sistema actual extendido) |
| Diseño + HLD/DLD | T+3 meses |
| Plan de Migración firmado | T+3 meses |
| Integración con CBS demostrada | T+6 meses |
| Corrida paralela ≥ 60 días | T+10 a T+12 meses |
| **Cumplimiento Acuerdo 1-2026 Art. 14** | **2027-06-30** |
| Go-live | 2028-Q1 (alineado con CBS Banda 1) |
| Calibración modelos IA | 2028-Q1 a 2029-Q1 |
| Estabilización + warranty | 2028-Q2 |
| Operación productiva → contrato 7 años | T+17 meses → T+84 meses |

---

## 7. Vendor Qualifications (Eliminatorios Pass/Fail)

| ID | Criterio | Aplica |
|----|----------|--------|
| E-1 | Soberanía de Datos en Territorio Panameño | ✓ |
| E-5 | Soporte 24/7 en Español con SLA Medible | ✓ |
| E-6 | Cumplimiento Acuerdo SBP 1-2026 (AML/CFT/FPADM) | ✓ |
| E-8 | Mínimo 3 Referencias LatAm Verificables en Producción ≥ 12 Meses | ✓ |
| E-9 | Certificaciones Obligatorias (ISO 27001, ISO 27017 si cloud, SOC 2 Tipo II) | ✓ |
| E-10 | Estabilidad Financiera y Continuidad del Vendor (ingresos globales ≥ USD 30M AML AI-native / USD 100M enterprise) | ✓ |
| E-11 | Aceptación de las 15 Cláusulas Contractuales Obligatorias | ✓ |
| E-12 | Idoneidad Jurídica Bajo Ley 22 | ✓ |
| E-15 | Deliverable Acuerdo 1-2026 Art. 14 antes del 30-jun-2027 | ✓ |

**Cualquier fallo en cualquiera de los 9 eliminatorios descalifica al vendor.**

---

## 8. Proposal Requirements (Estructura Obligatoria)

3 sobres independientes (Administrativo, Técnico, Económico).

### 8.1 Sobre Administrativo

- Documentación legal de Panamá.
- NDA firmado.
- Certificaciones ISO 27001 + ISO 27017 (si cloud) + SOC 2 Tipo II.
- Estados financieros auditados últimos 3 años.
- Aceptación firmada de las 15 cláusulas.
- Lista de referencias LatAm.

### 8.2 Sobre Técnico

- Resumen ejecutivo (máx 8 págs).
- Respuesta a cada uno de los 9 eliminatorios con evidencia.
- Cobertura de los 14 FRC-AML + NFR + INT — tabla por ID.
- Arquitectura HLD con integración a CBS + Panadata + Entra ID + Data Lake + UAF.
- Cronograma con cumplimiento de Art. 14 antes de 30-jun-2027.
- Plan de migración del AML actual con corrida paralela.
- Plan de calibración de modelos IA durante 12 meses post-go-live.
- Plan de capacitación en español.
- Equipo propuesto + CVs.
- Casos de éxito (≥ 3 referencias LatAm AML banking ≥ 12 meses).
- Métricas comparables de reducción de falsos positivos en clientes anteriores.
- Plan de gestión de riesgos.

### 8.3 Sobre Económico

- Precio total a 7 años con desglose CAPEX (años 1-3) / OPEX (años 4-7):
  - Licenciamiento (por usuario / por transacción / suscripción).
  - Implementación inicial (precio fijo).
  - Migración del AML actual.
  - Servicios profesionales (calibración IA).
  - Soporte y mantenimiento anual.
- Cláusula de tope ±10% firmada.
- TCO a 7 años con sensibilidad sobre volumen transaccional.
- Costos de salida.

---

## 9. Términos Contractuales

### 9.1 Cláusulas Obligatorias (las 15 — vendor AML acepta)

1. Residencia de datos en Panamá.
2. SLA con penalizaciones.
3. TCO con tope ±10%.
4. Cumplimiento regulatorio continuo.
5. Auditabilidad por Contraloría + SBP en inspección.
6. Coordinación con proveedor AML actual durante migración.
7. Capacitación en español certificada.
8. Documentación en español.
9. Salida ordenada — portabilidad de datos.
10. Penalización por incumplimiento Acuerdo 1-2026 Art. 14 (30-jun-2027): 15% del valor total por mes de retraso.
11. Confidencialidad y Ley 81.
12. Anticorrupción y Ley 22.
13. Integración con CBS — streaming + bloqueo bidireccional < 200 ms con SLA específico.
14. (No aplica — el motor AML es el "externo").
15. **Coordinación inter-RFP** con vendor CBS + vendor ERP; sesiones trimestrales de integración.

### 9.2 Estructura de Pago (Hybrid)

| Hito | % del precio fijo |
|------|--------------------|
| Firma del contrato | 10% |
| Diseño + HLD/DLD aprobados | 10% |
| Integración con CBS demostrada (< 200 ms + bloqueo) | 15% |
| Configuración de reglas + modelos IA | 10% |
| Workflow de ROS a UAF probado | 10% |
| Beneficiario final ≥ 10% + geolocalización demostrados | 10% |
| Corrida paralela ≥ 60 días con reducción ≥ 50% falsos positivos | 15% |
| Capacitación certificada 100% | 5% |
| Go-live | 10% |
| Estabilización 90 días sin P1 críticos | 5% |
| **Total Fixed-price** | **100%** |

**T&M** para change requests > 5% del scope original.

**Soporte anual recurrente** años 1-7 con SLA y reducción del 10% si SLA promedio < 99.9%.

**Calibración de modelos IA**: incluida en el precio fijo durante los primeros 12 meses post go-live; T&M a partir del mes 13.

### 9.3 Aceptación

- D-01..D-03 (Diseño y plan): aprobación firmada por Comité de Arquitectura + Cumplimiento.
- D-04 (Integración CBS): pruebas E2E con dataset proporcionado por el banco; latencia < 200 ms verificada en condiciones de carga.
- D-08 (Paralelo): reducción de falsos positivos ≥ 50% demostrada con evidencia comparable.
- D-11 (Capacitación): 100% del personal clave certificado por examen.
- D-12 (Pase a producción): go/no-go con voto explícito de Cumplimiento + CISO + JD.
- D-13 (Acuerdo 1-2026): validación regulatoria + dictamen de Cumplimiento.
- D-15 (Warranty): 90 días sin incidentes P1 críticos.

### 9.4 Gestión de Cambios

Igual al SOW CBS y ERP — change requests > 5% requieren análisis de impacto + aprobación correspondiente.

### 9.5 Propiedad Intelectual

- Software del vendor: licencia perpetua durante la vida del contrato + 5 años post-terminación.
- Configuraciones de reglas + modelos IA entrenados con datos de CAP: propiedad compartida con uso exclusivo para CAP durante la vida del contrato + portabilidad documentada.
- Código fuente: escrow.
- Datos: propiedad exclusiva de CAP.

### 9.6 Garantías y Soporte

- Warranty: 12 meses post go-live.
- Soporte L1/L2/L3 24/7 en español durante toda la vida del contrato.
- Actualizaciones de versión mayor incluidas.
- Calibración de modelos IA incluida durante los primeros 12 meses.

### 9.7 Cláusulas de Terminación

- Igual al SOW CBS.
- Adicional: **terminación por descoordinación con CBS** que impida el cumplimiento del Acuerdo 1-2026: penalización 15%.

### 9.8 Auditoría

- Contraloría puede auditar.
- SBP en inspección — el motor debe exponer evidencia auditable de forma inmediata.
- UAF puede solicitar evidencia de cualquier ROS.
- Pen-tests anuales a cargo del vendor.

---

## 10. Evaluación de Propuestas

### 10.1 Ponderación

- **70% Técnico / 30% Costo**.

### 10.2 Distribución del Score Técnico (sobre 70 pts)

- A — Encaje Funcional AML: 21 pts (30% × 70).
- B — IA / Tiempo Real / APIs: 17.5 pts (25% × 70).
- C — Cumplimiento Acuerdo 1-2026 + UAF + KYC: 10.5 pts (15% × 70).
- D — Referencias LatAm: 7 pts (10% × 70).
- E — Despliegue / Integración: 7 pts (10% × 70).
- Subtotal técnico: 63 pts → escalado a 70.

### 10.3 Distribución del Score Económico (sobre 30 pts)

- F.1 — TCO 7 años en banda B/. 13–25M con cláusula ±10%: 12 pts.
- F.2 — Pricing transparente con tope: 9 pts.
- F.3 — Modelo de licenciamiento adaptable (por transacción / por usuario / suscripción): 6 pts.
- F.4 — Servicios profesionales (incluida calibración IA): 3 pts.
- Subtotal económico: 30 pts.

### 10.4 Umbrales

- Apto para PoC: ≥ 70/100 + todos eliminatorios verdes.
- Wildcard: 65-69/100 con plan de mitigación.
- Rechazado: < 65/100 O cualquier eliminatorio rojo.

### 10.5 Empate Técnico

- Desempate: (1) mayor B (IA / Tiempo Real), (2) mayor capacidad demostrada de cumplimiento Art. 14 (C), (3) mejor TCO, (4) mejor cronograma de implementación.

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
| Hawk:AI | Best fit con FR-048 (streaming + bloqueo bidireccional + IA explicable + Acuerdo 1-2026); reducción 70% falsos positivos; TCO 40-50% menor que enterprise |
| NICE Actimize | Líder #1 mindshare AML 16.3%; usado por > 100 bancos top; mitigación enterprise; track record SBP |
| Oracle FCCM | Sinergia stack Oracle si CBS o ERP es Oracle; top-3 mindshare; rule base extensa |
| ComplyAdvantage (wildcard) | AI-native challenger; menos track record SBP pero TCO bajo |
| Featurespace ARIC (wildcard) | AI-native especializado fraude + AML |

> **Vendors no invitados** con memo justificativo: SAS AML (cumple objetivamente pero el banco prefiere AI-native por preferencia explícita de IA con XAI — documentado), FICO Siron/Tonbeller (igual).

### Apéndice B — Documentos Suministrados

| Doc | Acceso |
|-----|--------|
| ARC-001-REQ-v2.0.md (FR-046..054, FRC-AML, NFR, INT) | Bajo NDA |
| ARC-001-EVAL-v2.0.md (eliminatorios + ponderación AML) | Bajo NDA |
| ARC-000-PRIN-v1.1.md | Público |
| ARC-001-RSCH-v2.0.md (TCO referencia AML) | Bajo NDA |
| tech-notes/aml-real-time-streaming-patterns.md | Bajo NDA |
| tech-notes/acuerdo-1-2026-implementation.md | Bajo NDA |

### Apéndice C — Contactos

| Rol | Contacto |
|-----|----------|
| Líder del SOW AML | Cumplimiento + Aldo Ríos |
| PMO | [PENDING] |
| Asesores externos | GFT + SIA Partners |
| Auditoría Interna | [PENDING] |
| Legal | [PENDING] |

---

## External References

| Doc ID | Descripción |
|--------|-------------|
| ARC-001-REQ-v2.0 | Requisitos del programa (FR-046..054 AML; FRC-AML) |
| ARC-001-RISK-v2.0 | Riesgos del programa (R-023 AML Alto) |
| ARC-001-RSCH-v2.0 | Research de vendors (AML shortlist + TCO) |
| ARC-001-EVAL-v2.0 | Marco de Evaluación (eliminatorios + ponderación AML) |
| ARC-001-SOBC-v2.0 | Business Case del programa |
| ARC-000-PRIN-v1.1 | 21 principios |
| ARC-001-SOW-CBS-v1.0 | SOW track CBS (coordinación inter-RFP) |
| ARC-001-SOW-ERP-v1.0 | SOW track ERP (coordinación inter-RFP) |
| tech-notes/aml-real-time-streaming-patterns.md | Patrones de streaming en tiempo real para AML |
| tech-notes/acuerdo-1-2026-implementation.md | Implementación de Acuerdo 1-2026 (umbral 10%, plazos) |

---

**Generated by**: ArcKit `/arckit:sow` command
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Reemplazo del Core Banking + ERP + AML (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: SOW formal para RFP AML (3 de 3 RFPs coordinados). Track NUEVO en el programa post-v2.0 — emerge de FR-048 revisado (monitoreo AML externo, no embebido en CBS). Urgencia adicional por fin de soporte del proveedor AML actual en 2026. Contrato Hybrid; ponderación 70% Técnico / 30% Costo; 9 eliminatorios; shortlist Hawk:AI + NICE Actimize + Oracle FCCM + ComplyAdvantage + Featurespace.
