class myClass:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def info(self):
        print(f"{self.name}'s id is : {self.id}")

class student(myClass): # now student is a class which have all feature of myClass and his own feature's also
    def showDept(self):
        print("All depertment's are 'CSE', 'IT', 'ECE', 'EE', 'ME'")

Tanmoy = myClass("Tanmoy Patra", 23)
Tanmoy.info()
Shirsendu = student("Shirsendu Patra", "100")
Shirsendu.info()
Shirsendu.showDept()