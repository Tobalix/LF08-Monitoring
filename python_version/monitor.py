import math
import psutil
import logging
import datetime
import time


RAM_auslastung = psutil.sensors_battery()

from gpiozero import CPUTemperature

cpu = CPUTemperature()
print(cpu.temperature)

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
x = 101
def cpu_temp_log(PATH):
    CPU_TEMP = psutil.cpu_percent()
    logging.basicConfig(filename="%sCPU.log" % PATH, encoding='utf-8', level=logging.DEBUG)
    #logging.debug('This message should go to the log file')
    dt_string = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if CPU_USE >= 80:
        logging.warning("%s CPU Temp: %s" %( dt_string, CPU_TEMP) )
    else:
        logging.info("%s CPU Temp: %s" %( dt_string, CPU_TEMP) )


while(x < 100):
    cpu_log("")
    time.sleep(2)
    x = x+1
    print(x)
