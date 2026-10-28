# A class invariant is a property of objects of a class that is always guaranteed to be true.

from typing import TextIO

class Circle:
    _radius: float

    def __init__(self, radius: float) -> None:
        if radius < 0:
            self._radius = 0
            # raise ValueError('Error: radius cannot be negative')
        else:
            self._radius = radius

def parse_file(some_parameter: TextIO) -> None:
    pass

class Dog:
    name: str

    def bark(self) -> None:
        print(self.name)

def main() -> None:
    spot = Dog()
    spot.name = 'Spot'
    spot.bark()

    user_age = int(input('How old are you?: '))

    

    raise TypeError('This is a very cool type error')

    c = Circle(-1)

    try:
        print(int('Hello') + 1)
    except ValueError as my_cool_exception:
        # Handle it here
        pass

    with open('data.txt', 'r') as my_cool_file:
        parse_file(my_cool_file)

    if 1 + 2 == 2:
        x = 1
    print(x)

    spot.bark()
    jeff.bark()


if __name__ == '__main__':
    main()


