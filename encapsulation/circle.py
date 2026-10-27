# Encapsulation is largely useful for two reasons:
# 1. It helps control coupling
# 2. It can help establish class invariants

# A class invariant is a property of objects of a given class
# that is ALWAYS guaranteed to be true.

# I want a guarantee that no circle object will EVER have a
# negative radius.

class Circle:
    _radius: float

    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius

    # Getters and setters
    def get_radius(self) -> float:
        return self._radius

    def set_radius(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius

# Getters and setters often have very brittle interfaces.
# Modifying an implementation detail of a class often also
# necessessitates modifying getters and / or setters related
# to that implementation detail.

# Don't reflexively create getters and setters for any and all
# private attributes.

# General advice: When designing a class, identify some responsibilities
# that are fundamental to objects of that class. Create methods with
# interfaces aligning with those responsibilities. These interfaces
# are probably fairly stable. Figure out the implementation details from
# there.

def main() -> None:
    c = Circle(1.0)
    
    c.set_radius(5.0)

    print(3.14 * c.get_radius() ** 2)
    # c._radius = -1.0

    # A subtle incorrect output is the worst-case scenario.

if __name__ == '__main__':
    main()
