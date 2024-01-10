import threading
from monitor import start
from alarm import alarm


thread_one = threading.Thread(target=start())
thread_two = threading.Thread(target=alarm())
if __name__ == '__main__':
    thread_two.start()
    thread_one.start()
