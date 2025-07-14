# Remote Job Checker Agent

This is a Python-based agent that uses OpenAI, Playwright, and email to notify you about relevant remote job postings.

## Setup

1. Install dependencies:
=======
# 🧠 Remote Job Checker Agent (AI + Playwright + AWS)

Automatically checks multiple remote job boards and emails you matching job posts (e.g., DevOps, SRE, Cloud Engineer) using AI (GPT-4o), Playwright, and AWS Lambda.

---

## 🚀 Features

- ✅ Opens real job board URLs using **Playwright**
- 🧠 Extracts relevant job postings using **OpenAI GPT-4o**
- 📬 Sends daily email alerts with matches
- ☁️ Fully serverless deployment using **AWS Lambda**
- 🔄 Automated daily runs via **CloudWatch Events**
- 🔐 Secrets stored in **AWS Secrets Manager**
- 📦 CI/CD deployment via **GitHub Actions**

---

## 📦 Requirements

- Python 3.9+
- OpenAI API key
- Gmail account with **App Password**
- AWS CLI + IAM credentials
- Installed browsers via Playwright

---

## 🔧 Setup (Local)

### 1. Clone or Download the Project

```bash
git clone https://github.com/yourusername/remote-job-checker-agent.git
cd remote-job-checker-agent
```
—or download the ZIP and extract.

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
>>>>>>> 858f2a913b2095342bddea8be4a8046c3f1a171e

```bash
pip install -r requirements.txt
playwright install
```

<<<<<<< HEAD
2. Update `config.py` with:
- Job URLs
- Keywords
- Gmail sender + app password
- Receiver email

3. Run the main script:
=======
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
> Generate App Password from: https://myaccount.google.com/apppasswords

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

## ▶️ Run the Script Locally
>>>>>>> 858f2a913b2095342bddea8be4a8046c3f1a171e

```bash
python main.py
```

<<<<<<< HEAD
## How It Works

- Opens each job URL with Playwright
- Sends HTML to GPT-4o to extract matching jobs
- Emails you any relevant matches
=======
---

## ☁️ AWS Deployment

### 1. Package for Lambda

Use `zip` or GitHub Actions to bundle the code and dependencies.

### 2. Upload to S3

```bash
aws s3 cp remote-job-checker-agent.zip s3://your-bucket-name/
```

### 3. Deploy to Lambda

```bash
aws lambda update-function-code \
  --function-name jobCheckerAgent \
  --s3-bucket your-bucket-name \
  --s3-key remote-job-checker-agent.zip
```

### 4. Schedule Execution

- Use **CloudWatch Events** to run Lambda daily

### 5. Store Secrets Securely

- Use **AWS Secrets Manager** to store API keys and credentials

---

## 🔁 GitHub Actions CI/CD

- Runs on push to `main`
- Installs deps, zips code, uploads to S3
- Updates Lambda via AWS CLI

---

## 📬 Email Output

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

## 📌 Outcome

Enabled fully automated daily job search across 100+ remote boards with AI extraction and cloud-native infrastructure. Saved hours of manual effort.

---

## 🧑‍💻 Built By

Maharshi Pathak  
🔗 [LinkedIn](https://www.linkedin.com/in/mpathak7)

---

## 🛡️ License

MIT — use freely, modify, and share.
>>>>>>> 858f2a913b2095342bddea8be4a8046c3f1a171e
