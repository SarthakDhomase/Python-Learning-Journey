#Python compound interest calculator
# Approach: Using variables, input function, typecasting, while loops for input validation,
#           pow() function, and the compound interest formula.


principle = 0
rate = 0
time = 0

while principle <= 0 :
    principle= float(input("Enter the principle amount "))
    if principle <= 0:
        print("principle can't be less than or equal to zero")

while rate <= 0 :
    rate = float(input("Enter the Intereast rate "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

while time <= 0 :
    time = float(input("Enter time in years "))
    if time <= 0:
        print("Time cannot be less than or equal to 0")

total = principle * pow((1 + rate / 100),time)
print(f"Balance after {time} years : {total:.2f}")