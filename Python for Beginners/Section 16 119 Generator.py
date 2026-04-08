from typing import Generator

def five_numbers() -> Generator:
    for i in range(1, 6):
        yield i

numbers: Generator = five_numbers()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))