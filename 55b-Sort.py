# sort() method     = used with lists
# sort() function   = used with iterables

# List of tuples:
students = [("Squidward", "D", 60),
            ("Sandy", "A", 33),
            ("Patrick", "F", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

# no lambda for name since 0 is default
grade = lambda grades: grades[1]  # this is the func used, input is the index
age = lambda ages: ages[2]  # age
students.sort(key=age)  # key=func, reverse=True for reverse

for i in students:
    print(i)

print()
# Tuple of tuples:
studentsT = (("Squidward", "D", 60),
            ("Sandy", "A", 33),
            ("Patrick", "F", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

# using lambdas declared above
sorted_students = sorted(studentsT, key=age)  # can be used with lists to make a new sorted list
for i in sorted_students:
    print(i)
