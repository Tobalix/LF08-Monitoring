import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a MIME object for the email
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Login to the SMTP server (if authentication is required)
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, to_email, message.as_string())

# Example usage
subject = "Test Email"
body = "Hello, this is a test email sent from Python!"
to_email = "recipient@example.com"
smtp_server = "your_smtp_server.com"
smtp_port = 587  # Port number may vary, use the correct one for your SMTP server
smtp_username = "your_email@example.com"
smtp_password = "your_email_password"

send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
