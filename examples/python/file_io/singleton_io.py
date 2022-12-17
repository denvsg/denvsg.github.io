"""
##################################
# 单例模式，支持多线程
##################################
"""
import asyncio
import threading
from multiprocessing import Process


class DumpJson:
    _instance = None

    lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance

        with cls.lock:
            if cls._instance:
                return cls._instance
            cls._instance = object.__new__(cls)
            return cls._instance

    def __init__(self, file):
        self.file = file

    def write(self, info):
        with open(file=self.file, mode="a") as fp:
            fp.write(f"{info}")


f = "a.txt"

def a(x):
    dj = DumpJson(f)
    dj1 = DumpJson(f)
    if x % 2 == 0:
        for i in range(x, 50, 2):
            dj.write(f"{chr(i + 65)}")
    else:
        for i in range(x, 50, 2):
            dj1.write(f"{i}")


def b(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def c(x):
    new_loop = asyncio.get_event_loop()
    t1 = threading.Thread(target=b, args=(new_loop,))
    t2 = threading.Thread(target=b, args=(new_loop,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    new_loop.call_soon_threadsafe(a, 6)
    new_loop.call_soon_threadsafe(a, 3)


if __name__ == '__main__':
    t1 = Process(target=c, args=(0,))
    t2 = Process(target=c, args=(1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
