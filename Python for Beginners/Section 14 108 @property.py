from dataclasses import dataclass, field, InitVar

@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float

    @property
    def total_price(self) -> float:
        return(self.grams / 1000) * self.price_per_kg



    def describe(self) -> None:
        print(f'{self.grams}g of {self.name} costs ${self.total_price}')

def main() -> None:
    apple: Fruit = Fruit('Apple', 1500, 5)
    print(apple)
    apple.price_per_kg = 20
    print(apple)
    apple.describe()



if __name__ == '__main__':
    main()