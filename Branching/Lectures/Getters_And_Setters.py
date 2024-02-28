# ------------------------------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator and Getters & Setters --
# ------------------------------------------------------------------------------


class Member:

    def __init__(self, name):

        self.__name = name

    def say_hello(self):

        return f"Hello {self.__name}"

    def get_name(self):

        return self.__name

    def set_name(self, new_name):

        self.__name = new_name


one = Member("Ahmed")

one._Member__name = "Sayed"
print(one._Member__name)

print(one.get_name())
one.set_name('Abbas')
print(one.get_name())

# -----------------------------------------------------
# -- Object Oriented Programming => @Property Decorator
# -----------------------------------------------------
'''
The @property decorator in Python is used to define getter methods for class attributes. 
It allows you to access an attribute like a regular attribute (using dot notation) while
 actually calling a method behind the scenes to retrieve the attribute's value. 
 This provides a way to encapsulate the attribute and perform additional logic when getting its value.
'''


class Member:

    def __init__(self, name, age):

        self.__name = name

        self.age = age

    def say_hello(self):

        return f"Hello {self.__name}"

    @property
    def age_days(self):

        return self.age * 365


one = Member("Ahmed", 20)
# AttributeError: 'Member' object has no attribute '_Member__name'
print(one.say_hello())
print(one._Member__name)
print(one.age)
print(one.age_days)
