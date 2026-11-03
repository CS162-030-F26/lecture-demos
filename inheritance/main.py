from dog import Dog
from husky import Husky

def main() -> None:
    spot = Dog('Spot', 3)
    spot.bark()

    delilah = Husky('Delilah', 4)
    delilah.bark()

if __name__ == '__main__':
    main()
