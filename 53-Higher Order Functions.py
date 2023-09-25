# Higher Order Function = a function that either:
#                         1. accepts a function as an argument
#                             or
#                         2. returns a function
#                         (In python, functions are also treated as objects)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)


# returns a function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)  # returns dividend and assigns it to this var
print(divide(10))  # calls dividend and inputs 10
# divide here has a mem value
