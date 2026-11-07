from pet import Pet

class Dog(Pet):
    _name: str
    _age: int

    def __init__(self, owner: str, name: str, age: int) -> None:
        super().__init__(owner)
        self._name = name
        self._age = age

    def vocalize(self) -> None:
        print(f'Bark! Bark! My name is {self._name}, and I am {self._age} '
              f'years old.')
