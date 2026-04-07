class Animal:


    def __init__(self, name) -> None:
        self.name = name
        self.tricks: list[str] = []

    def teach_trick(self, trick_name: str) -> None:
        self.tricks.append(trick_name)

def main() -> None:
    cat: Animal = Animal("Helios")
    dog: Animal = Animal("Dog")

    cat.teach_trick("Wash dishes")
    cat.teach_trick("Get a job")
    print(cat.tricks)

    dog.teach_trick("Do finances")
    dog.teach_trick("Invest in stocks")
    print(dog.tricks)


if __name__ == "__main__":
    main()