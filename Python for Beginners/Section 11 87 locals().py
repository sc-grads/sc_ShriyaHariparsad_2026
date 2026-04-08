EXAMPLE: str = 'Bob'

def add(a: int, b: int) -> None:
    result: int = a + b
    print(f'{a} + {b} = {result}')

    print('add() has:', locals())
    print('add() can see:', globals())

add(1,1)

