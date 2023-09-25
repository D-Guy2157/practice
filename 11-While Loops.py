# while loop = a statement that will execute its block of code, as long as it's condition remains true

# INFINITE LOOP
while 1 == 1:
    print("Help! I'm stuck in a loop!")

first_name = ""

while len(first_name) == 0:
    first_name = input("Enter your first name: ")

print("Hello " + first_name)

# Another way:
last_name = None

while not last_name:
    last_name = input("Enter your last name: ")

print("Hello " + first_name + " " + last_name)
