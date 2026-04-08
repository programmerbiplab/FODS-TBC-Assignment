'''The following program takes employee records and
stores it in a csv file making it easier to view, modify and
add data and display the consisting data as output when asked'''

# To access and use csv data
import csv

# Creation of employee class
class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_list(self):
        return [self.empid, self.name, self.address, self.contact_number, self.spouse_name, self.number_of_child, self.salary]

# To update the record
def add_employee():
    empid = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    contact_number = input("Enter Contact Number: ")
    spouse_name = input("Enter Spouse Name: ")
    number_of_child = input("Enter Number of Children: ")
    salary = input("Enter Salary: ")
    return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)

def write_employees_to_file(employees, filename="employees.csv"):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(["EmpID", "Name", "Address", "Contact Number", "Spouse Name", "Number of Children", "Salary"])
            # Write employee data
            for emp in employees:
                writer.writerow(emp.to_list())
        print(f"Successfully saved {len(employees)} employees to '{filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_employees_from_file(filename="employees.csv"):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            employees = list(reader)
            return employees
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    except Exception as e:
        print(f"Error reading from file: {e}")
        return []

# For the display of record
def display_employees(employees):
    if not employees:
        print("No employee records found.")
        return
    print("\n--- Employee List ---")
    for emp in employees:
        print(f"ID: {emp[0]}, Name: {emp[1]}, Address: {emp[2]}, Contact: {emp[3]}, Spouse: {emp[4]}, Children: {emp[5]}, Salary: {emp[6]}")

# The console menu of the program
def main():
    employees = []
    while True:
        print("\nEmployee Management Menu:")
        print("1. Add Employee")
        print("2. Save Employees to File")
        print("3. View Employees from File")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp = add_employee()
            employees.append(emp)
            print("Employee added.")

        elif choice == '2':
            if employees:
                write_employees_to_file(employees)
            else:
                print("No employees to save. Add employees first.")

        elif choice == '3':
            emps = read_employees_from_file()
            display_employees(emps)

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# by Biplab Prasad Gajurel 25024641