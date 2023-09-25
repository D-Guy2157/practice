# for use with 40-OOP.py & 41-Class Variables

class Car:

    wheels = 4  # class variable

    def __init__(self, make, model, year, color):  # constructor
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
