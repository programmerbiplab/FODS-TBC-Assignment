'''The following program reads student data from
a csv file and displays the data as output'''

# To work on csv file, import csv is used
import csv

# To open and read the CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    # For printing student details
    print("Student Details:\n")
    
    for row in reader:
        name = row['name']
        student_id = row['id']
        course = row['course']
        level = row['level']
        section = row['section']
        
        print("Name:", name)
        print("ID:", student_id)
        print("Course:", course)
        print("Level:", level)
        print("Section:", section)
        print()

# by Biplab Prasad Gajurel 25024641
