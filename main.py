from config import job_urls, keywords, sender_email, receiver_email, app_password
from agents.navigator import fetch_job_board_html
from agents.extractor import extract_jobs_from_html
from notifier.emailer import send_email_notification

relevant_jobs = []

for url in job_urls:
    print(f"🔎 Checking: {url}")
    html = fetch_job_board_html(url)
    if not html:
        continue
    matches = extract_jobs_from_html(html, keywords, url)
    if matches:
        relevant_jobs.extend(matches)

if relevant_jobs:
    send_email_notification(relevant_jobs, sender_email, receiver_email, app_password)
else:
    print("❌ No matching jobs found.")