class Employee:
    def get_bonus(self, base_salary):
        # Standard bonus structure: 10% of base salary
        return base_salary * 0.10

class Manager(Employee):
    # Overriding the parent's get_bonus method specifically for Managers
    def get_bonus(self, base_salary):
        # Higher bonus structure for management: 25% of base salary
        return base_salary * 0.25

# Testing method overriding functionality
emp = Employee()
mgr = Manager()

print(f"Standard Employee bonus for a $5000 salary: ${emp.get_bonus(5000)}")
print(f"Manager bonus for a $5000 salary: ${mgr.get_bonus(5000)}")
