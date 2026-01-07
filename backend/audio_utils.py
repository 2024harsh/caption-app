from fastapi import HTTPException
from backend.config import MAX_AUDIO_MB, ALLOWED_TYPES



def validate_audio(file):
    # ---- type check ----
    if not file.content_type or not file.content_type.startswith("audio/"):
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported audio format: {file.content_type}"
        )


    # ---- size check ----
    file.file.seek(0, 2)  # move pointer to end
    size_mb = file.file.tell() / (1024 * 1024)
    file.file.seek(0)

    if size_mb > MAX_AUDIO_MB:
        raise HTTPException(
            status_code=400,
            detail=f"Audio exceeds {MAX_AUDIO_MB} MB limit"
        )
