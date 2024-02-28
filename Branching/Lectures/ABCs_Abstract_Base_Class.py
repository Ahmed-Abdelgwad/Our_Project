# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------


from abc import ABCMeta, abstractmethod


class Programming(metaclass=ABCMeta):

    """Abstract class for programming languages."""
    @abstractmethod
    def had_oop(self):
        """Returns True if the language has OOP features."""
        # pass
        return "Yes"


class PythonProgramming(Programming):

    def had_oop(self):
        """Returns True if the language has OOP features."""
        return "Yes"


class pascal(Programming):

    def had_oop(self):
        """Returns True if the language has OOP features."""
        return "No"

    def get_name(self):
        return "Pascal"


one = pascal()
print(one.get_name())
