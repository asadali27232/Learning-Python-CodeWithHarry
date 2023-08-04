# Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child(Parent):
    def func2(self):
        print("This function is in child class.")


object = Child()
object.func1()
object.func2()


# Single Inheritance
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def __init__(self, name, id, language):
        Employee.__init__(self, name, id)
        self.language = language

    def showLanguage(self):
        print(f"The working langauge of {self.name} is {self.language}")


e1 = Employee("Jameel Ahmad", 400)
e1.showDetails()

e2 = Programmer("Asad Ali", 401, "Python")
e2.showDetails()
e2.showLanguage()


# Multiple Inheritance
class Mother:
    def __init__(self, name) -> None:
        self.mothername = name

    def mother(self):
        print(f"Mother name: {self.mothername}")


class Father:
    def __init__(self, name) -> None:
        self.fathername = name

    def father(self):
        print(f"Father name: {self.fathername}")


class Son(Mother, Father):
    def __init__(self, name, fathername, mothername):
        self.sonname = name
        Father.__init__(self, fathername)
        Mother.__init__(self, mothername)

    def parents(self):
        print("Child's Father name is:", self.fathername)
        print("Child's Mother name is:", self.mothername)


s1 = Son("Asad", "Daddy", "Mummy")
s1.parents()

s1.fathername = "Ghaffar Ahmad"
s1.mothername = "Mom"

s1.father()
s1.mother()
s1.parents()


# Multilevel Inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def print_family(self):
        print("Grandfather name :", self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


s1 = Son("Prince", "Rampal", "Lal mani")
print(s1.grandfathername)
s1.print_family()


# Hierarchical Inheritance
class Parent:
    def __init__(self):
        print("This is parent class.")

    def func1(self):
        print("This function is in parent class.")


class Girl(Parent):
    def __init__(self):
        super().__init__()
        print("This is child class.")

    def func2(self):
        print("This function is in Girl Class.")


class Boy(Parent):
    def func3(self):
        print("This function is in Boy Class.")


girl = Girl()
boy = Boy()

boy.func1()
boy.func3()

girl.func1()
girl.func2()


# Hybrid Inheritance
class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


object = Student3()
object.func1()
object.func2()
