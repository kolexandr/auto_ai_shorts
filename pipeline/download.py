import subprocess
from pathlib import Path
import sys

VIDEO_PATH = Path("data/input/video.mp4")

def download_video(url: str):
  VIDEO_PATH.parent.mkdir(parents=True, exist_ok=True)

  command = [
    sys.executable, 
    "-m",
    "yt_dlp",
    "-f", "bv*+ba/b",
    "--merge-output-format", "mp4",
    "-o", str(VIDEO_PATH),
    url
  ]

  subprocess.run(command, check=True)
  print("Video successfully downloaded to", VIDEO_PATH.resolve())