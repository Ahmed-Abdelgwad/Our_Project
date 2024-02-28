class member:

    def __init__(self, name):

        self.name = name


one = member('ahmed')
print(one)
print(one.name)
one = member('hussien')
print(one.name)
one.name = 'mohamed'
print(one.name)

print("$" * 50)


class member:

    def __init__(self, name):

        self._name = name


one = member('ahmed')
print(one)
print(one._name)

# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------


class Member:

    def __init__(self, name):

        self.name = name  # Public


one = Member("Ahmed")
print(one.name)
one.name = "Sayed"
print(one.name)


class Member:

    def __init__(self, name):

        self._name = name  # Protected


one = Member("Ahmed")
print(one._name)
one._name = "Sayed"
print(one._name)


class Member:

    def __init__(self, name):

        self.__name = name  # Private

    def say_hello(self):

        return f"Hello {self.__name}"


one = Member("Ahmed")
# print(one.__name)
print(one.say_hello())
print(one._Member__name)

print('$' * 50)

# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------


class Member:

    def __init__(self, name):

        self.__name = name  # Private

    def say_hello(self):

        return f"Hello {self.__name}"

    def get_name(self):  # Getter

        return self.__name

    def set_name(self, new_name):

        self.__name = new_name


one = Member("Ahmed")

one._Member__name = "Sayed"
print(one._Member__name)

print(one.get_name())
one.set_name('Abbas')
print(one.get_name())
