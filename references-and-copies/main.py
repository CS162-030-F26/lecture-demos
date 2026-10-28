class City:
    name: str

def main() -> None:
    # Every piece of data in Python is an object

    # Every object has an ID.

    print(5)

    print(id(5))

    # At a given point in time, all of the objects that simultaneously
    # exist in a Python program are guaranteed to have UNIQUE IDs.

    x = 5
    y = 6

    print(id(x))
    print(id(y))

    # The assignment operator takes a reference on the left, and an object
    # on the right, and it binds the reference to the object.

    x = y

    print(id(x))
    print(id(y))

    corvallis = City()

    # The . operator reaches inside the object on the left to access the
    # reference inside it with the name given on the right
    corvallis.name = 'Corvallis'

    some_other_city = corvallis
    some_other_city.name = 'Eugene'
    print(corvallis.name) # Prints Eugene
    print(some_other_city.name) # Prints Eugene as well


if __name__ == '__main__':
    main()
