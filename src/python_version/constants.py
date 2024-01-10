from colorama import Fore, Back, Style
import configparser

# Terminal Beautify
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET

# Unify Strings
WARNING = "WARNING"
INFO = "INFO"
CPU = "CPU"
RAM = "RAM"
DISK = "DISK"

# Email Constants
config = configparser.ConfigParser()
config.read("..\..\config.ini")
SENDER_EMAIL = str(config['SMTP']['EMAIL_SENDER'])
PASSWORD = str(config['SMTP']['EMAIL_PASSWORD'])
RECEIVER_EMAIL = str(config['SMTP']['EMAIL_RECEIVER'])
SMTP_SERVER = "smtp.mail.de"
