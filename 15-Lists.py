# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

print(food[0])
food[0] = "sushi"
print(food[0])

food.append("ice cream")  # adds a value to the list
food.remove("hotdog")  # removes a value from the list
food.pop()  # removes the last value
food.insert(0, "cake")  # inserts a value at an index
food.sort()  # sorts alphabetically
# food.clear()  # clears the list, commented out to show other functions

for x in food:
    print(x)
