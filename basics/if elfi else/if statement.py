# if = Do some code only IF some condition is True
#        Else do something else
age = int(input("Enter your age: "))


if age >=100:
    print("Your too old to sign up")
elif age >= 18:
    print("Your are now signed up!")
elif age < 0:
    print("Your not born yet")
else:
    print("You must be 18+ to sign up")