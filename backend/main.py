from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import io
import requests

from backend.config import SPEECH_API_KEY, SPEECH_API_URL
from backend.audio_utils import validate_audio


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/enhance")
def enhance_audio(audio: UploadFile = File(...)):
    validate_audio(audio)

    headers = {
        "Authorization": f"Token {SPEECH_API_KEY}",
        "Content-Type": audio.content_type,
    }

    response = requests.post(
        SPEECH_API_URL,
        headers=headers,
        data=audio.file.read(),
        timeout=90
    )

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Enhancement failed")

    return StreamingResponse(
        io.BytesIO(response.content),
        media_type="audio/wav"
    )
