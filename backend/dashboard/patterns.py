from __future__ import annotations

from abc import ABC, abstractmethod


class DashboardObserver(ABC):
    """Observer pattern: dashboard reacts to case/reference/escalation events."""

    @abstractmethod
    async def update(self, event_name: str, payload: dict) -> None:
        raise NotImplementedError


class TriageOrderingStrategy(ABC):
    """Strategy contract for queue ordering; urgency logic is intentionally not implemented."""

    @abstractmethod
    def order(self, cases: list[dict]) -> list[dict]:
        raise NotImplementedError
