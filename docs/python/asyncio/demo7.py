#

import asyncio
import time

now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)
    await asyncio.sleep(x)
    return f"done after {x}s."


async def print_args(x):
    print(f"before:{x}")
    time.sleep(1)
    await asyncio.sleep(1)
    time.sleep(1)
    return f"after {x}s."


async def main():
    await asyncio.gather(do_some_work(1), do_some_work(2), do_some_work(3))


async def main1():
    await asyncio.gather(print_args("hello"), print_args("world"), print_args("python"))


start = now()
asyncio.run(main1())
end = now()
print(end - start)
