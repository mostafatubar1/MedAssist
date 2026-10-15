import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

TEST_DB = Path("/tmp/medassist_test.db")
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB}"
os.environ["JWT_SECRET"] = "test-secret-only-at-least-32-bytes-long"

from backend.database import Base, engine  # noqa: E402
from backend.main import app  # noqa: E402


@pytest.fixture(autouse=True)
def clean_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
