class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


asad = Person("Asad", 2)
asad.name = "Asad Ali"
asad.age = 22

print(f"Name: {asad._name} and Age: {asad._age}")
