# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments

# def add(num1,num2):
    # sum = num1 + num2
    # return sum

def add(*stuff):  # you can use anything after the * but args is commonplace
    sum = 0
    stuff = list(stuff)  # Changes the tuple to a list
    stuff[0] = 0  # Changes 1 to 0
    for i in stuff:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))
