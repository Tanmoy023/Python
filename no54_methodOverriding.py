class rtgShape:
    def __init__(self,h, w):
        self.h = h
        self.w = w
    def area(self):
        return self.h * self.w
class crclShape(rtgShape):
    def __init__(self, r):
        super().__init__(r,r)
    def area(self):
        return 3.14 * super().area()

rtg = rtgShape(10, 20)
print(f"the area of a rectangle is {rtg.area()}")
crcl = crclShape(15)
print(f"the area of a circle is {crcl.area()}")
