"""Practiced decorators"""


def main():
    def intro_modifier(func):
        def wrapper():
            print("hello")
            func()
            print("bye")

        return wrapper

    @intro_modifier
    def print_name():
        print("my name is ali")

    print_name()

    def calculation(func):
        def wrapper(*args, **kwargs):
            print("starting calculation")
            func(*args, **kwargs)
            print("Calculation finished")

        return wrapper

    @calculation
    def add(a, b):
        print(f" sum is {a + b}")

    add(2, 3)


if __name__ == "__main__":
    main()
