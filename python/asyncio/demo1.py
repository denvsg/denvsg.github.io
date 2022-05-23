# 旧代码使用装饰器
import time
import asyncio


@asyncio.coroutine
def func(num):
    print(num, "befer")
    yield from asyncio.sleep(2)
    print(num, "after")


tasks = [func(1), func(2)]

begin = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
end = time.time()
loop.close()
print(end - begin)
