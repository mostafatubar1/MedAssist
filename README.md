# MedAssist — Software Engineering Course Scaffold

MedAssist is a **university Software Engineering coursework scaffold** for a secure, agentic RAG-based medical Q&A platform. The repository intentionally contains contracts, stubs, interfaces, auth, routing, test patterns, and documentation/deployment scaffolding — **not** the graded feature implementations.

## Milestones

- **Phase 1 — Week 6:** SRS + working system prototype
- **Phase 2 — Week 15:** SRS + SDD + Testing Document + complete system

## Team ownership and branches

| Owner | Branch | Full-stack ownership |
|---|---|---|
| Mostafa | `feature/rag-core` | Agentic RAG pipeline contracts and minimal RAG-facing UI |
| Adham | `feature/body-map` | Interactive body map + pain-data-to-query adapter |
| Omar | `feature/patient-memory` | Patient conversation memory + doctor thread/reference UI |
| Ziad | `feature/security-consent` | Security/RBAC/rate-limit hooks + Consent & Trust Center |
| Nour | `feature/swe-lead` | Architecture, deployment, triage dashboard, evaluation harness |

## Repository map

```text
backend/
  auth/ security/ rag_core/ body_map/ patient_memory/ dashboard/ eval/
frontend/
  auth/ security/ rag_core/ body_map/ patient_memory/ dashboard/
shared/
  python/schemas.py
  types/index.ts
docs/
deploy/
.github/workflows/
```

`/shared/python/schemas.py` and `/shared/types/index.ts` are the cross-team API contracts and should be changed together in the same PR. SQLAlchemy persistence models live in `backend/models.py` and intentionally mirror those contracts.

## Local setup without Docker

### Backend

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r backend/requirements-dev.txt
cp .env.example .env
uvicorn backend.main:app --reload
```

Backend API: `http://localhost:8000`  
Swagger/OpenAPI: `http://localhost:8000/docs`

The backend defaults to SQLite if `DATABASE_URL` is not set, which is convenient for coursework smoke-testing. Docker Compose config uses PostgreSQL.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:5173`

## Local setup with Docker Compose

```bash
cp .env.example .env
docker compose up --build
```

Services:

- PostgreSQL: `localhost:5432`
- FastAPI: `localhost:8000`
- React/Vite: `localhost:5173`

## Auth flow

1. `POST /api/auth/signup` creates a patient/doctor user and returns a JWT; admin self-registration is blocked.
2. `POST /api/auth/login` verifies credentials and returns a JWT.
3. The frontend stores the token in `localStorage` for this prototype and sends it as `Authorization: Bearer <token>`.
4. `JWTIdentityMiddleware` decodes an optional bearer token into request state.
5. `require_roles(...)` dependencies enforce role access on protected routes.

> Coursework note: localStorage is convenient for the prototype but production systems should prefer a hardened token/session design (for example, secure HttpOnly cookies) and stronger account lifecycle controls.

## Shared-contract rule

Before merging any API-shape change:

1. Update `shared/python/schemas.py`.
2. Update `shared/types/index.ts` field-for-field.
3. Update `backend/models.py` if persistence changes.
4. Update/add tests.
5. Review OpenAPI at `/docs` and update `docs/SDD.md` API summary if needed.

## Database migrations

```bash
alembic -c backend/alembic.ini upgrade head
```

For the prototype, `backend.main` also calls `Base.metadata.create_all()` at startup so a fresh SQLite run works immediately. For shared/staging/prod databases, use Alembic migrations as the source of schema evolution.

## Tests

The test naming convention follows Sommerville's distinction:

- `*_validation.py`: are we building the system users/specification require?
- `*_defects.py`: does implementation behavior contain faults/edge-case failures?

Run:

```bash
pytest backend/tests
```

Example pair:

- `backend/tests/auth/test_auth_validation.py`
- `backend/tests/auth/test_auth_defects.py`

## Feature implementation boundaries

This scaffold deliberately does **not** implement:

- retrieval, sufficiency judging, query reformulation, or answer generation;
- clickable body-map behavior or medical interpretation;
- memory/reference-detection logic;
- encryption-at-rest implementation or real hash-chain verification;
- live dashboard analytics/urgency logic.

Those belong to the named feature branches.

## Design-pattern scaffolds

See `docs/SDD.md` and domain `patterns.py` files. Interfaces are provided only:

- RAG Core: **Strategy**
- Body Map: **Adapter**
- Patient Memory: **Repository** + event publisher contract
- Security: **Chain of Responsibility**
- Dashboard: **Observer**
- Evaluation: **Strategy**

## Production deployment scaffold

`deploy/backend.Dockerfile` and `deploy/frontend.Dockerfile` are production-oriented and separate from `backend/Dockerfile.dev` and `frontend/Dockerfile.dev` used by local Compose.

CI runs lint/tests/build checks on pull requests. A deploy-on-main workflow is included as a placeholder for Nour/team to connect to the final registry/host.
