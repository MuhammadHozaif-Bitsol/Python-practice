def main():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return self.name

    p1 = Person("Ali", 23)

    print(p1)


if __name__ == "__main__":
    main()
