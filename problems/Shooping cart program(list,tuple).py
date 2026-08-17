# Problem: Create a shopping cart program to add food items and calculate the total price
# Approach: Using lists, while loop, input(), typecasting, append(), for loops, and arithmetic operations.

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press q to quit):  ")
    if food.lower() == "q":  #.lower convers the input in to lower case if the user enters "Q" it will still work
        break
    else:
        price = float(input(f"Enter the price of a {food}: ₹"))
        foods.append(food)
        prices.append(price)

print("---------  YOUR CART ----------")

for  food in foods:
    print(food)

for price in prices:
    total = total + price

print(f"Your totle is: ₹{total}")