# --------------------
# -- Debugging Code --
# --------------------


my_list = [1, 2, 3, 4, 5, 6]

my_dict = {"Name": "Ahmed", "Age": "20", "Country": "Egypt"}

for num in my_list:
    print(num)

for key, value in my_dict.items():
    print(f"{key} => {value}")


def funs_number():

    print("Helloo Everybody!!!!")


funs_number()

# ------------------
# -- Type Hinting --
# ------------------
# Only Type


def say_hello(name) -> str:

    print(f"Hello {name}")


say_hello("Ahmed")


def calculate(n1, n2) -> str:

    print(n1 + n2)


calculate(10, 40)
