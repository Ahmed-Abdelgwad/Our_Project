"""
This is My Module
To Create Function
To Say Hello
"""


def say_hello(name):
    """This Function Only Say Hello To Someone"""
    msg = "Hello"
    return f"{msg} {name}"


say_hello("Ahmed")


myFriends = ["Ahmed", "Osama", "Sayed"]


def say_heello(peoples):
    """This Function Only Say Hello To Someone"""
    for someone in peoples:
        print(f"Hello {someone}")


say_heello(myFriends)
