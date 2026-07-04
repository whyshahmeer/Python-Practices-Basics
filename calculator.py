class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def calculate(self, operator):
        if operator == '+':
            result = self.num1 + self.num2
            print(f"{self.num1} + {self.num2} = {result}")
            return result
        
        elif operator == '-':
            result = self.num1 - self.num2
            print(f"{self.num1} - {self.num2} = {result}")
            return result
        
        elif operator == '*':
            result = self.num1 * self.num2
            print(f"{self.num1} * {self.num2} = {result}")
            return result
        
        elif operator == '/':
            if self.num2 == 0:
                print("Error cannot divide by zero!")
                return None
            
            result = self.num1 / self.num2
            print(f"{self.num1} / {self.num2} = {result}")
            return result
        else:
            print("Invalid operator! Use +, -, *, or /")
            return None

    if __name__ == "__main__":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    
        calc = calculator(num1, num2)

    
    operator = input("Enter operator (+, -, *, /): ")
    
    print("Result")
    calc.calculate(operator)











