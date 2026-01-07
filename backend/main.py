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
    # TEMP: just confirm upload works
    if not audio.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Not an audio file")

    return {
        "filename": audio.filename,
        "content_type": audio.content_type
    }

