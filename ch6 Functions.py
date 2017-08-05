# Task 1
# Simple main() definition and subfunction call:
def main():
    print("Let's call the subfunction:")
    hello()
    print("Quitting.")

def hello():
    print("Hello there!")


# Task 2
# Using parameters

def main():
    poweroftwo(int(input("Give a number: ")))

def poweroftwo(power):
    print("The result is", 2**power)


# Task 3
# Default parameters

def main():
    while True:
        string = input("Write something (quit ends): ")
        if string == "quit": quit()
        elif len(string) < 10: tester()
        else: tester(string)

def tester(givenstring = "Too short"):
    print(givenstring)


# Task 4
# Return values

def main():
    while True:
        string = input("Write something (quit ends): ")
        if string == "quit": 
            quit()
        elif len(string) < 10: 
            tester()
        else: 
            if tester(string):
                print("X spotted!")

def tester(givenstring = "Too short"):
    print(givenstring)
    return "x" in givenstring.lower()


# Call main if this file has been started as a program (comment out unused)
if __name__ == "__main__":
    main()
