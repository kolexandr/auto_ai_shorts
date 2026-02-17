import sys
from pipeline.download import download_video
from pipeline.audio import extract_audio
from pipeline.transcribe import transcribe_audio
from pipeline.highlight import detect_highlights
from pipeline.cutter import cut_and_crop
from pipeline.merging import merge_va
from pipeline.clearing import clear_input_folder


def main():
  if len(sys.argv) < 2:
    print("Please provide a YouTube URL")
    return
  
  url = sys.argv[1]

  download_video(url)
  extract_audio()
  transcribe_audio()
  detect_highlights()
  merge_va()
  cut_and_crop()
  # clear_input_folder()



if __name__ == "__main__":
  main()