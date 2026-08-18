# for loop =  execute a block of code a fixed number of times
#             You can iterate over a range, string, squnce, etc.abs

for x in reversed(range(1, 11)): #Print number form 1 to 10
    print(x)
print("Happy New Year!")


# print number but skip a few
for x in range(1,21):
    if x == 13:
        continue # used to skip the number also you can use "break" keywords to break out to the loop
    else:
        print(x)