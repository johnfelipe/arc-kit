# Tech Note: Core Banking Architectures — Microservices vs Modernized Monolith vs Composable SaaS

> **Template Origin**: Official | **ArcKit Version**: 5.0.1 | **Comando**: `/arckit:research`

## Document Control

| Campo | Valor |
|-------|-------|
| Document ID | ARC-001-TECH-core-banking-architectures-v1.0 |
| Document Type | Tech Note |
| Project | 001-evaluacion-core-banking (Caja de Ahorros) |
| Classification | OFFICIAL |
| Status | DRAFT |
| Version | 1.0 |
| Created Date | 2026-05-19 |
| Last Updated | 2026-05-19 |
| Owner | Aldo Ríos — Innovación |

---

## Summary

El mercado de Core Banking 2025-2026 se segmenta en tres arquetipos arquitectónicos con implicaciones diferenciadas para riesgo, TCO y agilidad: (1) **Legacy monolítico modernizado** (Datapro e-IBS, Cobis Topaz One, Bantotal, Finacle universal, Temenos Transact en su deployment tradicional), (2) **Tier-1 modular con re-platforming cloud** (Temenos Banking Cloud, TCS BaNCS composable core, Oracle FLEXCUBE on OCI, Finastra Fusion Phoenix on Azure, FIS Modern Banking Platform), y (3) **Cloud-native microservices SaaS** (Mambu, Thought Machine Vault Core, Pismo). Para un banco estatal como Caja de Ahorros, el balance entre madurez probada en Panamá / Latam y agilidad de microservices favorece el arquetipo (2) con despliegue en cloud privado local o on-prem, sobre opciones puramente SaaS bloqueadas por soberanía.

## Key Findings

### Arquetipo 1: Legacy Monolítico Modernizado

- **Definición**: códigos base maduros (Java EE, .NET, ocasionalmente Pro*C/COBOL), bases de datos relacionales centrales (Oracle DB, SQL Server, DB2), procesamiento batch nocturno tradicional con mejoras hacia real-time, APIs externas vía middleware adicional.
- **Vendors**: Datapro e-IBS, Bantotal, partes de Cobis (pre-Topaz One), Finacle universal deployments antiguos, Temenos T24 legacy.
- **Pros**: madurez probada, alto nivel de configurabilidad por años de uso real, conocimiento extendido entre SI regionales, regulación adaptada.
- **Cons**: escalado vertical predominante, dependencia de DB centralizada, deuda técnica acumulada, despliegues con downtime requeridos, deployments cada 6-12 meses no semanales.

### Arquetipo 2: Tier-1 Modular con Re-platforming Cloud

- **Definición**: arquitectura modular con servicios por dominio (cuentas, créditos, contabilidad), capacidad de despliegue en Kubernetes / cloud privado / hyperscaler, APIs REST + AsyncAPI nativas, eventos vía Kafka / MQ, transición desde monolito core hacia composable.
- **Vendors**: Temenos Banking Cloud / Hosted Private, TCS BaNCS Composable Core, Oracle FLEXCUBE on OCI, Finastra Fusion Phoenix on Azure, FIS Modern Banking Platform, Cobis Topaz One (evolución composable).
- **Pros**: balance madurez + modernización, posibilidad de despliegue privado para soberanía, ecosistema de SI familiar, certificaciones globales.
- **Cons**: deuda histórica subyacente puede aflorar, true-ups por módulos opcionales, customizaciones legacy pesan en upgrades.

### Arquetipo 3: Cloud-native Microservices SaaS

- **Definición**: microservices nativos desde diseño, multi-tenancy SaaS, smart contracts / DSLs para productos financieros (Vault Core Python), event-driven 24/7, deployments diarios, scaling automático, sin DB compartida.
- **Vendors**: Mambu, Thought Machine Vault Core, Pismo, 10X Banking (UK), Engine by Starling (UK).
- **Pros**: máxima agilidad, mejor experiencia developer, TCO inicial bajo en cloud público, time-to-market 6-12 meses para neo-banks.
- **Cons**: **sin opción on-prem ni cloud privado nativo** — bloquea soberanía nacional Panamá; menor cobertura funcional out-of-the-box para casos complejos (treasury, wealth, trade finance, regulaciones nacionales específicas); riesgo "primer cliente" en mercados como Panamá.

### Implicación para Caja de Ahorros

Dada la restricción de soberanía (BR-006 / DR-013 / Principio #6 PRIN v1.1), la complejidad regulatoria SBP (Acuerdos 6-2000, 4-2013, 5-2011, 3-2009, 8-2010, NIIF 9, modelo dual obligatorio), y la sensibilidad política de un banco estatal con AAA(pan), el **Arquetipo 2 con despliegue privado** (on-prem PA o cloud privado regional con presencia PA) es el sweet spot. Los candidatos del shortlist (Temenos, Finacle, FLEXCUBE, Cobis Topaz, Datapro) caen en este cuadrante. Arquetipo 3 quedaría disponible solo con waiver Junta+Contraloría sobre soberanía.

## Relevance to Projects

- **Project 001 — Caja de Ahorros — Evaluación y Selección de Core Banking** (Panamá, 2026): base para decisión de modelo de despliegue del nuevo Core.

## External References

| Citation ID | Source | Description |
|-------------|--------|-------------|
| Crassula 2026 | <https://crassula.io/guides/core-banking/> | Core Banking Systems 2026 — taxonomía arquitectónica |
| Mambu | <https://mambu.com/en/insights/articles/15-years-of-innovation> | 15 years of innovation — shifts arquitectónicos |
| Gartner MQ 2025 | <https://www.gartner.com/en/documents/6133159> | Gartner MQ Retail Core Banking NA 2025 |

---

**Generated by**: ArcKit `/arckit:research` agent
**Generated on**: 2026-05-19
**ArcKit Version**: 5.0.1
**Project**: Caja de Ahorros (Project 001)
**AI Model**: claude-opus-4-7 (1M context)
