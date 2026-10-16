# This file contains the cat module.
class Cat:
    color: str
    owner: str
    age: int

def create_cat(color: str, owner: str, age: int) -> Cat:
    the_cat = Cat()
    the_cat.color = color
    the_cat.owner = owner
    the_cat.age = age
    return the_cat

def print_cat(the_cat: Cat) -> None:
    print(the_cat.color)
    print(the_cat.owner)
    print(the_cat.age)
