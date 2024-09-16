
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.salary *= 2