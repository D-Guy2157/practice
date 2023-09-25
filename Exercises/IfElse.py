n = int(input("Input a number").strip())
if n % 2 == 1:  # odd
    print("Weird")
elif n % 2 == 0 and 1 < n < 6:  # even and between 2 and 5 inclusive
    print("Not Weird")
elif n % 2 == 0 and 5 < n < 21:  # even and between 6 and 20 inclusive
    print('Weird')
elif n % 2 == 0 and n > 20:  # even and greater than 20
    print("Not Weird")
else:
    print("How did u get here?")
