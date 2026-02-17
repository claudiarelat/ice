import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import AuthPage from "./components/AuthPage"; // 🔹 el teu component combinat de Login+Register
import { AuthProvider } from "./context/AuthContext";

function ProtectedRoute({ children }) {
  const { user } = React.useContext(AuthProvider._context); // o AuthContext

  if (!user || !user.authenticated) {
    return <Navigate to="/" replace />;
  }

  return children;
}

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<AuthPage />} /> {/* Login+Register alhora */}
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route path="*" element={<Navigate to="/" replace />} /> {/* fallback */}
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;





