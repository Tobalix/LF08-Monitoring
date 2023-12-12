import math
import psutil
import logging
import datetime
import time

print(psutil.virtual_memory().percent)


def cpu_log(PATH):
    cpu_use = psutil.cpu_percent()
    logging.basicConfig(filename="%sCPU.log" % PATH, encoding='utf-8', level=logging.DEBUG)
    # logging.debug('This message should go to the log file')
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if cpu_use >= 80:
        logging.warning("%s CPU: %s" % (dt_string, cpu_use))
    else:
        logging.info("%s CPU: %s" % (dt_string, cpu_use))
    # logging.warning('And this, too')
    # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


x = 0


def ram_log(PATH):
    ram_use = psutil.virtual_memory().percent
    logging.basicConfig(filename="%sRAM.log" % PATH, encoding='utf-8', level=logging.DEBUG)
    # logging.debug('This message should go to the log file')
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if ram_use >= 80:
        logging.warning("%s RAM: %s" % (dt_string, ram_use))
    else:
        logging.info("%s RAM: %s" % (dt_string, ram_use))


while (x < 10):
    cpu_log("")
    ram_log("")
    time.sleep(2)
    x = x + 1
    print(x)
