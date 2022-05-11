# static methods
# regular methods pass the instance as first argument
# class methods pass the class as the first argument
# static method doesn't pass anything
class Employee:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
my_date = datetime.date(1998, 5, 16)
print(Employee.is_workday(my_date))

# IMPORTANT:
# static methods are used when you don't access the instance
# or the class or any attribute
