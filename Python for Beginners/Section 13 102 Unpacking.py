def add(a: int, b: int) -> None:
    print(f'{a+b = }')

numbers: dict[str, int] = {'a': 5, 'b': 10}
add(**numbers)


