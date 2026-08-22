# default argument = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your function more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4.arbitarary


def net_price(list_price, discount=0, tax=0.05): #<=== default argumant
    return list_price * (1-discount) * (1 + tax)

print(net_price(500, 0.1))