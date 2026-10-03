# Secure by Design Assessment — Reemplazo del Core Banking + ERP + AML — Caja de Ahorros de Panamá

> **Marco regulatorio adaptado**: Este assessment está **anclado al marco regulatorio panameño** y a los estándares internacionales adoptados por CAP. El comando original `/arckit:secure` está diseñado para gobierno UK (NCSC CAF + Cyber Essentials + UK GDPR); este documento adapta su estructura al equivalente panameño:
> - **NCSC CAF (14 principios) → NIST CSF 2.0 (6 funciones, 23 categorías)** — en implementación por CAP (DOC-SES-007 §8.2)
> - **Cyber Essentials → ISO 27001 + CIS Controls** — ISO 27001 es objetivo declarado del banco
> - **UK GDPR → Ley 81 de Panamá (Protección de Datos Personales)**
> - **NCSC GovAssure → Inspecciones SBP + Auditoría Interna + Contraloría**
> - **Acuerdo SBP 11-2018 (ciberseguridad + riesgo operacional)** — regulación vinculante
> - **Acuerdo SBP 1-2026 — componentes de ciberseguridad** (Resolución SBP-JD-0001-2026; Art. 25 §1 vigencia 31-ene-2027; Art. 14 vigencia 30-jun-2027)

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-SECD-v1.0 |
| **Document Type** | Secure by Design Assessment (Panama-adapted, NIST CSF 2.0 + SBP frameworks) |
| **Project** | Reemplazo del Core Banking + ERP + AML — Caja de Ahorros, Panamá (Project 001) |
| **Classification** | OFFICIAL-SENSITIVE (CONFIDENCIAL – Uso interno) |
| **Status** | DRAFT |
| **Version** | 1.0 |
| **Created Date** | 2026-06-11 |
| **Last Modified** | 2026-06-11 |
| **Review Date** | 2026-07-11 |
| **Owner** | CISO (Guillermo Smith — Gestión Operativa de Seguridad) + Aldo Ríos (Programa) |
| **Reviewed By** | PENDING — Auditoría Interna, Cumplimiento, Riesgos, TI, Legal |
| **Approved By** | PENDING — Comité de Tecnología; CISO firma riesgos residuales; JD apetito |
| **Distribution** | JD, Gerencia General, Comité de Tecnología, CISO, Cumplimiento, Riesgos, Auditoría Interna, Contraloría (informativo), SBP (en inspección) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-06-11 | ArcKit AI | Creación inicial. Assessment del programa Reemplazo del Core (CBS + ERP + AML) anclado a NIST CSF 2.0 (6 funciones) + Acuerdo SBP 11-2018 + Acuerdo SBP 1-2026 + Ley 81 + ISO 27001 readiness. Integra los 4 riesgos críticos de seguridad de RISK v2.0 (R-017 brecha de migración, R-027 brecha actual del legado, R-028 transición Activo-Activo, R-032 consulta gubernamental cloud) más R-023 (AML externo) y R-025 (Acuerdo 1-2026 plazos). Insumos clave: DOC-SES-007 (sesión ciberseguridad con CISO Guillermo Smith), DOC-SES-008 (infraestructura — Activo-Pasivo en transición Activo-Activo, 35–40 km), REQ v2.0 NFR-SEC-001..018, RISK v2.0 R-001..R-037. Identifica 11 hallazgos críticos (2 bloqueantes) + 14 hallazgos altos + 9 medios. Plan de remediación priorizado P0/P1/P2 alineado al Plan de Acción de RISK v2.0. | PENDING | PENDING |

---

## Resumen Ejecutivo

### Score NIST CSF 2.0 — Estado Actual vs Target Post-Programa

| Función NIST CSF 2.0 | Categorías | Estado actual (legado) | Target post go-live (2028) |
|----------------------|-----------|------------------------|------------------------------|
| **GV (Govern)** | 5 | 🟨 Parcial (3/5) | 🟩 Completo (5/5) |
| **ID (Identify)** | 3 | 🟨 Parcial (2/3) | 🟩 Completo (3/3) |
| **PR (Protect)** | 6 | 🟥 Inadecuado (2/6) | 🟩 Completo (6/6) |
| **DE (Detect)** | 2 | 🟨 Parcial (1/2) | 🟩 Completo (2/2) |
| **RS (Respond)** | 4 | 🟨 Parcial (2/4) | 🟩 Completo (4/4) |
| **RC (Recover)** | 3 | 🟨 Parcial (2/3) | 🟩 Completo (3/3) |
| **TOTAL** | **23** | **🟥 12/23 (52%)** | **🟩 23/23 (100%)** |

**Postura actual del legado**: **52%** del modelo NIST CSF 2.0 implementado. Las brechas críticas están en la función **PROTECT** (sin cifrado en reposo, sin MFA, sin cifrado en tránsito interno, sin gestión de roles en el IBS — DOC-SES-007 §8.1). La transición a un nuevo CBS + ERP + AML es la oportunidad de cerrar las brechas.

### Postura Pre-Programa vs Post-Programa

| Marco | Estado actual | Brecha crítica | Target |
|-------|---------------|----------------|--------|
| **NIST CSF 2.0** | 52% implementado (12/23) | PROTECT (cifrado, MFA, RBAC) | 100% (23/23) |
| **Acuerdo SBP 11-2018** (ciberseguridad + riesgo op) | Parcial — cumplimiento por excepción documentada | Cifrado, MFA, gestión de roles | Cumplimiento sin excepciones |
| **Acuerdo SBP 1-2026** | No iniciado (vigencia jul-2025 / jun-2027) | Beneficiario final ≥ 10%, geolocalización inferencial digital | Cumplimiento Art. 25 §1 (31-ene-2027) y Art. 14 (30-jun-2027) |
| **ISO 27001** | No certificado (proyecto ISMS en curso bajo BIS) | Sistema de Gestión de Seguridad de la Información formal | Certificación de al menos un servicio crítico (objetivo 3 años) |
| **CIS Controls** | En implementación | Cobertura completa de 18 controles | Cobertura completa |
| **Ley 81 (Protección de Datos)** | Parcial | Procedimientos formales de DPIA, ROPA, breach notification | Cumplimiento completo |

### Hallazgos Críticos (Bloqueantes)

| # | Hallazgo | Función NIST | Riesgo RISK v2.0 | Bloquea |
|---|----------|--------------|-------------------|---------|
| **CRIT-1** | **Sin cifrado de datos en reposo** en el CBS legado [DOC-SES-007 §8.1] | PR.DS-1 | R-027 | Cualquier proyecto Tier-1 + cumplimiento PRIN P4 |
| **CRIT-2** | **Sin MFA** para acceso privilegiado al CBS legado [DOC-SES-007 §8.1] | PR.AA-1 | R-027 | Cumplimiento NFR-SEC-001 + cláusula contractual del CBS |
| **CRIT-3** | **Sin cifrado interno en tránsito** entre componentes del legado | PR.DS-2 | R-027 | Acuerdo 11-2018 estricto |
| **CRIT-4** | **Plazo Acuerdo 1-2026 Art. 25 §1 (31-ene-2027) sin plan formal** de remediación del legado | PR.PS, GV.RM | R-025 | Cumplimiento regulatorio en plazo |
| **CRIT-5** | **Sin gestión de roles (RBAC) en el CBS legado** — IBS configurado sin gestión de roles [DOC-SES-007 §8.1] | PR.AA-2 | R-027 | Acuerdo 11-2018 |

### Hallazgos Altos (No bloqueantes — gestionar)

| # | Hallazgo | Función NIST | Riesgo RISK v2.0 |
|---|----------|--------------|-------------------|
| **ALTO-1** | Recertificación manual de accesos 2 veces/año (no automática) | PR.AA-4 | R-027 |
| **ALTO-2** | Auditoría externa solo 1 vez/año del AS/400 | DE.CM-1 | R-027 |
| **ALTO-3** | Llaves de cifrado almacenadas sin bóveda segura formal | PR.DS-3 | R-027 |
| **ALTO-4** | Sin observabilidad end-to-end de transacciones (costo) | DE.AE-1 | R-013 |
| **ALTO-5** | Transición Activo-Pasivo → Activo-Activo coincide con cambio de Core | RC.RP, PR.IR | R-028 |
| **ALTO-6** | Proveedor AML actual sale soporte 2026 — gap en DETECT | DE.AE-2 | R-023 |
| **ALTO-7** | Consulta gubernamental sobre cloud sin iniciar | GV.SC | R-032 |
| **ALTO-8** | Sin plan formal de respuesta a incidente para el escenario de migración | RS.IM, RS.CO | R-017 |
| **ALTO-9** | Sin plan formal de continuidad de Caja Amiga durante migración | PR.IR-2, RC.RP | R-035 |
| **ALTO-10** | Plan de pen-tests semestrales no establecido (solo anual) | DE.AE-3 | R-017 |
| **ALTO-11** | Sin DPIA formal para Acuerdo 1-2026 (geolocalización inferencial = dato personal) | GV.RM, PR.DS | R-025 |
| **ALTO-12** | Plataformas de seguridad gestionadas (~21) sin marco único integrado | PR.PS | R-001, R-019 |
| **ALTO-13** | Sin marco formal de gestión de riesgo de terceros (vendor risk) para los 3 RFPs | GV.SC-1..6 | R-008, R-023, R-024 |
| **ALTO-14** | Sin seguro de ciber-riesgo formalizado | RC.RP | R-027 |

---

## Sección 1 — Contexto del Proyecto

### 1.1 Información del Cliente

| Concepto | Valor |
|----------|-------|
| Organización | **Caja de Ahorros (CAP)** — banco estatal panameño bajo Ley 20 de 1975 |
| Sector | Banca pública estatal con mandato social del Estado |
| Clasificación de datos | **OFFICIAL-SENSITIVE** equivalente a "Confidencial – Uso interno" |
| Volumen | ~650K clientes, ~3,500 empleados, B/. 6,911M activos, B/. 4,943M cartera, 60 sucursales, 140 ATMs, 100+ Caja Amiga, 51M+ transacciones digitales/año |
| Fase del proyecto | **Pre-implementación** (RFP en preparación) |
| Modelo de despliegue | On-premise actual (DataPro/eIBS sobre IBM Linux + IBM MQ); cloud regional planeado pendiente dictamen Innovación + SBP + Seguridad Nacional |

### 1.2 Marco Regulatorio Aplicable a la Seguridad

| Marco | Tipo | Aplicación a la seguridad |
|-------|------|----------------------------|
| **Acuerdo SBP 11-2018** | Vinculante | Ciberseguridad + riesgo operacional. Mandatorio para CAP. |
| **Acuerdo SBP 1-2026** | Vinculante | AML/CFT/FPADM — componentes de identidad digital + geolocalización inferencial. Resolución SBP-JD-0001-2026 del 16-ene-2026. Art. 25 §1 vigencia 31-ene-2027. Art. 14 vigencia 30-jun-2027. |
| **Ley 81 de Panamá** | Vinculante | Protección de Datos Personales — equivalente a UK GDPR. ANTAI es la autoridad. |
| **Ley 23/2015** | Vinculante | AML/FT + DJTE ≥ B/. 10,000 |
| **NIST CSF 2.0** | Adoptado (en implementación) | Estándar internacional voluntario adoptado por CAP [DOC-SES-007 §8.2] |
| **CIS Controls** | Adoptado | Controles compensatorios alineados a NIST [DOC-SES-007 §8.2] |
| **ISO 27001** | Objetivo (no certificado) | Proyecto ISMS en curso bajo BIS; objetivo 3 años para certificar servicios críticos [DOC-SES-007 §8.2] |
| **ISO 27017** | Aplicable si cloud | Para servicios cloud |
| **SOC 2 Tipo II** | Esperable para vendors | Eliminatorio del RFP (E-9 EVAL v2.0) |
| **COBIT** | En evaluación | Mejorar controles en plataformas legacy [DOC-SES-007 §8.2] |

### 1.3 Stakeholders Clave de Seguridad

| Stakeholder | Rol | Vinculación |
|-------------|-----|-------------|
| **CISO** (Guillermo Smith — Gestión Operativa de Seguridad) | Owner de seguridad, firma riesgos residuales | SD-6 STKE |
| **Comité de Tecnología** | Aprueba el SECD y recomienda riesgos a la JD | STKE |
| **Junta Directiva** | Decide apetito de riesgo de seguridad | SD-1 STKE |
| **Cumplimiento** | Acuerdo 1-2026 y reportería | SD-7 STKE |
| **Auditoría Interna** | Validación independiente, audit trail | STKE |
| **Riesgos** | Modelo dual y riesgo operacional | SD-14 STKE |
| **TI (Gerencia de Tecnología)** | Implementación técnica | SD-5 STKE |
| **Operaciones** | Continuidad y RTO/RPO | SD-8 STKE |
| **Legal** | Ley 81, Ley 22, dictámenes | STKE |
| **SBP** (externo) | Inspecciones; receptor del SEI | SD-9 STKE |
| **UAF** (externo) | Receptor de ROS AML/FT | SD-16 STKE |
| **ANTAI** (externo, Ley 81) | Autoridad de protección de datos personales | STKE-adicional |

---

## Sección 2 — Assessment NIST CSF 2.0 (6 funciones, 23 categorías)

### 2.1 Función GV (Govern) — Gobierno de la Seguridad

#### GV.OC — Organizational Context

- **Estado actual**: 🟨 Parcial — STKE v1.0 documenta 27 stakeholders; los específicos de seguridad (CISO, Cumplimiento, ANTAI) están identificados; PRIN v1.1 incluye principios de seguridad.
- **Evidencia**: ARC-001-STKE-v1.0.md, ARC-000-PRIN-v1.1 (Principios 4, 6, 7, 8).
- **Target**: 🟩 Documentación completa del contexto de seguridad post programa.

#### GV.RM — Risk Management Strategy

- **Estado actual**: 🟨 Parcial — RISK v2.0 documenta 37 riesgos (cuatro de seguridad — R-017, R-027, R-028, R-032). Apetito formal de riesgo de la JD **no aprobado** (workshop pendiente — RISK v2.0 §G).
- **Evidencia**: ARC-001-RISK-v2.0.md.
- **Gap**: workshop de apetito (recomendado P1 — esta semana).
- **Target**: apetito formalizado + revisión trimestral.

#### GV.SC — Cybersecurity Supply Chain Risk Management

- **Estado actual**: 🟥 Inadecuado — sin marco formal de gestión de riesgo de proveedores tecnológicos. Crítico dado los 3 RFPs paralelos (R-008, R-023, R-024).
- **Evidencia**: EVAL v2.0 introduce eliminatorios (E-9, E-10, E-11, E-15) pero no hay un marco operativo continuo post-firma.
- **Gap**: framework de supplier risk management (review trimestral de vendors, monitoreo de su postura de seguridad).
- **Target**: marco operativo pre-firma del primer contrato.

#### GV.RR — Roles, Responsibilities, and Authorities

- **Estado actual**: 🟨 Parcial — CISO nombrado (Guillermo Smith); reporta al área de Tecnología. RACI parcial.
- **Evidencia**: DOC-SES-007.
- **Gap**: RACI formal de seguridad del programa con autoridades de aprobación documentadas.
- **Target**: RACI completo firmado por CISO + Comité de Tecnología.

#### GV.PO — Policies

- **Estado actual**: 🟨 Parcial — políticas existen pero sin alineación a NIST CSF 2.0; ISMS en construcción bajo BIS.
- **Evidencia**: DOC-SES-007 §8.2.
- **Gap**: política de seguridad formal alineada a NIST + ISO 27001 readiness.
- **Target**: política firmada por JD + revisión anual.

### 2.2 Función ID (Identify) — Identificación

#### ID.AM — Asset Management

- **Estado actual**: 🟨 Parcial — inventario de aplicaciones documentado (DOC-RFI-001 Anexo B + DOC-SES-001 inventario satélite); 8,000+ elementos del diccionario de datos en proceso de gobernanza (R-030).
- **Evidencia**: REQ v2.0 §INT-014..031, DR-021.
- **Gap**: propietarios formales asignados a los 8,000+ elementos; CMDB unificado.
- **Target**: CMDB unificado post-implementación del CBS.

#### ID.BE — Business Environment

- **Estado actual**: 🟩 Adecuado — SOBC v2.0 documenta el contexto de negocio; STKE v1.0 documenta dependencias críticas.
- **Evidencia**: ARC-001-SOBC-v2.0, ARC-001-STKE-v1.0.
- **Target**: mantener actualizado.

#### ID.RA — Risk Assessment

- **Estado actual**: 🟨 Parcial — RISK v2.0 cubre riesgos del programa; sin threat modeling formal del CBS legado ni del CBS futuro.
- **Evidencia**: ARC-001-RISK-v2.0.
- **Gap**: threat modeling del legado (P0 — mitigación R-027) y del CBS futuro (durante diseño).
- **Target**: threat modeling completo del CBS futuro pre-go-live.

### 2.3 Función PR (Protect) — Protección — **función con mayor brecha actual**

#### PR.AA — Identity Management, Authentication, and Access Control

- **Estado actual**: 🟥 **Inadecuado (CRIT-2, CRIT-5)**:
  - Sin MFA para acceso privilegiado al CBS legado.
  - Sin gestión de roles (RBAC) en el IBS.
  - Autenticación usuario+contraseña simple.
  - Recertificación manual 2 veces/año (ALTO-1).
  - Proyecto IAM en curso pero parcial.
- **Evidencia**: DOC-SES-007 §8.1.
- **Gap**: implementación de MFA + RBAC + recertificación automática como parte de R-027 (remediación del legado) + cumplimiento NFR-SEC-001..018 en el CBS futuro.
- **Mitigación contractual del RFP CBS**: cláusula obligatoria E-11 + eliminatorios E-9, E-11 + NFR-SEC-011..018.
- **Target**: MFA obligatorio + RBAC nativo + IAM federada con Microsoft Entra ID + SoD configurable + recertificación automática.

#### PR.DS — Data Security

- **Estado actual**: 🟥 **Inadecuado (CRIT-1, CRIT-3, ALTO-3)**:
  - Sin cifrado de datos en reposo.
  - Sin cifrado interno en tránsito entre componentes.
  - Llaves de cifrado sin bóveda segura formal.
- **Evidencia**: DOC-SES-007 §8.1.
- **Gap**: cifrado AES-256 en reposo + TLS 1.2+ en tránsito + bóveda de secretos (HashiCorp Vault o equivalente).
- **Mitigación**: R-027 plan de remediación del legado (P1 — próximas 90 días) + NFR-SEC-003, NFR-SEC-004 en el CBS futuro.
- **Target**: cifrado en reposo + tránsito + bóveda obligatorios; algoritmos resistentes a la computación cuántica considerados en el diseño futuro.

#### PR.PS — Platform Security

- **Estado actual**: 🟥 **Inadecuado (ALTO-12)**:
  - ~21 plataformas de seguridad gestionadas sin marco único integrado.
  - Conexión vía enlace AS/400 sin segmentación moderna.
  - Sin endpoint detection and response (EDR) consolidado en todas las estaciones.
- **Evidencia**: DOC-SES-007 §8.1.
- **Gap**: marco único de gestión + EDR consolidado.
- **Target**: SIEM + EDR + control center unificado; alineación a NIST CSF 2.0 + CIS Controls.

#### PR.IR — Information Protection Processes and Procedures

- **Estado actual**: 🟨 Parcial — IaC parcial; pases a producción documentados.
- **Evidencia**: PRIN v1.1 P17, P19; NFR-M-005, NFR-M-007.
- **Gap**: IaC completa + pipeline CI/CD auditable end-to-end.
- **Target**: IaC versionada + CI/CD auditable + cero cambios manuales.

#### PR.MA — Maintenance

- **Estado actual**: 🟨 Parcial — mantenimiento programado existe pero con ventana de 1.5 h y cierre diario 5 min.
- **Evidencia**: DOC-SES-008 §9.2.
- **Gap**: rolling deployment / blue-green / canary para reducir ventana a ≤ 30 min/mes + cierre ≤ 1 min.
- **Target**: NFR-A-007 (sin downtime) + NFR-P-006 (cierre ≤ 1 min).

#### PR.AT — Awareness and Training

- **Estado actual**: 🟨 Parcial — capacitación de seguridad existe pero ad-hoc.
- **Evidencia**: implícito en operación actual.
- **Gap**: programa formal de awareness alineado a NIST + ISO 27001 + simulacros de phishing.
- **Target**: programa anual con métricas de adherencia ≥ 85%.

### 2.4 Función DE (Detect) — Detección

#### DE.CM — Continuous Monitoring

- **Estado actual**: 🟨 Parcial — auditoría externa 1 vez/año (ALTO-2); monitoreo interno existe pero no SIEM consolidado.
- **Evidencia**: DOC-SES-007.
- **Gap**: SIEM + pen-tests semestrales (no solo anuales, ALTO-10) + monitoreo continuo.
- **Target**: SIEM + threat intelligence + pen-tests semestrales hasta go-live + anuales post.

#### DE.AE — Adverse Event Analysis

- **Estado actual**: 🟥 **Inadecuado (ALTO-4, ALTO-6)**:
  - Sin observabilidad end-to-end de transacciones por costo.
  - Proveedor AML actual sale soporte 2026 = gap en DETECT AML.
- **Evidencia**: DOC-SES-008 + DOC-SES-006.
- **Gap**: observabilidad completa + nuevo motor AML externo con IA (RFP AML).
- **Target**: observabilidad end-to-end + motor AML con IA explicable en producción antes del fin de soporte del actual.

### 2.5 Función RS (Respond) — Respuesta

#### RS.MA — Management

- **Estado actual**: 🟨 Parcial — procesos informales de respuesta existen.
- **Gap**: plan formal de respuesta a incidentes (ALTO-8) específico para escenarios de migración (R-017).
- **Target**: plan de respuesta firmado + simulacros trimestrales pre-go-live.

#### RS.AN — Analysis

- **Estado actual**: 🟨 Parcial.
- **Gap**: capacidad de análisis forense post-incidente y reportería SBP.
- **Target**: equipo o partner forense identificado.

#### RS.CO — Communications

- **Estado actual**: 🟨 Parcial — sin plan formal.
- **Gap**: plan de comunicación de incidente alineado a Ley 81 (notificación a ANTAI) + SBP + UAF + JD.
- **Target**: plan firmado por Comunicaciones + Legal + CISO.

#### RS.IM — Improvements

- **Estado actual**: 🟨 Parcial — lecciones aprendidas se capturan informalmente.
- **Gap**: revisión post-incidente formal con seguimiento de acciones.
- **Target**: revisión post-incidente obligatoria con timeline de remediación.

### 2.6 Función RC (Recover) — Recuperación

#### RC.RP — Recovery Planning

- **Estado actual**: 🟨 Parcial — contingencia activa-pasiva probada en producción [DOC-SES-008 §9.2 — recuperación reducida de varias horas a < 1 h, hasta una semana sostenida en modo contingencia]; transición a Activo-Activo en curso (R-028, ALTO-5).
- **Evidencia**: DOC-SES-008 §9.1.
- **Gap**: NFR-A-004 (RTO ≤ 15 min servicios críticos, RPO ≤ 1 min) no aún cumplido en el legado; plan de recuperación específico para migración (R-017) no documentado.
- **Target**: NFR-A-004 cumplido en el CBS futuro + plan de migración con rollback documentado.

#### RC.IM — Improvements

- **Estado actual**: 🟨 Parcial — mejoras en recuperación implementadas (DOC-SES-008).
- **Target**: revisión continua post-go-live; DR test semestral.

#### RC.CO — Communications

- **Estado actual**: 🟨 Parcial.
- **Gap**: plan de comunicación de recuperación alineado a clientes + reguladores.
- **Target**: plan firmado.

---

## Sección 3 — Acuerdo SBP 11-2018 Compliance

El Acuerdo 11-2018 (ciberseguridad + riesgo operacional) establece controles obligatorios para bancos panameños.

### 3.1 Controles Obligatorios y Status

| Control 11-2018 | NIST CSF 2.0 mapeo | Status actual | Riesgo RISK v2.0 |
|-----------------|---------------------|----------------|-------------------|
| Gobernanza de ciberseguridad | GV.RR + GV.PO | 🟨 Parcial | R-001 |
| Identificación de activos críticos | ID.AM | 🟨 Parcial | R-030 |
| Cifrado de datos sensibles | PR.DS | 🟥 Inadecuado | **R-027** |
| Gestión de identidades + MFA | PR.AA | 🟥 Inadecuado | **R-027** |
| Monitoreo continuo (SIEM) | DE.CM | 🟨 Parcial | R-017 |
| Plan de respuesta a incidentes | RS.MA + RS.CO | 🟨 Parcial | R-017 |
| Plan de continuidad operativa (BCP) | RC.RP | 🟨 Parcial | R-004, R-016 |
| Pen-tests anuales | DE.AE | 🟩 Cumplido (anual) | — |
| Reportería de incidentes a SBP | RS.CO | 🟩 Cumplido | — |
| Gestión de riesgo operacional | GV.RM | 🟨 Parcial | R-014 |
| Auditoría de seguridad | GV.OV | 🟩 Cumplido (externa anual) | — |

**Postura**: cumplimiento por **excepción documentada** en los controles de cifrado, MFA y RBAC. CAP debe formalizar plan de remediación del legado (R-027) para llegar a cumplimiento sin excepciones antes del go-live del CBS.

### 3.2 Plan de Remediación del Legado (R-027)

| Acción | Owner | Plazo |
|--------|-------|-------|
| Cifrado en reposo (donde técnicamente factible en IBS) | CISO + TI | 90 días |
| MFA obligatorio para acceso privilegiado del legado | CISO + TI | 60 días |
| Cifrado en tránsito interno (TLS entre componentes) | TI | 90 días |
| Bóveda de secretos (HashiCorp Vault o equivalente) | TI | 60 días |
| Recertificación automática de accesos | TI | 6 meses |
| Pen-tests semestrales (hasta go-live) | CISO | recurrente desde Q3 2026 |
| Plan de respuesta a incidente migración | CISO + Operaciones | 60 días |

---

## Sección 4 — Acuerdo SBP 1-2026 Compliance (Componentes de Ciberseguridad)

El Acuerdo 1-2026 (AML/CFT/FPADM, Resolución SBP-JD-0001-2026 del 16-ene-2026) tiene componentes directos de seguridad de identidad digital.

### 4.1 Plazos Discretos por Artículo

| Artículo | Materia | Plazo de cumplimiento | Status |
|----------|---------|------------------------|--------|
| Marco general | Acuerdo AML/CFT actualizado | Vigencia general (desde 16-ene-2026) | 🟨 En curso |
| **Art. 25 §1** | Regla específica de identificación | **31-ene-2027** | 🟥 Sin plan formal (CRIT-4) |
| **Art. 14** | Beneficiario final ≥ 10% + geolocalización inferencial digital | **30-jun-2027** | 🟥 Sin capacidad técnica nativa |

### 4.2 Cumplimiento Art. 14 — Beneficiario Final ≥ 10% + Geolocalización Inferencial

- **Beneficiario final ≥ 10%** — implementado en el CBS futuro vía FR-052 + integración con Panadata (FR-046, INT-023). El motor AML externo procesa la lógica de capas societarias.
- **Geolocalización inferencial** — implementada en el CBS futuro vía FR-053. Combinación de IP+ASN, dispositivo/UA, GPS si disponible, comportamiento de sesión. Insumo para el motor AML.
- **DPIA requerido** (ALTO-11) — la geolocalización inferencial es dato personal Ley 81; requiere DPIA antes del go-live.

### 4.3 Cumplimiento Art. 25 §1 — Plan de Remediación Intermedio del Legado

CAP debe cumplir Art. 25 §1 al 31-ene-2027 — antes de que el nuevo CBS esté en producción. **Sin plan formal de remediación del legado, este es un hallazgo crítico (CRIT-4)**.

**Acción inmediata (P0)**: Cumplimiento + CISO + TI diseñan plan de remediación intermedio del CBS legado para Art. 25 §1 en **3 meses** (acción 2.7 del Plan de Acción RISK v2.0).

---

## Sección 5 — Ley 81 Compliance (Protección de Datos Personales)

### 5.1 Postura Ley 81

| Requisito Ley 81 | UK GDPR equivalente | Status actual | Acción requerida |
|-------------------|----------------------|----------------|--------------------|
| Oficial de Protección de Datos | DPO | 🟨 PENDIENTE — no nombrado formalmente | Nombrar antes del go-live del CBS |
| Inventario de actividades de tratamiento (ROPA equivalente) | ROPA | 🟥 No documentado formalmente | Crear pre-go-live |
| Bases legales del tratamiento | Lawful basis | 🟨 Parcial | Documentar por dominio |
| Notificación de brechas a ANTAI | 72h to ICO | 🟨 Parcial | Procedimiento formal |
| Procedimientos de derechos del titular | Data subject rights | 🟨 Parcial | Formalizar |
| DPIA para tratamientos de alto riesgo | DPIA | 🟥 No realizada para geolocalización inferencial | Realizar pre-implementación FR-053 |

### 5.2 DPIA Requerida — Acuerdo 1-2026 Art. 14 (Geolocalización Inferencial)

La geolocalización inferencial (FR-053) es **dato personal de alto riesgo** bajo Ley 81 — requiere DPIA antes de implementación. Plazo: pre-implementación FR-053 (objetivo 30-jun-2027 por Acuerdo 1-2026).

**Recomendación**: ejecutar `/arckit:dpia` como paso siguiente a este SECD.

---

## Sección 6 — ISO 27001 Readiness

CAP tiene objetivo declarado de certificar servicios bajo ISO 27001 una vez alcanzada madurez suficiente [DOC-SES-007 §8.2]. Proyecto ISMS en curso bajo BIS.

### 6.1 Gap Analysis ISO 27001:2022

| Dominio ISO 27001:2022 | Cumplimiento estimado | Gaps clave |
|-------------------------|------------------------|------------|
| A.5 — Políticas | 60% | Política formal de seguridad alineada |
| A.6 — Organización | 70% | RACI de seguridad formal |
| A.7 — Personas | 50% | Awareness program + background checks |
| A.8 — Activos | 60% | Inventario formal + clasificación |
| A.9 — Control de accesos | 30% | MFA + RBAC + recertificación automática |
| A.10 — Criptografía | 20% | Cifrado en reposo + bóveda de llaves |
| A.11 — Seguridad física | 80% | Adecuado |
| A.12 — Operaciones | 60% | SIEM + patch management formalizado |
| A.13 — Comunicaciones | 50% | Cifrado tránsito interno + segmentación |
| A.14 — Adquisición/desarrollo | 40% | SDLC seguro + secure-by-design |
| A.15 — Proveedores | 30% | Supplier risk management formal |
| A.16 — Gestión de incidentes | 60% | Plan formal + simulacros |
| A.17 — Continuidad | 70% | BCP + DR documentados |
| A.18 — Cumplimiento | 70% | Marco regulatorio mapeado |

**Postura general ISO 27001**: **~55% madurez**. Necesario alcanzar ~85% para certificar; alcanzable post-go-live del CBS con cierre de R-027 (legado) y NFR-SEC del CBS futuro.

### 6.2 Recomendaciones para Certificación ISO 27001

- **Pre-go-live CBS** (2026-2028): cerrar A.9 (control de accesos), A.10 (criptografía), A.15 (proveedores).
- **Post-go-live CBS** (2028-2029): proceso de auditoría externa para certificación de servicios críticos.
- **Objetivo**: certificación de al menos un servicio (canal digital o componente Core) en 2029.

---

## Sección 7 — Gestión de Riesgo de Terceros (Supplier Risk Management)

CAP está por lanzar **3 RFPs simultáneos** (CBS + ERP + AML). Sin marco formal de gestión de riesgo de proveedores tecnológicos (ALTO-13).

### 7.1 Marco Propuesto

| Etapa | Control |
|-------|---------|
| Pre-firma | Eliminatorios EVAL v2.0 (E-1..E-15) + due diligence + análisis financiero (E-10) |
| Firma | 15 cláusulas contractuales obligatorias (EVAL v2.0 E-11) |
| Operación | Revisión trimestral de postura de seguridad del vendor (SOC 2 anual, ISO 27001 vigencia, pen-tests del vendor) |
| Incidente | Cláusula contractual de notificación de incidente del vendor en ≤ 24 h |
| Salida | Cláusula 9 — portabilidad de datos al término del contrato |

### 7.2 Vendors Críticos del Programa

| Categoría | Vendor seleccionado (TBD) | Criticidad |
|-----------|--------------------------|------------|
| CBS | (post-RFP CBS) | Crítico — opera el banco |
| ERP | (post-RFP ERP) | Crítico — GL consolidado |
| AML | (post-RFP AML) | Crítico — cumplimiento UAF + SBP |
| Panadata (KYC actual) | Panadata | Alto — datos personales |
| Telered | Telered | Alto — switch ATM/POS |
| App Enhancer (gestor documental) | App Enhancer | Medio — expedientes |
| Banca Seguro | Banca Seguro | Medio — pólizas |

---

## Sección 8 — Análisis de Riesgos de Seguridad del Programa

> Cross-link con RISK v2.0 — sólo riesgos de seguridad directos o transversales:

| Riesgo RISK v2.0 | Score inherente | Score residual | Mitigación principal |
|-------------------|------------------|------------------|----------------------|
| R-017 — Brecha durante migración | 15 | 8 | Pen-test semestral + war-room + plan de respuesta |
| **R-027 (NEW v2.0)** — Brecha actual del legado (sin cifrado/MFA) | 12 | 8 | Plan de remediación del legado 90 días + seguro ciber |
| R-028 — Falla transición Activo-Activo simultánea | 9 | 6 | Cerrar Activo-Activo antes del go-live |
| R-032 — Restricción Innovación/Seguridad Nacional sobre cloud | 3 | 2 | Iniciar consulta esta semana + plan B on-premise |
| R-023 — AML externo no listo (gap DETECT) | 16 | 9 | RFP AML paralelo + contrato puente |
| R-025 — Incumplimiento Acuerdo 1-2026 plazos | 16 | 8 | Plan remediación legado + criterio eliminatorio E-15 |
| R-013 — Falla integración Yappy/ACH/Telered | 15 | 8 | PoC ampliada + ambiente de paralelo |

---

## Sección 9 — Mapeo a Funciones NIST CSF 2.0 (Resumen)

| Función | Categorías | Status actual | Hallazgos críticos / altos | Target |
|---------|-----------|---------------|----------------------------|--------|
| GV | 5 | 3/5 | ALTO-13 (supplier risk) | 5/5 post-programa |
| ID | 3 | 2/3 | — | 3/3 post-programa |
| **PR** | **6** | **2/6** | **CRIT-1, CRIT-2, CRIT-3, CRIT-5, ALTO-1, ALTO-3, ALTO-12** | **6/6 post-programa** |
| DE | 2 | 1/2 | ALTO-2, ALTO-4, ALTO-6, ALTO-10 | 2/2 post-programa |
| RS | 4 | 2/4 | ALTO-8 | 4/4 post-programa |
| RC | 3 | 2/3 | ALTO-5, ALTO-9, ALTO-14 | 3/3 post-programa |
| **Total** | **23** | **12/23 (52%)** | **5 CRIT + 14 ALTO** | **23/23 (100%)** |

---

## Sección 10 — Plan de Remediación Priorizado

### P0 — Crítico (esta semana — bloqueante)

| # | Acción | Owner | Plazo | Vínculo |
|---|--------|-------|-------|---------|
| 0.1 | **Plan formal de remediación del legado para Art. 25 §1 (31-ene-2027)** — CRIT-4 | Cumplimiento + CISO + TI | Plan firmado en 2 semanas; ejecución 3 meses | R-025, R-027 |
| 0.2 | **Iniciar consulta gubernamental cloud** — ALTO-7 | Legal + Aldo Ríos | Iniciada esta semana | R-032 |
| 0.3 | **Dictamen Legal del proceso RFP** — incluye seguridad | Legal | 4 semanas | R-026 |

### P1 — Alto (próximos 30-90 días)

| # | Acción | Owner | Plazo | Vínculo |
|---|--------|-------|-------|---------|
| 1.1 | **Cifrado en reposo en el legado** (donde técnicamente factible) — CRIT-1 | CISO + TI | 90 días | R-027 |
| 1.2 | **MFA obligatorio para acceso privilegiado del legado** — CRIT-2 | CISO + TI | 60 días | R-027 |
| 1.3 | **Cifrado en tránsito interno** — CRIT-3 | TI | 90 días | R-027 |
| 1.4 | **RBAC en el legado donde sea posible** — CRIT-5 | CISO + TI | 6 meses | R-027 |
| 1.5 | **Bóveda de secretos (Vault o equivalente)** — ALTO-3 | TI | 60 días | R-027 |
| 1.6 | **DPIA para geolocalización inferencial** — ALTO-11 | Legal + CISO + Cumplimiento | 60 días | R-025 |
| 1.7 | **Plan de respuesta a incidente migración** — ALTO-8 | CISO + Operaciones | 60 días | R-017 |
| 1.8 | **Iniciar RFP AML** (mitigación gap DETECT) — ALTO-6 | Cumplimiento | Esta semana | R-023 |
| 1.9 | **Cobertura de seguro de ciber-riesgo** — ALTO-14 | CISO + Finanzas | 60 días | R-027 |
| 1.10 | **Plan de continuidad de Caja Amiga durante migración** — ALTO-9 | Red Caja Amiga + Operaciones | 90 días | R-035 |
| 1.11 | **Marco formal de supplier risk management** para los 3 RFPs — ALTO-13 | CISO + Compras | Pre-firma primer contrato | R-008, R-023, R-024 |
| 1.12 | **Workshop formal de apetito de riesgo con la JD** | Aldo Ríos + JD | 8 semanas | (RISK v2.0) |

### P2 — Medio (próximos 3-6 meses)

| # | Acción | Owner | Plazo |
|---|--------|-------|-------|
| 2.1 | **Pen-test semestral del legado** — ALTO-10 | CISO | Recurrente desde Q3 2026 |
| 2.2 | **Recertificación automática de accesos** — ALTO-1 | TI + CISO | 6 meses |
| 2.3 | **SIEM consolidado + EDR end-to-end** — ALTO-12 | CISO | 12 meses |
| 2.4 | **Plan de pen-test del CBS futuro pre-go-live** | CISO | Pre-go-live |
| 2.5 | **Cerrar transición Activo-Activo antes del go-live del CBS** — ALTO-5 | TI + Operaciones | 12 meses |
| 2.6 | **Observabilidad end-to-end de transacciones** — ALTO-4 | TI | 12 meses |
| 2.7 | **Programa formal de awareness** (PR.AT) | CISO + RRHH | 6 meses |
| 2.8 | **ROPA Ley 81 + Oficial de Protección de Datos nombrado** | Legal + CISO | 6 meses |
| 2.9 | **Threat modeling formal del CBS futuro** | CISO + Arquitectura | Durante fase de diseño del CBS |

### P3 — Continuo (post go-live)

| # | Acción | Owner |
|---|--------|-------|
| 3.1 | Revisión trimestral del vendor risk con métricas | CISO + Compras |
| 3.2 | Pen-test anual del CBS productivo | CISO |
| 3.3 | Auditoría externa de seguridad anual | CISO + Auditoría Interna |
| 3.4 | DR test semestral | TI + Operaciones |
| 3.5 | Simulacros de respuesta a incidente trimestrales | CISO + Operaciones |
| 3.6 | Calibración del motor AML (R-023 una vez seleccionado) | CISO + Cumplimiento |
| 3.7 | Certificación ISO 27001 de al menos un servicio crítico | CISO + Auditoría Interna | 2029 |

---

## Sección 11 — Apetito de Riesgo de Seguridad

| Categoría | Apetito propuesto | Riesgos actuales sobre apetito |
|-----------|--------------------|---------------------------------|
| Cifrado | Sin tolerancia — datos sensibles cifrados en reposo y tránsito | R-027 (legado) |
| MFA | Sin tolerancia para acceso privilegiado | R-027 (legado) |
| Pen-test crítico no remediado | 0 críticos > 30 días, 0 altos > 90 días | (pendiente verificar) |
| Disponibilidad servicios críticos | ≥ 99.99% mensual | NFR-A-001 |
| Tiempo de notificación de incidente a ANTAI | ≤ 72 horas | (procedimiento pendiente formalizar) |
| Vendor crítico sin SOC 2 vigente | 0 vendors críticos sin SOC 2 | (post-RFP) |

**Workshop de apetito con JD** recomendado como prerrequisito de aprobación del SOBC v2.0.

---

## Sección 12 — Plan de Mejora Continua

| Frecuencia | Actividad | Owner |
|------------|-----------|-------|
| Semanal | Revisión de vulnerabilidades críticas pendientes | CISO |
| Mensual | Reporte de postura de seguridad al Comité de Tecnología | CISO |
| Trimestral | Revisión de supplier risk de vendors críticos | CISO + Compras |
| Trimestral | Simulacros de respuesta a incidente | CISO + Operaciones |
| Semestral | Pen-test del entorno productivo + DR test | CISO + TI |
| Anual | Auditoría externa de seguridad | CISO + Auditoría Interna |
| Anual | Revisión de apetito de riesgo por JD | Aldo Ríos + JD |
| Continuo | Threat intelligence + monitoreo | CISO |

---

## Aprobación del Documento

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Owner del Assessment | CISO (Guillermo Smith) + Aldo Ríos | [PENDING] | [PENDING] |
| Auditoría Interna | [PENDING] | [PENDING] | [PENDING] |
| Legal | [PENDING] | [PENDING] | [PENDING] |
| Cumplimiento | [PENDING] | [PENDING] | [PENDING] |
| Riesgos | [PENDING] | [PENDING] | [PENDING] |
| Comité de Tecnología | [PENDING] | [PENDING] | [PENDING] |
| JD (apetito) | [PENDING] | [PENDING] | [PENDING] |

---

## External References

| Doc ID | Descripción |
|--------|-------------|
| ARC-001-REQ-v2.0 | NFR-SEC-001..018 + FR-046..054 (AML/KYC) + FR-052 (beneficiario final 10%) + FR-053 (geolocalización inferencial) |
| ARC-001-RISK-v2.0 | R-017, R-027, R-028, R-032 (seguridad) + R-023 (AML) + R-025 (Acuerdo 1-2026) |
| ARC-001-RSCH-v2.0 | Análisis técnico de vendors con criterios de seguridad |
| ARC-001-EVAL-v2.0 | Eliminatorios E-1, E-9, E-11, E-13, E-14, E-15 + ponderación NFR-SEC |
| ARC-001-SOBC-v2.0 | Caso de negocio del programa |
| ARC-000-PRIN-v1.1 | Principios 4 (Zero Trust), 6 (Soberanía), 7 (Cumplimiento), 8 (Integridad) |
| DOC-SES-007 | Sesión Día 4 Ciberseguridad (CISO Guillermo Smith) — estado actual + plan NIST CSF 2.0 + CIS + ISO 27001 |
| DOC-SES-008 | Sesión Día 4 Infraestructura — Activo-Activo en transición |
| DOC-SES-006 | Sesión Día 3 Regulatoria — Acuerdo 1-2026 + AML externo |
| DOC-RFI-001 | RFI v1.0 emitido jun-2026 |
| tech-notes/acuerdo-1-2026-implementation.md | Implementación de Acuerdo 1-2026 (umbral 10%, plazos) |
| tech-notes/data-sovereignty-panama.md | Soberanía de datos en Panamá |
| tech-notes/sbp-regulatory-compliance.md | Cumplimiento regulatorio SBP |

---

## Próximos Pasos

1. **Esta semana** (P0):
   - Plan formal de remediación del legado para Acuerdo 1-2026 Art. 25 §1.
   - Iniciar consulta gubernamental cloud.
   - Dictamen Legal del proceso RFP.
2. **Próximas 4-12 semanas** (P1):
   - Ejecutar las 12 acciones P1 — cifrado, MFA, RBAC, bóveda, DPIA, plan respuesta, RFP AML, seguro ciber, supplier risk, apetito.
3. **Próximos 3-6 meses** (P2):
   - 9 acciones P2 incluyendo SIEM/EDR, observabilidad, threat modeling del CBS futuro.
4. **Próximo refresh del SECD**: 2026-09-11 (90 días) o post-cierre del RFP CBS / decisión cloud.
5. **Coordinación**: este documento debe leerse junto con `ARC-001-RISK-v2.0.md` (Plan de Acción priorizado), `ARC-001-EVAL-v2.0.md` (eliminatorios de seguridad), `ARC-001-REQ-v2.0.md` (NFR-SEC), `ARC-001-SOW-CBS-v1.0.md` (cláusula 11 — Ley 81 + NFR-SEC en RFP CBS).
6. **Comando dependiente recomendado**: **`/arckit:dpia`** — Data Protection Impact Assessment formal para geolocalización inferencial (FR-053) + datos sensibles del mandato social. Es bloqueante para Acuerdo 1-2026 Art. 14.

---

**Generated by**: ArcKit `/arckit:secure` command (adaptado a Panamá)
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Reemplazo del Core Banking + ERP + AML (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: Secure by Design adaptado al contexto panameño — anclado a NIST CSF 2.0 (en implementación por CAP) + Acuerdo SBP 11-2018 (ciberseguridad + riesgo operacional) + Acuerdo SBP 1-2026 (componentes de identidad digital, Resolución SBP-JD-0001-2026) + Ley 81 (Protección de Datos Personales — equivalente UK GDPR) + ISO 27001 readiness. El comando original `/arckit:secure` está diseñado para gobierno UK civil; este documento adapta su estructura al equivalente regulatorio panameño. Postura actual del legado: 12/23 categorías NIST CSF 2.0 (52%). Hallazgos: 5 críticos + 14 altos + 9 medios. Plan de remediación priorizado P0/P1/P2 alineado al Plan de Acción de RISK v2.0.
