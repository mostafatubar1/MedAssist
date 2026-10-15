import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import type { UserRole } from "@shared/index";
import { useAuth } from "./AuthContext";

export default function SignupPage() {
  const { signup } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState<UserRole>("patient");
  const [error, setError] = useState("");

  async function submit(event: FormEvent) {
    event.preventDefault(); setError("");
    try { await signup({ email, password, role }); navigate("/"); }
    catch (e) { setError(e instanceof Error ? e.message : "Signup failed"); }
  }
  return <main className="page"><div className="panel"><h1>Sign up</h1><form className="form" onSubmit={submit}>
    <input aria-label="Email" type="email" value={email} onChange={e => setEmail(e.target.value)} required />
    <input aria-label="Password" type="password" minLength={8} value={password} onChange={e => setPassword(e.target.value)} required />
    <select aria-label="Role" value={role} onChange={e => setRole(e.target.value as UserRole)}>
      <option value="patient">Patient</option><option value="doctor">Doctor</option>
    </select>
    <button type="submit">Create account</button>{error && <p className="error">{error}</p>}
  </form><p>Already registered? <Link to="/login">Login</Link></p></div></main>;
}
