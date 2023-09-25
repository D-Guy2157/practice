from tkinter import *

# grid() = geometry manager that organizes widgets in a table-like structure in a parent

def submit():
    firstName = firstNameEntry.get()
    print(firstName)
    lastName = lastNameEntry.get()
    print(lastName)
    email = emailEntry.get()
    print(email)


window = Tk()

Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)  # title label

Label(window, text="First name: ").grid(row=1, column=0)  # first name label
firstNameEntry = Entry(window)
firstNameEntry.grid(row=1, column=1)

Label(window, text="Last name: ").grid(row=2, column=0)  # last name label
lastNameEntry = Entry(window)
lastNameEntry.grid(row=2, column=1)

Label(window, text="Email: ").grid(row=3, column=0)  # email label
emailEntry = Entry(window)
emailEntry.grid(row=3, column=1)

Button(window, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)  # submit button

window.mainloop()
