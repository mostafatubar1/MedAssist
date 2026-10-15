# Scaffold Verification

This file records what was verified when the scaffold archive was produced.

## Verified

- `pytest backend/tests -q` — all scaffold tests pass.
- Real local FastAPI HTTP smoke flow — signup → JWT → login → `/api/auth/me` succeeds.
- RBAC defect test — patient access to doctor dashboard is rejected with HTTP 403.
- Admin self-signup is rejected with HTTP 403.
- Shared core Pydantic and TypeScript interface field names are checked for parity by an automated test.
- Alembic baseline migration applies successfully to a fresh SQLite database and creates all core tables.
- `docker-compose.yml` and both GitHub Actions workflow files parse as valid YAML.
- Python source compiles successfully.

## Environment-limited checks

The archive-generation environment does **not** provide a Docker daemon, so `docker compose up --build` could not be executed here. It also cannot reach the npm package registry, so a real `npm install && npm run build` could not be completed here. The Compose/Dockerfiles and frontend dependency/build configuration are provided for the team/CI to run in an environment with Docker and package-network access.

Recommended first team-machine verification:

```bash
cp .env.example .env
docker compose up --build
# in another terminal
curl http://localhost:8000/health
```

Then open `http://localhost:5173`, create a patient or doctor account, and verify login/role routing.
