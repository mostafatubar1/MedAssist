from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UserRole(str, Enum):
    patient = "patient"
    doctor = "doctor"
    admin = "admin"


class QuestionStatus(str, Enum):
    pending = "pending"
    answered = "answered"


class MessageRole(str, Enum):
    patient = "patient"
    doctor = "doctor"
    assistant = "assistant"
    system = "system"


class Citation(BaseModel):
    title: str
    url: str
    snippet: str | None = None


class ConversationMessage(BaseModel):
    role: MessageRole
    content: str
    timestamp: datetime


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: str
    role: UserRole
    created_at: datetime


class Patient(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    profile: dict[str, str | None] = Field(default_factory=dict)
    created_at: datetime


class Question(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    patient_id: UUID
    doctor_id: UUID | None = None
    text: str
    status: QuestionStatus
    created_at: datetime


class Answer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    question_id: UUID
    text: str
    sources: list[Citation] = Field(default_factory=list)
    grounding_confidence: float
    created_at: datetime


class PainReport(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    patient_id: UUID
    body_region: str
    pain_type: str
    severity: int = Field(ge=0, le=10)
    duration: str
    created_at: datetime


class ConversationMemory(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    patient_id: UUID
    doctor_id: UUID
    messages: list[ConversationMessage] = Field(default_factory=list)
    updated_at: datetime


class AuditLogEntry(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    actor_id: UUID
    action: str
    target_id: UUID | None = None
    timestamp: datetime
    prev_hash: str | None = None
    hash: str


class ConsentSetting(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    patient_id: UUID
    data_category: str
    shared: bool


class SignupRequest(BaseModel):
    email: str
    password: str = Field(min_length=8)
    role: UserRole = UserRole.patient


class LoginRequest(BaseModel):
    email: str
    password: str


class AuthToken(BaseModel):
    access_token: str
    token_type: Literal["bearer"] = "bearer"
    user: User


class QuestionCreate(BaseModel):
    patient_id: UUID
    doctor_id: UUID | None = None
    text: str = Field(min_length=1)


class PainReportCreate(BaseModel):
    patient_id: UUID
    body_region: str
    pain_type: str
    severity: int = Field(ge=0, le=10)
    duration: str


class ConsentSettingUpdate(BaseModel):
    patient_id: UUID
    data_category: str
    shared: bool


class ApiMessage(BaseModel):
    message: str
