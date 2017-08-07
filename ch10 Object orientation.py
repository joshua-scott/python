# Task 1:
# Basic class and object creation
class Player:
    """Class for player."""
    teamColour = "___"
    points = 0
    def printData(self):
        print("The {} contender has {} points!".format(self.teamColour, self.points))

def main():
    justJoined = Player()
    justJoined.teamColour = "Blue"
    justJoined.points = 300
    justJoined.printData()

if __name__ == "__main__":
    main()

# Task 2
# Assigning a private attribute to a class

class Player:
    """Class for player."""
    teamColour = "___"
    __points = 0
    def tellScore(self):
        print("I am {}, we have {} points!".format(self.teamColour, self.__points))
    def goal(self):
        self.__points += 1

def main():
    bookiesFavourite = Player()
    bookiesFavourite.teamColour = "Blue"
    bookiesFavourite.goal()
    bookiesFavourite.tellScore()

if __name__ == "__main__":
    main()


# Task 3
# Initialising an object's attributes using __init__

class Player:
    """Player-class: stores data on team colours and points."""
    __points = 0
    def __init__(self):
        self.__teamColour = input("What colour do I get?: ")
    def tellScore(self):
        print("I am {}, we have {} points!".format(self.__teamColour, self.__points))
    def goal(self):
        self.__points += 1

def main():
    teamOne = Player()
    teamTwo = Player()
    teamOne.goal()
    teamOne.goal()
    teamTwo.goal()
    teamOne.tellScore()     # Prints "I am Blue, we have 2 points!"
    teamTwo.tellScore()     # Prints "I am Red, we have 1 points!"

if __name__ == "__main__":
    main()
