from dataclasses import dataclass, field, InitVar

@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    is_rare: InitVar[bool | None] = None
    total_price: float = field(init=False)

    def __post_init__(self, is_rare: bool |None) -> None:
        if is_rare:
            self.price_per_kg *= 2

        self.total_price = (self.grams / 1000) * self.price_per_kg

    def describe(self) -> None:
        print(f'{self.grams}g of {self.name} costs ${self.total_price}')

def main() -> None:
    apple: Fruit = Fruit('Apple', 1500, 5)
    orange: Fruit = Fruit('Orange', 2500, 10)
    passion: Fruit = Fruit('Passion', 100, 50, is_rare=True)

    apple.describe()
    orange.describe()
    passion.describe()


if __name__ == '__main__':
    main()