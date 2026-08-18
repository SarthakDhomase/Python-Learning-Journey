import random
# use the import the random module and use the .randint(range) function to get random number from the range
# number = random.randint(1, 6)

# via a variable method 
low = 1
high = 100
num = random.randint(low, high)
print(num)


# get random float number 
numfloat = random.random()
print(numfloat)

# Roll random options 
# create a tuple and use the .choice to get random element form the tuple 
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

# Shuffel cards
cards = ["2", "3","4","5","6","7","8","9","10","J","K","Q","A"]
random.shuffle(cards)
print(cards)

