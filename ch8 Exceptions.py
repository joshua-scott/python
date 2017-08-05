# Task 1
# Basic exception handling

try:
    int(input("Give a number: "))
    print("The input was suitable!")
except Exception:
    print("The input was malformed.")


# Task 2
# Catching various types of errors

try:
    filename = input("Give the file name: ")
    sourcefile = open(filename)
    contents = sourcefile.read()
    sourcefile.close()
    integer = int(contents)
    divided = 1000 / integer
    print("The result was {}".format(divided))
except IOError:
    print("There seems to be no file with that name.")
except ValueError:
    print("The file contents were unsuitable.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except Exception:
    print("There was an unknown error.")


