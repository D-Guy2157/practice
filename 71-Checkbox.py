from tkinter import *

def display():
    if(x.get()==1):  # changes based on var type
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar()
# x = BooleanVar()
# x = StringVar()

walter_photo = PhotoImage(file='walter.png')

check_button = Checkbutton(window,
                           text="Agree to walter",
                           variable=x,
                           onvalue=1,  # 1 is default on
                           offvalue=0,  # 0 is default off
                           command=display,
                           font=('Arial', 20),
                           fg="#00FF00",
                           bg="Black",
                           activeforeground="#00FF00",
                           activebackground="Black",
                           padx=25,
                           pady=10,
                           image=walter_photo,
                           compound='left')
check_button.pack()

window.mainloop()
