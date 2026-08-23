# keyword argument 

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number= get_phone(country ="1", area="125", first="645", last="1254")

print(phone_number)