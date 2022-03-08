import numpy as np


def read_file(filename):
    with open(filename, "r") as file:
        return np.array(
            [
                list(map(int, list(line.strip())))
                for line in file.read().strip().split("\n")
            ]
        )


print(read_file("data/day9test.dat"))
