from tkinter import *  # instead of import tkinter so you don't have to call it as a function

# widgets = GUI elements: buttons, textbooks, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("First GUI")

icon = PhotoImage(file='walter.png')
window.iconphoto(True, icon)
window.config(background="#5cfcff")  # can use hex values, or words like 'Black'

window.mainloop()  # place window on screen, listen for events
