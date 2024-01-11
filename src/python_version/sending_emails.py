from src.python_version.resources.constants import *
import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(time_now, log_file_path, alarm_type):
    smtp_server = SMTP_SERVER
    port = 25

    message = MIMEMultipart("alternative")
    message["Subject"] = "Monitoring Alarm"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    with open(log_file_path, "r") as log_file:

        log_content = log_file.readlines()[-5:]
        send_content = "".join(log_content)

    html = f"""\
    <html>
      <body>
        <p>Hello,<br>
           Your alarm has triggered at {time_now} for {alarm_type} <br>
           Last Values of {alarm_type}:
           <pre>{send_content}</pre>
        </p>
      </body>
    </html>
    """
    part = MIMEText(html, "html")
    message.attach(part)

    # Attachment of logs
    file_path = f"{log_file_path}"  # Replace with the actual path to your file
    attachment = open(file_path, "rb")
    mime_type = "text/plain"
    part = MIMEBase(*mime_type.split("/"))
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    filename = os.path.basename(log_file_path)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    message.attach(part)

    context = ssl.create_default_context()

    server = None

    # Try to log in to the server and send email
    try:
        server = smtplib.SMTP(smtp_server, port, timeout=10)
        server.starttls(context=context)  # Secure the connection
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        if server:
            server.quit()


def send_mail_summary(cpu_log_file_path, disk_log_file_path, ram_log_file_path):
    # Setup
    smtp_server = SMTP_SERVER
    port = 25

    message = MIMEMultipart("alternative")
    message["Subject"] = "Monitoring Alarm"
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    with open(cpu_log_file_path, "r") as log_file:

        log_content = log_file.readlines()
    # send_content = "".join(log_content)

    html = f"""\
    <html>
      <body>
        <p>Hello,<br>
           Attached you can see your daily summary of logs
        </p>
      </body>
    </html>
    """
    part = MIMEText(html, "html")
    message.attach(part)

    file_path = f"{cpu_log_file_path}"
    attachment = open(file_path, "rb")
    mime_type = "text/plain"
    part = MIMEBase(*mime_type.split("/"))
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    filename = os.path.basename(cpu_log_file_path)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    message.attach(part)

    file_path = f"{disk_log_file_path}"
    attachment = open(file_path, "rb")
    mime_type = "text/plain"
    part = MIMEBase(*mime_type.split("/"))
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    filename = os.path.basename(disk_log_file_path)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    message.attach(part)

    file_path = f"{ram_log_file_path}"
    attachment = open(file_path, "rb")
    mime_type = "text/plain"
    part = MIMEBase(*mime_type.split("/"))
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    filename = os.path.basename(ram_log_file_path)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    message.attach(part)

    context = ssl.create_default_context()

    server = None

    # Try to log in to the server and send email
    try:
        server = smtplib.SMTP(smtp_server, port, timeout=10)
        server.starttls(context=context)  # Secure the connection
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        if server:
            server.quit()
