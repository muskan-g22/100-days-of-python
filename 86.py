# 86	Implement inheritance with Employee and Manager classes.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_manager_info(self):
        self.display_info()
        print("Department:", self.department)


# Create Manager object
manager = Manager("Muskan", 60000, "IT")

# Display information
manager.display_manager_info()