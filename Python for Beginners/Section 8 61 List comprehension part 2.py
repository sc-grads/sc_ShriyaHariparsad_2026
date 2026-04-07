numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers: list[int] = []

for number in numbers:
    if number % 2 == 0:
         even_numbers.append(number)

even_numbers_lc: list[int] = [number for number in numbers if number % 2 == 0]
print(even_numbers_lc)










