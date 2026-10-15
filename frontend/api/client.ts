import type { AuthToken, LoginRequest, SignupRequest, User } from "@shared/index";

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000";

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const token = localStorage.getItem("medassist_token");
  const response = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...(init.headers ?? {}),
    },
  });
  if (!response.ok) {
    const body = await response.json().catch(() => ({ detail: response.statusText }));
    throw new Error(body.detail ?? `Request failed (${response.status})`);
  }
  return response.json() as Promise<T>;
}

export const api = {
  signup: (payload: SignupRequest) => request<AuthToken>("/api/auth/signup", { method: "POST", body: JSON.stringify(payload) }),
  login: (payload: LoginRequest) => request<AuthToken>("/api/auth/login", { method: "POST", body: JSON.stringify(payload) }),
  me: () => request<User>("/api/auth/me"),
};
