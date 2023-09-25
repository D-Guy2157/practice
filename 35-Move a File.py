import os

source = input("Input name/directory of file: ")
destination = input("Input destination directory of file: ")
# source = "moveTest.txt"
# destination = "C:\\Users\\ddcoo\\Desktop\\moveTest.txt"

try:
    if os.path.exists(destination):  # used to check if a duplicate file already exists
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")
