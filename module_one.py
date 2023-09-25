# ***********************************
# if __name__ == '__main__'
# ***********************************

# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__
# Python will assign the __name__ variable a value of '__main__' if it's the initial module being run

# import module_two
print()
print(__name__)  # if this program is the original one being run it sets __name__ = __main__
# print(module_two.__name__)  # if not it is just the name of the file

# if __name__ == '__main__':
#     pass
