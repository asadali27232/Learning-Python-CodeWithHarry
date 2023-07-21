# First Way
try:
    a = input("Enter the number: ")
    print(f"Multiplication table of {a} is: ")
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

# Second Way
try:
    a = input("Enter the number: ")
    print(f"Multiplication table of {a} is: ")
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Input value is not a number.")

# Third Way
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Exception: Index Error!")

print("Some imp lines of code after exception handling.")
print("End of program")
