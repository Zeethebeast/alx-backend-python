#!/usr/bin/env python3
# import asyncio 

async def my_function():
    print("Before async")
    await asyncio.sleep(10)
    print("after async")

import asyncio

async def my_function():
    print("Before await")
    await asyncio.sleep(2)
    print("After await")
asyncio.run(my_function())

# import asyncio

# async def task():
#     print("started")
#     await asyncio.sleep(2)
#     print("done with task1")

# # async def task2():
# #     print("task2 started")
# #     await asyncio.sleep(3)
# #     print("done with task2")

# async def main():
#     # await asyncio.gather(task1(), task2())
#     task1 = asyncio.create_task(task())
#     task2 = asyncio.create_task(task())

#     await task1
#     await task2


# asyncio.run(main())

# import asyncio
# import random

# async def random_task(task_num):
#     delay = random.randint(1, 5)
#     print(f"Task {task_num} will take {delay} seconds.")
#     await asyncio.sleep(delay)
#     print(f"Task {task_num} finished.")

# async def main():
#     tasks = [asyncio.create_task(random_task(i)) for i in range(3)]  # 3 tasks
#     await asyncio.gather(*tasks)  # Run all tasks concurrently

# asyncio.run(main())
