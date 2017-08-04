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
