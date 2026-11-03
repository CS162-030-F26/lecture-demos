from copy import deepcopy, copy

class City:
    name: str

def my_cool_function(some_city: City) -> None:
    some_city.name = 'Timbuktoo'

class B:
    name: str

class A:
    b: B

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

    #some_other_city = corvallis
    #some_other_city.name = 'Eugene'
    #print(corvallis.name) # Prints Eugene
    #print(some_other_city.name) # Prints Eugene as well

    city2 = deepcopy(corvallis)
    print(city2.name) # Prints Corvallis
    my_cool_function(city2)
    print(city2.name) # Prints Timbuktoo

    print(corvallis.name) # Prints Corvallis

    # corvallis and some_other_city are different references, but the dot
    # operator doesn't operate on references, it operates on objects.

    my_a = A()
    my_a.b = B()
    my_a.b.name = 'Jeff'

    # The copy function from the copy package creates a shallow copy.
    # The outermost object is copied, but objects that its internal attributes
    # refer to are NOT copied.
    my_a_copy = copy(my_a)

    # So my_a_copy refers to a different object from my_a.
    # However, my_a_copy.b refers to the SAME object as my_a.b.

    my_a_copy.b.name = 'Jill'
    print(my_a.b.name) # Prints Jill

    my_a_copy.b = B()
    my_a_copy.b.name = 'Jack'
    print(my_a_copy.b.name) # Prints Jack
    print(my_a.b.name) # Prints Jill

    


    


if __name__ == '__main__':
    main()
