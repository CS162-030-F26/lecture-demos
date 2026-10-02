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

    # TODO range(stop) and range(start, stop)


if __name__ == '__main__':
    main()
