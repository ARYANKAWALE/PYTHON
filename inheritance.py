# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return "Some generic sound"
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
# my_pet = Dog("Buddy")
# print(f"{my_pet.name} says {my_pet.speak()}")


class Car:
    name = ""
    def model(self):
        print("Supra")

class mini(Car):
    def display(self):
        print("this car is", self.name )


vehicle = mini()
vehicle.name = "toyota"
vehicle.display()
vehicle.model()