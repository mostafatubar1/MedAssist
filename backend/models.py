from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Uuid

from backend.database import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)


class UserCredentialModel(Base):
    __tablename__ = "user_credentials"

    user_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    password_hash: Mapped[str] = mapped_column(String(512), nullable=False)


class PatientModel(Base):
    __tablename__ = "patients"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("users.id"), unique=True, index=True, nullable=False)
    profile: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)


class QuestionModel(Base):
    __tablename__ = "questions"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    patient_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("patients.id"), index=True, nullable=False)
    doctor_id: Mapped[UUID | None] = mapped_column(Uuid, ForeignKey("users.id"), index=True, nullable=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="pending", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)


class AnswerModel(Base):
    __tablename__ = "answers"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    question_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("questions.id"), unique=True, index=True, nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    sources: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    grounding_confidence: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)


class PainReportModel(Base):
    __tablename__ = "pain_reports"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    patient_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("patients.id"), index=True, nullable=False)
    body_region: Mapped[str] = mapped_column(String(120), nullable=False)
    pain_type: Mapped[str] = mapped_column(String(120), nullable=False)
    severity: Mapped[int] = mapped_column(Integer, nullable=False)
    duration: Mapped[str] = mapped_column(String(120), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)


class ConversationMemoryModel(Base):
    __tablename__ = "conversation_memories"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    patient_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("patients.id"), index=True, nullable=False)
    doctor_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("users.id"), index=True, nullable=False)
    messages: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)


class AuditLogEntryModel(Base):
    __tablename__ = "audit_log_entries"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    actor_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("users.id"), index=True, nullable=False)
    action: Mapped[str] = mapped_column(String(255), nullable=False)
    target_id: Mapped[UUID | None] = mapped_column(Uuid, nullable=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow, nullable=False)
    prev_hash: Mapped[str | None] = mapped_column(String(128), nullable=True)
    hash: Mapped[str] = mapped_column(String(128), nullable=False)


class ConsentSettingModel(Base):
    __tablename__ = "consent_settings"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    patient_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("patients.id"), index=True, nullable=False)
    data_category: Mapped[str] = mapped_column(String(120), nullable=False)
    shared: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
