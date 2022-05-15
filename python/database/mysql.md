# python 操作 mysql

```python
import asyncio
import aiomysql


async def execute(host, passwd, user="root"):
    print("running", host, "as", user)

    conn = await aiomysql.connect(
        host=host,
        port=3306,
        user=user,
        password=passwd,
        db='pythonTest'
    )

    cur = await conn.cursor()
    await cur.execute("select name,id from test")

    result = await cur.fetchall()
    print(result)

    await cur.close()
    conn.close()
    print("end", host, " as ", user)


# asyncio.run(execute('localhost', "123456"))

task_list = [
    execute('localhost', "123456"),
    execute('localhost', "1234", "test"),
]
asyncio.run(asyncio.wait(task_list))

```