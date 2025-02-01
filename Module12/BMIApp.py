from Module12.Adult import Adult
from Module12.Child import Child


class BMIApp:
    def __init__(self):
        self.people = []
    def add_person(self,person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        weight = float(input("Enter weight: "))
        height = float(input("Enter height: "))

        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name,age,weight,height)

        self.add_person(person)

    def print_results(self):
        for person in self.people:
            person.print_info()

    def run(self):
        while True:
            self.collect_user_data()
            const = input("Do you want to add another person? (Yes/No): ").strip().lower()
            if const != 'yes':
                break
        self.print_results()
