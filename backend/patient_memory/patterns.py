from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from shared.python.schemas import ConversationMemory


class ConversationMemoryRepository(ABC):
    """Repository pattern: persistence contract independent from SQLAlchemy details."""

    @abstractmethod
    async def get(self, patient_id: UUID, doctor_id: UUID) -> ConversationMemory | None:
        raise NotImplementedError

    @abstractmethod
    async def save(self, memory: ConversationMemory) -> ConversationMemory:
        raise NotImplementedError


class PatientReferenceEventPublisher(ABC):
    """Publisher half of Observer flow consumed by dashboard observers."""

    @abstractmethod
    async def publish_reference_detected(self, patient_id: UUID, doctor_id: UUID) -> None:
        raise NotImplementedError


class PatientReferenceDetector(ABC):
    """Contract for detecting when general doctor chat appears to reference a patient."""

    @abstractmethod
    async def detect(self, message: str, candidate_patient_ids: list[UUID]) -> UUID | None:
        raise NotImplementedError
