name = input("Enter your name: ")
ph_number = input("Enter your phone number: ")
#Find length of a string use len()
result = len(name) 

# Find the first occureance specifice charater use .find
result = name.find("m")
print(result)


# Find the last occureance specifice charater use .rfund
result = name.rfind("m")
print(result)

# Capatalize the first letter of string use .capitalize
name = name.capitalize()
print(name)

# Capatalize the full string use .upper()
name = name.upper()
print(name)

# Change the string to lower case use .lower()
name = name.lower()
print(name)

# .isdigit() will return true or false if a string contains only digits
digit = name.isdigit()
print(digit)

# .isalpha will return true or false if a string contains only aplhabets
digit = name.isalpha()
print(digit)

# Count a specific character in sting using the count("") 
symbolINph = ph_number.count("-")
print(symbolINph)

# Replace any charater with another use the .replace("-" , " ")
replaceph = ph_number.replace("-", " ")
print(replaceph)


print(help(str))