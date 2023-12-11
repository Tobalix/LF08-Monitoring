import math
import psutil
import logging


RAM_auslastung = psutil.virtual_memory().percent

#print(CPU_auslastung)
print(RAM_auslastung)

def cpu_log(PATH):
    CPU_auslastung = psutil.cpu_percent()
    logging.basicConfig(filename="example.log', encoding='utf-8', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

cpu_log("")