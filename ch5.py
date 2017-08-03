# # Task 1
# # Read the entire contents of a file to a variable
# sourcefile = open("facts.txt","r")
# contents = sourcefile.read()            
# print("Following was read from the file:", contents)
# sourcefile.close()


# # Task 2
# # Write some text to a file
# filename = input("Give a file name: ")   # Get file name
# toWrite = input("Write something: ")     # Get input

# openedFile = open(filename, "w")        # Open file
# openedFile.write(toWrite)               # Write the content to the file

# print("Wrote", toWrite, "to the file", filename)

#openedFile.close()


# Task 3
# Read lines from a file "strings.txt"
# Print them back, with a message saying whether the line was alphanumeric or not
sourcefile = open("strings.txt")
content = sourcefile.readlines()

for line in content:
    if line[:-1].isalnum():                 # [:-1] removes the newline character
        print(line[:-1], "was ok.")
    else:
        print(line[:-1], "was invalid.")

sourcefile.close()


# Task 4
# Create a program which allows the user to 
# (1) Read the contents of the notebook (notebook.txt)
# (2) Add notes to the file or
# (3) Delete all of the notes. 