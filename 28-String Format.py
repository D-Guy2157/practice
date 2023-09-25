
# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))  # positional argument (uses index)
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))
print()

name = "Dylan"

print("Hello, my name is {}".format(name))
print("Hello, my name is {name:10}. Nice to meet you".format(name="Dylan"))  # keyword
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # left align (also default)
print("Hello, my name is {:>10}. Nice to meet you".format(name))  # right align
print("Hello, my name is {:^10}. Nice to meet you".format(name))  # center align
print()

number = 3.14159
number2 = 1000

print("The number pi is {}".format(number))
print("The number pi is {:.2f}".format(number))  # rounds to 2 places
print("The number is {:,}".format(number2))  # commas
print("The number is {:b}".format(number2))  # binary
print("The number is {:o}".format(number2))  # oct
print("The number is {:x}".format(number2))  # hex, capitals
print("The number is {:e}".format(number2))  # scientific, capitals
