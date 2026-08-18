# logical operators = evaluate mltiple conditions (or, and, not)
#                     or = at least one condition must be true
#                     and = both conditions must be True
#                     not = inverts the condition (not Flase, not True)


# OR operations
temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor activity is cancelled")
else:
    print("The outdoor activity is still scheduled")


