from fastapi import APIRouter, Depends, HTTPException, status

from backend.auth.dependencies import require_roles
from shared.python.schemas import Answer, QuestionCreate, UserRole

router = APIRouter(prefix="/api/rag", tags=["rag-core"])


@router.post("/questions", response_model=Answer, responses={501: {"description": "Feature stub"}})
def ask_question(
    payload: QuestionCreate,
    _user=Depends(require_roles(UserRole.patient, UserRole.doctor)),
):
    """Mostafa-owned stub: retrieve → sufficiency-check → corrective retry → generate."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="rag-core feature branch owns implementation")
