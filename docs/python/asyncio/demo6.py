#

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)
    await asyncio.sleep(x)
    return f"done after {x}s."


# tasks = [
#     asyncio.ensure_future(func(1)),
#     asyncio.ensure_future(func(2)),
#     asyncio.ensure_future(func(3)),
# ]

start = now()
loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks)) # asyncio.gaher() 获取执行结果，多任务使用
loop.run_until_complete(asyncio.gather(do_some_work(3), do_some_work(5)))
loop.close()
end = now()
print(end - start)
