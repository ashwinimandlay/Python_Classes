# class variables (not same as attributes)
# they are variables common to all objects alike
# such as raise amount in an Employee class
class Employee:
    # 4 percent raise
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount


# here we can also use :
# self.pay = self.pay * Employee.raise_amount
emp1 = Employee('ashwini', 'mandlay', 50000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# we can access the class variable by Employee class or by
# its instance
print(Employee.raise_amount)
# this directly access raise amount variable

print(emp1.raise_amount)
# first it sees if the instance have raise amount attribute
# if it doesn't find it:
# then it checks if the class have raise amount variable
# then it checks if any of the class it inherits from contains
# the raise amount variable
