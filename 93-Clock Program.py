from tkinter import *
from time import *
# %H 24hrs, %I 12hrs
def update():
    time_string = strftime("%I:%M:%S %p")  # 12hrs, minutes, seconds, am/pm
    time_label.config(text=time_string)

    day_string = strftime("%A")  # Day
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")  # Name of month, day of month, year
    date_label.config(text=date_string)

    time_label.after(1000, update)  # 1000ms


window = Tk()
window.title("Clock :)")
window.config(bg="light yellow")

clock_image = PhotoImage(file='icon.png')
window.iconphoto(True, clock_image)

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25), fg="black", bg="light yellow")
day_label.pack()

date_label = Label(window, font=("Ink Free", 30), fg="black", bg="light yellow")
date_label.pack()

update()

window.mainloop()
