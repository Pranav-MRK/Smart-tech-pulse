import smtplib # it is for gmail   python special email liabrary 
import os
from email.mime.text import MIMEText # Python standard email library

from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(to_email,subject,content):
    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com",587) as server: # starttls() → secure connection
        server.starttls()
        server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        server.send_message(msg)