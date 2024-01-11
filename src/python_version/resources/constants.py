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


# Monitor Constants
LOG_PATH = "..\\..\\logs\\"

CPU_LOGGING = bool(config['Monitor CPU']["CPU_LOGGING"])
CPU_INTERVAL = int(config['Monitor CPU']["CPU_INTERVAL"])
CPU_SOFTWARN = int(config['Monitor CPU']["CPU_SOFTWARN"])
CPU_HARDWARN = int(config['Monitor CPU']["CPU_HARDWARN"])

RAM_LOGGING = bool(config['Monitor RAM']["RAM_LOGGING"])
RAM_INTERVAL = int(config['Monitor RAM']["RAM_INTERVAL"])
RAM_SOFTWARN = int(config['Monitor RAM']["RAM_SOFTWARN"])
RAM_HARDWARN = int(config['Monitor RAM']["RAM_HARDWARN"])

DISK_LOGGING = bool(config['Monitor Disk']["DISK_LOGGING"])
DISK_INTERVAL = int(config['Monitor Disk']["DISK_INTERVAL"])
DISK_SOFTWARN = int(config['Monitor Disk']["DISK_SOFTWARN"])
DISK_HARDWARN = int(config['Monitor Disk']["DISK_HARDWARN"])
DISK_PATH = str(config['Monitor Disk']["DISK_PATH"])

TEMP_LOGGING = bool(config['Monitor Temp']["TEMP_LOGGING"])
TEMP_INTERVAL = int(config['Monitor Temp']["TEMP_INTERVAL"])
TEMP_SOFTWARN = int(config['Monitor Temp']["TEMP_SOFTWARN"])
TEMP_HARDWARN = int(config['Monitor Temp']["TEMP_HARDWARN"])

LOGON_LOGGING = bool(config['Monitor Logon']["LOGON_LOGGING"])
LOGON_INTERVAL = int(config['Monitor Logon']["LOGON_INTERVAL"])
LOGON_SOFTWARN = int(config['Monitor Logon']["LOGON_INTERVAL"])
LOGON_HARDWARN = int(config['Monitor Logon']["LOGON_INTERVAL"])
