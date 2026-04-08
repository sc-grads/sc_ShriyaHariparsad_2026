class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.name} = {self.weight}kg'

cat: Animal = Animal('Cat', 10)
dog: Animal = Animal('Dog', 5)
kangaroo: Animal = Animal('Kangaroo', 50)

sorted_animals: list[Animal] = sorted([cat, dog, kangaroo], key=lambda animal: animal.weight)
print(sorted_animals)
