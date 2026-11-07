from player import Player
from monster import Monster

class Zombie(Monster):
    _sanity: int

    def __init__(self) -> None:
        self._sanity = 3

    def attack_player(self, player: Player) -> None:
        print('Zombie is attacking the player')
        if self._sanity > 0:
            # The zombie still has some sanity, so they don't
            # damage the player. Instead, they simply lose
            # 1 sanity.
            self._sanity -= 1
            return

        player.take_damage(2)
