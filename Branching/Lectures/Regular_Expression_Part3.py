import re

string_one = re.split(r"\s", "I am Ahmed AbdelJWWad Hussien", 2)

print(string_one)

print("#" * 50)

string_two = re.split(r"-|_", "How-do_you_do-very-nice")

print(string_two)

for counter, string in enumerate(string_two, 1):

    if len(string) == 1:

        continue

    print(f"Word Number: {counter} => {string}")


# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------


string_one = "I Love Python Programming Language"

search_one = re.split(r"\s", string_one, 1)

print(search_one)

print("#" * 50)

string_two = "How-To_Write_A_Very-Good-Article"

search_two = re.split(r"-|_", string_two)

print(search_two)

print("#" * 50)

# Get Words From URL

for counter, word in enumerate(search_two, 1):

    if len(word) == 1:

        continue

    print(f"Word Number: {counter} => {word.lower()}")

print("#" * 50)

my_string = "I Love Python"

print(re.sub(r"\s", "-", my_string, 1))

# my_web = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)","https://www.elzero.org:8080/category.php?article=105?name=how-to-do")

# print(my_web.group(1))
# print(my_web.groups())

# for group in groups:

#    print(group)

print("$" * 50)

# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------


my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

print(search.group())
print(search.groups())

for group in search.groups():

    print(group)

print(f"Protocol: {search.group(1)}")
print(f"Sub Domain: {search.group(2)}")
print(f"Domain Name: {search.group(3)}")
print(f"Top Level Domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query String: {search.group(6)}")
