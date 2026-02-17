import React, { useState } from "react";
import Login from "./Login";
import Register from "./Register";
import "../scss/layout/authpage.scss";

export default function AuthPage() {
  const [isRegister, setIsRegister] = useState(false);

  return (
    <div className="auth-page">
      <div className="auth-card">
        {isRegister ? (
          <>
            <Register />
            <div className="create-account">
              <p>
                Ja tens compte?{" "}
                <a
                  href="#"
                  onClick={(e) => {
                    e.preventDefault();
                    setIsRegister(false);
                  }}
                >
                  Entra aquí 
                </a>
              </p>
            </div>
          </>
        ) : (
          <>
            <Login />
            <div className="forgot-password">
              <a href="#">Has oblidat la contrasenya?</a>
            </div>

            <div className="create-account">
              <button onClick={() => setIsRegister(true)}>
                Crear un compte
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}





