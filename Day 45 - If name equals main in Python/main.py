# We use __name__ == "__main__" to make sure this code only runs if this file is executed directly
# Not when imported as module as you see in Asad.py file.

import Asad as ass

ass.welcome("Calling welcome function from main.py file")

print(__name__)  # Will be __main__ when run directly
