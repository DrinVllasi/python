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
        else: print(f"Its a {self.species}")

    def sleep(self):
        print(f"{self.name} is sleeping")
    def eat(self):
        print(f"{self.name} is eating")

info = Pet("Riki",3,"dog","doberman","black")
info.make_sound()
info.sleep()
info.eat()

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

infos = Student("Jimmy", 15)
print(infos.get_name())
print(infos.get_age())

infos.set_name("John")
print(infos.get_name())

infos.set_age(18)
print(infos.get_age())

class Animal:
    def sound(self):
        print("Make a sound")

class Dog(Animal):
    def sound(self):
        print("Ham ham")

class Cat(Animal):
    def sound(self):
        print("Meow meow")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()



