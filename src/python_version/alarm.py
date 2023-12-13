import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.mail.de"
port = 587  # For STARTTLS
sender_email = "IT.Monitor@mail.de"
receiver_email = "mike.jessen97@gmail.com"
password = "bagel-footman-prevent"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""
part = MIMEText(html, "html")
# Send email here
message.attach(part)

# Create a secure SSL context
context = ssl.create_default_context()

# Initialize server to None
server = None

# Try to log in to the server and send email
try:
    server = smtplib.SMTP(smtp_server, port, timeout=10)  # Increase the timeout value
    server.starttls(context=context)  # Secure the connection
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message.as_string())
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    if server:
        server.quit()
