class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child(Parent):
    def func2(self):
        print("This function is in child class.")


object = Child()
object.func1()
object.func2()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

    def showLanguage(self):
        print(f"The working langauge of {self.name} is {self.language}")


e1 = Employee("Jameel Ahmad", 400)
e1.showDetails()

e2 = Programmer("Asad Ali", 401, "Python")
e2.showDetails()
e2.showLanguage()


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
