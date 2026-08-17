# Problem: 1. Get the last 4 digits of a credit card number 
#          2. Print the card number backwards
# Approach: Using string indexing and slicing with positive and negative step values.

credit_num = "1256-4654-6548-6465"

last_digit = credit_num[-4:]
print(f"Last four digit of your credit card is XXXX-XXXX-XXXX-{last_digit}")

ReverseCardNum = credit_num[::-1]
print(ReverseCardNum)

