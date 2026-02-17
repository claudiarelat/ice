import React, { useState, useContext } from "react";
import ChartToggle from "./ChartToggle";
import "../scss/main.scss";
import { AuthContext } from "../context/AuthContext";

export default function Dashboard() {
  const { logout } = useContext(AuthContext);
  const [chartType, setChartType] = useState("bar");

  // Funció per formatar els valors en euros
  const formatEuro = (amount) => `€${amount}`;

  const summaryData = [
    { title: "Frozen", value: 200, colorClass: "frozen" },
    { title: "Saved", value: 200, colorClass: "saved" },
    { title: "Balance", value: 470, colorClass: "balance" },
    { title: "Expenses", value: 530, colorClass: "expenses" },
    { title: "Income", value: 1200, colorClass: "income" },
  ];

  return (
    <div className="dashboard">
      {/* Header amb logout */}
      <div className="dashboard-header">
        <h1>Dashboard</h1>
        <button onClick={logout} className="logout-btn">
          Logout
        </button>
      </div>

      {/* Summary */}
      <h1>Summary</h1>
      <p className="summary-date">February 2026</p>

      <div className="cards">
        {summaryData.map((item) => (
          <div key={item.title} className={`card ${item.colorClass}`}>
            <h3>{item.title}</h3>
            <p>{formatEuro(item.value)}</p>
          </div>
        ))}
      </div>

      {/* Chart Toggle */}
      <div className="chart-toggle">
        <ChartToggle onChange={setChartType} />
      </div>

      {/* Placeholder del Chart */}
      <div className="chart-placeholder">
        <p>Chart Type: {chartType.toUpperCase()}</p>
        <p>(Aquí anirà el Bar / Pie chart més endavant)</p>
      </div>
    </div>
  );
}


