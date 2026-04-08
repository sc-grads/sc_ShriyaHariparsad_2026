from typing import Any

text: str = 'Bob'
my_list: list[int] = [1, 2, 3]

def func() -> None:
    ...

my_globals: dict[str, Any] = dict(globals())
print(my_globals)

for k, v in my_globals.items():
    print(f'{k}: {v}')
    