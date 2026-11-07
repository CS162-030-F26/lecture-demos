from dog import Dog
from husky import Husky
from sled import Sled

def main() -> None:
    spot = Dog('David', 'Spot', 3)
    spot.vocalize() # This calls the Dog-class vocalize method

    # The Husky class now has two constructors.
    # If a class has 2+ "versions" of the same method,
    # because one or more were inherited, but then another
    # one is defined explicitly in said class, then in most
    # cases, by default, when you try to call the method,
    # the one that gets called is the one that is in the "most derived"
    # class.
    delilah = Husky('Alice', 'Delilah', 4)
    delilah.vocalize() # This calls the Husky-class vocalize method (the override)

    super(Husky, delilah).vocalize() # This calls the Dog-class vocalize method

    santas_sleigh = Sled()
    santas_sleigh.distance_pulled = 0

    delilah.pull_sled(santas_sleigh)
    delilah.pull_sled(santas_sleigh)

    print(santas_sleigh.distance_pulled) # Prints 10

if __name__ == '__main__':
    main()
