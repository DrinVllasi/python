from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self,value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self.weight = value

    @property
    def height(self):
        return self.height

    @weight.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self.height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"Name: {self.name},Age:{self.age}, Weight: {self.weight}kh, Height{self.height}m, "f"BMI: {self.calculate_bmi():.2f}"
        f"Category: {self.get_bmi_category()}")

