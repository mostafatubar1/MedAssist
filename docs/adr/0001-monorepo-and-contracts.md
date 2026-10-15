# ADR 0001 — Monorepo with Explicit Shared Contracts

## Status
Accepted for scaffold.

## Context
Five developers own independent full-stack features and need to merge without payload-shape drift.

## Decision
Use one monorepo, domain-aligned frontend/backend folders, and mirrored Pydantic/TypeScript contracts in `/shared`. FastAPI OpenAPI is the runtime API source of truth.

## Consequences
- Parallel work has stable integration boundaries.
- Contract changes become visible code-review events.
- Python/TypeScript duplication requires discipline; both files must change together.
