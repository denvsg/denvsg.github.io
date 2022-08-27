import asyncio
import time


async def get_html(url):
    print(f"start get url {url}")
    await asyncio.sleep(2)
    print(f"finish get url {url}")


start = time.time()
loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(get_html("www.baidu.com")) for i in range(9)
]

group1 = [get_html("douin.com") for _ in range(9)]
group2 = [get_html("yahoo.com") for _ in range(9)]
loop.run_until_complete(asyncio.gather(*group1, *group2))
loop.close()
end = time.time()
print(end - start)

# gather he await
# gather 更高层，还可以将task分组
