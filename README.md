# 🎬 Auto AI Shorts Generator (CLI Version)

A Python-based CLI tool that automatically generates short-form video scripts from YouTube links using a local LLM (Llama 3.1 8B).

This project demonstrates:
- AI integration with local LLMs
- Automation of content generation
- CLI tool development
- Practical AI application for creators

---

## 🚀 Features

- 🔗 Accepts a YouTube video link as input
- 🧠 Uses local LLM (Llama 3.1:8B via Ollama) for script generation
- ✂️ Generates short-form content ideas/scripts
- ⚡ Runs fully locally (no OpenAI API required)
- 💻 Lightweight CLI-based workflow

---

## 🛠 Tech Stack

- Python 3.x
- Llama 3.1:8B (local model)
- Ollama (for running LLM locally)
- YouTube transcript processing
- Prompt engineering

## External Dependencies

- FFmpeg (system-level)
- Ollama (local LLM runtime)
- Llama 3.1:8B model
- yt-dlp

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/auto-ai-shorts.git
cd auto_ai_shorts
```

### 2. Install dependecies

### 3. Run Llama 3.1 locally

```bash
olama pull llama3.1:8b
```

Make sure Ollama is running:

```bash
olama run llama3.1:8b
```

### 4. How to run

Run the script from terminal

```bash
python main.py [youtube_link]
```

## The tool will:

- Extract transcript
- Process content
- Generate short-form videos 9:16 output with related and animated captions


## 🎯 Project Goal

This project is part of a larger SaaS vision focused on helping creators generate short-form content automatically using AI.

## Author: Oleksandr Koniukh | Aspiring Software Developer | Building AI-powered tools
