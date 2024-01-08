import plotext
import numpy as np
import psutil
import time

l = 1000
x = range(1, l+1)
frames = 1000
cpu_data = []
ram_data = []

upper_lim = 20
lower_lim = 0
interval = 0

def anim_graph(title, data = [], max_point = 20, min_point = 0, pos = 1):
    plotext.title(title)
    plotext.clt()
    plotext.cld()
    plotext.xlim(min_point, max_point)
    plotext.ylim(0,100)
    plotext.plot(x, data, fillx=True, color="blue")
    plotext.show()
    

def get_cpu():
    cpu_percent = psutil.cpu_percent()
    return cpu_percent

def get_ram():
    ram_percent = psutil.virtual_memory().percent
    return ram_percent

def build_data(value, data):
    data.append(round(value))
    return data



plotext.clc()
plotext.clt()
plotext.subplots(1,2)

while True:
    plotext.subplot(1,1)
    anim_graph("CPU Graph", build_data(get_cpu(), cpu_data),upper_lim, lower_lim)
    plotext.subplot(1,2)
    anim_graph("RAM Graph", build_data(get_ram(), ram_data), upper_lim, lower_lim)
    if interval >=20:
        lower_lim += interval - 10
        upper_lim += interval
        interval = 0
    interval += 1 
    if len(ram_data) >=100:
        ram_data = []
        cpu_data = []
        upper_lim = 20
        lower_lim = -10
    time.sleep(0.1)