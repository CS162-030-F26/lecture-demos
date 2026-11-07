from player import Player
from zombie import Zombie
from vampire import Vampire
from monster import Monster

def do_turn(
        player: Player,
        monsters: list[Monster]) -> None:
    for m in monsters:
        m.attack_player(player)

    player.print()

def main() -> None:
    player = Player()

    # What we've done here is known as subtype polymorphism.
    # Polymorphism: Many forms. Generally, polymorphism
    # refers to a scenario where you have a variable that
    # can be bound to objects of many types.

    # Mypy allows subtype polymorphism, implemented via
    # implicit upcasting.

    monsters: list[Monster] = []
    for _ in range(5):
        monsters.append(Zombie())

    for _ in range(3):
        monsters.append(Vampire())

    while player.is_alive():
        # Monsters attack the player
        do_turn(player, monsters)
    

if __name__ == '__main__':
    main()
