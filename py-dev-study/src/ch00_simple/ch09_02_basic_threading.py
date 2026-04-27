"""

"""
import threading
import time

import logging as log
log.basicConfig(level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

import threading
def task(name):
    sum = 0
    for i in range(5000):
        sum += i
    time.sleep(5)
    log.info(f"{threading.current_thread().name}, Hello, {name}, sum = {sum}")

def firstTask():
    t = threading.Thread(target=task, args=("Alice",), name="我新建的线程")
    t.start()  # 启动线程
    t.join()    # 等待线程结束
    log.info("Done")

def task1():
    a = 0
    while a < 9999*9999:
        a += 1

    log.info("thread=%s, sum=%s", threading.current_thread().name, a)    
def secondTask():
    start_time = time.time()
    thread = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task1)
    thread2.start()
    thread.start()
    thread.join()
    thread2.join()
    task1()
    log.info("done, all time: %s", time.time() - start_time)


if __name__ == '__main__':
    firstTask()
    secondTask()
