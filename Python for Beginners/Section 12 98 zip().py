numbers: list[int] = [1, 2, 3, 4]
letters: list[str] = ['A', 'B', 'C', 'D']
symbols: list[str] = ['!', '?', '$']

zipped: zip = zip(numbers, symbols)
print(list(zipped))


