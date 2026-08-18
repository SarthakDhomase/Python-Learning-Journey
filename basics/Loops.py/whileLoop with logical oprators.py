food = input("what do you like to eat (q to quit)")
while not food == "q":
    print(f"ok you want to eat {food}")
    food = input("what do you like to eat (q to quit)")
print("bye")

num = int(input("Enter a number between 1 - 10"))
while num < 1 or num > 10 :
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10"))
print(f"Your number is {num}")