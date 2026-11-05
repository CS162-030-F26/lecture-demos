class Dog:
    _name: str
    _age: int

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def vocalize(self) -> None:
        print(f'Bark! Bark! My name is {self._name}, and I am {self._age} '
              f'years old.')
