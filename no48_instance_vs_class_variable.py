class myClass:
    university = "MAKAUT" # class variable(which same for all all class object) 
    def __init__(self,name):
        self.name = name # instance variable(which unic for all all class object) 
        self.age = 21 # instance variable(just for it don't directly declear in the class)
    def intro(self):
        print(f"The name is {self.name} and his age is {self.age}. Currently study in {self.university}")
c = myClass("Tanmoy Patra")
# myClass.intro(c)
c.university = "MAKAUT Kolaghat" # if i over write a class variable then it become a instance variable
c.intro()
c2 = myClass("Shirsendu Patra") # if i over write a instance variable then it still is a instance variable 
c2.age = 23
c2.intro()

myClass.university = "Makaut" # if i over write a class variable using his class original class name then it still is a class variable
c.intro()
c2.intro()