# python object-oriented programming
# instances --> class objects
#               ex: emp1 below
# attributes --> all the object variables in __init__
#                __init__(self,a,b,c) --> a,b,c are attributes
# methods --> functions inside a class that we can access
#             using class.method()

class Employee:
    pass


# NOTE: class Employee(object): is also the same thing
# because when we start python by default there is a class
# called as object (so we are basically inheriting all the
# attributes of object class)
emp1 = Employee()
emp2 = Employee()

# by printing out emp1,2 we can confirm if they are both
# Employee class objects
print(emp1)
print(emp1)

# now we can manually add class attributes
emp1.first = 'ashwini'
emp1.last = 'mandlay'
emp1.email = 'ashwini.mandlay@gmail.com'
emp1.pay = 50000

emp2.first = 'corey'
emp2.last = 'shafer'
emp2.email = 'corey.shafer@gmail.com'
emp2.pay = 60000

print(emp1.email)
print(emp2.email)

