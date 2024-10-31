name = "Tanmoy"
countries = "india"

mySelf = "My name is {} and i am from {}"
print(mySelf.format(name,countries)) # with out f-string

print(f"Hii my name is {name} and i am from {countries}") # in f-string

price = 10.1234
penPrice = f"The price of a pen is {price:.2f} rs."
print(penPrice)