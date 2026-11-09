# Python Calculator
# Created by Hamza

print("Welcome to My Python Calculator!")

# Get user input
num1 = float(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the calculation
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero!")
        result = None

else:
    print("Invalid operator!")
    result = None

# Display the result
if result is not None:
    print("Result:", result)
