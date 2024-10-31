class myClass:
    def __init__(self,name):
        self.name = name # default variable
        self.__salary = 0 # using '__' this '__salary' now a private variable, same way you can define a private function and other methods.
        self._phNo = 7501564476 # using '_' this '_phNo' now a protected variable, same way you can define a private function and other methods. but there is no protected concept in python

class class2(myClass):
    def showInfo(self):
        print(f"{self.name}'s salary is {self._myClass__salary}rs. contact : {self._phNo}")

t = myClass("Tanmoy Patra")
# print(t.__dir__()) # it show all methods which are able to perform in myClass
print(t.name)
# print(t.__salary) # private variable are not directly accesable 
print(t._myClass__salary) # in that way you can able to access a private variable
print(t._phNo)

c2 = class2("Shisendu Patra")
c2.showInfo()
print(c2._phNo)
print(c2._myClass__salary)