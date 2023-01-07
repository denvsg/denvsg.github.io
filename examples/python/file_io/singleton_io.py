"""
##################################
# 单例模式，支持多线程
##################################
"""
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


def b(x):
    t1 = threading.Thread(target=a, args=(0,))
    t2 = threading.Thread(target=a, args=(1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    t1 = Process(target=b, args=(0,))
    t2 = Process(target=b, args=(1,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
