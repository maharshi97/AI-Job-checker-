# AI-Job-checker-


Here’s a professional `README.md` file for your **Remote Job Checker Agent** project, ready to drop into the root folder:

---

````markdown
# 🧠 Remote Job Checker Agent (AI + Playwright)

Automatically checks multiple remote job boards and emails you matching job posts (e.g., DevOps, SRE, Cloud Engineer) using AI (GPT-4o), Playwright, and Gmail SMTP.

---

## 🚀 Features

- ✅ Opens real job board URLs using **Playwright**
- 🧠 Extracts relevant job postings using **OpenAI GPT-4o**
- 📬 Sends daily email alerts with matches
- 💻 Easily configurable with your own keywords, boards, and email
- 🔄 Automate using **Task Scheduler** (Windows) or crontab

---

## 📦 Requirements

- Python 3.9+
- OpenAI API key
- Gmail account with **App Password**
- Installed browsers via Playwright

---

## 🔧 Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/remote-job-checker-agent.git
cd remote-job-checker-agent
````

—or download the ZIP and extract.

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

## 🔐 Configure `config.py`

Edit the following:

```python
job_urls = [
    "https://boards.greenhouse.io/outlier",
    ...
]

keywords = ["DevOps", "SRE", "Cloud", "AWS", "Azure"]

sender_email = "your.email@gmail.com"
receiver_email = "maharshipathak4@gmail.com"
app_password = "your_16_char_gmail_app_password"
```

> 📌 Your Gmail must have 2FA enabled.
> Generate App Password from: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

---

## 🔑 Configure OpenAI Key

Either:

```powershell
$env:OPENAI_API_KEY="sk-..."
```

Or add to `extractor.py`:

```python
os.environ["OPENAI_API_KEY"] = "sk-..."
```

---

## ▶️ Run the Script

```bash
python main.py
```

---

## 💡 Automate It (Optional)

### Windows Task Scheduler

* Create a Basic Task
* Trigger: Daily
* Action: Start a Program
* Program/script: `python`
* Add arguments: `C:\Path\To\remote-job-checker-agent\main.py`

---

## 📬 Output

When matches are found, you’ll get an email like:

```
✅ New Remote Job Matches Found

Cloud Infrastructure Engineer
https://example.com/job123

Site Reliability Engineer - Remote
https://example.com/job456
```

---

## 📁 Project Structure

```
remote-job-checker-agent/
│
├── main.py                # Main runner
├── config.py              # Your URLs, keywords, credentials
│
├── agents/
│   ├── navigator.py       # Playwright HTML grabber
│   └── extractor.py       # GPT-4o HTML analyzer
│
├── notifier/
│   └── emailer.py         # SMTP notification system
│
├── requirements.txt
└── README.md
```

---

## 🧱 Future Ideas

* Add Slack or Telegram alerts
* Save results in Google Sheets
* Dashboard with Flask/Streamlit
* Daily scheduler in Replit or PythonAnywhere

---

## 🧑‍💻 Built By

Maharshi Pathak
🔗 [LinkedIn](https://www.linkedin.com/in/mpathak7)

---

## 🛡️ License

MIT — use freely, modify, and share.

```

---

Let me know if you'd like:
- A version pushed to GitHub
- Slack or Telegram notification support
- A button to deploy on Replit or PythonAnywhere

Happy automating, Maharshi!
```
