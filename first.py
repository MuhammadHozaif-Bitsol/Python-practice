"""Basic Python practice demonstrating variables, types, logic, and imports."""

from math import pi

import example


def main():
    """Run the practice script demonstrations."""
    # variables
    x = 5
    print(x)
    name = "ali"
    print(7 + 3)
    print("hello")
    x = str(3)
    print(type(x))
    print(type(name))
    a = b"hello"
    print(a)
    print(type(a))

    # typecasting
    num1 = "23"
    print(type(num1))
    num2 = 34
    int_num = int(num1)
    num3 = int_num + num2
    print(num3)
    print(type(num3))

    # conditionals
    score = 85

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    else:
        print("Grade: C or below")

    # loops
    for i in range(5):
        print(i)

    # list, sets, tuples
    fruits = ["apple", "banana", "orange"]
    ids = (1, 2, 3, 4)
    lights = {"red", "green", "blue"}
    print(fruits)
    print(ids)
    print(lights)

    # use the add method from the module we made
    print(example.add(34, 34))
    print(pi * pi)


if __name__ == "__main__":
    main()
