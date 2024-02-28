# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

a = 0

while a < 15:

  print(a)

  a += 1  # a = a + 1

print("Loop is Done")  # True Become False

while False:

  print("Will Not Print")


# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF))  # List Length [10]

a2 = 0

#while a2 < len(myF):  # a2 < 10
while a2 < 10 :

  print(f"#{str(a2 + 1).zfill(2)} {myF[a2]}") 

  a2 += 1  # a2 = a2 + 1

else:

  print("All Friends Printed To Screen.")

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])