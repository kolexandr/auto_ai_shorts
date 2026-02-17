import subprocess
from pathlib import Path

VIDEO_PATH = Path("data/input/video.mp4")
AUDIO_PATH = Path("data/input/audio.wav")

def extract_audio():
  AUDIO_PATH.parent.mkdir(parents=True, exist_ok=True)

  command = [
    "ffmpeg",
    "-y",
    "-i", str(VIDEO_PATH),
    "-ac", "1",
    "-ar", "16000",
    str(AUDIO_PATH)
  ]

  subprocess.run(command, check=True)
  print("Audion successfully extracted")