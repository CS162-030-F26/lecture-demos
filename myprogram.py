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
    # //  (integer division; divide, then floor)
    # %   (modulo; remainder after division)
    # ** (or, preferably, math.pow)

    # print(2 ** 5) # Prints 32, but may confuse Mypy
    # print(math.pow(2, 5)) # Less confusing to Mypy

    # Static means before runtime.
    # Mypy is a static analysis tool, specifically a type checker.
    # Analyzes code before runtime to make sure there are no type errors.
    # It has a hard time understanding the types of ** operations.
    
    # = is the assignment operator. It does two things:
    # 1. It fully computes the value of the expression on the right
    #    (1.5) If the variable on the left doesn't exist, it creates it
    # 2. It stores that value in the variable on the left
    x = math.pow(2, 5)
    print(type(x))
    
    print(x + 1) # Prints 33.0

    x = 12.5
    print(type(x))

    # In most programming languages, this is forbidden. 
    # In Python, this is totally allowed.
    # However, it's strongly discouraged. And Mypy forbids it.
    # x = 'hello'
    #print(x)
    #print(type(x))

    x = x + 1
    x += 1.5
    x -= 2
    x *= 2
    x /= 13
    print(x) # Prints 2

    # F strings
    print(f'The value of x is {x}')

    # Type casting is converting an expression of one type
    # into a new expression of another type.
    x = -1.999
    z = int(x) # The rule is truncation
    print(z)
    print(type(z))

    # To my knowledge, you can type-cast between any of the
    # primitive types that we've covered

    # If you type cast from int to float, the rule is
    # tack on a .0
    print(float(7))

if __name__ == '__main__':
    program()
