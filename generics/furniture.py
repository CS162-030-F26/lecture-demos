from typing import override

from item import Item

class Furniture(Item):
    _name: str

    def __init__(self, price: float, name: str) -> None:
        super().__init__(price)
        self._name = name

    @override
    def print(self) -> None:
        print(f'\tName: {self._name}')
        super().print()
