# Problem: Create a countdown timer
# Approach: Using the time module, input function, typecasting, reversed() with range(), 
#           arithmetic operators, formatted output, and time.sleep().

import time
#time.sleep(3)       # The program is executed after 3 sec

mytime = int(input("Enter the time in seconds:  "))

for x in reversed(range(0, mytime)):
    seconds = x %60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)    # There are 3600 secs in hour

    print(f"{hours:02}:{minutes:02}:{seconds:02}") # ":02 pads the digits in clock"
    time.sleep(1) # The program is executed after 1 sec or the next step is executed after the time 

print("TIMES UP!")
