import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_notification(matches, sender, receiver, password):
    message = MIMEMultipart("alternative")
    message["Subject"] = "✅ New Remote Job Matches Found"
    message["From"] = sender
    message["To"] = receiver

    body = "Here are new jobs found:\n\n"
    for job in matches:
        body += f"{job['title']}\n{job['link']}\n\n"

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")