# Public Access Modifier
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age  # public variable
        self.name = name  # public variable


obj = Student(21, "Asad")
print(obj.age)
print(obj.name)


class Student:
    def __init__(self, age, name):
        self.__age = age  # An indication of private variable

        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)


class Subject(Student):
    pass


obj = Student(201, "Asad")
obj1 = Subject

# Calling by object of class Student
# Not Accessible from outside the class
# print(obj.__age)
# print(obj.__funName())

# Calling by object  of class Subject
# Not Accessible in child class
# print(obj1.__age)
# print(obj1.__funName())


# Name Mangling
class MyClass:
    def __init__(self):
        self.nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"


my_object = MyClass()

print(my_object.nonmangled_attribute)  # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute)  # Throws an AttributeError
print(my_object._MyClass__mangled_attribute)  # Output: I am a mangled attribute


# Protected Access Modifier
# Just a convention
class Student:
    def __init__(self):
        self._name = "Asad"

    def _funName(self):  # protected method
        return "Asad's Function"


class Subject(Student):  # inherited class
    pass


obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
