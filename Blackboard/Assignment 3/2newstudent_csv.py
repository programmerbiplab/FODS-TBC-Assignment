'''The following program takes user input of the new student and
updates the students.csv file with the new record and
it also displays a message on terminal screen'''

# To use the csv file
import csv

# Graphical optimization
print("===================================")
print("  Add New Student Record to CSV")
print("===================================\n")

# Asking the user to input new student details
print("Please enter the following details:")

name = input("  Name     : ").strip()
student_id = input("  ID       : ").strip()
course = input("  Course   : ").strip()
level = input("  Level    : ").strip()
section = input("  Section  : ").strip()

# To open the CSV file in append mode and add the new record
with open("students.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, student_id, course, level, section])

print("\n-----------------------------------")
print("✅ New student record added!")
print("-----------------------------------")
print(f"  Name   : {name}")
print(f"  ID     : {student_id}")
print(f"  Course : {course}")
print(f"  Level  : {level}")
print(f"  Section: {section}")
print("-----------------------------------")
print("Thank you! The record has been saved to students.csv.\n")

# by Biplab Prasad Gajurel 25024641