from timeit import timeit, repeat

a: str = 'list(range(1000))'
b: str = 'list(range(1000))'

warmup: float = timeit(stmt=a, number=100_000)
a_time: float = timeit(stmt=a, number=100_000)
b_time: float = timeit(stmt=b, number=100_000)

print(f'a: {a_time:.3f}s')
print(f'b: {b_time:.3f}s')