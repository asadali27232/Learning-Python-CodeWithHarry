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
