import json
from pathlib import Path
from pipeline.config import CANDIDATE_LENGTH, CANDIDATE_OVERLAP

LOG_PATH = Path("data/output/candidate_finder.txt")

def find_candidates(transcripts):
  words = [(w["word"], w["start"], w["end"])
          for seg in transcripts["segments"]
          for w in seg["words"]]
  
  candidates = []
  log_lines = []

  step = CANDIDATE_LENGTH * (1 - CANDIDATE_OVERLAP)
  start_time = words[0][1]
  
  log_lines.append(f"Total words extracted: {len(words)}")
  log_lines.append(f"Candidate length: {CANDIDATE_LENGTH}s, Overlap: {CANDIDATE_OVERLAP}")
  log_lines.append(f"Step size: {step}s")
  log_lines.append("")
  log_lines.append("Processing candidates:")

  candidate_idx = 0
  while start_time < words[-1][2]:
    end_time = start_time + CANDIDATE_LENGTH
    chunk_words = [w for w in words if w[1] >= start_time and w[2] <= end_time]

    if len(chunk_words) >= 50:
      text = " ".join(w[0] for w in chunk_words)
      candidates.append({
        "start": chunk_words[0][1],
        "end": chunk_words[-1][2],
        "text": text
      })
      log_lines.append(f"Candidate {candidate_idx}: Time {start_time:.2f}-{end_time:.2f}s, Words: {len(chunk_words)}")
      candidate_idx += 1
    else:
      log_lines.append(f"Skipped chunk at {start_time:.2f}s: only {len(chunk_words)} words (need 100+)")

    start_time += step

  log_lines.append("")
  log_lines.append(f"Total candidates found: {len(candidates)}")
  
  # Write log to file
  LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
  with open(LOG_PATH, "w") as f:
    f.write("\n".join(log_lines))
  
  print(f"Candidates are found successfully! ({len(candidates)} candidates)")

  return candidates