info = {"name": "Karan", "age": 19, "eligible": True}
print(info)

print(info["name"])  # Error miss
print(info.get("eligible"))  # No Error on miss

print(info.values())
print(info.keys())
print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
