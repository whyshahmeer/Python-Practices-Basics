class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def details(self):
        return f"Name: {self.name}, Role: {self.role}, Salary: ${self.salary}"


class Company:
    def __init__(self):
        self.staff = {}

    def hire_employee(self, employee_id, employee_obj):
        if not isinstance(employee_obj, Employee):
            raise TypeError("Only Employee objects can be hired.")

        if employee_id in self.staff:
            raise ValueError("Employee ID already exists.")

        self.staff[employee_id] = employee_obj

    def fire_employee(self, employee_id):
        return self.staff.pop(employee_id, None)

    def get_total_payroll(self):
        total = 0
        for employee in self.staff.values():
            total += employee.salary
        return total


company = Company()

for i in range(2):
    print(f"\nEnter Employee {i + 1}")

    employee_id = int(input("Employee ID: "))
    name = input("Name: ")
    role = input("Role: ")
    salary = float(input("Salary: "))

    company.hire_employee(
        employee_id,
        Employee(name, role, salary)
    )


print("\nCompany Employees:")
for employee_id, employee in company.staff.items():
    print(f"ID: {employee_id} | {employee.details()}")

print(f"\nTotal Payroll: ${company.get_total_payroll()}")

employee_id = int(input("\nEnter Employee ID to fire: "))
company.fire_employee(employee_id)

print("\nAfter Firing Employee:")
for employee_id, employee in company.staff.items():
    print(f"ID: {employee_id} | {employee.details()}")

print(f"\nUpdated Payroll: ${company.get_total_payroll()}")



