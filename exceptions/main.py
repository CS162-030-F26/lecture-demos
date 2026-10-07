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
    c()

def a() -> None:
    b()

def main() -> None:
    try:
        # This is try body. This is where you TRY to do things, that might
        # raise errors.
        a()


    except:
        # This is the except block. This is where you handle errors
        # that occurred within the try block.

        # This block of code will be executed when the ValueError is raised.
        print('Value error was raised!')

    # Program continues here
    print('Continues here')

if __name__ == '__main__':
    main()
