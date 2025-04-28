class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

# Example
e = Employee("Hamza")
d = Department(e)
print(d.employee.name)
