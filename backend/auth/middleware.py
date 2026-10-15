from __future__ import annotations

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from backend.auth.security import decode_access_token


class JWTIdentityMiddleware(BaseHTTPMiddleware):
    """Decode an optional JWT into request.state.identity.

    Enforcement remains explicit at the router layer through `require_roles`,
    which makes access rules visible in generated OpenAPI and easy to test.
    """

    async def dispatch(self, request: Request, call_next):
        request.state.identity = None
        authorization = request.headers.get("Authorization", "")
        if authorization.startswith("Bearer "):
            token = authorization.removeprefix("Bearer ").strip()
            try:
                request.state.identity = decode_access_token(token)
            except Exception:  # identity enrichment only; dependencies enforce auth
                request.state.identity = None
        return await call_next(request)
