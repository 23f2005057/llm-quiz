# LLM Quiz Solver Agent 🚀

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

This repository contains an autonomous agent, built with LangChain, LangGraph, and FastAPI, designed to solve data science quiz challenges that require web scraping, analysis, and submission to a specified endpoint. The agent leverages Google Gemini (via `langchain-google-genai`) for reasoning, and Playwright for robust web automation and scraping.

---

## Features

- 🔗 **REST API** with `/solve` endpoint for quiz URLs  
- 🧠 **Gemini-powered reasoning** via LangChain + Google GenAI  
- 🕸️ **Playwright-based web scraping** (handles JS-heavy pages)  
- 📦 **Flexible file downloads** (PDF, CSV, images, etc.)  
- 🛠️ **Modular tools** for HTTP requests, code execution, dependency installs  
- 🔒 **Env-based secret management** for secure deployments  
- 🚦 **Robust error and retry handling**

---

## Architecture

```
                   ┌─────────────┐
   POST /solve ⇨   │   FastAPI   │
                   └──────┬──────┘
                          │
                   ┌──────▼────────┐
                   │  Agent (LLM)  │  <─ State machine, LangGraph
                   └─────┬┬┬┬──────┘
                         ││││
             ┌────────────┼┼┼─────────────┐
             ▼            ▼ ▼             ▼
         [Scraper]   [Downloader]   [Code Executor]
           (tools)       (tools)        (tools)
```

---

## Quick Start

### Prerequisites

- Python 3.12+
- [Node.js](https://nodejs.org/) (for Playwright dependencies)
- Chromium (install via `playwright install chromium`)

### Installation

1. **Clone repo:**
   ```bash
   git clone https://github.com/23f3002766/tds-geniesolver.git
   cd tds-geniesolver
   ```

2. **Python setup:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Environment variables:**  
   Create `.env` in your project root:
   ```env
   EMAIL=your.email@example.com
   SECRET=your_secret_value
   GOOGLE_API_KEY=your_google_api_key
   ```

---

### Usage

**Run API server:**
```bash
uvicorn main:app --host 0.0.0.0 --port 7860
```

**Solve a quiz via API:**
```bash
curl -X POST http://localhost:7860/solve \
  -H "Content-Type: application/json" \
  -d '{
    "email": "your.email@example.com",
    "secret": "your_secret_value",
    "url": "https://tds-llm-analysis.s-anand.net/demo"
  }'
```
A background process runs and logs completion on the CLI.

**Healthcheck:**
```bash
curl http://localhost:7860/healthz
```

---

## Project Structure

```
tds-geniesolver/
├── agent.py            # LangGraph agent orchestration
├── main.py             # FastAPI API server
├── tools/              # Modular action tools
│   ├── web_scraper.py
│   ├── download_file.py
│   ├── send_request.py
│   └── add_dependencies.py
├── requirements.txt    # Runtime dependencies
├── pyproject.toml      # Project metadata (optional)
├── .env                # Local secrets (not versioned)
└── README.md
```

---

## Configuration

- All sensitive credentials (EMAIL, SECRET, GOOGLE_API_KEY) are managed via environment variables or the `.env` file.
- API rate limits are respected via built-in agent throttling.

---

## Deployment

### Render

- Set up your repository as a Render web service.
- Set the Start Command:
  ```
  uvicorn main:app --host=0.0.0.0 --port=$PORT
  ```
- Add your secrets using the Environment tab (`EMAIL`, `SECRET`, `GOOGLE_API_KEY`).

### Docker (optional)

_If you wish to containerize your app:_

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install chromium
EXPOSE 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

---

## License

Licensed under the MIT License.

---

## Author

**Sumit**  
TDS Project – IIT Madras  
If you have questions, please open an issue on [GitHub](https://github.com/23f3002766/tds-geniesolver/issues).

---