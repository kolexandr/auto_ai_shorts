import json
from pathlib import Path

TRANSCRIPT_PATH = Path("data/input/transcript.json")
CAPTIONS_DIR = Path("data/output/captions")

def seconds_to_ass_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02}:{s:05.2f}"

def generate_captions(highlight_index, start, end):
    CAPTIONS_DIR.mkdir(parents=True, exist_ok=True)
    output_file = CAPTIONS_DIR / f"captions_{highlight_index}.ass"

    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        transcript = json.load(f)

    words = []

    ANIM = r"{\an5\pos(304,740)\fs40\t(0,120,\fs64)}"  

    for seg in transcript["segments"]:
        for w in seg["words"]:
            if start <= w["start"] <= end:
                words.append(w)

    with open(output_file, "w", encoding="utf-8") as f:
        # ASS header (change resolution)
        f.write("""[Script Info]
[Script Info]
ScriptType: v4.00+
PlayResX: 607
PlayResY: 1080
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Default,Arial,48,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,0,2,10,10,30,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
""")

        for w in words:
            start_t = seconds_to_ass_time(w["start"] - start)
            end_t = seconds_to_ass_time(w["end"] - start)
            text = w["word"].upper()
            line = (
                f"Dialogue: 0,{start_t},{end_t},Default,,0,0,0,,{ANIM}{text}\n")
            f.write(line)

    return output_file
