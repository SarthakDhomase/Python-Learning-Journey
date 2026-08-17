# Problem: Convert weight between kilograms and pounds
# Approach: Using input(), typecasting, if-elif-else statements,
#           arithmetic operations, and round() to convert and display the weight.


value = float(input("Enter the weight:  "))
unit = input("Kilogram or Pounds? (K or L): ")

if unit == "K":
    weight = value * 2.205
    print(f"{value} Kilogram in Pounds is: {round(weight, 1)}")
elif unit =="L":
    weight = value / 2.205
    print(f"{value} Pounts in Kilogram is: {weight}")
else:
    print(f"{unit} is not valid")
    print("Please enter a valid unit (K or L)")
