from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
#210929b500533cfb23309dd1158d2d1cb52bd587
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

    return Response(
        content=response.content,
        media_type="audio/wav"
    )
