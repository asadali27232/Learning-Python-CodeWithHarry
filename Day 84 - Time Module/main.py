import time


def usingWhile():
    i = 0
    while i < 50000:
        i = i + 1
        print(i)


def usingFor():
    for i in range(50000):
        print(i)


init = time.time()
usingFor()
t1 = time.time() - init

init = time.time()
usingWhile()
t2 = time.time() - init

print("Using for: ", t1)
print("Using while: ", t2)


print("This is printed immediately")
time.sleep(3)
print("This is printed after 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
