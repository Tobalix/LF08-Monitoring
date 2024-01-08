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


def send_mail(timenow, log_file_path, alarm_type):
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
        log_content = log_file.readlines()[-1]

    html = f"""\
    <html>
      <body>
        <p>Hello,<br>
           Your alarm has triggered at {timenow} for {alarm_type} <br>
           Last Value of {alarm_type}
           <pre>{log_content}</pre>
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
    alarm_type = "CPU"
    now = datetime.now()
    date_today = now.strftime("%Y-%m-%d_")
    while x == x:
        cpu_log_file_path = f"../../logs/{date_today}CPU.log"
        cpu_log = open(f'{cpu_log_file_path}', 'r')
        cpu_lines = cpu_log.readlines()

        count = 0
        for line in cpu_lines:
            count += 1
            print("L{}: {}".format(count, line.strip()))

        disk_log_file_path = f"../../logs/{date_today}DISK.log"
        disk_log = open(f'{disk_log_file_path}', 'r')
        disk_lines = disk_log.readlines()
        count = 0
        for line in disk_lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))

        ram_log_file_path = f"../../logs/{date_today}RAM.log"
        ram_log = open(f'{ram_log_file_path}', 'r')
        ram_lines = ram_log.readlines()
        count = 0
        for line in ram_lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))

        time_now = now.strftime("%Y-%m-%d, %H:%M:%S")

        if cpu_lines[-1].split(" ")[0] == "WARNING":
            alarm_type = "CPU"
            send_mail(time_now, cpu_log_file_path, alarm_type)
            time.sleep(500)
        if disk_lines[-1].split(" ")[0] == "WARNING":
            alarm_type = "DISK"
            send_mail(time_now, disk_log_file_path, alarm_type)
            time.sleep(500)
        if ram_lines[-1].split(" ")[0] == "WARNING":
            alarm_type = "RAM"
            send_mail(time_now, ram_log_file_path, alarm_type)
            time.sleep(500)
        else:
            print("no email sent")
            time.sleep(5)

        print(x)
        # send_mail(time_now, cpu_log_file_path, alarm_type)


alarm()
