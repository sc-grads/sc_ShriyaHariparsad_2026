fruit: str = 'apple'
number: int = 10

def func() -> None:
    print('func() was called!')

print(f'callable(): {callable(fruit)}')
print(f'callable(): {callable(number)}')
    

