# THE RANGE() FUNCTION

# range(a, b, c) - a=beginning number, b=end number(not inclusive), c=step
numbers = range(5, 10, 2)  # Don't necessarily need to store the result in a separate variable
for number in numbers:  # Could use range(_) for example after 'in' instead of the var numbers
    print(number)
