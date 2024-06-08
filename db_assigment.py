import asyncio
from database import Database
from datetime import datetime


async def main_1():
    await asyncio.sleep(2)
    print("Here Address data")
    Database.connect("SELECT * FROM address", "select ")


async def main_2():
    await asyncio.sleep(5)
    print("Here City data")
    Database.connect("SELECT * FROM city", "select ")


async def main():
    await asyncio.gather(main_1(), main_2())


if __name__ == "__main__":
    asyncio.run(main())
