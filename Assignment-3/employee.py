#  Create a class Employee and then do the following
# • Create a data member to count the number of Employees
# • Create a constructor to initialize name, family, salary, department
# • Create a function to average salary
# • Create a Fulltime Employee class and it should inherit the properties of Employee class
# • Create the instances of Fulltime Employee class and Employee class and call their member functions.

# Creating a Class Employee
class Employee:
    noOfEmployees = 0

    # creating a constructor, in python we use _init_() and this method invokes as soon as an object of a class is instantiated
    # we are passing 4 paramters and self refers to current object and binds the instance to the _init_()
    def __init__(self,name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.noOfEmployees += 1
# Writing Function to get salary input from console and performing validation on salary input. 
# If salary is not entered in digits It will consider as 0
def enter_salary():
    salary = input("Enter Salary: ")
    if salary.isdigit():
        return int(salary)
    else:
        return 0

# Function for calculating avaerage salary of all employees and returning it.   
def average_salary(totalemployees):
    totalsalary = sum(e.salary for e in totalemployees )
    average_salary = totalsalary / len(totalemployees)
    print("Average Salary: {:.1f}".format(average_salary))

# Creating a Class FullTimeEmployee and inheriting the properties of Employee Class
class FullTimeEmployee(Employee):
    def __init__(self,name,family,salary,department):
        Employee.__init__(self,name,family,salary,department)
        
# Creating List for all employees
listofallemployees = []

# First Approach
noofemployee = int(input("Enter the No of Employees: "))
nooffulltime_employees = int(input("Enter the No of Full Time Employees: "))
print(" ")

def create_employee(employee_type):
    return employee_type(
        input("Enter Employee Name: "),
        input("Enter Family Details: "),
        enter_salary(),
        input("Enter Department: ")
)

def create_fulltime_employee(employee_fulltime_type):
    return employee_fulltime_type(
        input("Enter Full Time Employee Name: "),
        input("Enter Family Details: "),
        enter_salary(),
        input("Enter Department: ")
)

for emp in range(noofemployee): 
    print("Employee: ",emp+1)
    employee = create_employee(Employee)
    listofallemployees.append(employee)
    print(" ")

for ftemp in range(nooffulltime_employees):
    print("Full Time Employee: ",ftemp+1)
    ft_employee = create_fulltime_employee(FullTimeEmployee)
    listofallemployees.append(ft_employee)
    print(" ")

# Second Approach
# Creating Employee Instance and appending it to list
# print("First Employee: ")
# employee1 = Employee(input("Enter First Employee Name: "), input("Enter Family Details: "),
#                      enter_salary(),
#                      input("Enter Department: "))
# listofallemployees.append(employee1)

# print("Second Employee: ")
# employee2 = Employee(input("Enter Second Employee Name: "), input("Enter Family Details: "),
#                      #int(input("Enter Salary: ")) if input("Enter Salary: ").isdigit() else 0,
#                      enter_salary(),
#                      input("Enter Department: "))
# listofallemployees.append(employee2)

# print("First Full Time Employee: ")
# ftemployee1 = FullTimeEmployee(input("Enter First Full Time Employee Name: "), input("Enter Family Details: "),
#                      enter_salary(),
#                      input("Enter Department: "))
# listofallemployees.append(ftemployee1)

# print("Second Full Time Employee: ")
# ftemployee2 = FullTimeEmployee(input("Enter Second Full Time Employee Name: "), input("Enter Family Details: "),
#                      enter_salary(),
#                      input("Enter Department: "))
# listofallemployees.append(ftemployee2)

# Printing Total No of Employees
print("Total Number of Employees: ", Employee.noOfEmployees)
print(" ")

# Calling Average Salary to print Average Salary of all employees
average_salary(listofallemployees)