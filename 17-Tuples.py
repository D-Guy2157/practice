# tuple =   collection which is ordered and unchangeable
#           used to group together related data

student = ("Dylan", 17, "male")

print(student.count("Dylan"))
print(student.index("male"))

for x in student:
    print(x)

if "Dylan" in student:
    print("Dylan is here!")
