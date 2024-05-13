# The Calculator App

#Objective:
#The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.





#Task 1: Create functions for each arithmetic operation.
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:  # Task 3 check for division by zero
        return "Error: Division by zero!"
    else:
        return x / y

#Task 2: Implement user input to receive numbers and an operation choice.
# Function to get user input for numbers and operation choice
def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        return num1, num2, operation
    except ValueError:
        print("Error: Invalid input! Please enter valid numbers.")
        return None, None, None

# Function to perform the chosen operation
def calculate(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        return "Error: Invalid operation!"

# Main function
def main():
    num1, num2, operation = get_user_input()
    if num1 is not None and num2 is not None and operation is not None:
        result = calculate(num1, num2, operation)
        print("Result:", result)

# Entry point of the program
if __name__ == "__main__":
    main()
