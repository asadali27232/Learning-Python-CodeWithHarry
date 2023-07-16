colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.sort()
print(num)

colors.sort(reverse=True)
print(colors)
num.sort(reverse=True)
print(num)

colors.reverse()
print(colors)
num.reverse()
print(num)

print(colors.index("green"))
print(num.index(3))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

newlist = colors.copy()
print(colors)
print(newlist)

colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")  # inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]
print(colors)

# add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
