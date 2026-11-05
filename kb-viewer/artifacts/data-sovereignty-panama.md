# Tech Note: Data Sovereignty for Banking — Panamá

> **Template Origin**: Official | **ArcKit Version**: 5.0.1 | **Comando**: `/arckit:research`

## Document Control

| Campo | Valor |
|-------|-------|
| Document ID | ARC-001-TECH-data-sovereignty-panama-v1.0 |
| Document Type | Tech Note |
| Project | 001-evaluacion-core-banking (Caja de Ahorros) |
| Classification | OFFICIAL-SENSITIVE |
| Status | DRAFT |
| Version | 1.0 |
| Created Date | 2026-05-19 |
| Last Updated | 2026-05-19 |
| Owner | Legal + CISO + Innovación |

---

## Summary

La soberanía y residencia de datos en Panamá es **criterio eliminatorio** para Caja de Ahorros (BR-006 / DR-013 / Principio #6 PRIN v1.1). Aplica a datos personales de clientes, financieros, transaccionales, hipotecarios, analíticos y logs. El relevamiento confidencial (DOC-CB-001-C10, DOC-CB-001-C11) y directrices potenciales del MEF y la Contraloría sobre uso de cloud pública para datos financieros hacen que **vendors SaaS en nube pública internacional queden eliminados salvo dictamen legal explícito**. La situación 2025-2026 muestra que **ningún hyperscaler tiene región dedicada en Panamá** (AWS, Azure, GCP, OCI) — las opciones cumplientes son **on-prem en DC local**, **cloud privado regional con presencia física PA**, o **partner cloud panameño**. AWS publicó un Compliance Center para Panamá pero no equivale a región dedicada.

## Key Findings

### Estado del Cloud Público en Panamá (2025-2026)

- **AWS**: regiones más cercanas son São Paulo (sa-east-1) y N. Virginia (us-east-1). Presencia de Edge / CloudFront en Panamá pero sin región. AWS Panama Compliance Center facilita due diligence pero no resuelve soberanía.
- **Microsoft Azure**: regiones más cercanas son East US, South Central US, Brazil South. Sin región Panamá.
- **Google Cloud**: regiones más cercanas son us-south1 (Dallas), us-east1 (S. Carolina), southamerica-east1 (São Paulo). Sin región Panamá.
- **Oracle Cloud Infrastructure (OCI)**: regiones más cercanas son Querétaro (Mexico), Vinhedo (Brazil), San José (Chile). Sin región Panamá.
- **IBM Cloud**: Multi-zone region más cercana es Dallas; sin Panamá.

### Opciones Cumplientes con Soberanía

1. **On-premises en DC propio de Caja de Ahorros**: control máximo, requiere capacidad de operación 24/7 con DR. Compatible con todos los vendors Tier-1/Tier-2 evaluados.
2. **DC local Panamá co-location** (proveedores como Cable & Wireless Panama, Liberty Networks, Inversiones de Datacenter, NAP de las Américas): infraestructura física en territorio panameño con SLA contractual.
3. **Cloud privado regional con presencia panameña** — algunos hyperscaler partners ofrecen "Panama Cloud" sobre infraestructura local con compliance a soberanía. Verificar tipo de presencia (lógica vs física) en RFP.
4. **Vendor hosted en DC panameño**: ej. Cobis Topaz puede operar desde su oficina PA; Datapro puede operar híbrido. Negociar SLA y auditabilidad.

### Implicaciones para Cada Vendor

- **Mambu, Thought Machine Vault**: **BLOQUEADOS** en su forma SaaS estándar. Mambu opera multi-cloud sobre AWS/GCP/Azure; Vault Core multi-cloud sobre AWS típicamente. Ningún hyperscaler tiene Panamá. Cliente Towerbank PA con Mambu opera en región AWS no panameña — caso no transferible a banco estatal.
- **Temenos Banking Cloud SaaS**: regiones disponibles globales (EU, US, APAC) — sin Panamá. Opción: Hosted Private en DC local o on-prem.
- **TCS BaNCS Cloud, Oracle FLEXCUBE on OCI**: sin región PA. Opción: on-prem o partner cloud local.
- **Cobis Topaz**: oficina PA permite hosting on-prem o privado local — ventaja diferencial.
- **Datapro**: incumbente, ya opera on-prem en Caja de Ahorros — soberanía nativa.
- **Finastra Fusion**: vía SONDA con cloud regional, validar presencia PA.

### Dictamen Legal Vinculante (BR-006)

- Debe emitirse **antes del cierre del RFP**.
- Cubre: residencia física de datos personales, financieros y transaccionales por tipo de dato (cliente, transaccional, hipotecario, analítico, logs).
- Cláusulas contractuales de residencia obligatorias en contrato final.
- Mecanismo de verificación continuo (auditoría trimestral).
- Excepciones aprobables solo por Junta Directiva + Contraloría + validación SBP.

### Tipos de Datos y Sensibilidad

| Tipo de Dato | Sensibilidad | Recomendación de Residencia |
|--------------|--------------|------------------------------|
| Cédula, datos personales (DR-001) | Restricted | **Panamá obligatorio** |
| Saldos, transacciones (DR-003) | Confidential | **Panamá obligatorio** |
| Hipotecas Interés Preferencial (DR-004) | Confidential | **Panamá obligatorio** |
| Logs de auditoría / seguridad (NFR-SEC-005, NFR-C-007) | Internal | **Panamá fuertemente preferido** (retención 7 años, evidencia para Contraloría / SBP) |
| Métricas agregadas | Public/Internal | Flexible — puede agregarse fuera con anonimización |
| Backups y DR | Igual al dato fuente | **Panamá obligatorio** o región Latam con dictamen |

### Riesgos Asociados

- **CR-1**: dictamen legal retrasa cierre RFP — mitigar emitiéndolo como hito independiente.
- **CR-2**: vendor cambia de región sin notificar — mitigar con cláusula contractual + auditoría trimestral.
- **CR-3**: incidente regulatorio si dato sale de PA — alto impacto: SBP, Contraloría, Asamblea Nacional, AAA(pan).

## Relevance to Projects

- **Project 001 — Caja de Ahorros — Evaluación y Selección de Core Banking** (Panamá, 2026): criterio eliminatorio BR-006 / DR-013 — bloquea Mambu y Thought Machine SaaS en sus formas estándar.

## External References

| Citation ID | Source | Description |
|-------------|--------|-------------|
| AWS Panama | <https://aws.amazon.com/financial-services/security-compliance/compliance-center/pa/> | AWS Panama Compliance Center |
| ARC-000-PRIN-v1.1 P6 | `projects/000-global/ARC-000-PRIN-v1.1.md` | Principio 6 — Soberanía y Residencia |
| ARC-001-REQ-v1.0 BR-006 | `projects/001-evaluacion-core-banking/ARC-001-REQ-v1.0.md` | BR-006 dictamen legal, DR-013 residencia |
| R-22 Towerbank | <https://mambu.com/en/customer/towerbank> | Caso Towerbank Panamá + Mambu + AWS (no transferible a banco estatal) |

---

**Generated by**: ArcKit `/arckit:research` agent
**Generated on**: 2026-05-19
**ArcKit Version**: 5.0.1
**Project**: Caja de Ahorros (Project 001)
**AI Model**: claude-opus-4-7 (1M context)
