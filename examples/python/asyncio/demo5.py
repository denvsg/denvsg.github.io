# 使用 await 获取执行结果

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

    dones, pending = await asyncio.wait(tasks)
    for task in tasks:
        print("Task ret:", task.result())


start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = now()
