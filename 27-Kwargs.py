# **kwargs =    parameter that wll pack all arguments into a dictionary
#               useful so that a function can accept a varying amount of keyword arguments

# def hello(first, last):
    # print("Hello " + first + " " + last)
def hello(**kwargs):  # kwargs can be named anything after the **
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Dylan", middle="Mitchell", last="Harvey")
