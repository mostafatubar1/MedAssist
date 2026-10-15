import { createContext, useContext, useEffect, useMemo, useState } from "react";
import type { PropsWithChildren } from "react";
import type { LoginRequest, SignupRequest, User } from "@shared/index";
import { api } from "../api/client";

type AuthContextValue = {
  user: User | null;
  loading: boolean;
  login: (payload: LoginRequest) => Promise<void>;
  signup: (payload: SignupRequest) => Promise<void>;
  logout: () => void;
};

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function AuthProvider({ children }: PropsWithChildren) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("medassist_token");
    if (!token) { setLoading(false); return; }
    api.me().then(setUser).catch(() => localStorage.removeItem("medassist_token")).finally(() => setLoading(false));
  }, []);

  const value = useMemo<AuthContextValue>(() => ({
    user,
    loading,
    login: async (payload) => {
      const result = await api.login(payload);
      localStorage.setItem("medassist_token", result.access_token);
      setUser(result.user);
    },
    signup: async (payload) => {
      const result = await api.signup(payload);
      localStorage.setItem("medassist_token", result.access_token);
      setUser(result.user);
    },
    logout: () => { localStorage.removeItem("medassist_token"); setUser(null); },
  }), [user, loading]);

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used inside AuthProvider");
  return context;
}
