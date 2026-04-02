people: list[str] = ['Bob', 'James', 'Maria']

for person in people:
    if len(person) > 4:
        print(f'{person}  has a long name')
    else:
        print(f'{person} has a short name')

