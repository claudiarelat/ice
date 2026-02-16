// src/components/SummaryCard.jsx
import React from "react";

export default function SummaryCard({ title, value, color }) {
  return (
    <div className={`p-4 rounded-lg shadow-md`} style={{ backgroundColor: color }}>
      <h3 className="text-gray-200 font-semibold">{title}</h3>
      <p className="text-2xl font-bold text-white">{value}</p>
    </div>
  );
}
