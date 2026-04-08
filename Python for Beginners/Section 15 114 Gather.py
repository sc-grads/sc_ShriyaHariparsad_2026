import asyncio
from asyncio import Task, Future
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
    tasks: Future[tuple] = asyncio.gather(
        fetch_data(1, delay=1),
        fetch_data(2, delay=2),
        fetch_data(3, delay=1)
    )

    result: tuple = await tasks
    for result in result:
        print(result)




if __name__ == "__main__":
    asyncio.run(main=main())