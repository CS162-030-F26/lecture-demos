# Note: classes are typically named in PascalCase
class Car:
    # Class body goes here
    # Field definitions go here.
    # A field is a smaller piece of data that instances
    #    of the given class have.
    make: str
    model: str
    year: int

def main() -> None:
    # int, bool, float: Primitive types.

    # Composite types: Types of data composed of smaller
    # types of data.

    # It turns out that you can create your own composite types
    # via classes.

    # For example, in my program, suppose every "car" consists of
    # a manufacturer (make), a model, and a year. I could define
    # a class that defines a Car to be an object that contains thosee
    # three things.


if __name__ == '__main__':
    main()
