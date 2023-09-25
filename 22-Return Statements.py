# return statement = Functions send python values/objects back to the caller.
#                    These values/objects are known as the functions return value

def multiply(number1, number2):
    # result = number1 * number2  # unnecessary
    # return result
    return number1 * number2


x = multiply(6, 8)

print(x)
