# store  student data using class and object
class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}")
        

n=int(input("enter number of students for data entry:"))
for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    roll_number = int(input("Enter roll number: "))
    student = Student(name, age, roll_number)
    
        
for i in range(n):
    student.display_info()   
        
