# The import keyword looks for the package or module of the given
# name in the directory containing the entry point of the program.
#import animals.dog as d
#from animals import dog
from animals.dog import create_dog, print_dog
# from dog import create_dog, print_dog, Dog # Alternatively
import animals.cat as c

def main() -> None:
    # the_dog = dog.Dog()

    clifford = create_dog('Big Red', 'Elizabeth', 50)
    print_dog(clifford)

    garfield = c.create_cat('Orange', 'John', 8)
    c.print_cat(garfield)



if __name__ == '__main__':
    main()
