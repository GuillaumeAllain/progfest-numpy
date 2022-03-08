import numpy as np

arr = np.random.rand(100)


def func_python():
    output = []
    for x in arr:
        if x > 0.5:
            output.append(x)
    return sum(output) / len(output)


def func_numpy():
    return None


def main():
    print(func_python())
    print()


if __name__ == "__main__":
    main()
