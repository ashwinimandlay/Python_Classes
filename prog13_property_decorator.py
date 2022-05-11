# getter (get it as an attribute)
# getter == property decorator
# if we define a class
#       emp1 = Employee('ash', 'mandlay')
# then when we change its attribute value
#       emp1.first = 'corey'
# then:
# emp1.email doesn't get updated
# emp1.fullname() gets updated
# one way to solve this is to make email attribute as a method
# but that changes our code
# so we make email method an attribute by property decorator
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('ashwini', 'mandlay')
emp1.first = 'corey'
print(emp1.email)
print(emp1.fullname())

# NOTE: property decorators are used as attributes that is
# we don't use parenthesis while using them
# emp1.email
# methods use parenthesis email.fullname()
