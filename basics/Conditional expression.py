# Conditional Expression = A one-line shortcut for the if-else statement (Ternary operator)
#                          Print or assign one of two values based on a conditon 
#                     FORMULA    =   X if condtion else Y

num = -5
a=5
b=8

# Positive & Odd or even 
print("Positive" if num>0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

#MIN & MAX
max_num = a if a>b else b
print(f"Max number is {max_num}")

min_num = a if a<b else b
print(f"Min number is {min_num}")

age = 18
status = "Adult" if age >=18 else "Child"
print(status)


temp = 30
wheather = "Hot" if temp >= 20 else "Cold"
print(wheather)

user_role = "admin"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)