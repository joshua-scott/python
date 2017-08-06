# Task 1
# Basic lists
# myList = [ "Blue", "Red", "Yellow", "Green" ]
# print("The first item in the list is:", myList[0])
# print("The entire list printed one at a time:")
# for i in myList: print(i)


# Task 2
# Use lists to allow the user to: 
# (1) add products, (2) remove items and (3) print the list and quit.
def main():
    shoppingList = []

    while True:
        selection = getSelection()

        if selection == 1:
            addItem(shoppingList)
        elif selection == 2:
            removeItem(shoppingList)
        elif selection == 3:
            gracefulExit(shoppingList)
        else:
            print("Incorrect selection.")

def getSelection():
    return int(input("""
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: """))

def addItem(list):
    newItem = input("What will be added?: ")
    list.append(newItem)

def removeItem(list):
    print("There are {} items in the list.".format(len(list)))
    deleteIndex = int(input("Which item is deleted?: "))
    try: 
        list.pop(deleteIndex)
    except Exception:
        print("Incorrect selection.")

def gracefulExit(list):
    print("The following items remain in the list: ")
    for i in list: print(i)
    quit()

if __name__ == "__main__":
    main()
