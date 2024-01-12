from multiprocessing import Process
from monitor import start
from alarm import Alarm


def monitoring(seconds):
    start()


def alarming(seconds):
    Alarm().alarm()


p1 = Process(target=monitoring, args=[1])
p2 = Process(target=alarming, args=[1])

if __name__ == "__main__":
    p1.start()
    p2.start()
