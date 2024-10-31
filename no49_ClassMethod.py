class employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod # by using it if you make any changes in variables show it directly reflect in class variables
    def changeCompany(self,newCompany):
        self.company = newCompany # by default(with out using @classmethod) it change the company according to the self(object), not change the class variable directly

e1 = employee()
e1.name = "suvendu"
e1.show()
e2 = employee()
e2.name = "divendu"
e2.changeCompany("Lux")
e2.show()

print(f"now employee.company is : {employee.company}")