from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from video_process import process_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_video(
    file: UploadFile = File(...),
    content_type: str = "story"
):
    output = process_video(file, content_type)
    return {"video": output}
