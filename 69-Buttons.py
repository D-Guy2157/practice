from tkinter import *

# button = you click it, then it does stuff
count = 0


def click():
    global count
    count += 1
    if count == 1:
        print("You clicked walter", count, "time!")
    else:
        print("You clicked walter", count, "times!")


window = Tk()
window.title("Walter Clicker")
photo = PhotoImage(file='walter.png')
icon = photo
window.iconphoto(True, icon)
button = Button(window,
                text="Click walter!",
                command=click,
                font=("Comic Sans", 30),  # cry about it
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()
