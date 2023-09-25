# sort() method     = used with lists
# sort() function   = used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
studentsT = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
students.sort(reverse=True)  # reverse=True; reverse alphabetical order
sorted_students = sorted(studentsT, reverse=True)

for i in students:
    print(i)

print()
for i in sorted_students:
    print(i)
