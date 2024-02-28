# -------------------------------------------------
# -- Advanced_Lessons => __name__ And "__main__" --
# -------------------------------------------------
# if __name__ == "__main__":
# - __name__ => Built In Variable
# - "__main__" => Value Of The __name__ Variable
# Executions Methods
# - Directly => Execute the Python File Using the Command Line.
# - From Import => Import The Code From File To Another File
# -------------------------------------------------------------
# In Some Cases You Want To Know If You Are Using A Module Method As Import
# Or You Use The Original Python File
# -------------------------------------------------------------------------
# In Direct Mode Python Assign A Value "__main__"
# To The Built In Variable __name__ in The Background
# ---------------------------------------------------

import timeit
print(__name__)


# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------


print(timeit.timeit("'Abdelgwad' * 50"))

print("--------------------------------")  # Print Separator Between Results

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print("--------------------------------")

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))


print(dir(timeit))

print(timeit.timeit("'Abdelgwad' * 1000"))

name = "Abdelgwad"

print(name * 1000)

print(timeit.timeit("name = 'Abdelgwad'; name * 1000"))

# print(random.randint(0, 50))

print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))

print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))
