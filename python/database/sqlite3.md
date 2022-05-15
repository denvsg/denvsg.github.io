# python 操作 sqlite3

```python
import asyncio
import aiosqlite3


async def execute(database):
    print("running", database)

    conn = await aiosqlite3.connect(database=database)

    cur = await conn.cursor()
    await cur.execute("select name,sex from ptest")

    result = await cur.fetchall()
    print(database, result)

    await conn.close()
    conn.close()
    print("end", database)


# asyncio.run(execute("main.db"))

task_list = [
    execute("main.db"),
    execute("sqlite.db"),
]
asyncio.run(asyncio.wait(task_list))

```