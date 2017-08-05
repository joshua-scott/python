# Task 1
# Simple while-loop
numLaps = 5
currentLap = 0

while currentLap < numLaps:
    print("This is lap", currentLap)
    currentLap += 1


# Task 2
# While-loop with ending criteria
while True:
    value = input("Write something: ")
    if value == "quit":
        print("Bye bye!")
        break
    else:
        print(value)


# Task 3
# For-in-range
limit = int(input("Give a number: "))
sum = 0

for i in range(limit):
    sum += i

print("The sum was:", sum)


# Task 4
# Improve the calculator using a while-loop
# It should only exit when the user commands, and have the option to change the inputted numbers

print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit")
    print("Current numbers:", num1, num2)
    selection = int(input("Please select something (1-6): "))

    if selection == 1:
        print("The result is: " + str(num1 + num2))
    elif selection == 2:
        print("The result is: " + str(num1 - num2))
    elif selection == 3:
        print("The result is: " + str(num1 * num2))
    elif selection == 4:
        print("The result is: " + str(num1 / num2))
    elif selection == 5:
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))
    elif selection == 6:
        print("Thank you!")
        break
    else:
        result = "Selection was not correct."
