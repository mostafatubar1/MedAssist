import { Link } from "react-router-dom";

export default function Page() {
  return <main className="page"><div className="panel">
    <p><Link to="/">← Home</Link></p>
    <h1>Interactive Body Map</h1>
    <p>Placeholder for SVG body regions, severity coding, and structured pain input.</p>
    <p className="muted">Owner: Adham / feature/body-map</p>
  </div></main>;
}
