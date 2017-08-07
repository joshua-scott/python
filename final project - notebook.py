# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#   This is the final project of the introductory Python course.    #
#   It demonstrates the ability to use the fundamentals of Python   #
#   to create a console-based simple notebook application.          #
#   The application has the ability to read, add, edit, and delete  #
#   notes, which are stored in a list. On exit, the list of notes   #
#   is serialized to a file using the Pickle module.                #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pickle
import time

DEFAULT_FILENAME = "notebook.dat"

def main():
    init()

def init():
    """The main logic of the program is contained here. Loops until user quits."""
    notebook = setNotebook(DEFAULT_FILENAME)

    while True:
        displayOptions()
        selection = getInt()
        if selection == 1:   read(notebook)
        elif selection == 2: add(notebook)
        elif selection == 3: edit(notebook)
        elif selection == 4: delete(notebook)
        elif selection == 5: saveAndQuit(notebook, DEFAULT_FILENAME)

def displayOptions():
    print( 
    """
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit\n""")

def setNotebook(filename):
    """Reads the file using Pickle, and returns the data. Creates a file if it doesn't exist (and returns empty list)."""
    try:
        with open(filename, "rb") as source:
            return pickle.load(source)
    except Exception:
        with open(filename, "wb") as newfile:
            pickle.dump([], newfile)
            print("\nNo default notebook was found, created one.")
            return []

def getInt():
    """Prompts the user to input an int, and returns it. Loops until user gives acceptable input."""
    while True:
        try:
            return int(input("Please select one: "))
        except Exception:
            print("Input must be an integer.")

def read(notebook):
    """Prints each note, one per line."""
    for i in notebook: print(i)

def add(notebook):
    """Gets input and appends it to the notebook. Calls formatNote() to add spacing and date."""
    newNote = input("Write a new note: ")
    notebook.append(formatNote(newNote))

def edit(notebook):
    """Allows user to edit a note (chosen by index)."""
    print("The list has {} notes.".format(len(notebook)))
    try:
        index = int(input("Which of them will be changed?: "))
        print(notebook[index])
    except Exception:
        print("Invalid index entered.")
        return
    newNote = input("Give the new note: ")
    notebook[index] = formatNote(newNote)

def delete(notebook):
    """Allows user to delete a note (chosen by index)."""
    print("The list has {} notes.".format(len(notebook)))
    try:
        index = int(input("Which of them will be deleted?: "))
        deleted = notebook.pop(index)
        print("Deleted note " + deleted)
    except Exception:
        print("Invalid index entered.")
        return

def formatNote(newNote):
    """Pads the given note to 30 chars (for neat printing), adds a visual separator, and the current time."""
    return newNote.ljust(30) + "::: " + time.strftime("%X %x")  # Pad the note so they're always printed neatly to the terminal

def saveAndQuit(notebook, filename):
    """Uses Pickle to serialize the data to the given file, then quits."""
    with open(filename, "wb") as f:
            pickle.dump(notebook, f)
    print("Notebook shutting down, thank you.")
    quit()

if __name__ == "__main__":
    main()
