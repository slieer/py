import threading
import time


class TestThread(threading.Thread):

    def __init__(self, name="TestThread"):
        """constructor, setting initial variables"""
        self._stopevent = threading.Event()
        self._sleepperiod = 1.0
        # 推荐方式使用 super()
        super().__init__(name=name)

    def run(self):
        """main control loop"""
        # 使用 self.name 替代已弃用的 self.getName()
        print(f"{self.name} starts")

        count = 0
        while not self._stopevent.is_set():  # is_set() 是推荐写法，isSet() 仍可用但旧式
            count += 1
            print(f"loop {count}")
            self._stopevent.wait(self._sleepperiod)

        print(f"{self.name} ends")

    def join(self, timeout=None):
        """Stop the thread."""
        self._stopevent.set()
        super().join(timeout)


if __name__ == "__main__":  # 修正了这里的空格问题
    testthread = TestThread()
    testthread.start()

    time.sleep(10.0)

    testthread.join()
