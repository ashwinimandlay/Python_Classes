# magic/dunder methods-->(double underscore methods)
# >>print(1+2)
# 3
# this is same as print(int.__add__(1,2))

# >>print('a'+'b')
# ab
# this is same as print(str.__add__('a'+'b'))

# so dunder methods are special methods and we can also define
# them for our function too
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.first(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.first)
        # return the length of first name


emp1 = Employee('ashwini', 'mandlay', 50000)
emp2 = Employee('corey', 'shafer', 60000)

# no we cannot add two employees together
# >> print(emp1+emp2)
# ERROR

# but we can make a dunder add function which adds the pay
# of the employees
print(emp1+emp2)

# __len__ gives the length of string
# >> print(len(emp1))
# ERROR
# same as print('test'.__len__)
print(len(emp1))


