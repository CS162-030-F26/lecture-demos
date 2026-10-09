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
    with open('data.txt', 'r') as my_awesome_file:
        # Context manager body

        # Here is where we do our file reading
        
        # my_awesome_file is an iterable
        for line in my_awesome_file:
            line = line.strip()
            print(line)


    # Once the context manager is over, my_awesome_file technically
    # still exists, but is no longer "valid".
        

if __name__ == '__main__':
    main()
