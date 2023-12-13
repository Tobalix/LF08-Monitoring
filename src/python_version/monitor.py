import math
import psutil
import logging
import datetime
import time

CPU_LOGGING = False
CPU_INTERVAL = 1
CPU_SOFTWARN = 50
CPU_HARDWARN = 80

RAM_LOGGING = True
RAM_INTERVAL = 1
RAM_SOFTWARN = 50
RAM_HARDWARN = 80

DISK_LOGGING = True
DISK_INTERVAL = 10
DISK_SOFTWARN = 50
DISK_HARDWARN = 80
DISK_PATH = "C:"



LOG_PATH = "C:\\Users\\tobal\\"


def cpu_logger(PATH, HARDWARN):
    cpu_use =  psutil.cpu_percent()

    cpu_handler = logging.FileHandler('%s%s_CPU.log' %(PATH,datetime.date.today()))
    cpu_log = logging.getLogger('cpu_log')
    cpu_log.setLevel(logging.INFO)
    cpu_log.addHandler(cpu_handler)

    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if cpu_use >= HARDWARN:
        cpu_log.warning("%s CPU: %s" % (dt_string, cpu_use))
    else:
        cpu_log.info("%s CPU: %s" % (dt_string, cpu_use))
    cpu_log.removeHandler(hdlr=cpu_handler)
    cpu_handler.close()
    return


def ram_logger(PATH, HARDWARN):
    ram_use = psutil.virtual_memory().percent
    ram_handler = logging.FileHandler('%s%s_RAM.log' %(PATH,datetime.date.today()))
    ram_log = logging.getLogger('ram_log')
    ram_log.setLevel(logging.INFO)
    ram_log.addHandler(ram_handler)

    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if ram_use >= HARDWARN:
        ram_log.warning("%s RAM: %s" % (dt_string, ram_use))
    else:
        ram_log.info("%s RAM: %s" % (dt_string, ram_use))
    
    ram_log.removeHandler(hdlr=ram_handler)
    ram_handler.close()
    return

def disk_logger(PATH, HARDWARN):
    disk_free = psutil.disk_usage(DISK_PATH).percent
    #DISK_LOG = setup_logger('ram_logger', '%s%s_DISK.log' %(PATH,datetime.date.today()))

    disk_handler = logging.FileHandler('%s%s_DISK.log' %(PATH,datetime.date.today()))
    disk_log = logging.getLogger('disk_log')
    disk_log.setLevel(logging.INFO)
    disk_log.addHandler(disk_handler)

    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if disk_free >= HARDWARN:
        disk_log.warning("%s DISK FREE: %s" % (dt_string, disk_free))
    else:
        disk_log.info("%s DISK FREE: %s" % (dt_string, disk_free))
    #print("disk")
    disk_log.removeHandler(hdlr=disk_handler)
    return
x = 0

# 
while (x < 100):
    print(x)
    if x%CPU_INTERVAL == 0 and CPU_LOGGING == True:
        cpu_logger(LOG_PATH, 80)
        print("CPU")
    if x%RAM_INTERVAL == 0 and RAM_LOGGING == True:
        ram_logger(LOG_PATH, 80)
        print("RAM")
    if x%DISK_INTERVAL == 0 and DISK_LOGGING == True:
        disk_logger(LOG_PATH, 80)
        print("DISK")
    time.sleep(1)
    x = x + 1

