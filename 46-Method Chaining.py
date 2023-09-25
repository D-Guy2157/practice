# method chaining = calling multiple methods sequentially
#                   each class performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

car.turn_on().drive()
print()
car.brake().turn_off()
print()
car.turn_on().drive().brake().turn_off()  # if chaining a lot it can be helpful to hit enter after each method call
#                                           for readability

print()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()  # like this
