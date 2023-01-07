import asyncio


async def run_cmd(*args):
    # Create subprocess
    process = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE,  # stdout must a ppe accessible as process.stdout
    )
    # wait for subprocess finish

    stdout, stderr = await process.communicate()
    # return stdout
    return stdout  # .decode().strip()


loop = asyncio.get_event_loop()
# gather uname and cmds
cmd = asyncio.gather(run_cmd("dir"), run_cmd("ipconfig"))
# run cmds
uname, date = loop.run_until_complete(cmd)
loop.close()
# print result
print(f"uname:{uname}, date:{date}")
