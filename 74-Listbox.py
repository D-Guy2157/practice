# listbox = A lisitng of selectable text items within it's own container

from tkinter import *

def submit():
    food = []

    for index in listbox.curselection():  # iterates once for each item selected
         food.insert(index, listbox.get(index))  # gets index number as well as item at each index number

    print("You have ordered: ")
    for index in food:
        print(index)
    listbox.selection_clear(0, END)

def add():
    if entryBox.get() != "":
        listbox.insert(listbox.size(), entryBox.get())
        listbox.config(height=listbox.size())
        entryBox.delete(0, END)
    else:
        print("You must input something!")

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",  # faded paper ish color
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())  # dynamically changes size of listbox

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()

deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()

window.mainloop()
