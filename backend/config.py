import os

# ===== Upload limits =====
MAX_AUDIO_MB = 20  # hard limit to protect server
ALLOWED_TYPES = {
    "audio/wav",
    "audio/x-wav",
    "audio/mpeg",
    "audio/mp3"
}

# ===== Deepgram Speech Enhancement =====
SPEECH_API_URL = os.getenv("SPEECH_API_URL")
SPEECH_API_KEY = os.getenv("SPEECH_API_KEY")
