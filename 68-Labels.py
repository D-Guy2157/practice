from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file="walter.png")

label = Label(window,
              text="Walter.",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,  #
              compound='bottom')  # places image below text
label.pack()  # places in top middle
# label.place(x=0, y=0)  # places in top left at x=0, y=0 (can be any coordinates)

window.mainloop()
