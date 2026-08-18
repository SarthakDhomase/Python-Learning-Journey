# Problem: Create a rectangle using any symbol based on the given number of rows and columns
# Approach: Using nested for loops, input function, typecasting, range(), and the end parameter in print().

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the columns of rows: "))
symbol = input("Enter a symbol")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()