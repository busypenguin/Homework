import threading
import time
import math
import datetime


var_i = None


def worker():
    global var_i
    while True:
        if var_i is not None:
            print("Поток завершается")
            break  # Завершение потока
###################################

t = threading.Thread(target=worker)
t.start()
t2 = threading.Thread(target=worker)
t2.start()
t.join()
time.sleep(2)
var_i = 1


def worker():
    for a in range(10):
        print(f"{datetime.datetime.now()}: ПОТОК {threading.get_ident()} НАЧАЛО")
        t=0
        for item in range(10000000):
            t = t+1
        time.sleep(0.2)
        print(f"{datetime.datetime.now()}: ПОТОК {threading.get_ident()} КОНЕЦ")
        time.sleep(1)


t = threading.Thread(target=worker)
t.start()
t2 = threading.Thread(target=worker)
t2.start()
