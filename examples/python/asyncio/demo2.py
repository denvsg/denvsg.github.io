# 使用 ensure_future 获取执行结果

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)
    await asyncio.sleep(x)
    return f"done after {x}s."


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(3)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    return await asyncio.gather(*tasks)


start = now()
loop = asyncio.get_event_loop()
rets = loop.run_until_complete(main())
end = now()

for ret in rets:
    print("Task ret:", ret)

print(end - start)
