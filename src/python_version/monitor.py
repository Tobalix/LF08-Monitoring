import math
import psutil
import logging
import datetime
import time



def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""
    handler = logging.FileHandler(log_file)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


def cpu_log(PATH, HARDWARN):
    CPU_USE = psutil.cpu_percent()
    CPU_LOG = setup_logger('cpu_logger', '%s_CPU.log' % PATH)
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if CPU_USE >= HARDWARN:
        CPU_LOG.warning("%s CPU: %s" % (dt_string, CPU_USE))
    else:
        CPU_LOG.info("%s CPU: %s" % (dt_string, CPU_USE))


def ram_log(PATH, HARDWARN):
    RAM_USE = psutil.virtual_memory().percent
    RAM_LOG = setup_logger('ram_logger', '%s_RAM.log' % PATH)
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if RAM_USE >= HARDWARN:
        RAM_LOG.warning("%s RAM: %s" % (dt_string, RAM_USE))
    else:
        RAM_LOG.info("%s RAM: %s" % (dt_string, RAM_USE))


x = 0

while (x < 10):
    cpu_log(datetime.date.today(), 80)
    ram_log(datetime.date.today(), 80)
    time.sleep(2)
    x = x + 1

# def cpu_log(PATH):
#     cpu_use = psutil.cpu_percent()
#     logging.basicConfig(filename="%sCPU.log" % PATH, encoding='utf-8', level=logging.DEBUG)
#     # logging.debug('This message should go to the log file')
#     dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#     if cpu_use >= 80:
#         logging.warning("%s CPU: %s" % (dt_string, cpu_use))
#     else:
#         logging.info("%s CPU: %s" % (dt_string, cpu_use))
#     # logging.warning('And this, too')
#     # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
#
#
# x = 0
#
#
# def ram_log(PATH):
#     ram_use = psutil.virtual_memory().percent
#     logging.basicConfig(filename="%sRAM.log" % PATH, encoding='utf-8', level=logging.DEBUG)
#     # logging.debug('This message should go to the log file')
#     dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#     if ram_use >= 80:
#         logging.warning("%s RAM: %s" % (dt_string, ram_use))
#     else:
#         logging.info("%s RAM: %s" % (dt_string, ram_use))
#
#
# while (x < 10):
#     cpu_log("")
#     ram_log("")
#     time.sleep(2)
#     x = x + 1
#     print(x)
