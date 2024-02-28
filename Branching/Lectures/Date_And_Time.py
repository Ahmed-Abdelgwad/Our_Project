# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date and Time
print(datetime.datetime.now())

print("#" * 40)

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

# print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("#" * 40)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("#" * 40)

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("#" * 40)

# Print Specific Date
print(datetime.datetime(1982, 10, 25))
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

print("#" * 40)

myBirthDay = datetime.datetime(1982, 10, 25)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")


# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------


myBirthday = datetime.datetime(1982, 10, 25)

print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))

"""
%a	Sun	Weekday as locale’s abbreviated name.
%A	Sunday	Weekday as locale’s full name.
%w	0	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d	08	Day of the month as a zero-padded decimal number.
%-d	8	Day of the month as a decimal number. (Platform specific)
%b	Sep	Month as locale’s abbreviated name.
%B	September	Month as locale’s full name.
%m	09	Month as a zero-padded decimal number.
%-m	9	Month as a decimal number. (Platform specific)
%y	13	Year without century as a zero-padded decimal number.
%Y	2013	Year with century as a decimal number.
%H	07	Hour (24-hour clock) as a zero-padded decimal number.
%-H	7	Hour (24-hour clock) as a decimal number. (Platform specific)
%I	07	Hour (12-hour clock) as a zero-padded decimal number.
%-I	7	Hour (12-hour clock) as a decimal number. (Platform specific)
%p	AM	Locale’s equivalent of either AM or PM.
%M	06	Minute as a zero-padded decimal number.
%-M	6	Minute as a decimal number. (Platform specific)
%S	05	Second as a zero-padded decimal number.
%-S	5	Second as a decimal number. (Platform specific)
%f	000000	Microsecond as a decimal number, zero-padded to 6 digits.
%z	+0000	UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
%Z	UTC	Time zone name (empty string if the object is naive).
%j	251	Day of the year as a zero-padded decimal number.
%-j	251	Day of the year as a decimal number. (Platform specific)
%U	36	Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
%-U	36	Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific)
%W	35	Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
%-W	35	Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific)
%c	Sun Sep 8 07:06:05 2013	Locale’s appropriate date and time representation.
%x	09/08/13	Locale’s appropriate date representation.
%X	07:06:05	Locale’s appropriate time representation.
%%	%	A literal '%' character.
"""
