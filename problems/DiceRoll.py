# create a dice roller program 

import random

# uni code line print("\u25CF \u250C \u2500 \u2510 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ ┐ │ └ ┘

dice_art = {
    1:(
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),

    2:(
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),

    3:(
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),

    4:(
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),

    5:(
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),

    6:(
        "┌──────────┐",
        "│   ●   ●  │",
        "│   ●   ●  │",
        "│   ●   ●  │",
        "└──────────┘"
    )
}


dice = []
total = 0
num_of_dice = int(input("How many dice?:  "))


# this loops rolls dice and appends the value in dice list 
for die in range(num_of_dice): # the range is set by the user
    dice.append(random.randint(1,6)) # the value is added in the list and the value is between 1-6

#``````````````USE this loop to print the dice vertically 
#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)


# used to print the die horizontallyh 
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()



# this loops get the rolled die values and sums them
for die in dice:
    total = total + die

print(dice)
print(f"total is:  {total}")
