from __future__ import annotations

from abc import ABC, abstractmethod


class EncryptionProvider(ABC):
    """Provider interface for field/data encryption at rest; implementation belongs to Ziad."""

    @abstractmethod
    def encrypt(self, plaintext: bytes) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, ciphertext: bytes) -> bytes:
        raise NotImplementedError


class AuditHashProvider(ABC):
    """Hash-chain contract only; no chain construction or verification is implemented here."""

    @abstractmethod
    def hash_entry(self, canonical_entry: bytes, previous_hash: str | None) -> str:
        raise NotImplementedError


class RateLimitPolicy(ABC):
    """Rate-limit decision contract; storage/counters/algorithms are intentionally absent."""

    @abstractmethod
    async def allow(self, key: str) -> bool:
        raise NotImplementedError


class SecurityHandler(ABC):
    """Chain of Responsibility: compose RBAC/rate-limit/audit checks without coupling."""

    def __init__(self, next_handler: "SecurityHandler | None" = None):
        self.next_handler = next_handler

    @abstractmethod
    async def check(self, context: dict) -> None:
        if self.next_handler:
            await self.next_handler.check(context)
