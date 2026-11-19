# Suppose I want to write a function that determines whether a string
# is a palindrome. A palindrome is a string whose characters are the
# same when reversed.

# racecar
# mom
# dad
# hello

def is_palindrome(the_string: str) -> bool:
    # The intuition of recursion: can I break this problem down into
    # smaller instances of the same problem, and then solve those smaller
    # instances with recursion, and then piece them together to solve
    # the original, large problem instance?

    # A string is a palindrome if and only if:
    # 1. The first and last characters are the same
    # 2. Everything in the middle (the substring) is a palindrome

    if len(the_string) <= 1:
        return True

    if the_string[0] != the_string[-1]:
        return False

    if not is_palindrome(the_string[1:-1]):
        return False

    return True

def main() -> None:
    print(is_palindrome('raccar'))
    print(is_palindrome('racecar'))
    print(is_palindrome(''))
    print(is_palindrome('a'))
    print(is_palindrome('hello'))

if __name__ == '__main__':
    main()
