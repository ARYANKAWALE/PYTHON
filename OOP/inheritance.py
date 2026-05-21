class Animal:
# attribute and method of the parent class
    name = ""
    def eat(self):
        print("I can eat")
# inherit from Animal
class Dog(Animal):
    def display(self):
        print("My name is ", self.name)

labrador = Dog()
labrador.name = "Rohu"
labrador.eat()
labrador.display()