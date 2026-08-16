# format specifiers = {value:flags} format a value based on what flags aree inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to left most position 
# :  = insert a space befor positive number
# :, = comma separator

price1 = 3.454544 
price2 = 5.23
price3 = 214123234321354
price4 = 56454
print(f"Price 1 is ${price1:010}") # pad the number
print(f"Price 2 is ${price2:.1f}") 
print(f"Price 3 is ${price3:,}") #seprate thousands with ,
print(f"Price 4 is ${price4:^10}")