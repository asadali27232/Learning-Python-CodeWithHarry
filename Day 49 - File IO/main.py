import os

print(os.getcwd())

os.chdir(os.getcwd() + "/Day 49 - File IO")

f = open("myfile.txt", "r")
contents = f.read()
print(contents)

f = open("myfile.txt", "w")
f.write("Hello, world!")

f = open("myfile.txt", "a")
f.write("Hello, world!")

f.close()

with open("myfile.txt", "r") as f:  # Auto
    content = f.read()
    print(content)
