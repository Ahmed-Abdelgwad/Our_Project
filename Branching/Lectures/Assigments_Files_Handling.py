import os

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))

python_folder = r"C:\AI\pythonProject1"

assign_file = os.path.join(python_folder, "assign.py")

for i in range(1, 51):
    txt_file = os.path.join(python_folder, f"txt{i}.txt")
    with open(txt_file, "w") as myfile:
        if i == 25:
            myfile.write("")
        else:
            myfile.write(f"Elzero Web School => {i}\n")
            myfile.write("Appended => Elzero Web " * 50 + "\n")

os.system(f"start notepad {assign_file}")

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))

myfile = open(r"C:\AI\pythonProject1\txt1.txt", "a")
myfile.write("Elzero Web School => 1\n")
myfile.write("Appended => Elzero Web School\n" * 50)
myfile.close()  # Close the file after writing

myfile = open(r"C:\AI\pythonProject1\txt1.txt", "r")
print(myfile.name)
print(myfile.readlines())
# myfile.close()  # Close the file after reading

# Reopen the file to truncate it
myfile = open(r"C:\AI\pythonProject1\txt1.txt", "a")
myfile.truncate()

# Reset the cursor to the beginning of the file
myfile.seek(0)

# Delete the last ten txt files
for i in range(41, 51):
    txt_to_delete = os.path.join(python_folder, f"txt{i}.txt")
    os.remove(txt_to_delete)