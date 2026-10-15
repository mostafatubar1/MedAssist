# Branch Workflow

Start branches from the same scaffold commit:

```bash
git checkout main
git pull
git checkout -b feature/rag-core
# repeat from main for each named branch
```

Recommended merge order is not based on feature importance; use small PRs and merge shared-contract changes first. If a feature needs a new field or endpoint contract, open that contract change separately or coordinate it before feature-specific implementation.

Protected integration surfaces:

- `/shared/**`
- `backend/models.py`
- route prefixes and response shapes
- auth role semantics
- Alembic migrations

Avoid cross-feature implementation imports. Depend on shared schemas/interfaces/events instead.
