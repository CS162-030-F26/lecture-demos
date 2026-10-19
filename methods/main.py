# Just as classes can have fields (data attributes), they can also
# have methods (function attributes)
from typing import Self


class Dog:
    breed: str
    owner: str
    age: int

    def bark(self) -> None:
        print('Bark! Bark!')

    def print(self) -> None:
        print(self.breed)
        print(self.owner)
        print(self.age)
        self.bark()

    def greet(self, another_dog: Self) -> None:
        print(f'Hello, {another_dog.owner}\'s dog')

    # There exist certain methods that are special and
    # can do special things / get called in special cases.

    # A constructor (initializer) is a special method that's
    # automatically called on an object the moment it's created.
    # The purpose of a constructor is to "set up", or initialize,
    # the object. Its name must be __init__. Constructors must
    # have a return type of None.
    def __init__(self, breed: str, owner: str, age: int) -> None:
        self.breed = breed
        self.owner = owner
        self.age = age

def main() -> None:
    clifford = Dog('Big Red', 'Elizabeth', 50)
    clifford.print()

    scooby = Dog('Great Dane', 'Shaggy', 1000)
    scooby.print()

    clifford.greet(scooby)

    # In Python, the word "object" is basically used to refer to
    # any piece of data.

    # In Python, basically every object is an instance of a class

    # You may hear a lot about "object-oriented programming".
    # It's a paradigm of programming centered around classes and objects.
    # In this context, an "object" is specifically something with
    # data AND behavior (AND identity)
    

if __name__ == '__main__':
    main()
