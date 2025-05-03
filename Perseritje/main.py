class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hi, im {self.name}")

p1 = Person("Drin")
p1.greet()

class Rectangle:
    def __init__(self,length:int,width:int):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)

values = Rectangle(10,5)
values.area()

class Pet:
    def __init__(self,name,age,species,breed,color):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.color = color
    def make_sound(self):
        if(self.species == "dog"):
            print("Woof woof")
        elif(self.species == "cat"):
            print("Meow")
        else: print(f"Its a {species}")

    def sleep(self):
        print(f"{self.name} is sleeping")
    def eat(self):
        print(f"{self.name} is eating")

info = Pet("Riki",3,"dog","doberman","black")
info.make_sound()
info.sleep()
info.eat()
