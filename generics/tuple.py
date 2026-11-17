def print_int_and_string(x: tuple[int, str]) -> None:
    print(x[0])
    print(x[1])

def main() -> None:
    # A tuple is a generalization of a pair. It's a collection of N
    # things.
    
    my_tuple = (3, 'hello')
    print_int_and_string(my_tuple)


if __name__ == '__main__':
    main()
