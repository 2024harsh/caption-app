async function upload() {
  const file = document.getElementById("video").files[0];
  const type = document.getElementById("type").value;

  if (!file) {
    alert("Upload a video first");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);
  formData.append("content_type", type);

  document.getElementById("status").innerText = "Processing...";

  const res = await fetch("http://127.0.0.1:8000/upload", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("status").innerText =
    "Done! Video saved at: " + data.video;
}
