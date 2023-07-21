def welcome(message):
    print(message)


welcome("This will run always even when file is imported as module")

if __name__ == "__main__":
    welcome("This will run when file is executed directly")

print("Asad.py __name__ = ", __name__)  # Will be name of module i.e Asad when run as imported code
