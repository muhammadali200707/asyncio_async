import asyncio
from datetime import datetime


async def assignment1():
    await asyncio.sleep(2)
    print("Assignment 1 ")


async def assignment2():
    await asyncio.sleep(6)
    print("Assignment 2 ")


async def assignment3():
    await asyncio.sleep(2)
    print("Assignment 3 ")


async def assignment4():
    await asyncio.sleep(2)
    print("Assignment 4 ")


async def assignment5():
    await asyncio.sleep(5)
    print("Assignment 5 ")


async def assignment6():
    await asyncio.sleep(2)
    print("Assignment 6 ")


async def assignment7():
    await asyncio.sleep(2)
    print("Assignment 7 ")


async def assignment8():
    await asyncio.sleep(2)
    print("Assignment 8 ")


async def assignment9():
    await asyncio.sleep(3)
    print("Assignment 9 ")


async def assignment10():
    await asyncio.sleep(2)
    print("Assignment 10 ")


async def main():
    await asyncio.gather(assignment1(), assignment2(), assignment3(), assignment4(), assignment5(), assignment6(),
                         assignment7(), assignment8(), assignment9(), assignment10())


if __name__ == "__main__":
    print(f"This is begin -> {datetime.now()}")
    asyncio.run(main())
    print(f"This is end -> {datetime.now()}")
