# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import termcolor
import pyfiglet
import sys
from random import randint, random
import random

print(random)
print(f"Print Random Float Number {random.random()}")

# Show All Functions Inside Module
# print(dir(random))

# Import One Or Two Functions From Module

print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")


# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------


sys.path.append(r"D:\Games")
print(sys.path)

# import elzero
# print(dir(elzero))

# elzero.sayHello("Ahmed")
# elzero.sayHello("Osama")
# elzero.sayHello("Mohamed")

# elzero.sayHowAreYou("Ahmed")
# elzero.sayHowAreYou("Osama")
# elzero.sayHowAreYou("Mohamed")

# Alias

# import elzero as ee

# ee.sayHello("Ahmed")
# ee.sayHello("Osama")
# ee.sayHello("Mohamed")

# ee.sayHowAreYou("Ahmed")
# ee.sayHowAreYou("Osama")
# ee.sayHowAreYou("Mohamed")

# from elzero import sayHello

# sayHello("Osama")

# from elzero import sayHello as ss

# ss("Osama")
# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------
print(dir(pyfiglet))
print(pyfiglet.figlet_format("Elzero"))
print(termcolor.colored("Elzero", color="yellow"))

print(termcolor.colored(pyfiglet.figlet_format("Elzero"), color="yellow"))
