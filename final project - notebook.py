import pickle
import time

DEFAULT_FILENAME = "notebook.dat"

def main():
    init()

def init():
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
    try:
        with open(filename, "rb") as source:
            return pickle.load(source)
    except Exception:
        with open(filename, "wb") as newfile:
            pickle.dump([], newfile)
            print("\nNo default notebook was found, created one.")
            return []

def getInt():
    while True:
        try:
            return int(input("Please select one: "))
        except Exception:
            print("Input must be an integer.")

def read(notebook):
    for i in notebook: print(i)

def add(notebook):
    newNote = input("Write a new note: ")
    notebook.append(formatNote(newNote))

def edit(notebook):
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
    print("The list has {} notes.".format(len(notebook)))
    try:
        index = int(input("Which of them will be deleted?: "))
        deleted = notebook.pop(index)
        print("Deleted note " + deleted)
    except Exception:
        print("Invalid index entered.")
        return

def formatNote(newNote):
    return newNote.ljust(30) + "::: " + time.strftime("%X %x")

def saveAndQuit(notebook, filename):
    with open(filename, "wb") as f:
            pickle.dump(notebook, f)
    print("Notebook shutting down, thank you.")
    quit()

if __name__ == "__main__":
    main()
