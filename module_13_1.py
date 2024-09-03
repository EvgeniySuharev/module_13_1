import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    number = 0
    for i in range(1, 6):
        number += 1
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {number}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
