#!/usr/bin/env python3
import time
import asyncio

async def main():
    print(f'{time.ctime()}: Hello')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye')

def blocking():
    time.sleep(0.5)
    print(f'{time.ctime()} Hello from a thread!')

loop1 = asyncio.get_event_loop()
task = loop1.create_task(main())

loop1.run_in_executor(None, blocking)
loop1.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop1)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop1.run_until_complete(group)
loop1.close()