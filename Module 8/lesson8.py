#
# def calculate_area(length,width):
#     return length * width
#
# def calculate_perimeter(length,width):
#     return 2 * (length + width)
#
# length = 5
# width = 6
#
# area = calculate_area(length,width)
# perimeter = calculate_perimeter(length,width)
#
# print(f"Area : {area}")
# print(f"Perimeter: {perimeter}")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(5, 3)


area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello I am {self.name} and I am {self.age} years old")

person1 = Person("Filan", 21)
person2 = Person("Artan",34)

person1.greet()
person2.greet()