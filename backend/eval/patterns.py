from __future__ import annotations

from abc import ABC, abstractmethod


class EvaluationMetric(ABC):
    """Strategy pattern: plug in accuracy, faithfulness, latency, or other metrics."""

    name: str

    @abstractmethod
    def score(self, sample: dict) -> float:
        raise NotImplementedError
