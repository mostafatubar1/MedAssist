from __future__ import annotations

from abc import ABC, abstractmethod

from shared.python.schemas import PainReportCreate


class PainQueryAdapter(ABC):
    """Adapter pattern: normalize structured body-map input into a RAG query contract."""

    @abstractmethod
    def to_natural_language_query(self, report: PainReportCreate) -> str:
        raise NotImplementedError
