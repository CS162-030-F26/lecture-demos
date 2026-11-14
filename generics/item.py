class Item:
    _price: float

    def __init__(self, price: float) -> None:
        self._price = price

    def get_price(self) -> float:
        return self._price

    def print(self) -> None:
        print(f'\tPrice: {self._price}')
