# A class can inherit attributes from another class.

# In this context, the class doing the inheriting is referred to as the
# derived class, AKA the child class, AKA the subclass

# The class that is being inherited from is referred to as the base class,
# AKA the parent class, AKA the superclass.

# When you create an inheritance relationship, every attribute that is defined
# in the base class becomes implicitly also defined in the derived class.

from dog import Dog
from sled import Sled

# The Husky class is derived from the Dog class (the Husky class inherits from
# the Dog class).
class Husky(Dog):
    # Extension: When you add additional methods and / or attributes in
    # a derived class
    _energy: int

    def __init__(self, name: str, age: int) -> None:
        # self._name = name # Violation of encapsulation
        # self._age = age # Same as above

        # The solution is delegation. I want to initialize _name and
        # _age of self, so I delegate that responsibility to a method of the
        # Dog class:
        # self.__init__(name, age) # This tells this function to call itself
        super().__init__(name, age) # This runs the Dog class constructor on self


        self._energy = 100

    # This is an override: a method in a derived class with the same
    # header as a corresponding method in one of its ancestor classes
    def vocalize(self) -> None:
        print('Awoooooo!')
        super().vocalize()

    def pull_sled(self, sled: Sled) -> None:
        if self._energy > 0:
            sled.distance_pulled += 5
            self._energy -= 1
