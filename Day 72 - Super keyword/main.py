class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        # Employee.__init__(self, name, id)
        # or
        super().__init__(name, id)
        self.lang = lang


rohan = Employee("Das", "420")
Asad = Programmer("Asad", "2345", "Python")
print(Asad.name)
print(Asad.id)
print(Asad.lang)


# Allows Mulitple Inheritance
# Conflicts in multiple inheritance will be resolved by the order of inheritance
# Method Resolution Order (MRO)
# Method will be searched in the order of inheritance
class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")


class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")


class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()


child_object = ChildClass()
child_object.child_method()
