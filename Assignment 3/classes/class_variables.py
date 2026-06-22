#!/usr/bin/env python3

class Employee:
    # Class variable (shared across ALL instances of this class)
    company_name = "TechSolutions"
    employee_count = 0

    def __init__(self, name, position):
        self.name = name  # Instance variable (unique to each object)
        self.position = position
        # Incrementing the shared class counter every time a new instance is created
        Employee.employee_count += 1

# Creating class instances
emp1 = Employee("Anna", "Developer")
emp2 = Employee("David", "Designer")

# Verifying individual instance variables
print(f"Employee 1: {emp1.name} ({emp1.position})")
print(f"Employee 2: {emp2.name} ({emp2.position})")

# Verifying class variable accessibility via instances and the class name
print(f"Company for emp1: {emp1.company_name}")
print(f"Company for emp2: {emp2.company_name}")
print(f"Total employees at {Employee.company_name}: {Employee.employee_count}")
