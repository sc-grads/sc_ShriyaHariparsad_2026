class Fruit:
    def __init__(self, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams

    def eat(self) -> None:
        print(f'Eating {self.grams} g of {self.name}')

def main() -> None:
    apple: Fruit = Fruit('Apple', 25)
    print(apple.name)
    apple.eat()


    banana: Fruit = Fruit('Banana', 10)
    print(banana.name)
    banana.eat()


if __name__ == '__main__':
    main()