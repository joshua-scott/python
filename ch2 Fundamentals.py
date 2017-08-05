# Task 1
# Create a str variable and print it
myString = "Our variable has a value which is string-type content. Isn't that nice?"
print(myString)


# Task 2
# Basics of calculation
number1 = 1000
number2 = 24
result = (number1 + number2 + 15)**2
print("The final results of the calculation was:", result)


# Task 3
# Type conversion
floaty = 10.6411
stringy = "Stringline!"

floaty = int(floaty)
stringy *= 2

output = "Integer conversion cannot do roundings: " + str(floaty)
output += "\nMultiplying strings also causes trouble: " + stringy

print(output)


# Task 4
# Using layout characters
print("This here is divided to several lines:\n\
I am still in the same print-command.\n\
\tName:\tPeter\n\
\tJob:\tBabysitter")


# Task 5
# Taking and converting input
print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
print("The result is:", (str(num1 + num2)))


# Task 6
# Slicing strings
food = "desserts"
a = food[:4]
b = food[-4:]
c = food[::-1]

print("The first 4 characters were:", a)
print("The last 4 characters were:", b)
print("The string backwards was:", c)
