from numpy import sum as npsum
from numpy import arange


def boucle_while():
    output = 0
    x = 0
    while x < 1000:
        output += x
        x += 1
    return output


def boucle_for():
    output = 0
    for x in range(1000):
        output += x
    return output


def boucle_comprehension():
    return sum([x for x in range(1000)])


def boucle_numpy():
    return npsum(arange(1000))


def bigbrain():
    return (999 * (999 + 1)) / 2


def main():
    breakpoint()


if __name__ == "__main__":
    main()
