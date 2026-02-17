import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import "../scss/main.scss"; // o login.scss si vols estil separat

export default function Login() {
  const navigate = useNavigate();
  const { login } = useContext(AuthContext);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await fetch("http://localhost:3000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      });

      const data = await response.json();

      if (response.ok) {
        login(data.token);
        navigate("/"); // ✅ redirecció al Dashboard protegit
      } else {
        alert("Credencials incorrectes");
      }
    } catch (error) {
      console.error("Error en el login:", error);
      alert("Hi ha hagut un error. Torna-ho a provar.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login">
      <h1>Login</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Entrant..." : "Entrar"}
        </button>
      </form>
    </div>
  );
}
