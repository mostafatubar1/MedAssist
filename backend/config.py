from __future__ import annotations

import os


def _csv_env(name: str, default: str) -> list[str]:
    return [item.strip() for item in os.getenv(name, default).split(",") if item.strip()]


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./medassist.db")
JWT_SECRET = os.getenv("JWT_SECRET", "development-only-change-me")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "120"))
CORS_ORIGINS = _csv_env("CORS_ORIGINS", "http://localhost:5173")
