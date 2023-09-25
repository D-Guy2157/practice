# for loop =    a statement that will execute its block of code a limited amount of times
#
#               while loop = unlimited
#               for loop = limited
import time

for i in range(10):
    print(i+1)  # i+1 since computers start at 0

for i in range(50, 100):  # first number is inclusive, last number is exclusive
    print(i)

for i in "Dylan Harvey":  # prints each letter of string on new line
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
