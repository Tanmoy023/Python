class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def intro(self):
        print(f"my name : {self.name} and my salary is {self.salary}rs per anum")

    @classmethod
    def splitStr(self,string):
        return self(string.split("-")[0],string.split("-")[1])

e1 = Employee("Tanmoy","60000")
e1.intro()
string = "Shirsendu-0"
e2 = Employee.splitStr(string)
e2.intro()
