// src/components/Dashboard.jsx
import React, { useState } from "react";
import SummaryCard from "./SummaryCard";
import ChartToggle from "./ChartToggle";

export default function Dashboard() {
  const [chartType, setChartType] = useState("bar");

  const summaryData = [
    { title: "Frozen", value: "$200", color: "#6B7280" },
    { title: "Saved", value: "$200", color: "#10B981" },
    { title: "Balance", value: "$470", color: "#3B82F6" },
    { title: "Expenses", value: "$530", color: "#EF4444" },
    { title: "Income", value: "$1200", color: "#F59E0B" },
  ];

  return (
    <div className="p-6 bg-gray-900 min-h-screen text-white">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      {/* Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-4 mb-6">
        {summaryData.map((item) => (
          <SummaryCard key={item.title} {...item} />
        ))}
      </div>

      {/* Chart Toggle */}
      <ChartToggle onChange={setChartType} />

      {/* Placeholder del Chart */}
      <div className="mt-6 p-4 rounded-lg bg-gray-800 text-center">
        <p>Chart Type: {chartType.toUpperCase()}</p>
        <p>(Aquí anirà el Bar / Pie chart més endavant)</p>
      </div>
    </div>
  );
}
