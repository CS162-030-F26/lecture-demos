# Importing is how you include code from other files into your file.
# import math # This is a full-package / full-module import
from math import pow, sqrt, sin as math_sin # This is individual object imports

def sin() -> None:
    print('Gluttony, the deadly sin')

def print_list(the_list: list[str]) -> None:
    for i in the_list:
        print(i)

def main() -> None:
    # standard output is a special stream, typically hooked up to the
    # terminal, that print() writes to.

    # There's also standard input. It's also typically hooked up to
    # the terminal.
    guess = int(input('Guess the magic number: '))

    # Relational operators in python
    # >
    # <
    # >=
    # <=
    # ==
    # !=

    if not (guess < 4 or guess > 4):
        print('Good job!')

        # If statements do NOT have their own scope.
        x = 'hello'
    elif guess < 4 and (not (guess > 4)):
        print('Too low!')
    else:
        print('Too high!')

    # print(x) # This works so long as guess == 4
    
    # Logical operators.
    # and, or, not
    # a and b: produces True if and only if a and b are both True
    # a or b: produces True if and only if at least one of a or b is True
    # not a: produces True if and only if a is False

    # Loops

    # 1. While loops
    # 2. For loops

    while guess != 4:
        guess = int(input('Guess the magic number: '))

    # For loops in Python are range-based.
    # What's an iterable? A collection where you can move from
    # one element (member) to the next.
    # ranges / lists / dicts / tuples
    
    # A range is a sequence of numbers with a
    # start, a stop, and a step.

    # To create a range, use the range() function.
    # range(start, stop, step)
    # The start is the first number that's included in the range.
    # The stop is the first number that's NOT included in the range.
    # range(2, 12, 3)
    # [2, 5, 8]
    for i in range(2, 11, 3):
        # Body goes here
        print(i)
    
    print(i) # What does this print? It prints 8


    # There are two other ways to construct ranges.
    # range(10): The start is implied to be zero, the step is implied
    # to be 1, and the stop is 10.
    for _ in range(10):
        print('hello')

    # range(1, 10): The start is 1, the stop is 10, the step is implied
    # to be 1.
    for i in range(1, 10):
        print(i) # Prints 1-9

    # The dot operator reaches inside the thing on the left to access
    # the thing on the right
    print(pow(2, 5)) # Prints 32
    print(sqrt(100)) # Prints 10

    print(math_sin(3.14))

    # A list is a mutable, ordered, collection of elements.
    # In Python, a List is heterogeneous (elements can be of different
    # types). Even though technically a List is heterogeneous in
    # Python, Mypy doesn't like that.
    my_list = ['hello', 'world', '!', '']
    
    print(my_list[1]) # Python Lists are indexed by 0. Prints world.
    # print(my_list[4]) # Raises an IndexError
    print(my_list[-1]) # Prints last element

    # Lists in Python can be expanded and shrunk.

    # The append method can be used to add an element to the end
    # of a list
    my_list.append('gosh')

    # ['hello', 'world', '!', '', 'gosh']

    # insert() can be used to add elements in arbitrary positions
    my_list.insert(1, 'goodbye')
    # ['hello', 'goodbye', 'world', '!', '', 'gosh']
    print(my_list[5]) # gosh
    print(my_list[1]) # goodbye

    del my_list[1]
    # ['hello', 'world', '!', '', 'gosh']

    # len() accepts a list as an argument and returns the length of the
    # list
    print(len(my_list))

    # Lists are iterables.
    for word in my_list:
        print(word)



if __name__ == '__main__':
    main()
