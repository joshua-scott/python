# Task 1
# Import random module to simulate a coin flip
# from random import randint
# print("Heads!") if randint(0,1) == 1 else print("Tails!")


# Task 2
# Rock/paper/scissors
# from random import randint

# rounds = 0
# score = 0
# ties = 0

# def main():
#     while True:
#         init()

# def init():
#     entry = input("Rock, Paper, or Scissors? (Quit ends): ").lower()

#     if entry == "quit":
#         print("You played {} rounds, and won {} rounds, playing tie in {} rounds.".format(rounds, score, ties))
#         quit()
#     elif entry in ["rock", "paper", "scissors"]:
#         play(entry)
#     else:
#         print("Invalid selection.")

# def play(p1):
#     global rounds, score, ties
    
#     cpu = cpuChoice()
    
#     result = decideOutcome(p1, cpu)
#     rounds += 1

#     if result == "win": score += 1
#     elif result == "tie": ties += 1

#     printResults(p1, cpu, result)

# def cpuChoice():
#     choices = ["rock", "paper", "scissors"]
#     return choices[randint(0,2)]

# def decideOutcome(p1, cpu):
#     if p1 == cpu: 
#         return "tie"
#     elif (p1 == "rock" and cpu == "scissors") or (p1 == "paper" and cpu == "rock") or (p1 == "scissors" and cpu == "paper"):
#         return "win"
#     else:
#         return "lose"

# def printResults(p1, cpu, result):
#     print("You chose:", p1)
#     print("Computer chose:", cpu)
#     if result == "tie":
#         print("Both LOSE!")
#     else:
#         print("You", result.upper())

# if __name__ == "__main__": main()


# Task 3
# Create own basic module (though it's really just a function as it's not in a separate file)
# def printme(toPrint):
#     print("I got: {}".format(toPrint))
#     print("The parameter was {} characters long.".format(len(toPrint)))


# Task 4
# Another module that's really just a function
# def testme(pw):
#     if len(pw) < 6 or pw.isalpha() or pw.isnumeric(): return False
#     else: return True


# Task 5
# Improve the calculator by adding sin and cos functions from the math module

# import math

# def main():
#     init()

# def init():
#     print("Calculator")
#     num1 = int(input("Give the first number: "))
#     num2 = int(input("Give the second number: "))

#     while True:
#         print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)(7)Change numbers\n(8)Quit")
#         print("Current numbers:", num1, num2)
#         selection = int(input("Please select something (1-6): "))

#         if selection == 1:
#             print("The result is: " + str(num1 + num2))
#         elif selection == 2:
#             print("The result is: " + str(num1 - num2))
#         elif selection == 3:
#             print("The result is: " + str(num1 * num2))
#         elif selection == 4:
#             print("The result is: " + str(num1 / num2))
#         elif selection == 5:
#             print("The result is: " + str(math.sin(num1 / num2)))
#         elif selection == 6:
#             print("The result is: " + str(math.cos(num1 / num2)))
#         elif selection == 7:
#             num1 = int(input("Give the first number: "))
#             num2 = int(input("Give the second number: "))
#         elif selection == 8:
#             print("Thank you!")
#             break
#         else:
#             result = "Selection was not correct."

# if __name__ == "__main__":
#     main()
