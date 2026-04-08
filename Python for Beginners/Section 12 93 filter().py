numbers: list[int] = list(range(1, 21))
print(numbers)

even_numbers: filter = filter(lambda n: n % 2 == 0, numbers)
print(list(even_numbers))
    

