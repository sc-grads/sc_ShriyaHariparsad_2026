import asyncio
from asyncio import Task
from datetime import datetime

async def fetch_data(input_data: int, *, delay: int) -> dict:
    print('Fetching data...')

    start_time: datetime = datetime.now()
    await asyncio.sleep(delay)
    end_time: datetime = datetime.now()

    print('Data retrieved!')

    return{'input': input_data,
           'start_time': f'{start_time:%H:%M:%S}',
           'end_time': f'{end_time:%H:%M:%S}'}


async def main() -> None:
    task: Task[dict] = asyncio.create_task(fetch_data(2, delay=10))
    await asyncio.sleep(1)
    task.cancel (msg='Took too long')

    try:
        data: dict = await task
        print(data)
    except asyncio.CancelledError as e:
        print('Task was cancelled...')
        print(e)
        print(task.cancelled())


    








if __name__ == "__main__":
    asyncio.run(main=main())