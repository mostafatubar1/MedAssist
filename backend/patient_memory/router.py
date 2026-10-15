from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from backend.auth.dependencies import require_roles
from shared.python.schemas import ConversationMemory, UserRole

router = APIRouter(prefix="/api/patient-memory", tags=["patient-memory"])


@router.get("/{patient_id}", response_model=ConversationMemory, responses={501: {"description": "Feature stub"}})
def get_memory(
    patient_id: UUID,
    _user=Depends(require_roles(UserRole.doctor)),
):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="patient-memory feature branch owns implementation")
