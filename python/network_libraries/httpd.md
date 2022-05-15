# httpd

```python
import threading
import time

import httpx
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()


def sync_main(url, sign):  # 同步
    response = httpx.get(url).status_code
    print(f"sync_main: {threading.current_thread()}: {sign}: {response}")


#
# sync_start = time.time()
# [sync_main(url='http://www.baidu.com', sign=i) for i in range(200)]
# sync_end = time.time()
# print(sync_end - sync_start)
url = "https://runoob.com/python3/python-modules.html"
while True:
    try:
        res = requests.get(url, verify=False)
    except requests.exceptions.ConnectionError:
        status_code = "Connect refused"
        print(status_code)
        time.sleep(2)
        continue
    else:
        soup = BeautifulSoup(res.text)
        print(soup)

```

```python
import asyncio
import threading
import time

import httpx

client = httpx.AsyncClient()


async def async_main(url, sign):  #
    response = await client.get(url)
    status_code = response.status_code
    # await client.aclose()
    print(f"async_main: {threading.current_thread()}: {sign}: {status_code}")


# loop = asyncio.new_event_loop()
loop = asyncio.get_event_loop()
tasks = [async_main(url='http://www.baidu.com', sign=i) for i in range(200)]
async_start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
async_end = time.time()
# loop.close()
print(async_end - async_start)

```

```python
import asyncio
import threading
import time

import httpx

client = httpx.AsyncClient()


async def async_main(url, sign):  #
    # async with httpx.AsyncClient() as client:
    response = client.get(url)
    # status_code = response.status_code
    print(f"async_main: {threading.current_thread()}: {sign}: {status_code}")


# coroutine=async_main()
# loop = asyncio.new_event_loop()
loop = asyncio.get_event_loop()
# tasks = [async_main(url='http://www.baidu.com', sign=i) for i in range(200)]
tasks = asyncio.ensure_future([async_main(url='http://www.baidu.com', sign=i) for i in range(200)])
async_start = time.time()
loop.run_until_complete((tasks))
async_end = time.time()
loop.close()
print(async_end - async_start)

```