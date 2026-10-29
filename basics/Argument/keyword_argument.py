# keyword arguments = an argument preceded by an identifier
#                     helps with readablility
#                     order of arguments doesn't matter 
#                     1. positional 2.default 3.KEYWORD 4.arbitrary

def hello(greeting, title, first, last):
   print(f"{greeting} {title}{first} {last}")


print(hello("Welcome",last = "cena", title = "Mr.", first = "john", ))


# write a code to generate a phone number
def get_phone(county, area, first, last):
    return (f"{county}-{area}-{first}-{last}")

phone_number =get_phone(last = "125", first = "556", county = "1", area = "45")
print(phone_number)
