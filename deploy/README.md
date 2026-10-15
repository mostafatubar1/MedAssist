# Deployment Scaffold

Owned by **Nour (`feature/swe-lead`)**.

- `backend.Dockerfile`: production-oriented FastAPI container.
- `frontend.Dockerfile`: multi-stage Vite build served by nginx.
- `nginx.conf`: SPA fallback only; add reverse proxy/TLS policy for the selected host.
- `.github/workflows/deploy.yml`: placeholder workflow triggered after merges to `main`.

The actual registry, secrets, host, TLS, database service, backups, observability, and migration strategy are intentionally left for the team to choose/document.
