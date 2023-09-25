# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit" or food == "QUIT" or food == "Quit":
        break
    foods.append(food)
print(foods)

# foods2 = list()
# while food2 := input("What food do you like?: ") != "quit":
#     foods2.append(food2)
# print(str(foods2))
# this doesn't work for some reason I really don't know
