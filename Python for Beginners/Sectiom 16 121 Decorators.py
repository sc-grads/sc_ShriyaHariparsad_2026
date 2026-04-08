import time
from typing import Callable
from functools import wraps

def get_time(func: Callable) -> Callable:
    """Times how long it takes to execute a function."""

    def wrapper(*args, **kwargs) -> None:
        start_time: float = time.perf_counter()
        func(*args, **kwargs)
        end_time: float = time.perf_counter()

        print(f'Time: {end_time - start_time:.3f}s')

    return wrapper
@get_time
def calculate() -> None:
    """calculate() docstring"""

    print('Calculating...')
    for i in range(20_000_000):
        pass

    print('Done')

def main() -> None:
    calculate()

if __name__ == '__main__':
    main()


