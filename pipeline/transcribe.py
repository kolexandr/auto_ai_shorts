import whisper
from pathlib import Path
import json

AUDIO_PATH = Path("data/input/audio.wav")
TRANSCRIPT_PATH = Path("data/input/transcript.json")

def transcribe_audio():
  TRANSCRIPT_PATH.parent.mkdir(parents=True, exist_ok=True)

  model = whisper.load_model("base")

  result = model.transcribe(
    str(AUDIO_PATH),
    word_timestamps=True
  )

  with open(TRANSCRIPT_PATH, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

  print("Transcription is done. Saved to", TRANSCRIPT_PATH.resolve())