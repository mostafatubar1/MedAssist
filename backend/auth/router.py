from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.auth.dependencies import get_current_user
from backend.auth.security import create_access_token, hash_password, verify_password
from backend.database import get_db
from backend.models import PatientModel, UserCredentialModel, UserModel
from shared.python.schemas import AuthToken, LoginRequest, SignupRequest, User, UserRole

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/signup", response_model=AuthToken, status_code=status.HTTP_201_CREATED)
def signup(payload: SignupRequest, db: Session = Depends(get_db)) -> AuthToken:
    email = payload.email.strip().lower()
    if payload.role == UserRole.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin accounts require controlled provisioning")
    if db.scalar(select(UserModel).where(UserModel.email == email)) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = UserModel(email=email, role=payload.role.value)
    db.add(user)
    db.flush()
    db.add(UserCredentialModel(user_id=user.id, password_hash=hash_password(payload.password)))
    if payload.role == UserRole.patient:
        db.add(PatientModel(user_id=user.id, profile={}))
    db.commit()
    db.refresh(user)

    token = create_access_token(user.id, user.role)
    return AuthToken(access_token=token, user=User.model_validate(user))


@router.post("/login", response_model=AuthToken)
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> AuthToken:
    email = payload.email.strip().lower()
    user = db.scalar(select(UserModel).where(UserModel.email == email))
    credential = None if user is None else db.get(UserCredentialModel, user.id)
    if user is None or credential is None or not verify_password(payload.password, credential.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    token = create_access_token(user.id, user.role)
    return AuthToken(access_token=token, user=User.model_validate(user))


@router.get("/me", response_model=User)
def me(user: UserModel = Depends(get_current_user)) -> User:
    return User.model_validate(user)
