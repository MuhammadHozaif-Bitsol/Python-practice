def main():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p1 = Person("Ali", 23)

    print(p1.name)


if __name__ == "__main__":
    main()
