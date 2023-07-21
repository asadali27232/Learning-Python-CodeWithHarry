# Ways of importing modules
from math import *  # Not recommended
import math as builtin_math  # Use builtin_math instead of math like bultin_math.sqrt(9)
# import math.pi  # XXX Only works when pi is a sub module not a variable or function
import pandas.core.algorithms as algo  # Importing sub modules
from pandas.core import algorithms  # Importing sub modules
from math import sqrt, pi  # Use sqrt and pi directly
from math import pi, sqrt as s  # Use pi directly and sqrt as s
from math import sqrt as s, pi as p  # Use sqrt as s and pi as p

result = builtin_math.sqrt(9) * builtin_math.pi
print(result)

from Asad import welcome, asad  # Importing specific functions and variables
import Asad as As  # Problem: When we import a module, the code in the module gets executed
import math

print(dir(math))  # To see all the functions inside the module
print(math.nan, type(math.nan))

As.welcome()
print(As.asad)
