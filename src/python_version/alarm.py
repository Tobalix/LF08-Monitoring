import datetime
import mimetypes
import os.path

import smtplib
import ssl
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from email.mime.base import MIMEBase
from email import encoders


# from src.log_examples.monitor import cpu_log, ram_log, disk_log


def send_mail(timenow, log_file_path):
    # Setup
    smtp_server = "smtp.mail.de"
    port = 25
    sender_email = "IT.Monitor@mail.de"
    receiver_email = "IT.Monitor@mail.de"
    password = "bagel-footman-prevent"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Monitoring Alarm"
    message["From"] = sender_email
    message["To"] = receiver_email

    with open(log_file_path, "r") as log_file:
        log_content = log_file.read()

    html = f"""\
    <html>
      <body>
        <p>Hello,<br>
           Your alarm has triggered at {timenow} for<br>
           <a href="https://theuselessweb.com/">ALARM</a> 
           <pre>{log_content}</pre>
        </p>
      </body>
    </html>
    """
    part = MIMEText(html, "html")
    message.attach(part)

    # Attachment of logs
    file_path = "../../logs/2023-12-20_CPU.log"  # Replace with the actual path to your file
    attachment = open(file_path, "rb")
    mime_type = "text/plain"
    part = MIMEBase(*mime_type.split("/"))
    part.set_payload((attachment).read())
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
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        if server:
            server.quit()


def alarm():
    x = 0
    while (x == x):
        log_file_path = "../../logs/2023-12-20_CPU.log"
        cpu_log = open(f'{log_file_path}', 'r')
        Lines = cpu_log.readlines()
        now = datetime.now()
        timenow = now.strftime("%Y-%m-%d, %H:%M:%S")

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))
        print(x)
        send_mail(timenow, log_file_path)
        time.sleep(60)


alarm()
