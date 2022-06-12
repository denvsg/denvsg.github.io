# Python 多线程 Multithreading

```python
import time
from threading import Thread


def do_some_works(x):
    print(f"now is {x}")
    time.sleep(2)
    print(f"{x}运行结束")


for i in range(9):
    t1 = Thread(target=do_some_works, args=(f"1-{i}",))
    t2 = Thread(target=do_some_works, args=(f"2-{i}",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

```