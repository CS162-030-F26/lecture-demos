from furniture import Furniture
from car import Car

from vendor import Vendor

def main() -> None:
    jacob = Vendor[Furniture]()

    couch = Furniture(300.00, 'Couch')
    chair = Furniture(30.00, 'Chair')

    jacob.add_item_to_stock(couch)
    jacob.add_item_to_stock(chair)

    jacob.print()

    jacob.sell_item(0)

    jacob.print()

    samantha = Vendor[Car]()

    ford_taurus = Car(800.00, 'Ford', 'Taurus', 2001)
    jeep_grand_cherokee = Car(3000.00, 'Jeep', 'Grand Cherokee', 2009)

    samantha.add_item_to_stock(ford_taurus)
    samantha.add_item_to_stock(jeep_grand_cherokee)

    # This now causes Mypy to raise errors, as we wanted.
    # rocking_chair = Furniture(100.00, 'Rocking Chair')
    # samantha.add_item_to_stock(rocking_chair)

    samantha.print()

    samantha.sell_item(0)

    samantha.print()


if __name__ == '__main__':
    main()
