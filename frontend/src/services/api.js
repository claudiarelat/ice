const API_URL = "http://127.0.0.1:8000";

export async function fetchUserSummary(userId, month, year) {
  const url = new URL(`${API_URL}/users/${userId}/summary`);
  if (month) url.searchParams.append("month", month);
  if (year) url.searchParams.append("year", year);

  const res = await fetch(url);
  if (!res.ok) throw new Error("Failed to fetch summary");
  return res.json();
}

export async function fetchTransactions(userId) {
  const res = await fetch(`${API_URL}/transactions?user_id=${userId}`);
  if (!res.ok) throw new Error("Failed to fetch transactions");
  return res.json();
}
