class employee:
    def __init__(self, name , id):
        self.name = name
        self.id = id
class programer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name, id)
        self.lang = lang

e = employee("Sankha",39)
p = programer("Tanmoy",23,"python")
print(p.name,p.id,p.lang)