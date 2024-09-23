import time
import asyncio


async def drink_coffee():
    print("Start Drinking Coffee")
    await asyncio.sleep(2)
    print("Stop Drinking Coffee")
    return 'Coffee'

async def eat_breakfast():
    print("Start Eating Breakfast")
    await asyncio.sleep(5)
    print("Stop Eating Breakfast")
    return "Breakfast"


async def main():
    start_time = time.time()

    Sync
    await drink_coffee()
    await eat_breakfast()


    Async
    coffee = asyncio.create_task(drink_coffee())
    breakfast = asyncio.create_task(eat_breakfast())


    await coffee
    await breakfast

    print(coffee)
    print(breakfast)

    results = asyncio.gather(drink_coffee(), eat_breakfast())

    task1, task2 = await results
    print(task1, task2)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Elapsed Time: {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    asyncio.run(main())











import random
import time
import asyncio


async def task(name, delay):
    print(f'{name} started')
    await asyncio.sleep(delay)
    print(f'{name} finished')
    return name

async def main():
    tasks = []
    for i in range(1, 6):
        task_name = f'Task {i}'
        delay = random.randint(1, 10)
        tasks.append(task(task_name, delay))

    # await asyncio.gather(*tasks)

    all_tasks_complete = asyncio.gather(*tasks)
    await all_tasks_complete
    print(all_tasks_complete)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()

    print(f'Elapsed Time: {(end_time - start_time):.2f}')





async def task1():
    return "Task 1"

async def task2(name):
    print(name)


async def main():

    task = asyncio.create_task(task1())

    await task

    await asyncio.create_task(task2(task))


if __name__ == '__main__':
    asyncio.run(main())