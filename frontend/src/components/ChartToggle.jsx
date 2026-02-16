// src/components/ChartToggle.jsx
import React, { useState } from "react";

export default function ChartToggle({ onChange }) {
  const [type, setType] = useState("bar");

  const handleChange = (newType) => {
    setType(newType);
    onChange(newType);
  };

  return (
    <div className="flex gap-2 mt-4">
      <button
        className={`px-4 py-2 rounded ${type === "bar" ? "bg-blue-500 text-white" : "bg-gray-200"}`}
        onClick={() => handleChange("bar")}
      >
        Bar
      </button>
      <button
        className={`px-4 py-2 rounded ${type === "pie" ? "bg-blue-500 text-white" : "bg-gray-200"}`}
        onClick={() => handleChange("pie")}
      >
        Pie
      </button>
    </div>
  );
}
