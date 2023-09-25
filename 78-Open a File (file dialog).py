from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\ddcoo\\PycharmProjects\\Main\\TestDoc.txt",
                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*"))
                                          )
    # filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())
    file.close()


window = Tk()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()