# while loop = execute some code WHILE some condition remains true

name = input("Enter your name:  ")

while name == "": # execute the below code while the <=== this condtion is true 
    print("You must enter your name")
    name = input("Enter your name:  ")
print(f"Hello {name}")



age = int(input("Enter your age:  "))
while age < 0 :
    print("Age cant be negative")
    age = int(input("Enter your age:  "))
print(f"Welcome! {name} you are {age} years old")


