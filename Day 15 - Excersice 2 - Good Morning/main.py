import time

# https://docs.python.org/3/library/time.html#time.strftime

timestamp = time.strftime("%H:%M:%S")
print("The Time is:", timestamp)

# Time based Greetings from Python
hour_of_the_day = int(time.strftime("%H"))

if hour_of_the_day < 12:
    print("Good Morning!")
elif hour_of_the_day >= 12:
    print("Good Afternoon!")
elif hour_of_the_day > 15:
    print("Good Evening!")
else:
    print("Good Night")
