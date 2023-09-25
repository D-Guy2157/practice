from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()
window.config(bg='#111111')

hotImage = PhotoImage(file='fire.png')
hotLabel = Label(image=hotImage)
hotLabel.config(bg='#111111')
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # default is VERTICAL
              font=('Consolas', 20),
              tickinterval=10,  # adds numeric indicators
              # showvalue=False,  # hides current value
              resolution=5,  # increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )
scale.set((scale['from']-scale['to'])/2+scale['to'])
scale.pack()

coldImage = PhotoImage(file='snow.png')
coldLabel = Label(image=coldImage)
coldLabel.config(bg='#111111')
coldLabel.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
