the_file = None
the_tries = 5

while the_tries > 0:
    try:
        print("Enter the file name with absolute path")
        print(f"You have {the_tries} tries left")
        print(
            r"Example: C:\Users\AHMED ABD ELGWAD\OneDrive\المستندات\business-metrics-lesson-terminology-and-formulas.pdf"
        )
        file_name_and_path = input("File Name => : ").strip()

        the_file = open(file_name_and_path, "r")

        print(the_file.read())

        the_file.close()  # Close the file inside the try block

        break

    except FileNotFoundError:
        print("File not found. Make sure the path is valid.")
        print(f"{the_tries} tries left")
        the_tries -= 1

    except:

        print("Error Happen")

    finally:
        if the_file is not None:
            the_file.close()
            print("File closed...")

else:
    print("All Tries Is Finished")
