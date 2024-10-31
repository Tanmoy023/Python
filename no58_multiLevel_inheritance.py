class animal:
    def __init__(self,name, species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"the name of the anima is : {self.name} and his species is : {self.species}")

class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name, species="dog")
        self.breed = breed
    def show_details(self):
        super().show_details()
        print(f"The breed of this dog is : {self.breed}")

class husky(dog):
    def __init__(self, name, env):
        super().__init__(name, breed = "husky")
        self.env = env
    def show_details(self):
        super().show_details()
        print(f"in {self.env} environment husky's are live")

h = husky("Hunter","cold")
h.show_details()