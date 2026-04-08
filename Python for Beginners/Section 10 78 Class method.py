from typing import Self

class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int) -> None:
        self.brand = brand
        self.max_speed = max_speed

    @classmethod
    def change_limit(cls, new_limit: int) -> None:
        cls.LIMITER = new_limit

    def display_info(self) -> None:
        print(f'{self.brand} (max={self.max_speed}, limiter={self.LIMITER})')

def main() -> None:
    bmw: Car = Car('BMW', 240)
    toyota: Car = Car('Toyota', 190)

    bmw.display_info()
    toyota.display_info()

if __name__ == '__main__':
    main()