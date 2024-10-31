class MyClass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"The value is {self._value}")

    @property
    def tenXvalue(self):
        return 10*self._value

    @tenXvalue.setter
    def tenXvalue(self,new_value):
        self._value = new_value

obj = MyClass(10)
obj.tenXvalue = 23
print(f"obj.tenXvalue is : {obj.tenXvalue}")
obj.show()