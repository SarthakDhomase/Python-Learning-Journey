# default argument = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your function more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4.arbitarary


def net_price(list_price, discount=0, tax=0.05): #<=== default argumant
    return list_price * (1-discount) * (1 + tax)

print(net_price(500, 0.1))


# counter
# example 
import time  # import time modult

def count(end, start= 0): # create a function called count with 1 variable end and 1 default argument as start
    for x in range (start, end+1): # use for loop for 
        print(x)                   # print each element form the range
        time.sleep(1)              # add dealy of 2 sec
    print("Done")                  # after execution print done

count(10)                          # pass in the value into the "end"