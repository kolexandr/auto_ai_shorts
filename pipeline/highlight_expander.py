from pipeline.config import MIN_SHORT_LENGTH, MAX_SHORT_LENGTH

def expand_highlights(candidate, words):
  center = (candidate["start"] + candidate["end"] ) / 2
  start, end = center, center

  while end - start < MIN_SHORT_LENGTH:
    start -= 2
    end += 2

    if end - start >= MAX_SHORT_LENGTH:
      break


  print("Higlight expanded!")

  return {
    "start": max(start, 0),
    "end": end
  }