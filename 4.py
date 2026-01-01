# Create a calculator program using OOPS. Make sure you create a class Calculator and then use its object to access the calculator operations such as addition, subtraction, division, and multiplication.
# One operation at a time.

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

print("\n select operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice from this - 1 / 2 / 3 / 4 : ")

if choice == "1" :
    print("Result :",calc.add(num1,num2))
elif choice == "2":
    print("Result :",calc.subtract(num1,num2))   
elif choice == "3":
    print("Result :",calc.multiply(num1,num2))    
elif choice == "4":
    print("Result :",calc.divide(num1,num2))  
else :
    print("Invalid choice.")        