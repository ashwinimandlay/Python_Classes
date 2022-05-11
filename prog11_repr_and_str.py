# repr and str (dunder methods)-->(double underscore)
# the goal of __repr__ is to be unambiguous
# the goal of __str__ is to be readable
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


emp1 = Employee('ashwini', 'mandlay', 50000)

# if both __str__ and __repr__ are commented out
print(emp1)
# this gives an employee object

# if only __str__ is commented
print(emp1)
# repr gives such an output that we run it on compiler

# if only __repr__ is commented
print(emp1)
# this gives a more readable output which tells what it
# actually is

# we can also access them by
print(emp1.__repr__())
print(emp1.__str__())
