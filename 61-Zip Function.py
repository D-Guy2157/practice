# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dylan", "Dude", "guest"]
passwords = ("p@assword", "abc123", "guest")
login_date = ["1/1/2022", "1/2/2022", "1/3/2022"]

users = dict(zip(usernames, passwords))  # combines 2 lists into a zip obj, default is tuples, this is dict
print(type(users))

for key, value in users.items():
    print(key+" : " + value)

# for i in users:
#     print(i)
print()  # -------------------------------------
users2 = zip(usernames, passwords, login_date)  # combines 3 lists into a zip object (tuples is default)
print(type(users2))

for i in users2:
    print(i)
