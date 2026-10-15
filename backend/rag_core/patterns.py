from __future__ import annotations

from abc import ABC, abstractmethod


class RetrievalStrategy(ABC):
    """Strategy pattern: allow retrieval implementations to be swapped independently."""

    @abstractmethod
    async def retrieve(self, query: str) -> list[dict]:
        raise NotImplementedError


class QueryReformulationStrategy(ABC):
    """Strategy pattern: corrective-retry query reformulation contract."""

    @abstractmethod
    async def reformulate(self, query: str, context: list[dict]) -> str:
        raise NotImplementedError


class SufficiencyJudge(ABC):
    @abstractmethod
    async def is_sufficient(self, query: str, context: list[dict]) -> bool:
        raise NotImplementedError
