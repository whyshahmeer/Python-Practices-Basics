class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager", "cashier", "cooker", "actor", "Developer"]
        return position in valid_positions
    
    
employee = Employee("ALI", "Developer")
employee1 = Employee("ahmed", "Cook")
employee2 = Employee("saad", "actor")

    
print(Employee.is_valid_position("cashier"))
print(employee1.get_info())
print(employee.get_info())
print(employee2.get_info())

