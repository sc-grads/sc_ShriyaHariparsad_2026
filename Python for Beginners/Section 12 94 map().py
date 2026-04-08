numbers: list[int] = [1, 2, 3, 4, 5]

def double(number: int) -> int:
    return number * 2

doubled: map = map(double, numbers)
print(doubled)
print(numbers)
