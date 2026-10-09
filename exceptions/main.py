from traceback import print_exc

def get_age(name: str) -> int:
    if name == 'Alex':
        return 27
    elif name == 'Ghandi':
        return 157
    else:
        raise ValueError(f'Unknown name {name}')



def c() -> None:
    # This line of code raises a ValueError.
    print(int('hello'))

    # A ValueError is a kind of Exception.
    # Error types (Exception subtypes) encode errors,
    # i.e., things that went wrong during runtime.

    # When an exception is raised, the control flow
    # of the program changes: the interpreter
    # checks to see if the offending line of code
    # is inside a try block with an accompanying
    # except block that is equipped to catch
    # the exception that was raised.

    # If it isn't, then the entire function terminates
    # immediately, and the exception propagates down
    # the call stack.

    # This continues until one of two things happens:
    # a) it finds a line of code on the call stack that IS inside
    #   a try block with an except block equipped to catch the exception.
    #   In that case, it executes the except block and continues on
    #   with its day.
    # b) If no such line of code is discovered, if the exception propagates
    #    beyond global scope, the program terminates, and a traceback
    #    is printed to the terminal.

def b() -> None:
    my_list: list[str] = []
    # print(my_list[0])
    c()

def a() -> int:
    b()
    return 1

def main() -> None:
    try:
        # This is try body. This is where you TRY to do things, that might
        # raise errors.
        x = a()


    except ValueError as my_cool_exception:
        # This is the except block. This is where you handle errors
        # that occurred within the try block.

        # This block of code will be executed when the ValueError is raised.
        print('Value error was raised!')

        print(my_cool_exception)

        print_exc()
    except IndexError:
        # This will execute if an IndexError is raised in the try block.
        print('Index error was raised!')

    # Program continues here
    print('Continues here')

    # Here's a real use case for exceptions
    valid_input = False
    while not valid_input:
        valid_input = True
        try:
            age = int(input('What is your age?: '))

            if age < 0:
                valid_input = False
        except ValueError:
            valid_input = False

    print(get_age('Alex'))
    print(get_age('Ghandi'))
    print(get_age('Jessica'))

    



if __name__ == '__main__':
    main()
