import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

print("Sending Email...")

message = Mail(
    from_email=os.environ.get("FROM_EMAIL"),
    to_emails=os.environ.get("TO_EMAILS"),
    subject="Regarding Email Notifications",
    html_content="<h1>Email Notification</h1><br/> <p>Status:<b>Sent</b></p>",
)
try:
    print(os.environ.get("SENDGRID_API_KEY"))
    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
