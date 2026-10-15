import { Link } from "react-router-dom";

export default function Page() {
  return <main className="page"><div className="panel">
    <p><Link to="/">← Home</Link></p>
    <h1>Triage Dashboard</h1>
    <p>Placeholder for urgency-sorted live queue, actions, and basic analytics.</p>
    <p className="muted">Owner: Nour / feature/swe-lead</p>
  </div></main>;
}
