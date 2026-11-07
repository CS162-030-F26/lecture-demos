class Player:
    _hp: int

    def __init__(self) -> None:
        self._hp = 100

    def take_damage(self, amount: int) -> None:
        self._hp -= amount

    def print(self) -> None:
        print(f'Remaining HP: {self._hp}')

    def is_alive(self) -> bool:
        return self._hp > 0
