# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Dylan Harvey"

first_name = name[0:5]  # start index is inclusive, stopping index is exclusive
last_name = name[6:12]  # leave start blank to assume 0, leave stop blank to assume end of string
every_other_letter = name[::2]  # step of 2 skips every other letter
reversed_name = name[::-1]  # step of -1 reverses the string

print(first_name)
print(last_name)
print(every_other_letter)
print(reversed_name)

website1 = "https://www.google.com"
website2 = "https://www.youtube.com"

slice_url = slice(12,-4)  # may vary

print(website1[slice_url])
print(website2[slice_url])
