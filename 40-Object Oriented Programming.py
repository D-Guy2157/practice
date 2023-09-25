from car import Car

# class Car:  # you can do it in file too but importing is helpful for large projects
#     pass

car_1 = Car("Toyota", "Yaris", 2019, "silver")
car_2 = Car("Kia", "Sportage", 2017, "white")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

print()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()
