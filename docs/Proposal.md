# Project Proposal — MedAssist

## Title
**MedAssist — Secure Agentic RAG-Based Medical Question Answering Platform**

## Description
MedAssist is a university Software Engineering project that explores a secure medical Q&A workflow combining structured symptom input, retrieval-augmented generation, patient-specific conversational context, consent/audit controls, and a doctor-facing triage surface. The implementation is organized as independently owned full-stack domains behind shared contracts to support parallel development and controlled integration.

> The project is educational and must not be represented as a substitute for professional medical diagnosis or emergency care.

## Team Roles and Branches

| Team member | Branch | Responsibility |
|---|---|---|
| Mostafa | `feature/rag-core` | Agentic RAG: retrieve → sufficiency-check → corrective retry/reformulation → generate; minimal dedicated frontend |
| Adham | `feature/body-map` | Interactive SVG body map, severity/color coding, backend adapter from structured pain data to RAG query |
| Omar | `feature/patient-memory` | Per-patient conversation memory, patient-reference detection, doctor thread/switch UI |
| Ziad | `feature/security-consent` | Encryption-at-rest implementation, tamper-evident audit log, RBAC, rate limiting, Consent & Trust Center UI |
| Nour | `feature/swe-lead` | Architecture decisions, deployment pipeline, triage dashboard full-stack, evaluation harness |

## Timeline

### Phase 1 — Week 6
- SRS baseline completed and reviewed.
- Shared schemas/API contracts stable enough for parallel development.
- Working prototype with implemented auth and first integrated vertical slices.
- Swagger/OpenAPI reviewed as current API contract.

### Phase 2 — Week 15
- Updated SRS.
- Completed SDD with architecture, class/sequence diagrams, design-pattern rationale, DB/API documentation.
- Completed Testing Document with traceable validation and defect tests.
- Integrated complete system and deployment pipeline.
- Evaluation harness reports plain-RAG vs agentic-RAG metrics.

## Initial Risks / Mitigations

| Risk | Mitigation |
|---|---|
| Parallel branches drift in data shape | Shared Python/TypeScript contracts changed together via PR review |
| Large merges late in semester | Small PRs, stable router boundaries, early integration |
| RAG quality claims are hard to justify | Versioned evaluation set + defined metrics + baseline comparison |
| Medical/security scope becomes too large | Keep prototype scope explicit; implement only rubric-relevant requirements |
