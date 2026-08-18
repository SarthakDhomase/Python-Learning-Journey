# Problem: Convert temperature between Celsius and Fahrenheit
# Approach: Using input(), typecasting, if-elif-else statements, and temperature conversion formulas.

unit = (input("Is the Temprature in Celsius or Fahrenheit (C/F):  "))
value = float(input("Enter the temperature: "))

if unit == "C" :
    temp = (9*value) / 5 +32
    print(f"{value} in Fahrenheit is: {temp} F ")
elif unit == "F" :
    temp = (value-32) * 5 /9
    print(f"{value} in Celsius is: {temp}")
else:
    print(f"{unit} is not VAlLID")