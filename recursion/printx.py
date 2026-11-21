# Goal: Write a function that accepts a height and a padding, and print
# a big X made out of asterisks of that height and with that left-padding

# print_x(5, 2)
#  *   *
#   * *
#    *
#   * *
#  *   *

def print_x(height: int, padding: int) -> None:
    if height % 2 == 0 or height <= 0 or padding < 0:
        raise ValueError('height must be positive and odd, and padding must be non-negative')

    # Base cases
    if height == 1:
        for _ in range(padding):
            print(' ', end='')
        print('*')
        return

    # Print the top line of text of the big X
    for _ in range(padding):
        print(' ', end='')
    print('*', end='')
    for _ in range(height - 2):
        print(' ', end='')
    print('*')

    # Recurse to print the smaller X inside it
    print_x(height - 2, padding + 1)

    # Print the bottom line of text of the big X
    for _ in range(padding):
        print(' ', end='')
    print('*', end='')
    for _ in range(height - 2):
        print(' ', end='')
    print('*')

def main() -> None:
    print_x(7, 0)
    print_x(13, 3)

if __name__ == '__main__':
    main()
