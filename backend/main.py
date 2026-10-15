from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.auth.middleware import JWTIdentityMiddleware
from backend.auth.router import router as auth_router
from backend.body_map.router import router as body_map_router
from backend.config import CORS_ORIGINS
from backend.dashboard.router import router as dashboard_router
from backend.database import Base, engine
from backend.eval.router import router as eval_router
from backend.patient_memory.router import router as patient_memory_router
from backend.rag_core.router import router as rag_core_router
from backend.security.router import router as security_router

# Import models so SQLAlchemy metadata is registered.
from backend import models as _models  # noqa: F401,E402

@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Prototype convenience; shared/staging/prod schema changes should use Alembic.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="MedAssist API",
    version="0.1.0",
    description="Coursework scaffold. Swagger is the SDD API Contract Summary source of truth.",
    docs_url="/docs",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(JWTIdentityMiddleware)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth_router)
app.include_router(rag_core_router)
app.include_router(body_map_router)
app.include_router(patient_memory_router)
app.include_router(security_router)
app.include_router(dashboard_router)
app.include_router(eval_router)
