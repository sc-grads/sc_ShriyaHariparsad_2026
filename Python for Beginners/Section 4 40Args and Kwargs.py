def func(*args: str, default: int, **kwargs: int) -> None:
    print(args)
    print(kwargs)
    print(default)

func('a', 'b', default=20, a=1, b=2)





