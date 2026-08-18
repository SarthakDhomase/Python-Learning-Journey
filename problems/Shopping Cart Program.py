# Problem: Create a shopping cart program to calculate the total cost of an item based on its price and quantity
# Approach: Using input() function, typecasting, variables, multiplication, and formatted output.

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price*quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ₹{total}")