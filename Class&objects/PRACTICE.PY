# create class and objects for  that store the data form user  of 100 student and pirnt it
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

students = []
i = int(input("Enter the number of students: "))
# using for loop to create objects for each student

for i in range(i):
    name = input(f"Enter the name of student {i+1}: ")
    age = int(input(f"Enter the age of student {i+1}: "))
    grade = input(f"Enter the grade of student {i+1}: ")
    student = Student(name, age, grade)
    students.append(student)

# Display information for all students
for student in students:
    student.display_info()