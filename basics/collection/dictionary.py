# dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"India":"New Delhi",
            "USA":"Washington D.C",
            "China":"Beiging",
            "Russia":"Moscow"}


# print(capitals)

#to get any form element use .get the dictionary
# print(capitals.get("USA")) 

# use .update to add an element in the dictionary
# capitals.update({"Germany":"Berlin"}) 

# .update to change any values in the dectionary 
# capitals.update({"USA": "Detroit"}) 


# use  .pop() to remove an element form the dictionrary
# capitals.pop("China") 


# .popitem will remove the latest(or the last ) element form the dictionary
# capitals.popitem() 

# use .clear() to clear the dictionary 
# capitals.clear()  

# to get all of the keys with in the dictionary but not the values use .keys()
# keys = capitals.keys()
# print(keys)

# to itrate over all the kyes
# for key in capitals:
#    print(key)

# to get all the values form the dictionary use .values()
values = capitals.values()
print(values)

# to iterate over all the values in the dictionary
for values in capitals.values():
        print(values)


