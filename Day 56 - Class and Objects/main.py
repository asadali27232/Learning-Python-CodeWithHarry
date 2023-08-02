class Person:
    name = "Asad"
    occupation = "Data Scientist"
    networth = 1000000

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Ahmad"
a.occupation = "Developer"

b.name = "Jhon"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
