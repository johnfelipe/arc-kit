# Tech Note: Implementación del Acuerdo SBP 1-2026 — Plazos, Umbrales y Patrones de Diseño

> **Template Origin**: Official | **ArcKit Version**: 5.13.0 | **Comando**: `/arckit:research`

## Document Control

| Campo | Valor |
|-------|-------|
| Document ID | ARC-001-TECH-acuerdo-1-2026-implementation-v1.0 |
| Document Type | Tech Note |
| Project | 001-evaluacion-core-banking (Caja de Ahorros) |
| Classification | OFFICIAL-SENSITIVE |
| Status | DRAFT |
| Version | 1.0 |
| Created Date | 2026-06-11 |
| Last Updated | 2026-06-11 |
| Owner | Cumplimiento + Innovación |

---

## Summary

El **Acuerdo 1-2026 de la SBP** (Resolución SBP-JD-0001-2026 del 16 de enero 2026 [DOC-RSCH-v2-09, DOC-RSCH-v2-13]) actualiza las disposiciones para prevenir el uso indebido de los servicios bancarios y fiduciarios con propósitos AML/CFT/FPADM (financiamiento de la proliferación de armas de destrucción masiva). Transforma el cumplimiento de un modelo **reactivo, manual y uniforme a uno proactivo, tecnológico y basado en riesgos** [DOC-RSCH-v2-15]. Introduce dos cambios cuantificables que el CBS y el motor AML deben soportar antes de plazos discretos:

1. **Identificación del beneficiario final con umbral ≥ 10%** (no 25% como aparece en REQ v2.0 — error a corregir).
2. **Geolocalización inferencial obligatoria** para clientes digitales — sirve para verificar la ubicación real del solicitante y mitigar riesgos asociados a jurisdicciones sancionadas.

## Key Findings

### Plazos críticos del Acuerdo 1-2026

| Artículo | Materia | Plazo de cumplimiento | Impacto en el proyecto |
|----------|---------|-----------------------|------------------------|
| Articulado general | Marco AML/CFT actualizado | Vigencia general inmediata (jul-2025 según vigencia plena del nuevo marco) | El CBS legado debe cumplir lo aplicable mientras se implementa el nuevo CBS |
| **Artículo 25 §1** | (regla específica de identificación) | **31 enero 2027** | Mitigación pre-nuevo-CBS si el go-live es posterior |
| **Artículo 14** | Beneficiario final + geolocalización inferencial digital | **30 junio 2027** | **Criterio eliminatorio temporal del RFP**: cualquier vendor cuyo cronograma no entregue antes de jun-2027 queda descartado |

### Disposiciones clave

- **Beneficiario final**: identificar y verificar al individuo que posee el **10% o más** de las acciones o ejerce control efectivo. Diferencia con UE (25%) y FATF (25%): Panamá adopta un umbral más estricto.
- **Documentación**: fuentes confiables internas y externas — el motor AML debe integrarse con Panadata (KYC) y opcionalmente con APIs corporativas para validación.
- **Geolocalización inferencial**: no es solo capturar GPS — es **inferir** la ubicación a partir de IP, comportamiento, dispositivo. Comparar contra perfil del cliente para detectar anomalías (sanctioned jurisdictions).
- **Risk-based approach**: la due diligence debe escalar según riesgo, no aplicarse uniformemente.
- **Multas**: el RSM Consultoría documenta que las multas son **elevadas** y disuasivas [DOC-RSCH-v2-15].

### Implicación para el RFP CBS

- Todos los vendors CBS deben entregar **FR-052** (beneficiario final ≥ 10%) y **FR-053** (geolocalización inferencial digital) **antes de junio 2027**.
- Vendors con cronograma > 18 meses post-decisión quedan en zona roja — si el RFP cierra en oct-2026, deben entregar antes de jun-2027 (8 meses) — solo Cobis (oficina PA), Datapro (incumbente) y vendors con configuración pre-existente Panamá lo cumplen razonablemente.
- **Plan B para vendors Tier-1**: parametrización ad-hoc del módulo de compliance regional + integración Panadata + extensión por SI.

### Implicación para el RFP AML

- Motor AML debe procesar geolocalización inferencial como atributo del evento transaccional (FR-048 streaming).
- Workflow de beneficiario final debe disparar alertas ante cambios societarios (FR-052) — integración con Panadata + bureau (INT-023).
- Hawk:AI publica capacidades nativas alineadas; NICE Actimize y Oracle FCCM requieren configuración del módulo de risk scoring.

### Patrones de diseño recomendados

1. **Captura de geolocalización en el canal digital**:
   - Multiple signals: IP+ASN, dispositivo (UA), GPS si disponible, comportamiento (BIN, antecedentes de login).
   - Inferencia: confidence score por feature; combinación bayesiana.
   - Persistencia: como atributo de la sesión (DR-022 streaming hacia Data Lake) y del evento transaccional.

2. **Workflow de beneficiario final**:
   - Apertura de persona jurídica → análisis de capas societarias (Panadata API) → identificación de personas con ≥ 10% control → creación de CIF para cada uno → enlace con la sociedad.
   - Triggers de re-evaluación: alta de socio, baja, transferencia accionaria, fusión.
   - Almacenamiento inmutable de la cadena de evidencia (DR-018).

3. **Risk scoring centralizado**:
   - El CBS expone el evento transaccional + atributos (geolocalización + perfil cliente + producto) al motor AML.
   - El motor AML calcula score y devuelve decisión (allow / hold / block) con latencia < 200 ms (NFR-P-005).
   - El CBS bloquea la transacción si el motor AML lo instruye (FR-048).

### Riesgos de implementación

- **CR-2025-A**: Vendor selecciona post-feb 2027 → no llega antes de jun-2027 → multa.
- **CR-2025-B**: Implementación Panadata insuficiente → Cumplimiento opera con manual capa de validación → carga operacional.
- **CR-2025-C**: Geolocalización inferencial mal calibrada → falsos positivos UAF → reputación.

## Relevance to Projects

- **Project 001 — Caja de Ahorros — Evaluación y Selección de Core Banking** (Panamá, 2026): criterio eliminatorio temporal de RFP CBS y AML; pilar de Categoría 3 AML; afecta cronograma maestro.

## External References

| Citation ID | Source | Description |
|-------------|--------|-------------|
| DOC-RSCH-v2-09 | <https://www.superbancos.gob.pa/documentos/regulacion/acuerdos_otros_sujetos/2026/Acuerdo_01-2026.pdf> | Acuerdo 1-2026 PDF oficial SBP |
| DOC-RSCH-v2-13 | <https://www.superbancos.gob.pa/en/node/1652> | SBP press release Rule 1-2026 (inglés) |
| DOC-RSCH-v2-14 | <https://gala.com.pa/nuevo-marco-aml-cft-bancario-en-panama-acuerdo-1-2026/> | Galindo Arias López — análisis legal Acuerdo 1-2026 |
| DOC-RSCH-v2-15 | <https://www.rsm.global/panama/es/insights/actualizacion-clave-en-prevencion-de-blanqueo-de-capitales-que-cambia-con-el-acuerdo-1-2026> | RSM Panamá — Acuerdo 1-2026 transforma de reactivo a proactivo basado en riesgos |
| ARC-001-REQ-v2.0 | `projects/001-evaluacion-core-banking/ARC-001-REQ-v2.0.md` | FR-052, FR-053 |

---

**Generated by**: ArcKit `/arckit:research` agent
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros (Project 001)
**AI Model**: Claude Opus 4.7
