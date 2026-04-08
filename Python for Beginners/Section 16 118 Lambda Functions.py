from typing import Callable

def use_all(f: Callable, values: list[int]) -> None:
    for value in values:
        f(value)

use_all(lambda v: print(f'{v * 'X'}'), [2, 4, 10])
