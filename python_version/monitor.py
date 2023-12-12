import math
import psutil
import logging
import datetime
import time

print(psutil.virtual_memory().percent)

def cpu_log(PATH):
    CPU_USE = psutil.cpu_percent()
    logging.basicConfig(filename="%sCPU.log" % PATH, encoding='utf-8', level=logging.DEBUG)
    #logging.debug('This message should go to the log file')
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if CPU_USE >= 80:
        logging.warning("%s CPU: %s" %( dt_string, CPU_USE) )
    else:
        logging.info("%s CPU: %s" %( dt_string, CPU_USE) )
    #logging.warning('And this, too')
    #logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
x = 0
def ram_log(PATH):
    RAM_USE = psutil.virtual_memory().percent
    logging.basicConfig(filename="%sRAM.log" % PATH, encoding='utf-8', level=logging.DEBUG)
    #logging.debug('This message should go to the log file')
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if RAM_USE >= 80:
        logging.warning("%s RAM: %s" %( dt_string, RAM_USE) )
    else:
        logging.info("%s RAM: %s" %( dt_string, RAM_USE) )


while(x < 100):
    cpu_log("")
    ram_log("")
    time.sleep(2)
    x = x+1
    print(x)
