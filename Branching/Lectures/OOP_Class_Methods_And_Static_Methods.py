class Member:

    not_allowed_names = ["Hell", "Shit", "Baloot"]

    users_num = 0

    @classmethod
    def show_user_num(cls):

        print(f"We have {cls.users_num} Users in our systemcc")

    @staticmethod
    def show_user_num():
        print(f"We have {Member.users_num} Users in our systemcc")

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender

        Member.users_num += 1  # Member.users_num = Member.users_num + 1

    @staticmethod
    def say_hello():
        print("Hello Man")

    def full_name(self):

        if self.fname in Member.not_allowed_names:

            raise ValueError("Name Not Allowed")

        else:

            return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self):

        if self.gender == "Male":

            return f"Hello Mr {self.fname}"

        elif self.gender == "Female":

            return f"Hello Miss {self.fname}"

        else:

            return f"Hello {self.fname}"

    def get_all_info(self):

        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

    def delete_user(self):

        Member.users_num -= 1  # Member.users_num = Member.users_num -1

        return f"User {self.fname} Is Deleted."


print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

print(Member.users_num)

print(member_four.delete_user())

print(Member.users_num)

print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)

print(member_two.full_name())
print(member_two.name_with_title())

# print(member_three.get_all_info())
Member.show_user_num()
# print(dir(Member))
print("$" * 50)
print(member_one.full_name())
print(Member.full_name(member_one))

print(member_one.get_all_info())


Member.show_user_num()
Member.say_hello()
