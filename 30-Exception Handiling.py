# exception =   events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:  # as e optional but can be helpful to see the exception
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:  # not good practice to use a broad exception block
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("Done!")  # This will always execute
