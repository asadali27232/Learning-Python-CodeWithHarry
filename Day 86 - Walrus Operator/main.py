numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

names = ["John", "Jane", "Jim"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")
