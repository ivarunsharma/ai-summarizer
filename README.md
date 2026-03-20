# AI Text Summarizer

A clean web app that summarizes any text or article URL using Claude AI.
Built with Python, Streamlit, and the Anthropic API.

## Features
- Paste text or summarize directly from a URL
- 4 summary styles: Brief, Bullet points, ELI5, Key takeaways
- Word / sentence / compression stats
- Download summary as .txt

## Project structure
```
ai-summarizer/
├── app.py              # Streamlit UI entry point
├── requirements.txt    # Python dependencies
├── .env                # API key — not committed
└── src/
    ├── summarizer.py   # Claude API logic
    ├── utils.py        # URL fetching and text stats
    └── test_api.py     # Quick API connection test
```

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-summarizer.git
cd ai-summarizer
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your-key-here
```

### 5. Run the app
```bash
streamlit run app.py
```

## Tech stack
- Python 3.13
- Streamlit
- Anthropic Claude Haiku
- newspaper3k