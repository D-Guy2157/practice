
# with open('C:\\Users\\ddcoo\\Desktop\\test.txt') as file:  if the file wasn't in the project folder you need the path
try:
    with open('test.txt') as file:
        print(file.read())
        print(file.closed)  # prints the value of whether the file is open, they are automatically closed
except FileNotFoundError:
    print("That file was not found :(")
