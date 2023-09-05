# Hybrid Inheritance: Combination of Hierarchical and Multiple Inheritance or any other inheritance


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)


class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)


class Student(Person, Program):
    def __init__(self, name, age, address, program_name, duration):
        Person.__init__(self, name, age, address)
        Program.__init__(self, program_name, duration)

    def show_details(self):
        Person.show_details(self)
        Program.show_details(self)


std = Student("John", 22, "London", "B.Tech", 4)
std.show_details()


# Hierarchical Inheritance: More than one derived class is created from a single base class, tree like structure
class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)


class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)


dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()
