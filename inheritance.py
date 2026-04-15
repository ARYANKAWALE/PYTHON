class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some generic sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
my_pet = Dog("Buddy")
print(f"{my_pet.name} says {my_pet.speak()}")