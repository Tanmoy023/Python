# String 
a = '''Tanmoy patra
CEMK student
CSE/21/023
'''
print(a)

fruit = "banana, apple" # strings are imutable for all programing languages
print(len(fruit))
print(fruit[0:10])

Qu = "Harry"
print(Qu[-4:-2])

name = "!! Tanmoy Patra !!"
print(name.upper())
print(name.lower())
print(name.rstrip("!")) # Python rstrip() method removes all the trailing characters from the string. It means it removes all the specified characters from right side of the string. If we don't specify the parameter, It removes all the whitespaces from the string. This method returns a string value.

print(name.replace("Tanmoy Patra","Software Developer"))
print(name.split(" "))
print(name.count("a"))
print(name.endswith("!!"))

work = "college CEMK student"
print(work.capitalize()) # it change first letter into capital form, and remaining all are turn into small letter
print(work.center(30)) # it reserve 30 latter's space and place the main content into center of that space
print(work.find("student"))
print(work.index("CEMK"))

rev = "reverse me"
print(rev[::-1])