# Concession stand program 

menu = {"pizza": 299.00,
        "popcorn": 249.00,    
        "fries": 89.00,    
        "chips": 79.00,
        "soda": 60.00,
        "juice": 55.00}

cart = []
total = 0


# Print the menu using the for loop 
print("~~~~~~~~~~~~~~~~~    MENU    ~~~~~~~~~~~~~~~~~")
for key,value in menu.items():
    print(f"{key:10}: ₹{value:.2f}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# take the order form the user and after pressing q break the loop 
# and if the the enter values(food items) are not NONE meaning those value are in the diction and append those values in the varialble cart
while True:
    food = input("Select an item (press q to quit):  ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print(cart)

# get all the values in the cart and print totle 
for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is ₹{total}")