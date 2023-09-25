x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k != n])
# prints 3 values in a 2d list, each range starts at 0 and ends at input
# if at the end makes sure that the 3 values do not add to n
