import json
import subprocess
from pathlib import Path
from pipeline.captions import generate_captions

MERGED_PATH = Path("data/input/merged.mp4")
HIGHLIGHTS_PATH = Path("data/input/highlights.json")
OUTPUT_DIR = Path("data/output")

def cropped():
  cmd = [
      "ffprobe",
      "-v", "error",
      "-select_streams", "v:0",
      "-show_entries", "stream=height",
      "-of", "default=noprint_wrappers=1:nokey=1",
      MERGED_PATH
  ]

  result = subprocess.run(cmd, capture_output=True, text=True, check=True)
  original_height = int(result.stdout.strip())

  print("Original video height:", original_height)

  return(original_height)

def cut_and_crop():
  OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

  cropped_height = cropped()
  cropped_width = int(cropped_height * 9 / 16)

  with open(HIGHLIGHTS_PATH, "r", encoding="utf-8") as f:
    highlights = json.load(f)

  for i, h in enumerate(highlights, start=1):
    output_file = OUTPUT_DIR / f"short_{i}.mp4"

    start = h["start"]
    end = h["end"]
    duration = end - start

    captions = generate_captions(i, start,end)

    captions = Path(f"data/output/captions/captions_{i}.ass")

    cmd = [
      "ffmpeg",
      "-y",
      "-ss", str(start),
      "-i", str(MERGED_PATH),
      "-t", str(duration),
      "-vf", f"crop={cropped_width}:{cropped_height},ass={captions.as_posix()}",
      "-c:a", "copy",
      str(output_file)
    ]

    print(" ".join(cmd))

    subprocess.run(cmd, check=True)

    print(f"Created {output_file.name}")