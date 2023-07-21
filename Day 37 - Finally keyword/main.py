def func():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("Finally: I am always executed")

    print("I want to always execute but not able to")


x = func()
print("func() return value:", x)
