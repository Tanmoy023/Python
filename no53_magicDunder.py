from typing import Any


class employee:
    def __init__(self,name):
        self.name = name
    def __len__(self): # you can call using len(employee). it only return a integer value
        length = len(self.name)
        return length
    def __str__(self): # if you call only employee it will run. it only return a string value. you also call it as str(employee)
        return f"the name of employee is {self.name} from str"
    def __repr__(self): # same as __str__, if __str__ is not present so it will be run
        return f"the name of employee is {self.name} from repr"
    def __call__(self): # you can call it using employee()
        print("Hey i am __call__(self)")
    

e = employee("Tanmoy")
print(len(e))
print(e)
# print(str(e))
print(repr(e))
e()
