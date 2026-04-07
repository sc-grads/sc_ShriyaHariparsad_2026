people: list[str] = ['Anna', 'Bob', 'Chris', 'David', 'Fred']

for person in people:
    print(person)

    if person == 'Bob':
        print(f'Removing: {person}')
        people.remove('Bob')












