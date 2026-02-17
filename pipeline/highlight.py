import json
from pathlib import Path
from pipeline.llm import rank_candidate, save_llm_log
from pipeline.candidate_finder import find_candidates
from pipeline.highlight_expander import expand_highlights
from pipeline.config import MAX_HIGHLIGHTS

TRANSCRIPT_PATH = Path("data/input/transcript.json")
HIGHLIGHTS_PATH = Path("data/input/highlights.json")
DEBUG_LOG_PATH = Path("data/output/highlight_detection.txt")

def detect_highlights():
    debug_log = []
    
    transcript = json.load(open(TRANSCRIPT_PATH, "r", encoding="utf-8"))
    debug_log.append("Transcript loaded successfully")

    candidates = find_candidates(transcript)
    debug_log.append(f"Found {len(candidates)} candidates")
    
    if len(candidates) == 0:
        debug_log.append("ERROR: No candidates found! Check candidate_finder.txt for details.")

    ranked = []
    successful_ranks = 0
    failed_ranks = 0

    for idx, c in enumerate(candidates):
        result = rank_candidate(c, idx)
        if result:
            c["importance"] = result["importance"]
            c["reason"] = result["reason"]
            ranked.append(c)
            successful_ranks += 1
        else:
            failed_ranks += 1
    
    debug_log.append(f"Ranked candidates: {successful_ranks} successful, {failed_ranks} failed")
    
    if len(ranked) == 0:
        debug_log.append("ERROR: No candidates were successfully ranked!")
        debug_log.append("Check llm_ranking.txt for error details.")
    
    ranked.sort(key=lambda x: x["importance"], reverse=True)
    top = ranked[:MAX_HIGHLIGHTS]
    
    debug_log.append(f"Selected top {len(top)} highlights from {len(ranked)} ranked")

    words = [(w["word"], w["start"], w["end"])
             for seg in transcript["segments"]
             for w in seg["words"]]

    highlights = []
    for c in top:
        clip = expand_highlights(c, words)
        clip["importance"] = c["importance"]
        clip["reason"] = c["reason"]
        highlights.append(clip)

    json.dump(highlights, open(HIGHLIGHTS_PATH, "w"), indent=2)
    debug_log.append(f"Saved {len(highlights)} highlights to {HIGHLIGHTS_PATH}")
    
    # Save all logs
    save_llm_log()
    DEBUG_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DEBUG_LOG_PATH, "w") as f:
        f.write("\n".join(debug_log))
    
    print(f"Saved {len(highlights)} highlights.")
    print("Debug logs saved to data/output/")
