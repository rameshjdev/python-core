class Animal:
    def eat(self):
        print("The Abstract Animal is Eating")

class Dog(Animal):
    def bark(self):
        print("The Dog is Barking")

d = Dog()
d.eat()
d.bark()