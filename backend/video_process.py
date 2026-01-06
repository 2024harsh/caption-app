from moviepy import VideoFileClip, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np

from speech_to_text import transcribe
from caption_logic import generate_captions
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)
def text_to_image(text, width):
    img = Image.new("RGBA", (width, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]

    x = (width - text_width) // 2
    y = 30

    draw.text((x, y), text, fill="white", font=font)
    return np.array(img)


def process_video(file, content_type):
    input_path = os.path.join(UPLOAD_DIR, file.filename)
    output_path = os.path.join(UPLOAD_DIR, f"output_{file.filename}")


    with open(input_path, "wb") as f:
        f.write(file.file.read())

    video = VideoFileClip(input_path)

    segments = transcribe(input_path)
    captions = generate_captions(segments, content_type)

    clips = [video]

    for cap in captions:
        img = text_to_image(cap["text"], video.w)

        subtitle = (
            ImageClip(img)
            .with_start(cap["start"])
            .with_duration(cap["end"] - cap["start"])
            .with_position(("center", video.h - 140))
        )

        clips.append(subtitle)


    final = CompositeVideoClip(clips)
    final.write_videofile(output_path, codec="libx264")

    return output_path
