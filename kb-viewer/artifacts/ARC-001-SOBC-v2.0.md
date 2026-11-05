# Strategic Outline Business Case — Reemplazo del Core Banking + ERP + AML — Caja de Ahorros de Panamá

> **Modelo**: HM Treasury Green Book 5-case (Strategic, Economic, Commercial, Financial, Management) adaptado al contexto de banca pública panameña.

## Document Control

| Campo | Valor |
|-------|-------|
| **Document ID** | ARC-001-SOBC-v2.0 |
| **Document Type** | Strategic Outline Business Case (SOBC) |
| **Project** | Reemplazo del Core Banking + ERP + Motor AML — Caja de Ahorros, Panamá |
| **Classification** | OFFICIAL-SENSITIVE (CONFIDENCIAL – Uso interno) |
| **Status** | DRAFT |
| **Version** | 2.0 |
| **Created Date** | 2026-05-19 (v1.0) |
| **Last Modified** | 2026-06-11 (v2.0) |
| **Review Cycle** | Trimestral durante la fase de selección; semestral durante implementación |
| **Next Review Date** | 2026-08-19 (alineado con cierre del RFP CBS) |
| **Owner** | Aldo Ríos — Gerencia de Innovación / Líder del Programa |
| **Reviewed By** | PENDING — Comité de Tecnología, CFO, CISO, Cumplimiento, Riesgos, Legal, Auditoría Interna |
| **Approved By** | PENDING — Junta Directiva (aprobación del SOBC y del presupuesto blendado de las 3 categorías) |
| **Distribution** | Junta Directiva, Gerencia General, Comité de Tecnología, Comité Ejecutivo, Auditoría Interna, Contraloría (informativo) |

## Revision History

| Versión | Fecha | Autor | Cambios | Aprobado por | Fecha de Aprobación |
|---------|-------|-------|---------|--------------|---------------------|
| 1.0 | 2026-05-19 | ArcKit AI | Versión inicial — 4 opciones (No hacer / Mínima / Balanceada / Comprehensiva); recomienda Opción 2 (RFP competitivo con 4 vendors CBS); TCO 7 años B/. 113-180M; NPV +B/. 15.5M punto medio. Cobertura 85-92% de metas STKE G-1..G-10. | PENDING | PENDING |
| 2.0 | 2026-06-11 | ArcKit AI | **Major refresh** tras (a) las 8 sesiones presenciales de evaluación (25–28 mayo 2026); (b) el RFI v1.0 emitido en junio; (c) el refresh masivo de REQ a v2.0 (193 reqs vs 165), RISK a v2.0 (37 riesgos vs 22), RSCH a v2.0 (3 categorías: CBS + ERP + AML), EVAL a v2.0 (15 eliminatorios + 3 ponderaciones); y (d) el corrigendum del Acuerdo 1-2026 (umbral beneficiario final 10% no 25%; plazos Art. 14 → 30-jun-2027, Art. 25 §1 → 31-ene-2027). **Cambios materiales del SOBC**: (1) **el programa ya no es 1 RFP sino 3 RFPs coordinados**: CBS + ERP + AML — el CBS no incluirá GL completo (BR-013) y el monitoreo AML se externaliza con motor IA (FR-048). (2) **TCO 7 años blendado** ahora cubre las 3 categorías: rango B/. 115–245M, recomendado **B/. 150–195M**, punto medio **B/. 175M** (vs B/. 113–180M para CBS solo en v1.0). (3) **Las 4 opciones se reformulan** para reflejar la realidad de 3 categorías: Op-0 (No Hacer multi-categoría — más inviable que en v1.0 porque el proveedor AML sale de soporte en 2026), Op-1 (Mínima — incumbente + AML forzado + GL en CBS — **no aceptable regulatoriamente** dado Acuerdo 1-2026), Op-2 (Balanceada — RECOMENDADA — Tier-2 LatAm CBS + Tier-1 Cloud ERP + AI-native AML), Op-3 (Comprehensiva — Tier-1 Global CBS + Tier-1 ERP + Enterprise AML). (4) **NPV refrescado** con flujos blendados 7 años → punto medio +B/. 22M (subió de +B/. 15.5M por mayor cobertura de eficiencia y mayor "expected loss" del Op-0 dado el Acuerdo 1-2026). (5) **Riesgo R-024 (ERP no listo al go-live) elevado a Crítico inherente (score 25)** y materializado como **dependencia crítica del cronograma**. (6) **Riesgo R-023 (AML externo no listo)** con cronograma forzado por fin de soporte 2026. (7) **R-026 (sesgo COBIS → impugnación Contraloría)** se mitiga estructuralmente mediante el Marco de Evaluación v2.0 (EVAL v2.0) con validación previa de Auditoría Interna. (8) **Acuerdo 1-2026 elevado a hito eliminatorio temporal del RFP**: vendors cuyo cronograma no entregue Art. 14 antes del 30-jun-2027 quedan descalificados. (9) **Plazos del programa** ajustados: cierre del RFP CBS cierre 2026, ERP y AML cierre Q4 2026 (RFI ya emitido para CBS — DOC-RFI-001). (10) **Cobertura de metas STKE** sube a **89-95%** para Opción 2 (vs 85-92% en v1.0) por la integración explícita de ERP + AML. (11) **Riesgos sobre apetito** identificados: 14 riesgos (38%) exceden apetito propuesto — workshop de apetito formal con JD recomendado como prerrequisito de aprobación final. (12) **Inventario detallado de sistemas satélite** ahora visible: SITECA, BPMs (Ultimus/Asicom-Finflow/Genexus), Emerix, Átomos, Talentía, BCG, Banca Seguro, SISCARD, Panadata, App Enhancer — afecta el alcance de integración del Caso de Gestión. (13) **Preferencias del banco** (COBIS preferido / Temenos, Finacle, SAP descartados) documentadas como insumo informativo de ponderación, NO eliminatorio — para sostener el proceso ante Contraloría. Nuevas citas DOC-SES-001..009, DOC-RFI-001, DOC-POC-001, ARC-001-RSCH-v2.0, ARC-001-EVAL-v2.0. | PENDING | PENDING |

---

## Resumen Ejecutivo

### Decisión Solicitada a la Junta Directiva

> Aprobar el lanzamiento de **tres procesos RFP paralelos y coordinados** (CBS + ERP + AML), con presupuesto blendado de **B/. 150–195M a 7 años** (punto medio **B/. 175M**), bajo gobernanza de un único Steering Committee. El SOBC v2.0 recomienda la **Opción 2 — Balanceada** (CBS Tier-2 LatAm + ERP Cloud Tier-1 + AML AI-native).

### Por qué actuar ahora

1. **Plazos regulatorios discretos del Acuerdo 1-2026** (Resolución SBP-JD-0001-2026 del 16-ene-2026): Art. 25 §1 vigencia **31-ene-2027** (solo ~7 meses tras cierre planeado del RFP); Art. 14 (beneficiario final ≥ 10% + geolocalización inferencial digital) vigencia **30-jun-2027**. El cronograma no admite más demora.
2. **El proveedor actual de monitoreo AML deja de dar soporte en 2026** [DOC-SES-006, DOC-SES-009 §10.3]. Sin reemplazo, el banco queda sin capacidad AML — incumple obligación UAF.
3. **La relación con Datapro está deteriorada** ("cotizaciones lentas, asignación de recursos lenta, costo excesivo" — DOC-SES-001, DOC-SES-009 §3.3). El vendor incumbente no representa una alternativa de continuidad.
4. **El CBS legado tiene brechas críticas de ciberseguridad** (sin cifrado en reposo, sin cifrado en tránsito interno, sin MFA — DOC-SES-007 §8.1). La exposición es real durante toda la vida del programa.
5. **La agenda digital activa** (Super App, Yappy, A.N.D.R.E.A., Caja Amiga, Omnicaja en ejecución 24 meses) requiere un Core moderno como habilitador.
6. **Caja de Ahorros está calificada AAA(pan)** y un fallo de cumplimiento durante el reemplazo del Core afectaría costo de fondeo, mandato social y reputación institucional.

### Opciones evaluadas y opción preferida

| # | Opción | Alcance | TCO 7Y (B/. M) | Cobertura STKE | Veredicto |
|---|--------|---------|----------------|-----------------|-----------|
| 0 | No Hacer (Datapro continúa) | Renovar status quo en las 3 categorías | 95–135 | 15% | ❌ Inviable — incumple Acuerdo 1-2026 + AML sin soporte |
| 1 | Mínima (incumbente + AML forzado + GL en CBS) | Mantener Datapro CBS modernizado + extender proveedor AML actual + GL en CBS | 100–145 | 35% | ❌ No viable regulatoriamente — fin de soporte AML + observación Contraloría |
| 2 | **Balanceada** (Tier-2 CBS + Cloud Tier-1 ERP + AI-native AML) | RFP competitivo bajo Ley 22 — 3 categorías coordinadas | **150–195** (recomendado) | **89–95%** | ✅ **PREFERIDA** |
| 3 | Comprehensiva (Tier-1 CBS + Tier-1 ERP + Enterprise AML) | Tier-1 globales en las 3 categorías | 200–245 | 95–97% | ⚠️ Prima de costo +B/. 50M sin retorno proporcional + R-026 amplificado |

### Valor por Dinero (resumen)

- **TCO 7 años Opción 2 (preferida) — punto medio**: B/. 175M (CBS B/. 95M + ERP B/. 40M + AML B/. 19M + integración B/. 21M).
- **TCO 7 años Opción 0 (do-nothing)** — punto medio: B/. 110M directos + B/. 30M expected loss = B/. 140M ajustado al riesgo.
- **NPV incremental Opción 2 vs Opción 0** (5% real, 7 años): **+B/. 22M punto medio** (rango -B/. 28M a +B/. 58M con sensibilidades adversas/favorables 20%).
- **Payback período**: ~4.5 años contables desde inicio del programa.

### Trazabilidad: 10 metas STKE × 14 BR × 37 riesgos × 15 eliminatorios

Cada beneficio del SOBC se vincula a una meta del STKE (G-1..G-10). Cada riesgo del SOBC enlaza con el RISK register v2.0 (R-001..R-037). Cada criterio de selección enlaza con el EVAL v2.0 (E-1..E-15 eliminatorios + ponderación por categoría). La integridad de trazabilidad sostiene la defensibilidad del proceso ante Contraloría.

---

## Parte A — Caso Estratégico (Strategic Case)

### A.1 Declaración del problema

Caja de Ahorros de Panamá (CAP) opera el Core Banking **DataPro/eIBS** desde hace 90 años con extensiones sucesivas. El sistema ha llegado al fin de su ciclo de vida útil [DOC-CB-001-C1, DOC-RFI-001]:

- **Time-to-market degradado**: cualquier requerimiento toma hasta 24 meses en implementarse [DOC-SES-001, DOC-SES-009 §3.3].
- **Costos crecientes y opacos**: "cotizaciones lentas, asignación de recursos lenta, costo excesivo" — relación deteriorada con DataPro/Vencora.
- **Lock-in profundo**: lenguaje de programación obsoleto, customizaciones extensivas que impiden actualizar el core base.
- **Brechas regulatorias**: el sistema no soporta nativamente NIIF 9, Acuerdo 6-2000, Acuerdo 1-2026 (nuevo regulatorio AML/CFT), FATCA/CRS — todo se ha sostenido con apoyo manual o customización.
- **Brechas funcionales para el negocio**: sin sobregiros nativos, sin reestructuración nativa, sin créditos sindicados, sin sub-cuentas, sin factoring con pagador estatal automatizado, sin hipotecario para residentes en el exterior.
- **Brechas de ciberseguridad** críticas: sin cifrado en reposo, sin MFA, sin cifrado interno en tránsito [DOC-SES-007 §8.1].
- **Inhabilita el mandato social**: la cartera de Interés Preferencial (Ley 468/2025), Profimype, "Una Cuenta Para Todos" requieren parametrización ágil que el legado no provee.
- **Fragmentación de satélites**: SITECA (originación hipotecaria), múltiples BPMs (Ultimus, Asicom-Finflow, Genexus), Emerix (cobros con desfase 1 día), Átomos, Banca Seguro, SISCARD, hojas Excel/Access — todo requiere consolidación.

**Decisiones arquitectónicas nuevas (v2.0)** que afectan el problema:

- El **CBS no incluirá GL completo** [DOC-RFI-001 §3.9] → CAP debe adquirir **ERP externo** (BR-013, R-024 Crítico).
- El **monitoreo AML se externaliza** del CBS [FR-048] → CAP debe seleccionar **motor AML externo con IA y APIs** (R-023). Proveedor actual sale soporte en 2026.

### A.2 Alineación Estratégica

**Stakeholder drivers críticos** (de STKE):

| Driver | Stakeholder | Intensidad | Vinculación |
|--------|-------------|------------|-------------|
| SD-1 — Continuidad operativa y AAA(pan) | JD + CFO | CRITICAL | BR-001, BR-011 |
| SD-2 — Cumplimiento regulatorio SBP / Acuerdo 1-2026 | Cumplimiento, CFO | CRITICAL | BR-002, FR-052, FR-053 |
| SD-3 — Mandato social (Interés Preferencial, FGA, Profimype) | Gerencia General, Áreas de negocio | HIGH | BR-004 |
| SD-4 — Soberanía de datos en territorio panameño | Legal, CISO, Cumplimiento | HIGH | BR-006, DR-013 |
| SD-5 — Calidad de servicio (24/7 español, disponibilidad) | Operaciones | HIGH | BR-009, NFR-A-001..003 |
| SD-6 — Modernización digital (Super App, Yappy, Omnicaja) | Innovación, Negocio | HIGH | BR-010 |
| SD-7 — TCO controlado y auditable por Contraloría | CFO, Auditoría Interna | HIGH | BR-003, BR-007 |
| SD-8 — Caja Amiga / inclusión financiera rural | Áreas de negocio + Comunicaciones | MEDIUM | BR-012 |
| SD-9 (NEW v2.0) — ERP propio para contabilidad consolidada | CFO, Contabilidad | HIGH | BR-013 |
| SD-10 (NEW v2.0) — AML externo con IA y APIs | Cumplimiento, CISO | HIGH | R-023, FR-048 |

**Principios PRIN v1.1** (21 principios) alineados — particularmente:
- P5 (Cumplimiento Regulatorio Continuo), P6 (Soberanía de Datos), P7 (Reportería SBP Nativa), P8 (Integridad Contable + Modelo Dual Provisiones), P11 (APIs Abiertas), P14 (Performance Real-Time), P20 (Parametrización vs Código), P21 (Soporte Local en Español).

### A.3 Alcance

**En el alcance (los 3 RFPs)**:

1. **CBS** — Core Banking transaccional (cuentas, depósitos, créditos, hipotecas, contabilidad transaccional, reportería regulatoria SEI/UAF/APC), integraciones con Yappy / ACH / Telered / SWIFT / SEI / SIACAP / MIVIOT / MEF / DGI, migración del legado DataPro/eIBS, consolidación de SITECA/BPMs/Profimype/Excel/Access.
2. **ERP** — Libro Mayor (GL) consolidado, plan de cuentas SBP, doble contabilidad NIIF + regulatoria, IAS 21, NIIF 16, rentabilidad por sucursal, integración con CBS vía API en tiempo real o micro-batch.
3. **Motor AML externo** — monitoreo transaccional en tiempo real, IA explicable, integración Panadata, ROS a UAF, geolocalización inferencial (Acuerdo 1-2026 Art. 14), beneficiario final ≥ 10%.
4. **Cambios de infraestructura críticos** coordinados: finalización de la transición Activo-Activo (35–40 km), remediación de la brecha de seguridad del legado, sustitución del proveedor AML antes del go-live del CBS.

**Fuera del alcance** (Fase 2 o paralelo):

- Reemplazo de SISCARD (core de tarjetas) — se mantiene e integra.
- Reemplazo del bus IBM MQ + API Gateway — se preservan como capa de abstracción.
- Reemplazo de la Super App, A.N.D.R.E.A., Omnicaja (en ejecución 24 meses) — se integran al nuevo CBS pero su desarrollo continúa paralelo.
- Implementación de XBRL completo (Fase 2, alineado al roadmap SBP).
- Reemplazo de los BPMs (Ultimus, Asicom-Finflow, Genexus) — decisión estratégica de estandarización planificada para Fase 2.
- Consolidación de Emerix (cobros) — Fase 2 una vez que el CBS gestione 0-90 días nativos.

### A.4 Dependencias críticas

1. **Dictamen Legal de soberanía de datos** (P0 Plan de Acción RISK v2.0) — pre-RFP, prerrequisito para definir reglas de soberanía y modelo de despliegue.
2. **Consulta formal a Autoridad de Innovación + SBP + Seguridad Nacional** sobre cloud (R-032) — pendiente, condiciona el modelo de despliegue.
3. **Plan de remediación de seguridad del CBS legado** (R-027) — cifrado en reposo, MFA, recertificación automática — debe iniciar paralelo al RFP, no esperar al nuevo CBS.
4. **Selección del ERP externo iniciada en paralelo** (R-024 Crítico) — RFI ERP debe abrirse esta semana.
5. **Selección del motor AML externo iniciada en paralelo** (R-023 Alto) — RFI AML debe abrirse esta semana.
6. **Transición Activo-Activo** entre los dos sitios (35–40 km) completada antes del go-live del CBS (R-028).
7. **Validación del Marco de Evaluación por Auditoría Interna** (mitigación R-026 sesgo COBIS) — pre-RFP.
8. **Workshop formal de apetito de riesgo con la JD** (Orange Book) — pre-aprobación final del SOBC.

### A.5 ¿Por qué ahora?

| Razón | Detalle | Costo de demora |
|-------|---------|-----------------|
| **Acuerdo 1-2026 plazos discretos** | Art. 25 §1 vigencia 31-ene-2027; Art. 14 (beneficiario final + geolocalización inferencial) vigencia 30-jun-2027 | Multas SBP elevadas + restricciones operativas + observación Contraloría |
| **Fin de soporte AML del proveedor actual 2026** | Banco queda sin monitoreo AML si no hay reemplazo operativo | Incumplimiento UAF + sanción SBP + responsabilidad personal de directores firmantes |
| **Relación con DataPro deteriorada** | El incumbente no es alternativa de continuidad | Aceleración de degradación operativa + lock-in profundizado si se renegocia |
| **Brecha de seguridad activa del legado** | Sin cifrado, sin MFA, durante toda la vida del programa | Incidente público + pérdida AAA(pan) + cobertura mediática |
| **Agenda digital activa con presión competitiva** | Omnicaja, Super App, Yappy expandiendo | Pérdida de cuota de mercado + queja política |
| **Ventana de gobernanza estable** | Gerencia General + JD alineadas; Innovación con autoridad delegada | Cambio político o de gobierno desestabiliza prioridades (R-014) |

**Ventana operativa óptima**: 2026-Q3 a 2027-Q1 — antes de la presión completa del Acuerdo 1-2026 y mientras la gobernanza está estable.

### A.6 Factores Críticos de Éxito (CSF)

1. **CSF-1**: Tres RFPs (CBS + ERP + AML) abiertos en paralelo con un único Steering Committee — coordinación efectiva.
2. **CSF-2**: Marco de Evaluación firmado por Auditoría Interna **antes** del envío del RFP (mitigación R-026).
3. **CSF-3**: Selección de vendor que entregue capacidades Acuerdo 1-2026 Art. 14 **antes del 30-jun-2027** (eliminatorio E-15).
4. **CSF-4**: Mantener disponibilidad ≥ 99.95% canales digitales / ≥ 99.99% críticos durante toda la migración (BR-001).
5. **CSF-5**: Plan de migración por bandos con paralelo ≥ 3 meses por bando (no big-bang).
6. **CSF-6**: Cero diferencias materiales en conciliación contable post-corte (BR-008).
7. **CSF-7**: 100% del personal capacitado en español pre-corte (BR-009).
8. **CSF-8**: Mandato social operativo desde día 1 con parametrización (no código del vendor) (BR-004, PRIN P20).
9. **CSF-9**: Soberanía de datos validada legalmente y verificada trimestralmente.
10. **CSF-10**: Dictamen Contraloría sin observaciones materiales (BR-007).
11. **CSF-11 (NEW v2.0)**: ERP externo operativo al go-live del CBS sin gap contable (R-024).
12. **CSF-12 (NEW v2.0)**: Motor AML externo operativo antes de fin de soporte del actual (R-023).

---

## Parte B — Caso Económico (Economic Case)

### B.1 Apreciación de Opciones (4 opciones — reformuladas v2.0 para reflejar 3 categorías)

Las 4 opciones se evalúan contra Opción 0 (No Hacer / status quo) usando apreciación semi-cuantitativa: ROM costs del RSCH v2.0 (3 categorías), beneficios cuantificados clave, NPV simplificado a 5% real (estándar LatAm), análisis básico de sensibilidad.

#### Opción 0 — No Hacer

- **Descripción**: mantener DataPro/eIBS bajo contrato continuo con Vencora; extender al proveedor AML actual a pesar de fin de soporte 2026; mantener GL dentro de DataPro.
- **Costos directos 7 años (con +25% contingencia)**: B/. 80M (B/. 60M DataPro + B/. 15M customizaciones regulatorias defensivas + B/. 5M extensión AML).
- **Costos de riesgo esperados (expected loss)**: B/. 30–50M (multas SBP por Acuerdo 1-2026, AML sin soporte = sanción UAF + responsabilidad personal de directores, downgrade AAA con impacto en costo de fondeo, brecha de seguridad explotada).
- **Costo total ajustado al riesgo**: **B/. 110–130M**.
- **Cobertura de metas STKE (G-1..G-10)**: **15%** — solo continuidad parcial; ninguna meta de modernización, mandato social, soberanía o ERP.
- **Pros**: mínima disrupción operativa inmediata; equipo conoce el sistema; sin RFP.
- **Contras**: **inviable estratégica y regulatoriamente** — incumple Acuerdo 1-2026 plazo Art. 14 jun-2027; AML proveedor sin soporte = incumplimiento UAF inmediato; brecha de seguridad escalable; vendor lock-in profundizado.
- **Veredicto**: ❌ **No viable** — sirve sólo como baseline contable.

#### Opción 1 — Mínima (incumbente CBS + AML forzado + GL en CBS)

- **Descripción**: negociar con Vencora modernización del e-IBS (capa APIs, refactoring incremental); extender contrato AML actual via negociación de prórroga de soporte; mantener GL dentro del CBS modernizado. Sin RFP — contratación directa.
- **Costos directos 7 años (con +25% contingencia)**: B/. 95–135M (B/. 80–100M base CBS modernización + B/. 10–20M AML prórroga + B/. 5–15M consolidación satélites).
- **Costos de riesgo esperados**: B/. 25–50M (Vencora roadmap incierto, AML sin actualización a Acuerdo 1-2026 plazo Art. 14, Contraloría observación crítica por contratación directa, brechas residuales en soberanía).
- **Costo total ajustado al riesgo**: **B/. 120–185M**.
- **Cobertura de metas STKE**: **35%** — G-3, G-4, parcial G-1, G-2, G-6, G-9; gaps en G-5 (mandato social), G-7 (soberanía), G-8 (Contraloría con cuestionamiento crítico por no-RFP), G-9 (nueva — ERP no atendido).
- **Pros**: continuidad del vendor; conocimiento del equipo; menor curva de aprendizaje; sin necesidad de adquirir ERP separado.
- **Contras**: **Contraloría observación crítica** por contratación directa (R-002); incumple Principio 20 PRIN v1.1 (parametrización vs código); el proveedor AML actual no garantiza el Acuerdo 1-2026 Art. 14 plazo jun-2027 (R-025); no resuelve la fragmentación de satélites (SITECA, BPMs, Emerix, etc.); lock-in profundizado.
- **Veredicto**: ❌ **No viable** — incumple Ley 22 (proceso competitivo) + Acuerdo 1-2026 + Principio 20.

#### Opción 2 — Balanceada (RECOMENDADA) — RFP competitivo en 3 categorías paralelas

- **Descripción**:
  - **CBS**: shortlist de 4 vendors + 2 wildcards (Infosys Finacle, Temenos Transact, Cobis Topaz, Datapro/Vencora como benchmark, + Oracle FLEXCUBE, Bantotal). Selección por mérito en demos + PoC ampliada (caso hipotecario DOC-POC-001 + sindicados + factoring estatal + DDI).
  - **ERP**: shortlist de 4 + 1 wildcard (Microsoft Dynamics 365 F&O, Oracle Fusion Cloud ERP, SAP S/4HANA PCE, Infor CloudSuite Financials, + Oracle NetSuite). Selección por encaje contable + integración con CBS + soberanía.
  - **AML**: shortlist de 3 + 2 wildcards (NICE Actimize, Hawk:AI, Oracle FCCM, + ComplyAdvantage, Featurespace ARIC). Selección por IA explicable + tiempo real + cumplimiento Acuerdo 1-2026.
  - **Despliegue**: on-premise CAP o cloud privado regional con presencia panameña (resuelve BR-006).
  - **Gobernanza**: un único Steering Committee con sub-paneles por categoría; Auditoría Interna valida criterios y pesos pre-RFP.
- **Costos directos 7 años (con +25% contingencia)**: **B/. 150–195M** (CBS B/. 80–110M + ERP B/. 30–50M + AML B/. 15–25M + integración cross-RFP B/. 20–30M).
  - Banda Cobis CBS + Dynamics 365 ERP + Hawk:AI AML: B/. 145M (banda baja recomendada).
  - Punto medio (Finacle CBS + Oracle Fusion ERP + NICE Actimize AML): **B/. 175M**.
  - Banda alta (Temenos CBS + SAP S/4HANA ERP + NICE Actimize AML): B/. 195M.
- **Costos de riesgo esperados**: B/. 10–18M (riesgos R-001..R-037 con controles diseñados; R-024 + R-023 bajo monitoreo intensivo del Steering Committee).
- **Costo total ajustado al riesgo**: **B/. 160–213M**.
- **Cobertura de metas STKE**: **89–95%** — todas G-1..G-10 cubiertas + nueva G-11 (ERP) implícita + nueva G-12 (AML) implícita; gaps acotados en integración panameña out-of-the-box (todos requieren proyecto dirigido — el mismo que en v1.0).
- **Pros**:
  - **Competencia real en 3 categorías**: poder de negociación + defensibilidad ante Contraloría.
  - **Mitigación estructural de R-026**: Marco de Evaluación validado por Auditoría Interna + memo justificativo por vendor invitado/no invitado.
  - **Soberanía cumplible**: todos los shortlists soportan despliegue panameño.
  - **Mandato social verificable**: demos con datos reales como precondición.
  - **Acuerdo 1-2026 entregable en plazos** (E-15 eliminatorio).
- **Contras**:
  - **Cronograma agresivo**: 3 RFPs en paralelo requieren intensidad operativa.
  - **R-024 dependencia ERP** sigue siendo crítica — mitigada pero no eliminable.
  - Vendor lock-in mitigado pero no eliminable.
  - Implementación 24-36 meses post-firma.
- **Veredicto**: ✅ **PREFERIDA** — equilibrio óptimo cobertura/costo/riesgo/defensibilidad.

#### Opción 3 — Comprehensiva (Tier-1 Global en las 3 categorías)

- **Descripción**: seleccionar Tier-1 global líder Gartner MQ en las 3 categorías: Temenos Transact CBS + SAP S/4HANA Public Cloud ERP + NICE Actimize AML. RFP restringido a Tier-1.
- **Costos directos 7 años (con +25% contingencia)**: **B/. 200–245M** (CBS Temenos B/. 100–125M + SAP S/4HANA B/. 60–80M + NICE Actimize B/. 25–40M + integración Tier-1 cross-RFP B/. 15M).
- **Costos de riesgo esperados**: B/. 12–22M.
- **Costo total ajustado al riesgo**: B/. 212–267M.
- **Cobertura de metas STKE**: **95–97%** — máxima cobertura funcional; capacidades avanzadas no necesarias inmediatamente (wealth management, trading, advanced analytics).
- **Pros**: cobertura funcional máxima; ecosystem SI más amplio (Accenture, Capgemini, IBM, Deloitte); líderes Gartner MQ.
- **Contras**:
  - **Prima de costo +B/. 50M sobre Opción 2** sin beneficio incremental proporcional para banco social pública AAA(pan).
  - **R-026 amplificado**: descartar regional/AI-native sin justificación rigurosa es observable por Contraloría — favorece marcas globales sin base costo-beneficio.
  - **Capacidades sin uso**: módulos opcionales que no aportan al mandato social.
  - **Vendor lock-in mayor**: salida de Tier-1 monolítico cuesta más.
  - **Plazos**: implementación 36-48 meses post-firma — riesgo de no entregar Acuerdo 1-2026 antes de jun-2027.
- **Veredicto**: ⚠️ **Prima no justifica cobertura adicional** — descartada por valor por dinero, mantenida en shortlist competitivo de Opción 2.

### B.2 Resumen Comparativo de Opciones

| Criterio | Opción 0 | Opción 1 | **Opción 2** | Opción 3 |
|----------|----------|----------|--------------|----------|
| **TCO directo 7 años (B/. M)** | 80 | 95–135 | **150–195** | 200–245 |
| **Expected loss (B/. M)** | 30–50 | 25–50 | 10–18 | 12–22 |
| **Total ajustado al riesgo (B/. M)** | 110–130 | 120–185 | **160–213** | 212–267 |
| **Cobertura metas STKE** | 15% | 35% | **89–95%** | 95–97% |
| **Riesgo Contraloría** | 🟥 Crítico | 🟥 Alto | 🟨 **Medio (controlado)** | 🟧 Alto |
| **Riesgo regulatorio SBP / Acuerdo 1-2026** | 🟥 Crítico | 🟥 Alto | 🟨 Medio | 🟨 Medio |
| **Defensibilidad pública** | 🟥 Mínima | 🟥 Mínima | 🟩 **Alta** | 🟨 Cuestionable (favoritismo Tier-1) |
| **Tiempo a go-live** | N/A | 18–24 m | 30–36 m | 36–48 m |
| **Cobertura mandato social** | 15% | 50% | **92%** | 92% |
| **Resuelve R-024 (ERP)** | ❌ No | ❌ Parcial | ✅ Sí | ✅ Sí |
| **Resuelve R-023 (AML)** | ❌ No | ⚠️ Forzado | ✅ Sí | ✅ Sí |
| **Acuerdo 1-2026 plazos** | ❌ No | ⚠️ Riesgo | ✅ Sí (E-15) | ⚠️ Riesgo (timeline) |

### B.3 NPV Incremental (5% descuento real, 7 años)

Análisis de NPV incremental de Opción 2 vs Opción 0 (baseline). ROM — debe refinarse en la OBC.

**Flujo de costos incrementales Opción 2 vs Opción 0 (B/. M, punto medio):**

| Año | Costo Op2 | Costo Op0 | Costo incr. | Beneficio incr. | Flujo neto | Factor 5% | PV |
|-----|-----------|-----------|-------------|------------------|-----------|-----------|-----|
| 1 | 28 | 12 | +16 | 3 | -13 | 0.952 | -12.4 |
| 2 | 35 | 12 | +23 | 5 | -18 | 0.907 | -16.3 |
| 3 | 30 | 12 | +18 | 10 | -8 | 0.864 | -6.9 |
| 4 | 22 | 12 | +10 | 22 | +12 | 0.823 | +9.9 |
| 5 | 20 | 12 | +8 | 27 | +19 | 0.784 | +14.9 |
| 6 | 20 | 12 | +8 | 28 | +20 | 0.746 | +14.9 |
| 7 | 20 | 12 | +8 | 28 | +20 | 0.711 | +14.2 |
| **Total** | **175** | **84** | **+91** | **+123** | **+32** | | **+18.3** |

**NPV incremental Opción 2 vs Opción 0 = +B/. 18.3M (punto medio)**

Si añadimos el costo evitado por la expected loss de Opción 0 que no se materializa en Opción 2 (~B/. 30–50M descontado a ~B/. 28M):

**NPV ajustado al riesgo = +B/. 22M punto medio**

**Sensibilidades:**

| Escenario | NPV (B/. M) |
|-----------|-------------|
| Punto medio (base case) | **+22** |
| Beneficios incrementales -20% | -6 |
| Costos +20% | -13 |
| Doble adverso (-20% beneficios + +20% costos) | -28 |
| Doble favorable (+20% beneficios -20% costos) | +58 |

**Rango NPV 7 años**: **-B/. 28M a +B/. 58M**, punto central +B/. 22M.

**Análisis**: el NPV punto medio es positivo. La banda pesimista representa una pérdida bordemarcada que se justifica por:

1. Beneficios estratégicos no monetizados (AAA(pan) sostenido, mandato social cumplido, agenda digital sustentada).
2. Imposibilidad de capturar todo el costo evitado en términos contables conservadores (sanción Acuerdo 1-2026, sanción UAF, downgrade AAA).
3. Optimism bias HM Treasury (+20%) ya incluido en el +25% de contingencia.

### B.4 Beneficios Mapeados a Metas STKE

| ID | Beneficio | Categoría | Cuantificación 7Y (B/. M) | Meta STKE | Outcome STKE |
|----|-----------|-----------|----------------------------|-----------|--------------|
| BF-1 | Reducción de tiempo-a-mercado de productos (24m → < 3m) | OPERATIONAL | 35 | G-3 (Modernización digital) | O-3 (Time-to-market) |
| BF-2 | Evitar multas SBP por Acuerdo 1-2026 | COMPLIANCE | 18 (expected loss evitada) | G-2 (Cumplimiento) | O-2 (Sanción nula) |
| BF-3 | Evitar pérdida de AAA(pan) por incidente o incumplimiento | STRATEGIC | 25 (impacto cost-of-funds) | G-1 (AAA sostenido) | O-1 (AAA mantenido) |
| BF-4 | Eficiencia operativa (eliminación de procesos manuales: bóveda Excel, reportería manual) | OPERATIONAL | 12 | G-5 (Operación eficiente) | O-5 (% manual) |
| BF-5 | Mandato social operativo con parametrización | STRATEGIC + COMPLIANCE | 8 (riesgo político evitado) | G-4 (Mandato social) | O-4 (Productos sociales operativos) |
| BF-6 | Agenda digital sostenida (Super App, Yappy, Omnicaja) | STRATEGIC | 15 | G-6 (Agenda digital) | O-6 (Disponibilidad digital) |
| BF-7 | Soberanía de datos verificable | COMPLIANCE | 5 (riesgo legal evitado) | G-7 (Soberanía) | O-7 (Dictamen Legal) |
| BF-8 | Contraloría sin observaciones materiales | COMPLIANCE | 3 (riesgo político evitado) | G-8 (Contraloría OK) | O-8 (Sin observaciones) |
| BF-9 | Mejora de calidad de datos (8,000+ elementos con propietarios) | OPERATIONAL | 5 | G-10 (Datos de calidad) | O-10 (% campos validados) |
| BF-10 (NEW v2.0) | ERP externo profesional para GL consolidado | OPERATIONAL + COMPLIANCE | 8 | G-11 (Contabilidad robusta) | O-11 (Cierre mensual sin diferencias) |
| BF-11 (NEW v2.0) | Motor AML con IA → reducción de falsos positivos 70% | OPERATIONAL + COMPLIANCE | 6 | G-12 (AML efectivo) | O-12 (% falsos positivos) |
| **TOTAL beneficios cuantificados** | | | **140** | | |

> Beneficios estratégicos adicionales no cuantificables monetariamente: confianza institucional, posicionamiento competitivo, atractividad como empleador del banco, alineación con visión de banca pública moderna.

### B.5 Optimism Bias y Contingencia

Aplicación del HM Treasury Green Book optimism bias para proyectos de TI de gran escala:

- **Costos**: contingencia +25% (en línea con Green Book +20% para "Standard Civil Engineering" + 5% adicional por complejidad multi-track) — ya incluida en TCO ROM.
- **Plazos**: buffer +20% sobre cronograma planeado del vendor — incluido en target de 30-36 meses para Opción 2.
- **Beneficios**: -20% del beneficio cuantificado por área de incertidumbre — ya reflejado en sensibilidad pesimista.

### B.6 Recomendación del Caso Económico

**Recomendación**: **Opción 2 — Balanceada**.

**Rationale**:

1. NPV punto medio positivo (+B/. 22M).
2. Cobertura STKE 89-95% — la más alta sin prima de costo.
3. Único camino que cumple **simultáneamente** con Acuerdo 1-2026 (E-15) y proceso competitivo Ley 22.
4. Defensibilidad pública alta (Marco EVAL v2.0 con Auditoría Interna).
5. Mitiga R-024 (ERP) y R-023 (AML) — críticos del programa.
6. Ventana de implementación 30-36 meses compatible con plazos regulatorios.

---

## Parte C — Caso Comercial (Commercial Case)

### C.1 Estrategia de Procurement

**Tres RFPs paralelos coordinados** bajo Ley 22 de Contrataciones Públicas:

| RFP | Categoría | Modalidad | Cronograma |
|-----|-----------|-----------|------------|
| **RFP-CBS** | Core Banking System | Procedimiento abierto bajo Ley 22; RFI ya emitido (DOC-RFI-001 junio 2026) | Apertura: ago-2026 / Cierre: oct-2026 / Selección: dic-2026 / Firma: feb-2027 |
| **RFP-ERP** | ERP externo para GL | Procedimiento abierto bajo Ley 22 | RFI: jun-2026 / Apertura: sep-2026 / Cierre: nov-2026 / Selección: ene-2027 / Firma: mar-2027 |
| **RFP-AML** | Motor AML externo | Procedimiento abierto bajo Ley 22 | RFI: jun-2026 / Apertura: sep-2026 / Cierre: nov-2026 / Selección: ene-2027 / Firma: mar-2027 |

**Marco normativo aplicable**: Ley 22 de Contrataciones Públicas; idoneidad jurídica SBP/MICI por categoría; participación abierta a vendors nacionales e internacionales con representación legal local.

### C.2 Evaluación del Mercado

**CBS** — Mercado evaluado en RSCH v2.0:
- **Tier-1 Global**: Temenos Transact (Líder Gartner MQ), Infosys Finacle (único con referente directo Panamá — BCP), TCS BaNCS, Oracle FLEXCUBE.
- **Tier-2 LatAm**: Cobis Topaz (oficina PA + 7 referentes locales), Bantotal, Datapro/eIBS (incumbente con Vencora).
- **Cloud-native**: Mambu, Thought Machine — descartados por soberanía.
- **Descartados verbalmente por el banco pero invitados objetivamente al RFP**: Temenos, Finacle, Mambu, SAP.

**ERP** — Mercado evaluado en RSCH v2.0:
- **Líderes Gartner MQ Cloud ERP for Service-Centric Enterprises**: Oracle Fusion, SAP S/4HANA, Microsoft Dynamics 365, Workday.
- **Challengers**: Infor CloudSuite, Oracle NetSuite.

**AML** — Mercado evaluado en RSCH v2.0:
- **Enterprise líderes (mindshare)**: NICE Actimize (16.3%), Oracle FCCM, SAS AML, FICO Siron/Tonbeller.
- **AI-native challengers**: Hawk:AI, ComplyAdvantage, Featurespace ARIC, Quantexa, Napier.

### C.3 Ruta de Sourcing

Para cada RFP:

1. **Pre-RFP (4-6 semanas)**: validación de criterios y pesos por Auditoría Interna; dictamen Legal del proceso (mitigación R-026); aprobación Comité de Tecnología.
2. **RFP emitido (6 semanas para respuesta del vendor)**: emisión a los vendors invitados con NDA firmado.
3. **Evaluación de propuestas (3 semanas)**: apertura administrativa (eliminatorios) + scoring ponderado por sub-paneles.
4. **Demos extendidas + PoC (8 semanas)**: para top-3 por categoría; PoC ampliada por R-031 (caso hipotecario + sindicados + factoring estatal + DDI).
5. **Reuniones de referencia (2 semanas)**: con clientes en producción.
6. **Síntesis y deliberación (2 semanas)**: sub-paneles → Steering Committee → recomendación.
7. **Decisión final (1 semana)**: Comité de Tecnología → JD.
8. **Negociación y contratación (8 semanas)**: Legal + Finanzas + Contraloría dictamen.

### C.4 Enfoque Contractual y Asignación de Riesgo

**Cláusulas obligatorias** (15, EVAL v2.0 E-11):

1. Residencia de datos en Panamá (BR-006).
2. SLA con penalizaciones (E-5).
3. TCO con tope ±10% + tope a true-ups + inflación (BR-003).
4. Cumplimiento regulatorio continuo (NFR-C-010).
5. Auditabilidad por Contraloría (NFR-C-008).
6. Soporte transicional con incumbente durante migración.
7. Capacitación en español certificada.
8. Documentación funcional y técnica en español.
9. Salida ordenada — portabilidad de datos.
10. Penalización por incumplimiento de plazos críticos (Acuerdo 1-2026).
11. Confidencialidad y protección de datos personales (Ley 81).
12. Anticorrupción y cumplimiento Ley 22.
13. **(NUEVA v2.0)** CBS: integración con ERP externo con SLA específico.
14. **(NUEVA v2.0)** CBS: exposición de eventos al motor AML externo.
15. **(NUEVA v2.0)** Tres RFPs: coordinación inter-RFP (sesiones de integración trimestrales).

**Asignación de riesgo CAP–Vendor**:

| Riesgo | Asignación | Mitigación contractual |
|--------|------------|------------------------|
| Cambio regulatorio durante el proyecto | Vendor | Cláusula NFR-C-010 cumplimiento continuo sin cobros extraordinarios |
| Incumplimiento de plazo Acuerdo 1-2026 | Vendor | Penalización contractual + cronograma con buffer |
| Falla de migración | Compartido | Paralelo ≥ 3 meses por bando + go/no-go con voto Operaciones + Riesgos |
| Calidad de datos heredada | CAP | Gobernanza diccionario (R-030) — proyecto interno paralelo |
| Brecha de seguridad del legado | CAP | Plan de remediación del legado (R-027) |
| Disponibilidad ≥ 99.95% / 99.99% | Vendor | SLA con penalizaciones |
| Vendor lock-in | CAP (mitigado) | Cláusula 9 portabilidad + arquitectura API abierta |
| Sobrecosto contractual | Vendor | Cláusula 3 (±10%, tope true-ups) |

---

## Parte D — Caso Financiero (Financial Case)

### D.1 Requerimiento Presupuestario

**Presupuesto total a 7 años (Opción 2 recomendada — punto medio)**: **B/. 175M**

Desglose por categoría (TCO 7 años punto medio):

| Categoría | CAPEX (años 1-3) | OPEX recurrente (años 4-7) | Total 7 años |
|-----------|------------------|-----------------------------|--------------|
| **CBS** | B/. 50M (licencias + implementación + migración) | B/. 45M | B/. 95M |
| **ERP** | B/. 22M (licencia + implementación) | B/. 18M | B/. 40M |
| **AML** | B/. 10M (licencia + implementación) | B/. 9M | B/. 19M |
| **Integración cross-RFP + remediación legado + transición Activo-Activo + capacitación + change management** | B/. 16M | B/. 5M | B/. 21M |
| **Total** | **B/. 98M** | **B/. 77M** | **B/. 175M** |

> Banda baja: B/. 150M (Cobis + Dynamics 365 + Hawk:AI con menor implementación SI).
> Banda alta: B/. 195M (Finacle + Oracle Fusion + NICE Actimize).
> Contingencia +25% sobre los ROM ya incluida en estos rangos.

### D.2 Fuente de Fondeo

**Propuesto**:

- **Reservas patrimoniales** + **emisión interna** (CAPEX años 1-3): ~B/. 98M.
- **Presupuesto operativo recurrente** (OPEX años 4-7): ~B/. 77M / 4 años = ~B/. 19M/año.
- **Modelo de fondeo CAPEX → OPEX** (BR-014): si el banco selecciona despliegue cloud regional con suscripción, el CAPEX se reduce a B/. ~50M y el OPEX sube a ~B/. ~26M/año. Decisión pendiente de la JD basada en dictamen Legal de soberanía y resultado de la consulta gubernamental sobre cloud.

### D.3 Umbrales de Aprobación

| Hito | Cuantía | Aprobador |
|------|---------|-----------|
| Aprobación del SOBC (este documento) | Total programa B/. 175M | Junta Directiva |
| Lanzamiento de RFI (ya hecho — CBS) | N/A | Comité de Tecnología |
| Aprobación del Marco de Evaluación (EVAL v2.0) | N/A | Comité de Tecnología + Auditoría Interna |
| Firma de contratos de los 3 RFPs | B/. 175M | JD + Contraloría dictamen |
| Variación material del cronograma o presupuesto (> 10%) | > B/. 17M | JD + Comité de Tecnología |
| Cambios contractuales menores | < B/. 5M | Comité de Tecnología |

### D.4 Asequibilidad

**Análisis de asequibilidad**:

- Patrimonio neto CAP: ~B/. 1,500M (referencia).
- ROE histórico: ~10%.
- Pago anual sostenido (B/. 19M OPEX, B/. 33M CAPEX peak año 1) representa ~1.3% del patrimonio en su año más alto.
- Cobertura por ingresos operativos brutos: comfortable.

**Veredicto preliminar**: **asequible** sin presión sobre la calificación crediticia ni sobre la operación normal. Análisis detallado en OBC.

### D.5 Flujo de Caja Proyectado (indicativo, B/. M)

| Año | CBS | ERP | AML | Integración / otros | Total flujo de caja |
|-----|-----|-----|-----|---------------------|---------------------|
| 1 | 18 | 6 | 3 | 5 | 32 |
| 2 | 22 | 10 | 5 | 8 | 45 |
| 3 | 10 | 6 | 2 | 3 | 21 |
| 4 | 12 | 4 | 2 | 2 | 20 |
| 5 | 11 | 4 | 2 | 1 | 18 |
| 6 | 11 | 5 | 2 | 1 | 19 |
| 7 | 11 | 5 | 3 | 1 | 20 |
| **Total** | **95** | **40** | **19** | **21** | **175** |

### D.6 Restricciones Presupuestarias

- Presupuesto JD anual aprobado debe absorber peak de B/. 45M en año 2 (implementación intensiva).
- Negociación de cronograma con vendors para suavizar el peak si la JD lo requiere (extender implementación 3 meses adicionales = reducción de peak ~15%).
- Reserva para contingencias del 25% ya incluida en los ROM.

### D.7 Valor por Dinero (VfM)

| Métrica | Opción 0 | Opción 1 | **Opción 2** | Opción 3 |
|---------|----------|----------|--------------|----------|
| TCO 7Y ajustado al riesgo (B/. M) | 110–130 | 120–185 | **160–213** | 212–267 |
| Cobertura metas STKE | 15% | 35% | **89–95%** | 95–97% |
| B/. M por % de cobertura | 8.0 | 4.5 | **2.0** | 2.4 |
| Beneficios cuantificados (B/. M) | ~10 | ~40 | **140** | 150 |
| Ratio beneficio/costo (B/C) | 0.08 | 0.30 | **0.85** | 0.62 |

**Valor por dinero**: Opción 2 es la más eficiente en términos de B/. por punto de cobertura y ratio B/C.

---

## Parte E — Caso de Gestión (Management Case)

### E.1 Gobernanza

**Estructura del Programa**:

- **Junta Directiva**: aprobación de gates (SOBC, presupuesto, contratos), apetito de riesgo, decisión final del vendor por categoría.
- **Comité de Tecnología**: revisión de avance, criterios y pesos del EVAL, recomendación a la JD.
- **Steering Committee del Programa** (semanal):
  - Aldo Ríos (Chair) — Innovación.
  - Gerencia de Tecnología (TI senior).
  - CFO — Finanzas.
  - CISO — Seguridad.
  - Cumplimiento.
  - Riesgos.
  - Legal.
  - PMO.
- **Sub-comités por categoría** (CBS / ERP / AML) con líderes técnicos respectivos.
- **Validación independiente**: Auditoría Interna valida criterios y pesos pre-RFP (mitigación R-026); Contraloría informada y consultada para gates clave.

**RACI** (extracto):

| Decisión | R | A | C | I |
|----------|---|---|---|---|
| Aprobación SOBC | Aldo Ríos | JD | Comité de Tecnología | Contraloría |
| Apertura RFP CBS / ERP / AML | Aldo Ríos | Comité de Tecnología | Auditoría Interna, Legal | JD, Contraloría |
| Selección de vendor por categoría | Sub-panel | JD | Comité de Tecnología, Steering | Contraloría |
| Firma de contrato | Legal + Finanzas | JD | Contraloría dictamen | Cumplimiento |
| Modificación contractual > B/. 5M | Aldo Ríos + Legal | Comité de Tecnología | Auditoría Interna | JD |

### E.2 Enfoque del Proyecto

**Enfoque general**: Híbrido — Waterfall para el RFP/contratación (estructura formal de gates) + Agile para la implementación (sprints quincenales con go/no-go por bando de migración).

**Migración por bandos** (no big-bang) con paralelo ≥ 3 meses por bando:

- Banda 1: cuentas pasivas + sucursales urbanas + canales digitales.
- Banda 2: cartera de crédito (hipotecario + personal + consumo).
- Banda 3: cartera comercial + sindicados + factoring + cartas de crédito.
- Banda 4: Caja Amiga + comarcas + segmentos especiales.

### E.3 Hitos Clave

| Hito | Fecha objetivo | Owner | Dependencias |
|------|----------------|-------|--------------|
| SOBC v2.0 aprobado por JD | 2026-07-15 | Aldo Ríos | Workshop apetito de riesgo + validación EVAL por Auditoría |
| Marco EVAL v2.0 firmado | 2026-07-30 | Comité de Tecnología | Dictamen Legal previo |
| RFI ERP + AML emitidos | 2026-06-25 | Aldo Ríos | Decisión arquitectónica firmada (ADRs) |
| RFP CBS / ERP / AML emitidos | 2026-08-15 | Aldo Ríos + Comité de Tecnología | EVAL aprobado |
| Cierre RFP CBS | 2026-10-15 | Sub-panel CBS | Vendors responden |
| Cierre RFP ERP + AML | 2026-11-15 | Sub-panel respectivos | Vendors responden |
| PoC ampliada (top-3 por categoría) | 2026-12-15 | Steering Committee | Casos definidos |
| Selección vendor CBS / ERP / AML | 2027-01-31 | JD | Síntesis sub-panel + recomendación |
| Firma de los 3 contratos | 2027-03-31 | Legal + JD | Contraloría dictamen |
| Plan de remediación legado para Art. 25 §1 (R-027) | 2027-01-31 | CISO + TI | — |
| Cumplimiento Art. 25 §1 vigencia | **2027-01-31** | Cumplimiento + TI | Plan de remediación legado |
| Implementación Banda 1 (cuentas + canales) | 2027-Q3 | Vendor + TI + Operaciones | Contratos firmados |
| Implementación Banda 2 (crédito) | 2027-Q4 / 2028-Q1 | Vendor + Negocio | Banda 1 estable |
| Cumplimiento Art. 14 vigencia | **2027-06-30** | Cumplimiento + TI | Funcionalidad nativa en CBS o plan de remediación |
| Go-live ERP + AML (paralelo a CBS Banda 2) | 2028-Q1 | Vendor + Finanzas | — |
| Go-live full CBS | 2028-Q2 | Vendor + Programa | Migración exitosa |
| Estabilización post-corte | 2028-Q2 / Q3 | Operaciones + Vendor | Go-live full |

### E.4 Recursos Requeridos

**Equipo CAP** (FTE peak año 1-2):

- **PMO**: 3 FTE (líder + 2 PMs por sub-comité).
- **Arquitectura**: 4 FTE (lead arquitecto + 3 dominios — datos, integración, seguridad).
- **Desarrollo / Integración**: 8 FTE.
- **Datos / Migración**: 6 FTE.
- **Negocio (subject matter experts)**: 10 FTE × 50% dedicación = 5 FTE.
- **Cumplimiento / Riesgos**: 2 FTE.
- **CISO / Seguridad**: 2 FTE.
- **Capacitación / change management**: 2 FTE.
- **Total CAP peak**: ~32 FTE.

**Equipo Vendor + SI**: tamaño dependiente del vendor; estimado 50–80 FTE peak.

**Costos de RRHH durante el programa**: ya incluidos en los ROM (~B/. 18-22M de los B/. 175M).

### E.5 Cambio Organizacional (Change Management)

**Plan de stakeholders**:

- **Stakeholder analysis** (STKE v1.0) ya identifica 27 stakeholders + 17 drivers.
- **Communication plan** dirigido a empleados, clientes externos, vendors actuales, Contraloría, Asamblea Nacional, prensa.
- **Capacitación en español** certificada (BR-009, NFR-U-002) — ~3,500 empleados a capacitar.
- **War room** durante migración (90 días previos + 90 días post go-live por banda).

**Resistencia al cambio (R-019)**:

- Mitigaciones: comunicación temprana, bonos de retención, claridad de carrera post-migración, sesiones de Q&A con empleados.

### E.6 Realización de Beneficios

**Mecanismo de seguimiento**:

- KPIs por beneficio BF-1..BF-11 (Caso Económico).
- Tablero de beneficios revisado mensualmente por Steering Committee.
- Revisión semestral por Comité de Tecnología.
- Revisión anual por JD.

**Owner de beneficios**: Aldo Ríos (responsable global), CFO (BF-2, BF-3, BF-10), Cumplimiento (BF-2, BF-7, BF-8, BF-11), Innovación (BF-1, BF-6), Operaciones (BF-4), Áreas de negocio (BF-5).

### E.7 Gestión de Riesgos

**Top 5 riesgos estratégicos** (ver RISK v2.0):

1. **R-024 (TECH, Crítico inherente / Alto residual 12)** — ERP no listo al go-live del CBS → cierre contable inviable. Mitigación: selección paralela del ERP, contrato con paralelo 90 días, cláusula coordinación inter-RFP (E-11.15).
2. **R-026 (COMPLIANCE, Alto residual 9)** — sesgo COBIS → impugnación Contraloría. Mitigación: Marco EVAL v2.0 validado por Auditoría Interna, dictamen Legal previo, memo justificativo por vendor.
3. **R-023 (COMPLIANCE, Alto residual 9)** — AML externo no listo → ROS UAF interrumpidos. Mitigación: selección paralela AML, contrato puente con proveedor actual, cláusula coordinación inter-RFP.
4. **R-025 (COMPLIANCE, Alto residual 8)** — Incumplimiento Acuerdo 1-2026 plazos Art. 25 §1 (ene-2027) y Art. 14 (jun-2027). Mitigación: plan de remediación del legado para Art. 25 §1 + criterio eliminatorio E-15 en RFP + monitoreo mensual.
5. **R-008 (STRATEGIC, Medio residual 9)** — Vendor lock-in. Mitigación: cláusula 9 contractual de portabilidad, arquitectura API abierta.

**Riesgos sobre apetito**: 14 de 37 riesgos (38%) exceden el apetito propuesto. **Recomendación**: workshop formal de apetito de riesgo con la JD como prerrequisito de aprobación del SOBC.

---

## Apéndices

### Apéndice A — Trazabilidad SOBC → STKE → REQ → RISK → EVAL

> Cada elemento del SOBC tiene trazabilidad documentada:
> - Stakeholder drivers (STKE) → BR del REQ v2.0 → eliminatorios del EVAL v2.0
> - Riesgos del RISK v2.0 → mitigaciones contractuales del Caso Comercial
> - Beneficios BF-N (Caso Económico) → metas STKE G-N → outcomes O-N

### Apéndice B — Resumen de los 3 procesos RFP

(Ver detalle en EVAL v2.0)

### Apéndice C — Plan de Acción priorizado del Programa

Sincronizado con el Plan de Acción del RISK v2.0:

- **P0 (esta semana)**: RFI ERP, RFI AML, dictamen Legal RFP, consulta gubernamental cloud, dictamen Legal soberanía.
- **P1 (próximas 4-8 semanas)**: Plan retención talento, remediación seguridad legado, cláusulas eliminatorias del RFP, contrato extendido con DataPro, ampliación de PoC, matriz ponderación validada por Auditoría, workshop apetito.
- **P2 (próximos 3-6 meses)**: Pen-test legado, war-room comunicación, decisión BPMs, gobernanza diccionario, transición Activo-Activo, plan offline Caja Amiga, plan remediación Art. 25 §1, seguro ciber, caso CAPEX/OPEX.
- **P3 (próximos 6-12 meses)**: Validación FECI, plan migración SITECA, plan estabilización post-corte, reglas calidad y Data Stewards, FinOps, gobernanza cambio.

---

## Recomendación Final y Decisión Solicitada

### Recomendación

> **Aprobar el lanzamiento del programa Reemplazo de Core Banking + ERP + AML** bajo la **Opción 2 — Balanceada**, con presupuesto blendado de **B/. 150–195M a 7 años** (punto medio **B/. 175M**), tres RFPs paralelos coordinados bajo Ley 22, despliegue on-premise o cloud privado regional con presencia panameña, y gobernanza con Steering Committee único + Auditoría Interna como validador independiente.

### Criterios Go / No-Go

- **GO si**:
  - JD aprueba el presupuesto blendado y el modelo de gobernanza propuesto.
  - Workshop de apetito de riesgo formalizado.
  - Dictamen Legal sobre soberanía iniciado (no necesariamente cerrado, pero iniciado).
  - Marco EVAL validado por Auditoría Interna en proceso.
- **NO-GO si**:
  - JD requiere reformular alcance (e.g., excluir ERP — pero esto requiere otra arquitectura que el equipo no recomienda).
  - Cambio político / de gobierno desestabiliza prioridades.
  - Dictamen Legal de soberanía revela barrera regulatoria infranqueable que requiera redesign.

### Próximos pasos si se aprueba

1. **Esta semana**: emitir RFI ERP + AML; iniciar dictamen Legal RFP (P0).
2. **Próximas 4 semanas**: cerrar Marco EVAL v2.0 con Auditoría Interna; ADRs formales (8 decisiones); workshop apetito JD.
3. **Próximas 6 semanas**: aprobación Comité de Tecnología + JD; ejecutar `/arckit:sow` para los 3 SOWs formales.
4. **Próximas 10 semanas**: emisión de los 3 RFPs.

---

## Aprobación del Documento

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Owner del SOBC | Aldo Ríos — Innovación | [PENDING] | [PENDING] |
| CFO / Finanzas | [PENDING] | [PENDING] | [PENDING] |
| CISO | [PENDING] | [PENDING] | [PENDING] |
| Cumplimiento | [PENDING] | [PENDING] | [PENDING] |
| Riesgos | [PENDING] | [PENDING] | [PENDING] |
| Legal | [PENDING] | [PENDING] | [PENDING] |
| Auditoría Interna | [PENDING] | [PENDING] | [PENDING] |
| Comité de Tecnología | [PENDING] | [PENDING] | [PENDING] |
| **Junta Directiva (aprobación final)** | [PENDING] | [PENDING] | [PENDING] |

---

## External References

| Doc ID | Filename | Type | Source Location | Description |
|--------|----------|------|-----------------|-------------|
| ARC-001-REQ-v2.0 | ARC-001-REQ-v2.0.md | Markdown | `projects/001-evaluacion-core-banking/` | 193 requisitos refrescados con corrigendum Acuerdo 1-2026 |
| ARC-001-RISK-v2.0 | ARC-001-RISK-v2.0.md | Markdown | `projects/001-evaluacion-core-banking/` | 37 riesgos refrescados con corrigendum |
| ARC-001-RSCH-v2.0 | research/ARC-001-RSCH-v2.0.md | Markdown | `projects/001-evaluacion-core-banking/research/` | Research de 3 categorías (CBS, ERP, AML) |
| ARC-001-EVAL-v2.0 | ARC-001-EVAL-v2.0.md | Markdown | `projects/001-evaluacion-core-banking/` | Marco de Evaluación multi-track con 15 eliminatorios + 3 ponderaciones |
| ARC-001-STKE-v1.0 | ARC-001-STKE-v1.0.md | Markdown | `projects/001-evaluacion-core-banking/` | 27 stakeholders, 17 drivers, 10 metas, 10 outcomes |
| ARC-000-PRIN-v1.1 | ARC-000-PRIN-v1.1.md | Markdown | `projects/000-global/` | 21 principios |
| DOC-RFI-001 | 7.RFI-RFI_CAP_CoreBancario_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | RFI v1.0 emitido jun-2026 |
| DOC-POC-001 | 5.PreparaciónPOC-POC_seleccion_core_banking_CAP_v1.docx | Word | `projects/001-evaluacion-core-banking/external/` | Ficha PoC v1.0 |
| DOC-SES-001..009 | Resúmenes de las 8 sesiones presenciales | Word | `projects/001-evaluacion-core-banking/external/` | Insumos sesiones 25–28 mayo 2026 |
| tech-notes/acuerdo-1-2026-implementation.md | Tech Note | Markdown | `projects/001-evaluacion-core-banking/tech-notes/` | Implementación de Acuerdo 1-2026 (umbral 10%, plazos) |

---

**Generated by**: ArcKit `/arckit:sobc` command
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros — Evaluación y Selección de Core Banking (Project 001)
**AI Model**: Claude Opus 4.7
**Generation Context**: v2.0 refresh — refleja la decisión arquitectónica de v2.0 (CBS + ERP + AML como 3 procesos coordinados), TCO blendado B/. 150–195M a 7 años, NPV +B/. 22M punto medio, R-024 (ERP Crítico) + R-023 (AML Alto) + R-025 (Acuerdo 1-2026 plazos) + R-026 (sesgo COBIS) integrados como dependencias críticas del cronograma y del proceso. Recomienda Opción 2 — Balanceada.
