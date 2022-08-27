# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import selectors
import time

import aiohttp

URL = 'https://www.xiazaiba.com'


async def job(session):
    response = await session.get(URL)
    return str(response.url)


async def main(_loop):
    async with aiohttp.ClientSession() as session:
        tasks = [_loop.create_task(job(session)) for _ in range(5)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]  # 得到工作回报.
        print(all_results)


if __name__ == '__main__':
    t2 = time.time()
    # loop = asyncio.get_event_loop()           # Removed
    selector = selectors.SelectSelector()  # New line
    loop = asyncio.SelectorEventLoop(selector)  # New line
    try:
        loop.run_until_complete(main(loop))  # 完成事件循环，直到最后一个任务结束
    finally:
        loop.close()  # 结束事件循环.
    print("Async total time:", time.time() - t2)
