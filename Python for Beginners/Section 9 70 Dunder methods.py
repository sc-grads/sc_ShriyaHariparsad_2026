from typing import Self

class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages

    def __add__(self, other: Self) -> Self:
        combined_title: str = f'{self.title} & {other.title}'
        combined_pages: int = self.pages + other.pages
        return Book(combined_title, combined_pages)


def main() -> None:
    py_daily: Book = Book("PyDaily", 100)
    harry_potter: Book = Book("Harry Potter", 340)

    print(len (py_daily))
    print(len (harry_potter))

    combined_books: Book = py_daily + harry_potter
    print(combined_books.title)
    print(combined_books.pages)

if __name__ == "__main__":
    main()
