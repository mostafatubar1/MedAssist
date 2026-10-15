import { Link } from "react-router-dom";

export default function Page() {
  return <main className="page"><div className="panel">
    <p><Link to="/">← Home</Link></p>
    <h1>Patient Q&A</h1>
    <p>Placeholder chat surface. Agentic RAG implementation is intentionally absent.</p>
    <p className="muted">Owner: Mostafa / feature/rag-core</p>
  </div></main>;
}
