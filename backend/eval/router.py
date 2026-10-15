from fastapi import APIRouter, Depends, HTTPException, status

from backend.auth.dependencies import require_roles
from shared.python.schemas import UserRole

router = APIRouter(prefix="/api/eval", tags=["evaluation"])


@router.get("/status", responses={501: {"description": "Feature stub"}})
def evaluation_status(_user=Depends(require_roles(UserRole.doctor, UserRole.admin))):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="evaluation harness is owned by feature/swe-lead")
