# Remote Job Checker Agent

This is a Python-based agent that uses OpenAI, Playwright, and email to notify you about relevant remote job postings.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

2. Update `config.py` with:
- Job URLs
- Keywords
- Gmail sender + app password
- Receiver email

3. Run the main script:

```bash
python main.py
```

## How It Works

- Opens each job URL with Playwright
- Sends HTML to GPT-4o to extract matching jobs
- Emails you any relevant matches