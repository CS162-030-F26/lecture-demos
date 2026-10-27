def main() -> None:
    # Union type.
    # A union type is the union of two or more types.
    # It is okay (even from Mypy's perspective) to assign values
    # to a union-typed variable so long as those values' types are
    # compatible with at least ONE of the unioned types.
    x: int | str = 1
    x = 'hello'
    x = True
    print(x)

if __name__ == '__main__':
    main()
