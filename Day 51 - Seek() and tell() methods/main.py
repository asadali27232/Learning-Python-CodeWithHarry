with open("file.txt", "r+") as f:
    f.write("123456789 Asad Ali")

    print("Position in file after writing 18 bytes:", f.tell())

    # Move to the 10th byte in the file
    f.seek(10)

    print("Position in file after seek(10):", f.tell())

    # Read the next 5 bytes
    data = f.read(5)

    print("Data:", data)
    print("Position in file after reading 5 bytes:", f.tell())

with open("file.txt", "r") as f:
    # Read the first 10 bytes
    data = f.read(10)

    print("Data:", data)

    # Save the current position
    current_position = f.tell()
    print("Current read position:", current_position)

    # Seek to the saved position
    f.seek(current_position)

    # Read the next 5 bytes
    data = f.read(5)
    print("Data:", data)

with open("file.txt", "w") as f:
    f.write("Hello World!")
    f.truncate(5)

with open("file.txt", "r") as f:
    print(f.read())
