def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))
    return sum / len(numbers)


# Python will consider latest defination i.e. no method over loading
def average(a, b, c=1):
    print("The average is ", (a + b + c) / 3)
    return (a + b + c) / 2


average(4, 6, 4)

c = average(5, 6, 4)
print(c)


def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")
