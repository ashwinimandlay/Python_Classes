# subclass
class Employee:

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


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev1 = Developer('ashwini', 'm', 50000, 'python')
print(dev1.first)
print(dev1.prog_lang)


class Manger(Employee):
    def __init__(self, first, last, pay, employee=None):
        # never use mutable data type as default argument
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_employees(self):
        for emp in self.employee:
            print('-->', emp.fullname())


mg2 = Manger('corey', 'smith', 60000, [dev1])
mg2.print_employees()

# note that we are passing a whole developer object and not
# a name string
# mgr1 = Manger('ashwini', 'mandlay', 50000)
# mgr1.add_emp('user1')
# mgr1.add_emp('user2')
#
# mgr1.print_employees()
# Error --> because user1 has no attribute fullname()
