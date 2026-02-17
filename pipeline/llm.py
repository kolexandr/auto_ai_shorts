import requests
import json
from pathlib import Path
from pipeline.config import MIN_IMPORTANCE_SCORE

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"
LOG_PATH = Path("data/output/llm_ranking.txt")

log_lines = []  # Global log buffer

def extract_json(text): #only for local LLM
    start = text.find("{")
    end = text.rfind("}") + 1
    return json.loads(text[start:end])

def rank_candidate(candidate, candidate_idx=0):
    global log_lines
    
    prompt = f"""
You are an expert video editor creating short-form content for social media.

You are selecting highlights from a long video.

Transcript:
---
{candidate["text"]}
---

Score this moment from 0 to 10 for:
- insight
- emotion
- novelty
- quote-worthiness

Then compute:
importance = average of the four scores

Return ONLY JSON:
{{
  "importance": 0,
  "reason": ""
}}
"""

    payload = {
      "model": MODEL,
      "prompt": prompt,
      "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()

        content = response.json()["response"].strip()
        result = extract_json(content)
        
        log_lines.append(f"Candidate {candidate_idx}: Time {candidate['start']:.2f}-{candidate['end']:.2f}s")
        log_lines.append(f"  Text preview: {candidate['text'][:80]}...")
        log_lines.append(f"  Importance score: {result['importance']}")
        log_lines.append(f"  Reason: {result['reason']}")
        log_lines.append("")
        
        return result
    except Exception as e:
        log_lines.append(f"Candidate {candidate_idx}: ERROR - {str(e)}")
        log_lines.append("")
        return None

def save_llm_log():
    """Save the accumulated log to file"""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "w") as f:
        f.write("\n".join(log_lines))
