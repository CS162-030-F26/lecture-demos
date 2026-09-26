import math

# A given computer understands its own machine language, and nothing else.

# Programs written in any other language have to be translated
# into the computer's machine language.

# There are two main kinds of translators:
# compilers: translation up front (before runtime)
# interpreters: translation on demand (at runtime)

# The standard Python translator is a CPython interpreter.

def program() -> None:
    # Every process has a special file stream known as
    # standard output. In most normal use cases,
    # a process's standard output is hooked up to the
    # terminal by default.

    # A process is a running instance of a program.

    print('Hello, World!')

    # Python has the following primitive types:
    # int: integer (numbers without decimal points)
    #       1, -1, -1000000, 0
    # float: floating point number (a number with a decimal point)
    #       3.14, -3.14, 3.0, 3., .3
    # bool: boolean
    #       True, False
    # str: string (a sequence of zero or more characters)
    #       '', "", 'h', 'e', 'Hello, World!'
    
    # Literal: hardcoded value.

    # An expression is a piece of code with a type and a value.
    # An example of an expression would be a literal.

    # Operators.
    # Combine expressions to form new expressions.
    # Arithmetic operators in Python:
    # +
    # -
    # *
    # /   (regular division)
    # //  (integer division; divide, then truncate)
    # %   (modulo; remainder after division)
    # ** (or, preferably, math.pow)

    # print(2 ** 5) # Prints 32, but may confuse Mypy
    print(math.pow(2, 5)) # Less confusing to Mypy

    # Static means before runtime.
    # Mypy is a static analysis tool, specifically a type checker.
    # Analyzes code before runtime to make sure there are no type errors.
    # It has a hard time understanding the types of ** operations.
    

if __name__ == '__main__':
    program()
