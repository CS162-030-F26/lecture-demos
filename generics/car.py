from typing import override

from item import Item

class Car(Item):
    _make: str
    _model: str
    _year: int

    def __init__(self, price: float, make: str, model: str, year: int) -> None:
        super().__init__(price)
        self._make = make
        self._model = model
        self._year = year

    def print(self) -> None:
        print(f'\tMake: {self._make}')
        print(f'\tModel: {self._model}')
        print(f'\tYear: {self._year}')
        super().print()
