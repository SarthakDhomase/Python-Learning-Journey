# logical operators = evaluate mltiple conditions (or, and, not)
#                     or = at least one condition must be true
#                     and = both conditions must be True
#                     not = inverts the condition (not Flase, not True)

#Not
temp = 30
is_sunny = False

if temp >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("IT is SUNNY")

elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is SUNNY")

elif 28 > temp > 0 and not is_sunny :
    print("It is WARM outside")