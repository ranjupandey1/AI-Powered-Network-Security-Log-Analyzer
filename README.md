# AI-Powered Cyber Security Threat Analyzer

A lightweight Python application that processes local server threat logs using **NumPy** and utilizes **Google Gemini 2.5 Flash** to generate instant, actionable SecOps threat intelligence briefs.

## 🌟 Features
* **Matrix Data Processing**: Efficiently aggregates multi-node server attack data across time intervals using NumPy.
* **Automated Aggregation**: Calculates historical peaks and node vulnerabilities locally before transmitting data.
* **AI SecOps Synthesis**: Leverages the Gemini 2.5 Flash model to convert raw numeric matrices into human-readable executive security reports.

## 🛠️ Tech Stack
* **Language**: Python 3.10+
* **AI Engine**: [Google Gen AI SDK](https://github.com) (Model: `gemini-2.5-flash`)
* **Mathematical Operations**: NumPy

## 🚀 Getting Started

### Prerequisites
You need a Gemini API Key to use the AI reporting feature. You can generate a key from [Google AI Studio](https://google.dev).

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com
   cd YOUR-REPO-NAME
   ```

2. Install the necessary Python packages:
   ```bash
   pip install google-genai numpy
   ```

### Configuration
Set your Gemini API key as an environment variable before running the script:

* **Linux/macOS**:
  ```bash
  export GEMINI_API_KEY="your_api_key_here"
  ```
* **Windows (Command Prompt)**:
  ```cmd
  set GEMINI_API_KEY="your_api_key_here"
  ```
* **Windows (PowerShell)**:
  ```powershell
  \$env:GEMINI_API_KEY="your_api_key_here"
  ```

## 💻 Usage
Execute the analyzer script from your terminal:
```bash
python threat_analyzer.py
```

### Script Workflow
1. **Local Crunching**: The script computes node sums, daily averages, and pinpointed spike days locally via NumPy.
2. **AI Briefing**: It compiles a target prompt and pushes the minimal mathematical metrics to the AI cloud.
3. **SecOps Output**: The console prints a sharp, 3-sentence executive summary detailing system weaknesses.
