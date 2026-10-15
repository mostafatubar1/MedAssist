import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

export default function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function submit(event: FormEvent) {
    event.preventDefault(); setError("");
    try { await login({ email, password }); navigate("/"); }
    catch (e) { setError(e instanceof Error ? e.message : "Login failed"); }
  }
  return <main className="page"><div className="panel"><h1>Login</h1><form className="form" onSubmit={submit}>
    <input aria-label="Email" type="email" value={email} onChange={e => setEmail(e.target.value)} required />
    <input aria-label="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} required />
    <button type="submit">Login</button>{error && <p className="error">{error}</p>}
  </form><p>New here? <Link to="/signup">Create an account</Link></p></div></main>;
}
