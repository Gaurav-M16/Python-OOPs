class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def show_details(self):
        print("Student Information")
        print("-"*20)
        print(f"Name: {self.name}, \nAge: {self.age}, \nRoll no: {self.roll_no}")

obj = Student("gaurav", 21, 2016)
obj.show_details()