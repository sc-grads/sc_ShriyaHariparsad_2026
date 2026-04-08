from typing import override

class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def describe(self) -> None:
        print(f'{self.name} ({self.sides})')

    def shape_method(self)-> None:
        print(f'{self.name}: shape_method()')

class Square(Shape):
    def __init__(self, size: float):
        super().__init__('Square', 4)
        self.size = size

    @override
    def describe(self) -> None:
        print(f'I am a {self.name} with a size of ({self.size})')

class Rectangle(Shape):
    def __init__(self, length: float, height: float):
        super().__init__('Rectangle', 4)
        self.length = length
        self.height = height

    @override
    def describe(self) -> None:
        print(f'{self.name} ({self.height}x{self.length}')



def main() -> None:
    rectangle: Rectangle = Rectangle(10,15)
    rectangle.describe()
    rectangle.shape_method()


if __name__ == '__main__':
    main()


