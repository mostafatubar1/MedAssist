import { Link, Navigate, Route, Routes } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";
import LoginPage from "../auth/LoginPage";
import SignupPage from "../auth/SignupPage";
import RoleRoute from "../auth/RoleRoute";
import RagCorePage from "../rag_core/RagCorePage";
import BodyMapPage from "../body_map/BodyMapPage";
import PatientMemoryPage from "../patient_memory/PatientMemoryPage";
import SecurityConsentPage from "../security/SecurityConsentPage";
import DashboardPage from "../dashboard/DashboardPage";

function Home() {
  const { user, logout } = useAuth();
  return <main className="page">
    <h1>MedAssist</h1>
    <p>Software Engineering course scaffold — feature logic intentionally lives on team branches.</p>
    {!user ? <p><Link to="/login">Login</Link> · <Link to="/signup">Sign up</Link></p> : <>
      <p>Signed in as <strong>{user.email}</strong> ({user.role}) <button onClick={logout}>Logout</button></p>
      <nav className="cards">
        {user.role === "patient" && <><Link to="/patient/chat">Q&A</Link><Link to="/patient/body-map">Body map</Link><Link to="/patient/consent">Consent & Trust Center</Link></>}
        {user.role === "doctor" && <><Link to="/doctor/chat">Doctor chat</Link><Link to="/doctor/dashboard">Triage dashboard</Link></>}
        {user.role === "admin" && <><Link to="/admin/security">Security console</Link><Link to="/admin/dashboard">Dashboard</Link></>}
      </nav>
    </>}
  </main>;
}

export default function App() {
  return <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/login" element={<LoginPage />} />
    <Route path="/signup" element={<SignupPage />} />
    <Route path="/patient/chat" element={<RoleRoute roles={["patient"]}><RagCorePage /></RoleRoute>} />
    <Route path="/patient/body-map" element={<RoleRoute roles={["patient"]}><BodyMapPage /></RoleRoute>} />
    <Route path="/patient/consent" element={<RoleRoute roles={["patient"]}><SecurityConsentPage /></RoleRoute>} />
    <Route path="/doctor/chat" element={<RoleRoute roles={["doctor"]}><PatientMemoryPage /></RoleRoute>} />
    <Route path="/doctor/dashboard" element={<RoleRoute roles={["doctor"]}><DashboardPage /></RoleRoute>} />
    <Route path="/admin/security" element={<RoleRoute roles={["admin"]}><SecurityConsentPage /></RoleRoute>} />
    <Route path="/admin/dashboard" element={<RoleRoute roles={["admin"]}><DashboardPage /></RoleRoute>} />
    <Route path="*" element={<Navigate to="/" replace />} />
  </Routes>;
}
