# a 2d list is just a list made up of lists

vegetables =    ["Carrot", "Potato", "Tomato", "Spinach"]
fruits =        ["Apple", "Banana", "Mango", "Orange"]
food =          ["Pizza", "Burger", "Pasta", "Sandwich"]

groceries =[vegetables, fruits, food]

print(groceries[0][0]) # index the first [] prints the full row and the 2nd [] frints the element from that row 


for collection in groceries:
    for food in collection:
        print(food, end=" ")