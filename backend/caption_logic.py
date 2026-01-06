def generate_captions(segments, content_type):
    captions = []

    for seg in segments:
        text = seg["text"].strip()
        start = float(seg["start"])
        end = float(seg["end"])

        # skip very small noise
        if len(text) < 2:
            continue

        captions.append({
            "text": text,
            "start": start,
            "end": end
        })

    return captions
