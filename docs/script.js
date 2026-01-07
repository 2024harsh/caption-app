// 🔁 CHANGE THIS WHEN DEPLOYED
const API_BASE = "https://caption-app-v6s8.onrender.com";
// AFTER DEPLOY (GitHub Pages):
// const API_BASE = "https://YOUR-RENDER-URL.onrender.com";

const audioInput = document.getElementById("audioInput");
const enhanceBtn = document.getElementById("enhanceBtn");
const statusl = document.getElementById("status");

const originalAudio = document.getElementById("originalAudio");
const enhancedAudio = document.getElementById("enhancedAudio");
const downloadLink = document.getElementById("downloadLink");

enhanceBtn.onclick = async () => {
  const file = audioInput.files[0];

  if (!file) {
    alert("Please select an audio file");
    return;
  }

  statusEl.textContent = "Uploading & processing...";
  downloadLink.style.display = "none";

  // play original audio
  originalAudio.src = URL.createObjectURL(file);

  const formData = new FormData();
  formData.append("audio", file);

  try {
    const res = await fetch(`${API_BASE}/enhance`, {
      method: "POST",
      body: formData
    });

    if (!res.ok) {
      throw new Error("Enhancement failed");
    }

    const blob = await res.blob();
    const url = URL.createObjectURL(blob);

    enhancedAudio.src = url;
    downloadLink.href = url;
    downloadLink.style.display = "inline-block";

    statusEl.textContent = "Enhancement complete ✅";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error enhancing audio ❌";
  }
};
