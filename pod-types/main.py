# POD types (plain-old-data)

class SteeringWheel:
    diameter_inches: float

# Note: classes are typically named in PascalCase
class Car:
    # Class body goes here
    # Field definitions go here.
    # A field is a smaller piece of data that instances
    #    of the given class have.

    # Field definitions establish "has-a" relationships.
    make: str
    model: str
    year: int
    steering_wheel: SteeringWheel

def create_steering_wheel(diameter_inches: float) -> SteeringWheel:
    result = SteeringWheel()
    result.diameter_inches = diameter_inches
    return result

def create_car(make: str, model: str, year: int, steering_wheel: SteeringWheel) -> Car:
    result = Car()
    result.make = make
    result.model = model
    result.year = year
    result.steering_wheel = steering_wheel
    return result

def print_steering_wheel(steering_wheel: SteeringWheel) -> None:
    print(f'Steering wheel diameter: {steering_wheel.diameter_inches} inches')

def print_car(the_car: Car) -> None:
    print(f'Make: {the_car.make}')
    print(f'Model: {the_car.model}')
    print(f'Year: {the_car.year}')
    print_steering_wheel(the_car.steering_wheel)

    # the_car.year = 2100 # As it turns out, this actually does modify
    # the year field of the car that was passed in as an argument


def main() -> None:
    # int, bool, float: Primitive types.

    # Composite types: Types of data composed of smaller
    # types of data.

    # It turns out that you can create your own composite types
    # via classes.

    # For example, in my program, suppose every "car" consists of
    # a manufacturer (make), a model, and a year. I could define
    # a class that defines a Car to be an object that contains those
    # three things.

    
    ford_taurus = create_car(
        'Ford',
        'Taurus',
        2001,
        create_steering_wheel(12.0)
    )
    toyota_tacoma = create_car(
        'Toyota',
        'Tacoma',
        2026,
        create_steering_wheel(13.5)
    )
    #ford_taurus = Car()
    #ford_taurus.make = 'Ford'
    #ford_taurus.model = 'Taurus'
    #ford_taurus.year = 2001

    print_car(ford_taurus)
    print()
    print_car(toyota_tacoma)

    # print()
    # print(ford_taurus.year) # 2100
    # print(toyota_tacoma.year) # 2100

if __name__ == '__main__':
    main()
