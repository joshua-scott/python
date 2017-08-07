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
