# python 操作 sqlite3

```python
import asyncio
import aioredis


async def execute(address, passwd):
    print("running", address)

    redis = await aioredis.create_redis(address, passwd)

    await redis.hmset_dict('car', key1=1, key2=2, key3=3)

    result = await redis.hgetall('car', encoding='utf8')
    print(result)

    redis.close()
    await redis.wait_closed()

    print("end", address)


asyncio.run(execute('redis://127.0.0.1:6379'))

# task_list = [
#     execute('redis://1.1.1.1:80', "1234"),
#     execute('redis://1.1.1.1:80', "1234"),
# ]
# asyncio.run(asyncio.wait(task_list))

```