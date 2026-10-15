import type { PropsWithChildren } from "react";
import type { UserRole } from "@shared/index";
import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

export default function RoleRoute({ roles, children }: PropsWithChildren<{ roles: UserRole[] }>) {
  const { user, loading } = useAuth();
  if (loading) return <main className="page">Loading…</main>;
  if (!user) return <Navigate to="/login" replace />;
  if (!roles.includes(user.role)) return <Navigate to="/" replace />;
  return <>{children}</>;
}
