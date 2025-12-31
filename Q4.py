# Create a calculator program using OOPS. Make sure you create a class Calculator and then use its object to access the calculator operations such as addition, subtraction, division, and multiplication.

class Calculator:
    def add (self,a,b):
        return a + b 
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"
        
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

calc = Calculator()

print("Addition: ", calc.add(num1, num2))
print("Subtraction: ", calc.subtract(num1, num2))
print("Multiplication: ", calc.multiply(num1, num2))
print("Division: ", calc.divide(num1, num2))
