import asyncio
import sqlite3

import aiosqlite3


class DB:
    def __init__(self, database):
        self._database = database
        self._connect = None
        self._curser = None

    def __enter__(self):
        self._connect = sqlite3.connect(self._database)
        self._curser = self._connect.cursor()
        return self._curser

    def __exit__(self, exc_type, exc_val, exc_tb, *args):
        self._connect.commit()
        self._curser.close()
        self._connect.close()


class AsyncDB:
    def __init__(self, database):
        self._database = database
        self._connect = None
        self._curser = None

    async def __aenter__(self):
        self._connect = await aiosqlite3.connect(self._database)
        self._curser = await self._connect.cursor()
        return self._curser

    async def __aexit__(self, exc_type, exc_val, exc_tb, *args):
        await self._connect.commit()
        await self._curser.close()
        await self._connect.close()


sqlite_db = r"./sqlite.db"
with DB(sqlite_db) as db:
    aa = db.execute("select * from ptest")
    [print(i) for i in aa.fetchall()]
print("*" * 72)


async def func():
    async with AsyncDB(sqlite_db) as db:
        await db.execute("select name,sex from ptest")
        result = await db.fetchall()
        [print(i) for i in result]


asyncio.run(func())
