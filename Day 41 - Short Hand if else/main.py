a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a > b else 0
print(c)

value_if_true = "value if true"
value_if_false = "value if false"

condition = True

result = value_if_true if condition else value_if_false

if condition:
    result = value_if_true
else:
    result = value_if_false
