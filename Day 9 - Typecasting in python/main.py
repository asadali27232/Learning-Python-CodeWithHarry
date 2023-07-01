a = "1"
# a = 1
b = "2"
# b = 2
print(int(a) + int(b))

# Implicit TypeCasting
c = 1.9
d = 8

print(c + d)

# Explicit Typecasting
string = "15"
number = 7
string_number = int(string)  # throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the numbers is: ", sum)
