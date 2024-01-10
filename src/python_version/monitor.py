import psutil
import logging
import datetime
import time
import configparser
import wmi
import win32evtlog
from src.python_version.resources.constants import YELLOW, RESET



# Config file is loaded
# CONFIG_PATH = os.environ["Monitor"]+"\\config.ini"
config = configparser.ConfigParser()
config.read("..\..\config.ini")
# config.read(CONFIG_PATH)

# Values from the config.ini
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

LOG_PATH = "..\\..\\logs\\"


def cpu_logger(PATH):
    # CPU useage in percent
    cpu_use = psutil.cpu_percent()
    # Create/Open Log file
    cpu_handler = logging.FileHandler('%s%s_CPU.log' % (PATH, datetime.date.today()))
    cpu_log = logging.getLogger('cpu_log')
    cpu_log.setLevel(logging.DEBUG)
    cpu_log.addHandler(cpu_handler)
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
    # Write Log file
    if cpu_use >= CPU_HARDWARN:
        cpu_log.warning("WARNING %s CPU: %s" % (dt_string, cpu_use))
    elif cpu_use >= CPU_SOFTWARN:
        cpu_log.info("INFO %s CPU: %s" % (dt_string, cpu_use))
    else:
        cpu_log.debug("DEBUG %s CPU: %s" % (dt_string, cpu_use))
    # Close Log file
    cpu_log.removeHandler(hdlr=cpu_handler)
    cpu_handler.close()
    return


def ram_logger(PATH):
    # RAM useage in percent
    ram_use = psutil.virtual_memory().percent
    # Create/Open Log file
    ram_handler = logging.FileHandler('%s%s_RAM.log' % (PATH, datetime.date.today()))
    ram_log = logging.getLogger('ram_log')
    ram_log.setLevel(logging.DEBUG)
    ram_log.addHandler(ram_handler)
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
    # Wirte the Log Entry
    if ram_use >= RAM_HARDWARN:
        ram_log.warning("WARNING %s RAM: %s" % (dt_string, ram_use))
    elif ram_use >= RAM_SOFTWARN:
        ram_log.info("INFO %s RAM: %s" % (dt_string, ram_use))
    else:
        ram_log.debug("DEBUG %s RAM: %s" % (dt_string, ram_use))
    # Close the Log file

    ram_log.removeHandler(hdlr=ram_handler)
    ram_handler.close()



def disk_logger(PATH):
    # Free Diskspace in percent
    disk_free = 100 - psutil.disk_usage(DISK_PATH).percent
    # Create/Open Log file
    disk_handler = logging.FileHandler('%s%s_DISK.log' % (PATH, datetime.date.today()))
    disk_log = logging.getLogger('disk_log')
    disk_log.setLevel(logging.DEBUG)
    disk_log.addHandler(disk_handler)
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
    # Wirte the Log Entry
    if disk_free >= DISK_HARDWARN:
        disk_log.warning("WARNING %s DISK FREE: %s" % (dt_string, disk_free))
    elif disk_free >= DISK_SOFTWARN:
        disk_log.info("INFO %s DISK FREE: %s" % (dt_string, disk_free))
    else:
        disk_log.debug("DEBUG %s DISK FREE: %s" % (dt_string, disk_free))
    # close the Log file
    disk_log.removeHandler(hdlr=disk_handler)
    disk_handler.close()
    return


def temp_logger(PATH):
    # Temperature in Celsius
    temp_val = wmi.WMI(namespace="root\\wmi").MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature
    temp_val = (temp_val - 2732) / 10
    # Create/Open Log file
    temp_handler = logging.FileHandler('%s%s_TEMP.log' % (PATH, datetime.date.today()))
    temp_log = logging.getLogger('temp_log')
    temp_log.setLevel(logging.DEBUG)
    temp_log.addHandler(temp_handler)
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
    # Wirte the Log Entry
    if temp_val >= TEMP_HARDWARN:
        temp_log.warning("WARNING %s TEMP: %s" % (dt_string, temp_val))
    elif temp_val >= TEMP_SOFTWARN:
        temp_log.info("INFO %s TEMP: %s" % (dt_string, temp_val))
    else:
        temp_log.debug("DEBUG %s TEMP: %s" % (dt_string, temp_val))
    # close the Log file
    temp_log.removeHandler(hdlr=temp_handler)
    temp_handler.close()
    return


def logon_logger(PATH):
    # logon reader from the eventlog
    log_type = "Security"
    log_source = "Security"
    num_records = 1000
    handle = win32evtlog.OpenEventLog(None, log_source)
    try:
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total = win32evtlog.GetNumberOfEventLogRecords(handle)
        # Create/Open Log file
        logon_handler = logging.FileHandler('%s%s_LOGON.log' % (PATH, datetime.date.today()))
        logon_log = logging.getLogger('logon_log')
        logon_log.setLevel(logging.DEBUG)
        logon_log.addHandler(logon_handler)
        dt_string = datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S")

        if num_records > total:
            num_records = total
        for counter in range(num_records):
            event_tuple = win32evtlog.ReadEventLog(handle, flags, 0)
            for part in event_tuple:
                if part.EventID == (4624 or 4625 or 4634 or 4647 or 4648 or 4779) and (
                        part.TimeGenerated + datetime.timedelta(seconds=LOGON_INTERVAL)) > datetime.datetime.now():
                    print(
                        f"Record Number: %s" % part.RecordNumber + "\n""Event Type: %s" % part.EventType + "\n""Event Category: %s" % part.EventCategory + "\n""Time Generated: %s" % part.TimeGenerated + "\n""Event ID: %s" % part.EventID + "\n""Event Strings: %s" % part.Data + "\n" + "\n" + "-" * 50 + "\n" + "\n")
                    # Write Log file
                    if part.EventID == 4624:
                        logon_log.info("INFO %s LOGON: %s" % (dt_string, "Erfolgreicher Anmeldeversuch"))
                    elif part.EventID == 4625:
                        logon_log.warning("WARNING %s LOGON: %s" % (dt_string, "Fehlgeschlagener Anmeldeversuch"))

            # Close Log file
        logon_log.removeHandler(hdlr=logon_handler)
        logon_handler.close()
    finally:
        win32evtlog.CloseEventLog(handle)
    return

def start():
    print(YELLOW, "Monitoring program starts" + RESET)
    x = 0
    while x == x:
        # print(x)
        if (x % CPU_INTERVAL == 0) and CPU_LOGGING == True:
            cpu_logger(LOG_PATH)
            # print("CPU")
        if x % RAM_INTERVAL == 0 and RAM_LOGGING == True:
            ram_logger(LOG_PATH)
            # print("RAM")
        if x % DISK_INTERVAL == 0 and DISK_LOGGING == True:
            disk_logger(LOG_PATH)
            # print("DISK")

        time.sleep(0)
        # if x%TEMP_INTERVAL == 0 and TEMP_LOGGING == True:
        #     temp_logger(LOG_PATH)
        # print("TEMP")
        #  if x%LOGON_INTERVAL == 0 and LOGON_LOGGING == True:
        #      logon_logger(LOG_PATH)
        # print("TEMP")
        time.sleep(1)
       # print(datetime.timedelta(seconds=x))
        x = x + 1
