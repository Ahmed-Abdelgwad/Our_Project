# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

#myFile = open("D:\Python\Files\osama.txt", "w")
myFile = open(r"C:\AI\PYTHON\nfile\hussien.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"C:\AI\PYTHON\nfile\hussien.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open(r"C:\AI\PYTHON\nfile\hussien.txt", "w")
myFile.writelines(myList)

myFile = open(r"C:\AI\PYTHON\nfile\hussien.txt", "w")
myFile.write("Elzero")


# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open(r"C:\AI\PYTHON\nfile\hussien.txt", "a")
myFile.truncate(5)

myFile = open(r"C:\AI\PYTHON\nfile\hussien.txt", "a")
print(myFile.tell())

myFile = open(r"C:\AI\PYTHON\nfile\hussien.txt", "a")
myFile.seek(11)
print(myFile.read())

os.remove(r"C:\AI\PYTHON\nfile\hussien.txt")