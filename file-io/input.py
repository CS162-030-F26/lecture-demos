# import typing
from typing import TextIO

def read_from_file(the_file: TextIO) -> None:
    for line in the_file:
        line = line.strip()
        tokens = line.split(',')

        last_name = tokens[0]
        first_name = tokens[1]
        age = int(tokens[2])

        print(f'Name: {first_name} {last_name}')
        print(f'Age: {age}')
        print()

def main() -> None:
    # Standard I/O:

    # print() writes data to standard output, which is usually
    # hooked up to the terminal.

    # input() reads data from standard input, which is usually
    # hooked up to the terminal.

    # File I/O: The goal is to read data from files and write data
    # to files.
    # Text I/O: reading / writing text files

    # File input: reading data from files.

    # r: Reading
    # w: Writing
    # a: Appending

    try:
        with open('data.txt', 'r') as my_awesome_file:
            # Context manager body

            # Here is where we do our file reading
            
            # my_awesome_file is an iterable
            read_from_file(my_awesome_file)
    except FileNotFoundError as my_exception:
        print('Error: data.txt not found')
        return


    # Once the context manager is over, my_awesome_file technically
    # still exists, but is no longer "valid".
        

if __name__ == '__main__':
    main()
