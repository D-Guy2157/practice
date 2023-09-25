from tkinter import *
from tkinter import colorchooser  # submodule

def click():
    # window.config(bg=colorchooser.askcolor()[1])  # could run all in 1 line of code
    color = colorchooser.askcolor()  # assigns color to var
    print(color)  # prints the full tuple
    colorHex = color[1]  # picks the hex value from the tuple of color
    print(colorHex)  # prints the hex
    print(color[0])  # prints rgb, use [1] for hex
    window.config(bg=colorHex)  # change bg color


window = Tk()
window.geometry("420x420")

button = Button(text='click me', command=click)
button.pack()

window.mainloop()
