
# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "dylan harvey!"

if(name[0].islower()):  # redundant parenthesis
    name = name.capitalize()

first_name = name[:5].upper()  # 0 is assumed
last_name = name[6:].upper()  # end is assumed
last_character = name[-1]  # -1 is last char

print(first_name)
print(last_name)
print(last_character)
