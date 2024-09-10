import asyncio
import time

#Basic synchronous example
def slow_task1(name, delay):
    print(f"Starting task {name}: {time.strftime('%X')}")
    time.sleep(delay)
    print(f"Finished task {name}: {time.strftime('%X')}")

def main1():
    slow_task1("Task 1", 3)
    slow_task1("Task 2", 7)
    print("All tasks finished")

main1()

#Basic async Python example

async def slow_task2(name, delay):
    print(f"Starting task {name}: {time.strftime('%X')}")
    await asyncio.sleep(delay)
    print(f"Finished task {name}: {time.strftime('%X')}")

async def main2():
    await slow_task2("Task 1", 3)
    await slow_task2("Task 2", 7)
    print("All tasks finished")

asyncio.run(main2())

#Understanding Concurrency with Async Tasks
async def main3():
    print(f"Starting: {time.strftime('%X')}")

    task1 = asyncio.create_task(slow_task2("Task 1", 3))
    print(f"Created task 1: {time.strftime('%X')}")

    task2 = asyncio.create_task(slow_task2("Task 2", 7))
    print(f"Created task 2: {time.strftime('%X')}")

    await task1
    print(f"Awaited task 1: {time.strftime('%X')}")

    await task2
    print(f"Awaited task 2: {time.strftime('%X')}")

asyncio.run(main3())