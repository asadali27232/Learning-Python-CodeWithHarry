i = int(input("Enter the number: "))
print(i)

while i <= 38:
    i = int(input("Enter the number: "))
    print(i)

print("Done with the loop")

count = 5
while count > 0:
    print(count)
    count = count - 1
else:
    print("I am inside else")

# Not Possibl
# do {
#   loop body;
# }while(condition);

x = 0
while True:
    print("Do while like loop in python")
    x += 1
    if not (x < 10):
        break
