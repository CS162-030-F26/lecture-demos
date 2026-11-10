from monster import Monster

# The Skeleton class is also an abstract class. It inherits
# an interface (attack_player) with no implementation,
# and fails to override it with an implementation.
class Skeleton(Monster):
    pass
