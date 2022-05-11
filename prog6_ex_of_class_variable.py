# example for class variable
class Employee:

    num_of_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.num_of_employees += 1


# whenever a new object is created the init method runs
emp1 = Employee('ashwini')
emp2 = Employee('corey')
print(Employee.num_of_employees)

emp3 = Employee('testname')
print(Employee.num_of_employees)
