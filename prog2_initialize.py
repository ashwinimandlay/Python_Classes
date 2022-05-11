# self is simply the instance like
# self.first = first -->
#                       emp1 = Employee('ash', 'ma', 20)
#                       emp1.first = ash
# __init__ --> initialize or constructor
#              whenever a new object is formed init runs
# methods receive the instance as first argument
class Employee(object):
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp1 = Employee('ashwini', 'mandlay', 50000)
emp2 = Employee('corey', 'shafer', 60000)

print(emp1.email)
print(emp2.email)
