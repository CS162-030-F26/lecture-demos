def main() -> None:
    # w is for writing (in truncate mode)
    # a is for writing (in append mode)
    with open('out.txt', 'a') as f:
        # \n is an escape seqeuence that represents a newline
        #    character sequence.
        # Escape sequences generally start with \ and they're
        # used to represent characters (or sequences of characters)
        # that are otherwise hard to express.
        f.write('My text\n')
        f.write('My text\n')

if __name__ == '__main__':
    main()
