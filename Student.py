
class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f'student name: {self.name}, ID: {self.school_id}, gpa: {self.gpa}'

susan = Student('Susan', '135468', 3.5)
print(susan.name)
print(susan)

#this version is a lot easier to read because it is broken down into a class and the "def __init__" and "def __str__"


