class Asad:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):  # representation of object
        return f"Person({self.name}, {self.age})"

    def __str__(self):  # string representation of object
        return f"Name: {self.name}, Age: {self.age}"

    def __add__(self, other):
        return self.age + other.age

    def __mul__(self, other):
        return self.age * other.age

    def __len__(self):
        return len(self.name)

    def __call__(self):
        print("I am Asad's object")


asad = Asad("Asad", 21)
print(asad)
print(repr(asad))
print(asad + asad)
print(asad * asad)
print(len(asad))
asad()
