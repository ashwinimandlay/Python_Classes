# ex for @classmethod
# suppose we get employee name and pay in form of string ex
# emp1 = ashwini-mandlay-50000
# we can manually split the arguments and pass them to our
# Employee class or use @classmethod
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def string_form(cls, str_in):
        first1, last1, pay1 = str_in.split('-')
        return cls(first1, last1, pay1)


emp1_str = 'ashwini-mandlay-50000'
emp1 = Employee.string_form(emp1_str)

print('{} {} with pay {}'.format(emp1.first, emp1.last, emp1.pay))

# this is same as splitting string outside the class and
# then passing them to emp1 = Employee(f, l, p)

# IMPORTANT:
# make sure to return cls(f,l,p) at the end
