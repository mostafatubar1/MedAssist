import { Link } from "react-router-dom";

export default function Page() {
  return <main className="page"><div className="panel">
    <p><Link to="/">← Home</Link></p>
    <h1>Doctor Patient Threads</h1>
    <p>Placeholder for per-patient memory, reference detection, and thread switching.</p>
    <p className="muted">Owner: Omar / feature/patient-memory</p>
  </div></main>;
}
