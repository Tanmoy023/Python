class person:
    name = "Name Title"
    address = "Home Location"
    id = 123456789
    def info(self):
        print(f"details :: name:{self.name}, address:{self.address}, id:{self.id}")


pubg = person()
pubg.name = "ind->GodOfWar"
pubg.address = "Erangle"
pubg.id = "564641864565"

coc = person()
coc.name = "bgmi Tanmoy"
coc.address = "Multiplayer"
coc.id = "#6646561"

pubg.info()
coc.info()