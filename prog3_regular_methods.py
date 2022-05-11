# methods are functions that uses attributes to do a
# particular task
# NOTE: regular methods need parenthesis and attributes don't
#       regular methods receive the instance as first argument
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('ashwini', 'mandlay', 50000)
emp2 = Employee('corey', 'shafer', 60000)
print(emp1.fullname())
# this is same as writing:
# print('{} {}'.format(emp1.first, emp1.last))
# outside of the class
# but now we can use it for any other objects too
print(emp2.fullname())

# IMPORTANT: methods can also be called directly by function
# itself but we have to pass in the instance then
print(Employee.fullname(emp1))
# actually in background:
# emp1.fullname is translated to Employee.fullname(emp1)
