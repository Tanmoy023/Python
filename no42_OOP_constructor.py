class person:
    def __init__(self,name, occ):
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")

rln23 = person("Tanmoy Patra","Full stack Developer")
rln39 = person("Sankhadeep Gayan","Highly skilled pro player")
rln23.info()
rln39.info()