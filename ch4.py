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
