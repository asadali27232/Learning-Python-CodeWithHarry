lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes'

print(animals[4:])  # using positive indexes
print(animals[-4:])  # using negative indexes

print(animals[:6])  # using positive indexes
print(animals[:-3])  # using negative indexes

print(animals[::2])  # using positive indexes
print(animals[-8:-1:2])  # using negative indexes

print(animals[1:8:3])

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

namesWith_len_greater_then_4 = [item for item in names if (len(item) > 4)]
print(namesWith_O)
