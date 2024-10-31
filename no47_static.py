class myClass:
    def __init__(self,num):
        self.num = num
    def add_in_num(self,num):
        self.num = self.num + num
    @staticmethod # it help to write method without using self
    def add(a,b):
        return a+b
c = myClass(23)
print(f"c.num : {c.num}")
c.add_in_num(39)
print(f"c.num : {c.num}")
print(f"c.add(5,7) : {c.add(5,6)}")
print(f"myClass.add(5,7) : {myClass.add(5,6)}")