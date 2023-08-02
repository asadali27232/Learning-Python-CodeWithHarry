# Default Constructor
class Details:
    def __init__(self):
        print("animal Crab belongs to Crustaceans group")


obj1 = Details()


# Parameterized Constructor
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

    def info(self):
        print(f"{self.animal} is a {self.group}")


obj1 = Details("Crab", "Crustaceans")
obj1.info()


# Destructor
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

    def info(self):
        print(f"{self.animal} is a {self.group}")

    def __del__(self):
        print("Destructor called, Details deleted.")


obj1 = Details("Crab", "Crustaceans")
obj1.info()

del obj1
# obj1.info() not possible as obj1 is deleted
