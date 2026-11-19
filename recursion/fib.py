def f(x: int) -> int:
    # The obvious answers are covered by the base cases.
    if x == 1:
        return 0
    elif x == 2:
        return 1
    elif x <= 0:
        raise ValueError('x cannot be negative!')
    else:
        # This can often feel like black magic.
        # Intuition: Recursion breaks a problem down into smaller
        # / simpler instances of the same problem, until you
        # eventually have such small / simple problem instances
        # that the answers are "obvious".
        return f(x - 1) + f(x - 2)

# Solutions to speed up this algorithm:
# 1. Memoization is caching of answers as they're computed
# 2. Dynamic programming. This is a general algorithmic design
#     strategy.



def main() -> None:
    print(f(11))

if __name__ == '__main__':
    main()

# To compute f(100), the computer first needs to compute
# f(99) and f(98).

# So it pauses computing f(100), and starts computing, say, f(99)

# In order to compute f(99), it must first compute f(98) and f(97).

# So it pauses computing f(99), and starts computing, say, f(98)
