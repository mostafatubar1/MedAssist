from fastapi import APIRouter, Depends, HTTPException, status

from backend.auth.dependencies import require_roles
from shared.python.schemas import AuditLogEntry, ConsentSetting, ConsentSettingUpdate, UserRole

router = APIRouter(prefix="/api/security", tags=["security-consent"])


@router.get("/consents", response_model=list[ConsentSetting], responses={501: {"description": "Feature stub"}})
def list_consents(_user=Depends(require_roles(UserRole.patient))):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="security-consent feature branch owns implementation")


@router.put("/consents", response_model=ConsentSetting, responses={501: {"description": "Feature stub"}})
def update_consent(
    payload: ConsentSettingUpdate,
    _user=Depends(require_roles(UserRole.patient)),
):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="security-consent feature branch owns implementation")


@router.get("/audit-log", response_model=list[AuditLogEntry], responses={501: {"description": "Feature stub"}})
def audit_log(_user=Depends(require_roles(UserRole.patient, UserRole.admin))):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="security-consent feature branch owns implementation")
