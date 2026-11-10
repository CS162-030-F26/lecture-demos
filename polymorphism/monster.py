from abc import abstractmethod, ABC

from player import Player

# An abstract class is a class with one or more
# unimplemented abstract methods. If you want
# a class to be abstract, it SHOULD inherit from
# ABC, provided by abc
class Monster(ABC):
    # There is such a thing as an abstract method.
    # An abstract method is defined in a base class,
    # and it specifies an interface but no implementation.
    # In order to do this, we can decorate our method
    # with the @abstractmethod decorator provided by
    # the abc module
    @abstractmethod
    def attack_player(self, player: Player) -> None:
        pass
