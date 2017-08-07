# Task 1:
# Basic class and object creation
class Player:
    """Class for player."""
    teamColour = "White"
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

