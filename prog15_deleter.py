# deleter
# only a property decorator can be a deleter
# deletes the attribute specified
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

    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.first = None
        self.last = None


emp1 = Employee('ashwini', 'mandlay')

del emp1.fullname
print(emp1.first)