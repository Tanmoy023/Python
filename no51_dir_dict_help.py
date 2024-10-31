x = [1,2,3]
# print(dir(x)) # dir(x) show all methods which i can perform with x. All __method__ are getter method


class Employe:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = Employe("Tanmoy","0")
print(e.__dict__) # it show all atributes

# print(help(str)) # it say every thing about a str
print(help(e)) # it say every thing about e