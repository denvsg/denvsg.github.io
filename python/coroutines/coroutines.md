## 协程 coroutines

```python
"""
concurrent.futures.Future 对像
"""
import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):
    time.sleep(2)
    print(value)


pool = ThreadPoolExecutor(max_workers=5)

pool1 = ProcessPoolExecutor(max_workers=5)

for i in range(10):
    fut = pool.submit(func, 1)
    print(fut)

```

```python
import asyncio


async def func(args):
    print(1)
    await asyncio.sleep(2)
    print(2)
    return f"func{args}"


async def main():
    print("main function")

    task_list = [
        asyncio.create_task(func("f1")),
        asyncio.create_task(func("f2"))
    ]

    print("main result")

    done, pending = await asyncio.wait(task_list, timeout=None)
    return done


r = asyncio.run(main())
for i in r:
    print(i.result())

```

```python
"""
Future object
"""
import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("1234")


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    await loop.create_task(set_after(fut))
    data = await fut
    print(data)


r = asyncio.run(main())
```

```python
import asyncio


async def func(args):
    print(1)
    await asyncio.sleep(2)
    print(2)
    return f"func{args}"


task_list = [
    func("f1"),
    func("f2")
]
done, pending = asyncio.run(asyncio.wait(task_list, timeout=None))

for i in done:
    print(i.result())
```

```python
import time
import asyncio
import concurrent.futures


def func1():
    time.sleep(2)
    return "func1"


async def main():
    loop = asyncio.get_running_loop()

    fut = loop.run_in_executor(None, func1)
    result = await fut

    print("default: thread pool", result)


asyncio.run(main())

```

<br />
<br />
<br />
<br />
<br />

......     
[上一篇：异步](../asyncio/asyncio.md)    
[回到目录](../Readme.md)   
......
