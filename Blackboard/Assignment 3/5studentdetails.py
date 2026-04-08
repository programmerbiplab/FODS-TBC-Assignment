'''The following program defines a class and
takes input as student details and 
displays the input data as output'''

# Defining a class called Student
class Student:
    def __init__(self, sid, name, address, admission_year, level, section):
        self.id = sid
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def display(self):
        print("\n--- Student Details ---")
        print("ID:", self.id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Admission Year:", self.admission_year)
        print("Level:", self.level)
        print("Section:", self.section)


# Taking input from the user
sid = input("Enter Student ID: ")
name = input("Enter Student Name: ")
address = input("Enter Address: ")
admission_year = input("Enter Admission Year: ")
level = input("Enter Level: ")
section = input("Enter Section: ")

# Creating Student object
student1 = Student(sid, name, address, admission_year, level, section)

# Displaying the details
student1.display()

# by Biplab Prasad Gajurel 25024641