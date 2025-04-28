class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

# Example
emp = Employee("Ali", 50000, "123-45-6789")
print(emp.name)           # Public - Accessible
print(emp._salary)        # Protected - Accessible but discouraged
# print(emp.__ssn)        # Private - Error
print(emp._Employee__ssn) # Accessing private using name mangling
