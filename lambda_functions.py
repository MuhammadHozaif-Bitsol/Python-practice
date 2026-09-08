"""Practicing lambda functions"""


def main():
    multiply_by_2 = lambda x: 2 * x
    print(multiply_by_2(3))

    n = [4, 3, 2, 1]
    print([x**2 for x in n])


if __name__ == "__main__":
    main()
