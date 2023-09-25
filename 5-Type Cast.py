# type casting = convert the data type of a value to another data type

x = 1   # int
y = 2.0 # float
z = "3" # str

x = str(x)  # Permanent change to str
y = int(y)  # Permanent change to int
z = str(z)

print("X is " + x)
print(float(y))  # float(y) in the print function is non-permanent
print(z*3)  # if this was str it prints 3 3 times but if typecast to int it prints 3*3 (aka 9)

print(type(x))
print(type(y))
print(type(z))
