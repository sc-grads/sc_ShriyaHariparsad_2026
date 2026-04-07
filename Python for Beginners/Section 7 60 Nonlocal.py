def outer_func() -> None:
    name: str = ''
    value: int = 0

    def inner_func() -> None:
        nonlocal name, value
        name = 'Tom'
        value = 100

    inner_func()
    print(name, value)
outer_func()










