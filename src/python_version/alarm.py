import configparser
from colorama import Fore, Back, Style
import datetime
import os.path
import smtplib
import ssl
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from email.mime.base import MIMEBase
from email import encoders

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET
WARNING = "WARNING"
INFO = "INFO"

def send_mail(timenow, log_file_path, alarm_type):
    # Setup
    config = configparser.ConfigParser()
    config.read("..\..\config.ini")

    smtp_server = "smtp.mail.de"
    port = 25
    SENDER_EMAIL = str(config['SMTP']['EMAIL_SENDER'])
    PASSWORD = str(config['SMTP']['EMAIL_PASSWORD'])
    RECEIVER_EMAIL = str(config['SMTP']['EMAIL_RECEIVER'])

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
           Your alarm has triggered at {timenow} for {alarm_type} <br>
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


def alarm():
    x = 0
    time.sleep(10)

    now = datetime.now()
    date_today = now.strftime("%Y-%m-%d_")
    while x == x:
        cpu_log_file_path = f"../../logs/{date_today}CPU.log"
        cpu_log = open(f'{cpu_log_file_path}', 'r')
        cpu_lines = cpu_log.readlines()

        count = 0
        for line in cpu_lines:
            count += 1
            print("CPU L{}: {}".format(count, line.strip()))
        print("\n")

        disk_log_file_path = f"../../logs/{date_today}DISK.log"
        disk_log = open(f'{disk_log_file_path}', 'r')
        disk_lines = disk_log.readlines()
        count = 0
        for line in disk_lines:
            count += 1
            print("DISK L{}: {}".format(count, line.strip()))
        print("\n")

        ram_log_file_path = f"../../logs/{date_today}RAM.log"
        ram_log = open(f'{ram_log_file_path}', 'r')
        ram_lines = ram_log.readlines()
        count = 0
        for line in ram_lines:
            count += 1
            print("RAM L{}: {}".format(count, line.strip()))
        print("\n")

        time_now = now.strftime("%Y-%m-%d, %H:%M:%S")
        alarm_message = "MESSAGE: Alarm Email was sent for"
        info_message = "MESSAGE: Info Email was sent for"
        no_mail_message = "MESSAGE: No Email sent for"

# Send Alarm or not?
        alarm_type = "CPU"
        if cpu_lines[-1].split(" ")[0] == INFO:
            send_mail(time_now, cpu_log_file_path, alarm_type)
            print(YELLOW + info_message, alarm_type)
        elif cpu_lines[-1].split(" ")[0] == WARNING:
            send_mail(time_now, cpu_log_file_path, alarm_type)
            print(RED + alarm_message, alarm_type)
        else:
            print(GREEN + no_mail_message, alarm_type)

        alarm_type = "DISK"
        if disk_lines[-1].split(" ")[0] == INFO:
            send_mail(time_now, disk_log_file_path, alarm_type)
            print(YELLOW + alarm_message, alarm_type)
        elif disk_lines[-1].split(" ")[0] == WARNING:
            send_mail(time_now, disk_log_file_path, alarm_type)
            print(RED + alarm_message, alarm_type)
        else:
            print(GREEN + no_mail_message, alarm_type)

        alarm_type = "RAM"
        if ram_lines[-1].split(" ")[0] == INFO:
            send_mail(time_now, ram_log_file_path, alarm_type)
            print(YELLOW + alarm_message, alarm_type)
        elif ram_lines[-1].split(" ")[0] == WARNING:
            send_mail(time_now, ram_log_file_path, alarm_type)
            print(RED + alarm_message, alarm_type)
        else:
            print(GREEN + no_mail_message, alarm_type)
            time.sleep(5)
        print(RESET)


