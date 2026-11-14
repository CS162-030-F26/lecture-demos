from item import Item

# T is a generic type parameter.
# Understand that a parameter is a placeholder.
# A generic type parameter is specifically a placeholder for the NAME
# OF A TYPE.

# A class with one or more generic type parameters is sometimes
# referred to as a generic class.

# An upper bound on a generic type parameter specifies a base class
# from which generic type arguments must inherit in order to be
# valid
class Vendor[T: Item]:
    _inventory: list[T]
    _money: float

    def __init__(self) -> None:
        self._inventory = []
        self._money = 0

    def add_item_to_stock(self, item: T) -> None:
        self._inventory.append(item)

    def sell_item(self, index: int) -> None:
        self._money += self._inventory[index].get_price()
        del self._inventory[index]

    def print(self) -> None:
        print(f'Money: {self._money}')
        print(f'Inventory:')
        for item in self._inventory:
            item.print()
