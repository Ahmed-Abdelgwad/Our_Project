# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------

from time import time


def myDecorator(func):  # Decorator

    def nestedFunc():  # Any Name Its Just For Decoration

        print("Before")  # Message From Decorator

        func()  # Execute Function

        print("After")  # Message From Decorator

    return nestedFunc  # Return All Data


@myDecorator
def sayHello():

    print("Hello From Say Hello Function")


@myDecorator
def sayHowAreYou():

    print("Hello From Say How Are You Function")


afterDecoration = myDecorator(sayHello)

afterDecoration()

sayHello()

print("#" * 50)

sayHowAreYou()


# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def myDecorator(func):  # Decorator

    def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

        if num1 < 0 or num2 < 0:

            print("Beware One Of The Numbers Is Less Than Zero")

        func(num1, num2)  # Execute Function

    return nestedFunc  # Return All Data


def myDecoratorTwo(func):  # Decorator

    def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

        print("Coming From Decorator Two")

        func(num1, num2)  # Execute Function

    return nestedFunc  # Return All Data


@myDecorator
@myDecoratorTwo
def calculate(n1, n2):

    print(n1 + n2)


calculate(-5, 90)


print("$" * 50)

# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------


def myDecorator(func):  # Decorator

    def nestedFunc(*numbers):  # Any Name Its Just For Decoration

        for number in numbers:

            if number < 0:

                print("Beware One Of The Numbers Is Less Than Zero")

        func(*numbers)  # Execute Function

    return nestedFunc  # Return All Data


@myDecorator
def calculate(n1, n2, n3, n4):

    print(n1 + n2 + n3 + n4)


calculate(-5, 90, 50, 150)


def speedTest(func):

    def wrapper():

        start = time()

        func()

        end = time()

        print(f"Function Running Time Is: {end - start}")

    return wrapper


@speedTest
def bigLoop():

    for number in range(1, 200):

        print(number)


bigLoop()
