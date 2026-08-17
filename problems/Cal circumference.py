# Problem: Find circumference & Area of a circle 


# Approach: Using the math module, variables, typecasting, input function, mathematical formulas, 
#           and rounding the output.


import math
# Circumference
radius = float(input("Enter the radius of circle:  "))
cricumference = 2 * math.pi * radius # area of circle = 2 * pi * 3

print(f"Circumferance of the circle is :{round(cricumference,2)} cm")

# Area
area = math.pi * pow(radius, 2) # area of circle = pi * r(square)
print(f"Area of circle is:  {round(area, 2)}cm^2")

