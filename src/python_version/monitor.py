import psutil
import logging
import datetime
import time
import wmi
import win32evtlog
from src.python_version.resources.constants import *


def cpu_logger(path):
    # CPU useage in percent
    cpu_use = psutil.cpu_percent()
    # Create/Open Log file
    cpu_handler = logging.FileHandler('%s%s_CPU.log' % (path, datetime.date.today()))
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


def ram_logger(path):
    # RAM useage in percent
    ram_use = psutil.virtual_memory().percent
    # Create/Open Log file
    ram_handler = logging.FileHandler('%s%s_RAM.log' % (path, datetime.date.today()))
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


def disk_logger(path):
    # Free Diskspace in percent
    disk_free = 100 - psutil.disk_usage(DISK_PATH).percent
    # Create/Open Log file
    disk_handler = logging.FileHandler('%s%s_DISK.log' % (path, datetime.date.today()))
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


def temp_logger(path):
    # Temperature in Celsius
    temp_val = wmi.WMI(namespace="root\\wmi").MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature
    temp_val = (temp_val - 2732) / 10
    # Create/Open Log file
    temp_handler = logging.FileHandler('%s%s_TEMP.log' % (path, datetime.date.today()))
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


def logon_logger(path):
    # logon reader from the eventlog
    log_type = "Security"
    log_source = "Security"
    num_records = 1000
    handle = win32evtlog.OpenEventLog(None, log_source)
    try:
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total = win32evtlog.GetNumberOfEventLogRecords(handle)
        # Create/Open Log file
        logon_handler = logging.FileHandler('%s%s_LOGON.log' % (path, datetime.date.today()))
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
        if (x % CPU_INTERVAL == 0) and CPU_LOGGING is True:
            cpu_logger(LOG_PATH)
            # print("CPU")
        if x % RAM_INTERVAL == 0 and RAM_LOGGING is True:
            ram_logger(LOG_PATH)
            # print("RAM")
        if x % DISK_INTERVAL == 0 and DISK_LOGGING is True:
            disk_logger(LOG_PATH)
            # print("DISK")
        # if x%TEMP_INTERVAL == 0 and TEMP_LOGGING == True:
        #     temp_logger(LOG_PATH)
        # print("TEMP")
        # if x % LOGON_INTERVAL == 0 and LOGON_LOGGING is True:
        #     logon_logger(LOG_PATH)
        #     print("LOGON")
        time.sleep(1)

        x = x + 1
