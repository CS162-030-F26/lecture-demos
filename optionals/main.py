def foo(some_value: int | str) -> float | str:
    print(some_value)

    if 1 + 1 == 2:
        return 3.14
    else:
        return 'hello'

def f(x: int | str) -> None:
    # The only operations that are definitely always supported
    # by a given union type are the operations supported by
    # ALL types in the union.
    print(x) # This is fine
    # print(x * 3.5) # This causes Mypy errors

def print_hp(pokemon: Pokemon) -> None:
    print(pokemon.get_hp())

class City:
    name: str
    population: int | None

class Pokemon:
    _hp: int
    def __init__(self) -> None:
        self._hp = 5

    def get_hp(self) -> int:
        return self._hp


def main() -> None:
    # Union type.
    # A union type is the union of two or more types.
    # It is okay (even from Mypy's perspective) to assign values
    # to a union-typed variable so long as those values' types are
    # compatible with at least ONE of the unioned types.
    x: int | str = 1
    print(type(x)) # class <int>
    x = 'hello'
    print(type(x)) # class <str>
    x = True
    print(x)

    # Union types are often not very useful
    f(x)

    # However, there's an exception to this rule of thumb: optionals.
    # An optional is a kind of union type that's very useful.
    # An optional is a union type consisting of two types in the union:
    # 1. Some regular type, 2. None.

    # The purpose of an optional is to represent some data that may
    # or may not be known / exist at a given point in time
    player_1_pokemon: Pokemon | None = None

    player_1_pokemon = Pokemon()

    player_1_pokemon = None

    
    if player_1_pokemon is not None:
        print(player_1_pokemon.get_hp())
        print_hp(player_1_pokemon)

if __name__ == '__main__':
    main()
