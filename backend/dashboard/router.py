from fastapi import APIRouter, Depends, HTTPException, status

from backend.auth.dependencies import require_roles
from shared.python.schemas import Question, UserRole

router = APIRouter(prefix="/api/dashboard", tags=["triage-dashboard"])


@router.get("/queue", response_model=list[Question], responses={501: {"description": "Feature stub"}})
def queue(_user=Depends(require_roles(UserRole.doctor, UserRole.admin))):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="dashboard feature branch owns implementation")
