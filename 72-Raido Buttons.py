# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh?")


window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
hamburgerImage = PhotoImage(file='hamburger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text to radio buttons
                              variable=x,  # groups radio buttons together if they share the same var
                              value=index,  # assigns each radiobutton a different value
                              padx=25,  # adds padding on x-axis
                              font=("Impact", 50),
                              image=foodImages[index],  # adds image to radiobutton
                              compound='left',  # adds image & text (left side)
                              indicatoron=False,  # eliminate circle indicators
                              width=450,  # sets width of radio buttons
                              command=order,
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
