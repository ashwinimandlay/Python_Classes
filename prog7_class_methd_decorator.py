# class method decorator
# alternative constructor or initializer
# it is same as function decorator (class plus something!!)

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee('ashwini', 'mandlay', 50000)

print(emp1.raise_amount)
print(Employee.raise_amount)

Employee.set_raise_amount(1.09)
# this is same as saying
# Employee.raise_amount = 1.09

print('change raise amount using @classmethod')
print(emp1.raise_amount)
print(Employee.raise_amount)

# see ex2 class method for more detail
