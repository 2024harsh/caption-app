const API_BASE = "https://caption-app-v6s8.onrender.com";

function checkAPI() {
  const statusEl = document.getElementById("apiStatus");
  statusEl.textContent = "Checking...";

  fetch(`${API_BASE}/health`)
    .then(res => {
      if (!res.ok) throw new Error("Server error");
      return res.json();
    })
    .then(data => {
      statusEl.textContent = "Status: " + data.status;
    })
    .catch(() => {
      statusEl.textContent = "Backend not reachable";
    });
}
