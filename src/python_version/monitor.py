import math
import psutil
import logging
import datetime
import time

CPU_INTERVALL = 1  #Interval der Prüfung in Sekuden
RAM_INTERVALL = 5
DISK_INTERVALL = 10

LOG_PATH = "C:\\Users\\tobal\\"
DISK_PATH = "C:"


def cpu_log(PATH, HARDWARN):
    CPU_USE =  psutil.cpu_percent()

    CPU_handler = logging.FileHandler('%s%s_CPU.log' %(PATH,datetime.date.today()))
    CPU_LOG = logging.getLogger('cpu_logger')
    CPU_LOG.setLevel(logging.INFO)
    CPU_LOG.addHandler(CPU_handler)

    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if CPU_USE >= HARDWARN:
        CPU_LOG.warning("%s CPU: %s" % (dt_string, CPU_USE))
    else:
        CPU_LOG.info("%s CPU: %s" % (dt_string, CPU_USE))
    CPU_LOG.removeHandler(hdlr=CPU_handler)
    CPU_handler.close()
    return


def ram_log(PATH, HARDWARN):
    RAM_USE = psutil.virtual_memory().percent
    RAM_handler = logging.FileHandler('%s%s_RAM.log' %(PATH,datetime.date.today()))
    RAM_LOG = logging.getLogger('ram_logger')
    RAM_LOG.setLevel(logging.INFO)
    RAM_LOG.addHandler(RAM_handler)

    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if RAM_USE >= HARDWARN:
        RAM_LOG.warning("%s RAM: %s" % (dt_string, RAM_USE))
    else:
        RAM_LOG.info("%s RAM: %s" % (dt_string, RAM_USE))
    
    RAM_LOG.removeHandler(hdlr=RAM_handler)
    RAM_handler.close()
    return

def disk_log(PATH, HARDWARN):
    DISK_FREE = psutil.disk_usage(DISK_PATH).percent
    #DISK_LOG = setup_logger('ram_logger', '%s%s_DISK.log' %(PATH,datetime.date.today()))

    DISK_handler = logging.FileHandler('%s%s_DISK.log' %(PATH,datetime.date.today()))
    DISK_LOG = logging.getLogger('disk_logger')
    DISK_LOG.setLevel(logging.INFO)
    DISK_LOG.addHandler(DISK_handler)

    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if DISK_FREE >= HARDWARN:
        DISK_LOG.warning("%s DISK FREE: %s" % (dt_string, DISK_FREE))
    else:
        DISK_LOG.info("%s DISK FREE: %s" % (dt_string, DISK_FREE))
    #print("disk")
    DISK_LOG.removeHandler(hdlr=DISK_handler)
    return
x = 0

# 
while (x < 100):
    print(x)
    if x%CPU_INTERVALL == 0:
        cpu_log(LOG_PATH, 80)
        print("CPU")
    if x%RAM_INTERVALL == 0:
        ram_log(LOG_PATH, 80)
        print("RAM")
    if x%DISK_INTERVALL == 0:
        disk_log(LOG_PATH, 80)
        print("DISK")
    time.sleep(1)
    x = x + 1

