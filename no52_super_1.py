class parentClass:
    def parentMethod(self):
        print("i am parentMethod() form parentClass")

class childClass(parentClass):
    def childMethod(self):
        print("i am childMethod() form childClass")
        super().parentMethod() # it check this method in his parentClass and run that
    def parentMethod(self):
        print("i am parentMethod() form childClass")
        super().parentMethod() # if parentMethod() is not present in parent class it show error

p = parentClass()
p.parentMethod()

c = childClass()
c.parentMethod()