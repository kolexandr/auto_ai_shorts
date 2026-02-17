from pathlib import Path
import subprocess

VIDEO_PATH = Path("data/input/video.mp4")
AUDIO_PATH = Path("data/input/audio.wav")

OUTPUT_FILE = Path("data/input/merged.mp4")

def merge_va(video_path: Path = VIDEO_PATH, audio_path: Path = AUDIO_PATH):
  OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

  cmd = [
    "ffmpeg",
    "-y",
    "-i", video_path.as_posix(),
    "-i", audio_path.as_posix(),
    "-c:v", "copy",
    "-c:a", "aac",
    OUTPUT_FILE.as_posix()
  ]

  subprocess.run(cmd, check=True)