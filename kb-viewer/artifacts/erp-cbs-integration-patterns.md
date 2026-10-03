# Tech Note: Patrones de Integración CBS ↔ ERP Externo

> **Template Origin**: Official | **ArcKit Version**: 5.13.0 | **Comando**: `/arckit:research`

## Document Control

| Campo | Valor |
|-------|-------|
| Document ID | ARC-001-TECH-erp-cbs-integration-patterns-v1.0 |
| Document Type | Tech Note |
| Project | 001-evaluacion-core-banking (Caja de Ahorros) |
| Classification | OFFICIAL |
| Status | DRAFT |
| Version | 1.0 |
| Created Date | 2026-06-11 |
| Last Updated | 2026-06-11 |
| Owner | TI + Finanzas + Innovación |

---

## Summary

A partir de v2.0 de los requisitos (BR-013), el nuevo CBS de CAP **no incluye GL completo**; el Libro Mayor consolidado migra a un **ERP externo** (Oracle Fusion Cloud ERP / Microsoft Dynamics 365 F&O / SAP S/4HANA según selección). El CBS sigue siendo responsable de los asientos contables transaccionales y debe exponerlos al ERP en **tiempo real o micro-batch ≤ 5 minutos** (INT-021 REQ v2.0). Esta nota documenta patrones recomendados de integración, mapeo de plan de cuentas SBP, gobernanza de cierre coordinado y consideraciones de reconciliación.

## Key Findings

### Patrones de Integración Recomendados

#### Patrón 1: Event-driven streaming (RECOMENDADO para alta volumetría)

- CBS publica eventos contables a un **bus / Kafka** por dominio (depósitos, créditos, comisiones, FECI, IAS 21, NIIF 16).
- ERP consume eventos vía conector Kafka (Oracle Fusion Integration Cloud, Microsoft Logic Apps + Service Bus, SAP Integration Suite) y materializa asientos en GL.
- Latencia objetivo: < 5 seg desde transacción a aparición en GL.
- Pros: tiempo real, desacople, escalable.
- Cons: complejidad operacional, requiere idempotencia y manejo de fallos en orden.

#### Patrón 2: Micro-batch por API REST (RECOMENDADO para baja volumetría inicial)

- CBS expone API REST `POST /accounting-entries/{batch-id}` con asientos del último ciclo de 5 min.
- ERP recibe el batch, valida, persiste en GL, devuelve ack con número de asiento ERP.
- CBS persiste el cruce.
- Pros: más simple, debuggable, auditable, suficiente para volúmenes iniciales.
- Cons: latencia > 1 min, riesgo de pérdida si lock ERP, no apto para volumetría > 5K TPS.

#### Patrón 3: Archivo + reconciliación nocturna (LEGACY — no recomendado)

- CBS genera archivo diario; ERP procesa en cierre nocturno.
- No cumple con micro-batch ≤ 5 min de BR-013.

### Mapeo del Plan de Cuentas SBP

- Plan SBP (1xx-6xx) cargado tanto en CBS como en ERP — **mismo catálogo, una fuente de verdad** (DR-006 REQ v2.0).
- Cambios de plan SBP propagados desde el ERP (master) al CBS (consumidor) vía proceso controlado.
- Cuentas "no modificables unilateralmente" (NFR-C-006) — workflow de gobernanza.

### Cierre Coordinado

- **Cierre diario CBS** → emisión final de asientos en `T+0`.
- **Recepción y validación en ERP** → cuadre con CBS antes de `T+1 09:00`.
- **Cierre mensual ERP** → bloqueo del mes en ERP solo cuando CBS confirma cierre estable.
- **Modelo dual NIIF 9 + Acuerdo 6-2000** (BR-005, FR-064, FR-065) — el ERP almacena ambas vistas vía Multi-GAAP / sub-ledgers diferenciados.

### Reconciliación

- **Reconciliación diaria** entre CBS y ERP — diferencia = 0 al cierre del corte.
- **Reconciliación mensual** consolidada con auditoría interna.
- **Trazabilidad bidireccional**: cada asiento ERP rastrea al evento transaccional CBS de origen (DR-008 linaje).

### Consideraciones por ERP vendor

| ERP | Patrón nativo recomendado | Conector pre-built CBS | Esfuerzo integración |
|-----|---------------------------|------------------------|----------------------|
| Oracle Fusion Cloud ERP | OIC (Oracle Integration Cloud) — REST + Event | Sinergia si FLEXCUBE (Oracle adapter) | Medio (si Oracle CBS), Alto si vendor heterogéneo |
| Microsoft Dynamics 365 F&O | Azure Service Bus + Logic Apps + Data Integrator | Conectores genéricos REST/Kafka | Medio |
| SAP S/4HANA PCE | SAP Integration Suite + Event Mesh | Conector Bank Communication Management | Medio (si SAP Banking) o Alto |
| Infor CloudSuite Financials | Infor ION middleware | Adaptadores REST | Alto |

### Idempotencia y Orden

- **Idempotencia**: cada evento contable incluye `idempotency-key` único — ERP rechaza duplicados.
- **Orden**: por instrumento / cuenta cliente, los asientos llegan en orden estricto (Kafka particionado por client-id o instrument-id).
- **Compensación**: si un asiento falla en ERP, el CBS recibe ack negativo y dispara compensación (asiento reverso).

## Relevance to Projects

- **Project 001 — Caja de Ahorros — Evaluación y Selección de Core Banking** (Panamá, 2026): pilar arquitectónico de la coordinación CBS ↔ ERP (BR-013, INT-021, FR-069).

## External References

| Citation ID | Source | Description |
|-------------|--------|-------------|
| DOC-RSCH-v2-08 | <https://www.aspiresys.com/casestudies/oracle-erp-fusion-finanical-cloud-implementation-for-banking/> | Aspire Systems — Oracle ERP Fusion implementation for banking patterns |
| ARC-001-REQ-v2.0 | `projects/001-evaluacion-core-banking/ARC-001-REQ-v2.0.md` | BR-013, INT-021, FR-069, FR-070 |

---

**Generated by**: ArcKit `/arckit:research` agent
**Generated on**: 2026-06-11
**ArcKit Version**: 5.13.0
**Project**: Caja de Ahorros (Project 001)
**AI Model**: Claude Opus 4.7
