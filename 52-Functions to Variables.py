def hello():
    print("Hello")


hello()  # runs hello function
print(hello)  # prints mem address in hex
print()

hi = hello  # now, the hello function essentially has 2 names
hi()  # also runs hello(hi) function
print()

say = print  # assigns the print function to a variable
say("Wow I can't believe this works! :O")
