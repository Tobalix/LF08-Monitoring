import logging
import smtplib
import ssl
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# from src.log_examples.monitor import cpu_log, ram_log, disk_log


def send_mail():
    smtp_server = "smtp.mail.de"
    port = 25
    sender_email = "IT.Monitor@mail.de"
    receiver_email = "IT.Monitor@mail.de"
    password = "bagel-footman-prevent"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Monitoring Alarm"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = """\
    <html>
      <body>
        <p>Hello,<br>
           Your alarm has triggered for<br>
           <a href="https://theuselessweb.com/">ALARM</a> 
           please refer to this link to see the alert.
        </p>
      </body>
    </html>
    """
    part = MIMEText(html, "html")
    message.attach(part)

    context = ssl.create_default_context()

    server = None

    # Try to log in to the server and send email
    try:
        server = smtplib.SMTP(smtp_server, port, timeout=10)
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        logging.debug(f"Email sent: {message}")
        print("Email sent")
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        if server:
            server.quit()


def alarm():
    x = 0
    while (x == x):
        cpu_log = open('../../logs/2023-12-20_CPU.log', 'r')
        Lines = cpu_log.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))
        print(x)
        send_mail()
        time.sleep(60)


alarm()
