# setter decorator
# methods which are under property decorator can only be used
# as setter decorator
# WHAT IT DOES:
# we can change the value of attribute: emp1.first = 'corey'
# but we cannot change the value using methods or property decorator
# ex: emp1.email = 'corey.shafer@gmail.com' --> ERROR
# ex2: emp1.fullname() = 'ash mand'-->don't use methods use
#                                     property decorator only

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp1 = Employee('ashwini', 'mandlay')
print(emp1.fullname)

emp1.fullname = 'corey shafer'
print(emp1.fullname)
