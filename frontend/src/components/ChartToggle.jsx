import React, { useState } from "react";

export default function ChartToggle({ onChange }) {
  const [type, setType] = useState("bar");

  const handleChange = (newType) => {
    setType(newType);
    onChange(newType);
  };

  return (
    <>
      <button
        className={type === "bar" ? "active" : ""}
        onClick={() => handleChange("bar")}
      >
        Bar
      </button>
      <button
        className={type === "pie" ? "active" : ""}
        onClick={() => handleChange("pie")}
      >
        Pie
      </button>
    </>
  );
}

