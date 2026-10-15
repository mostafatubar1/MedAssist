import { Link } from "react-router-dom";

export default function Page() {
  return <main className="page"><div className="panel">
    <p><Link to="/">← Home</Link></p>
    <h1>Consent & Trust Center</h1>
    <p>Placeholder for sharing toggles and patient-visible access history.</p>
    <p className="muted">Owner: Ziad / feature/security-consent</p>
  </div></main>;
}
