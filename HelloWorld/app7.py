# LISTS & LIST METHODS

names = ["John", "Bob", "Dylan", "Sam", "Mary"]
names[0] = "Jon"
# print(names[0]) -1 Represents the last element in the list
print(names[0:3])
print(names)


numbers = [1, 2, 3, 4, 5, 25]
numbers.insert(0, -1)
numbers.remove(3)
# numbers.clear()
print(numbers)  # Prints the list
print(10 in numbers)  # Boolean
print(len(numbers))  # Number of elements in the list
