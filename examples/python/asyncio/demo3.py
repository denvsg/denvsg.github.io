# 异步和线程

import asyncio
import time
from threading import Thread

now = lambda: time.time()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def do_works(x):
    print(f"do work {x}")
    time.sleep(x)
    print(f"finish work {x}")


start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()

end = now()

print(f"time {end - start}")

asyncio.run_coroutine_threadsafe(do_works(6), new_loop)
# new_loop.call_soon_threadsafe(do_works, 6)
# new_loop.call_soon_threadsafe(do_works, 3)
