import asyncio
import multiprocessing
import os
import random
import threading


# import nest_asyncio

# nest_asyncio.apply()


async def fun(keys, *args):
    print(keys, f"process:{keys}")
    await asyncio.sleep(random.randint(1, 5))
    print("pid is: ", os.getpid(), args)


def func(key, *args):
    # asyncio.set_event_loop(loops)
    # loops.run_forever()
    coroutines = []
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [fun(key, args),
             fun(key, *args)]
    loop.run_until_complete(
        asyncio.gather(asyncio.gather(*tasks))
    )


def main(key, *value):
    print(f"process:{key}")
    threads = []
    for j in range(1, 5):
        print(f"current process {key}, create thread t{j}")
        t = threading.Thread(target=func, args=(key, value))
        t.start()
        threads.append(t)
    [t.join() for t in threads]


if __name__ == '__main__':
    proc = []
    for i in range(1, 5):
        print(f"create process p{i}")
        p = multiprocessing.Process(target=main, args=(f"p{i}", 3 * i, 3 * i + 1, 3 * i + 2, 3 * i + 3,))
        proc.append(p)
        p.start()
    [p.join() for p in proc]

    # for p in proc:
    #     p.join()
