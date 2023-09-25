# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup",}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)  # adds the elements from dishes to utensils
dinner_table = utensils.union(dishes)  # combines the elements in each set into a new set

print(utensils.difference(dishes))  # what utensils contains but dishes lacks
print(dishes.difference(utensils))
print(utensils.intersection(dishes))  # what they have in common

for x in dinner_table:
    print(x)
