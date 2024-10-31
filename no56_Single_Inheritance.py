class animal:
    def legs(self):
        print("most of animal's have 4 legs")
    def nightVision(self):
        print("only some animal's able to see in night")

class cat(animal):
    def legs(self):
        super().legs()
        print("cat's also have 4 legs")
    def nightVision(self):
        super().nightVision()
        print("cat's are able to see in night")
    
a = animal()
c = cat()
c.legs()
c.nightVision()