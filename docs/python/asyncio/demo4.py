# asyncio.gather 获取执行结果

import time
import asyncio


async def func(x):
    print(f"before {x}")
    await asyncio.sleep(3)
    print(f"after {x}")


tasks = [
    asyncio.ensure_future(func(1)),
    asyncio.ensure_future(func(2)),
    asyncio.ensure_future(func(3)),
]
start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))  # asyncio.gather 获取执行结果
loop.close()
end = time.time()
print(end - start)
