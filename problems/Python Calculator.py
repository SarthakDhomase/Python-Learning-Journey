# Problem: Create a basic calculator that performs addition, subtraction, multiplication, or division
# Approach: Using input(), typecasting, variables, if-elif-else statements, arithmetic operators, and
#           formatted output.
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(f"Addition of num1 and num2 is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Substraction of num1 and num2 is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Multiplication of num1 and num2 is: {result}")
elif operator == "/":
    result = num1 / num2
    print(f"Division of num1 by num2 is: {result}")
else:
    print(f"{operator} is not a valid operator")