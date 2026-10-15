from fastapi import APIRouter, Depends, HTTPException, status

from backend.auth.dependencies import require_roles
from shared.python.schemas import PainReport, PainReportCreate, UserRole

router = APIRouter(prefix="/api/body-map", tags=["body-map"])


@router.post("/pain-reports", response_model=PainReport, responses={501: {"description": "Feature stub"}})
def create_pain_report(
    payload: PainReportCreate,
    _user=Depends(require_roles(UserRole.patient, UserRole.doctor)),
):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="body-map feature branch owns implementation")
