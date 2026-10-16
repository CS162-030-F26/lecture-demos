# This file contains the dog module.
# A Python module is basically any .py file.

# In this module, I'm going to define the Dog class, and functions
# that are closely related to the Dog class, but nothing else.
class Dog:
    breed: str
    owner: str
    age: int

# The outermost scope is called global scope, AKA module scope.
# Anything defined in module scope is available in THIS MODULE,
# but NOT other modules! To make the below functions available in
# other modules, you must make use of `import`. See main.py.

def create_dog(breed: str, owner: str, age: int) -> Dog:
    the_dog = Dog()
    the_dog.breed = breed
    the_dog.owner = owner
    the_dog.age = age
    return the_dog

def print_dog(the_dog: Dog) -> None:
    print(the_dog.breed)
    print(the_dog.owner)
    print(the_dog.age)
