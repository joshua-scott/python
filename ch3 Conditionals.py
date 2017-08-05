# Task 1
# Basic if-statement
number = int(input("Give a number: "))
if number % 2 == 0:
    print("The given number was even.")


# Task 2
# Nested if-else statements to verify username/password input
if input("Give name: ") == "John":
    if input("Give password: ") == "ABC123":
        print("Both inputs are correct!")
    else:
        print("The password is incorrect.")
else:
    print("The given name is wrong.")


# Task 3
# Basic if-elif
number = int(input("Select a number (1-3): "))
output = "You selected "

if number == 1: output += "one."
elif number == 2: output += "two."
elif number == 3: output += "three."

print(output)


# Task 4
# If-statement with multiple parameters
num1 = int(input("Give a number: "))
num2 = int(input("Give another number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 == 1 and num2 % 2 == 1:
    print("Both numbers are odd.")
else:
    print("One of the numbers is even.")


# Task 5
# Improve the calculator so the user chooses the type of calculation

print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

print("(1) +\n(2) -\n(3) *\n(4) /")
selection = int(input("Please select something (1-4): "))
result = "The result is: "

if selection == 1:
    result += str(num1 + num2)
elif selection == 2:
    result += str(num1 - num2)
elif selection == 3:
    result += str(num1 * num2)
elif selection == 4:
    result += str(num1 / num2)
else:
    result = "Selection was not correct."

print(result)
