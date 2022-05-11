# modifying class variables
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount


# here we can also use :
# self.pay = self.pay * Employee.raise_amount
emp1 = Employee('ashwini', 'mandlay', 50000)

# to see all the attributes in an object we use __dict__
print(emp1.__dict__)
# notice there is no raise_amount attribute

print('change raise_amount using Employee class')
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp1.raise_amount)

print('use instance to change raise_amount')
emp1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp1.raise_amount)
# here class variable doesn't change and the instance creates
# a new attribute
print(emp1.__dict__)

# CONCLUSION: so preferably we use self.raise_amount because
# it gives control over individual employee
