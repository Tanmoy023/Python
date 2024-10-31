# a = False
# # print(a=True) # in general case, within a expression you can't assign anything
# print(a := True) # using walrus operator, you can assign within a expression

# numbers = ["krishmoy","Tanmoy","shirsendu", "rahul dev", "divendu", "suvendu"]
# while((n := len(numbers))>0):
#     print(f"length of numbers is : {n}")
#     print(f"numbers.pop() : {numbers.pop()}")

foods = list()
while(food := input("Enter what food you like : ")) != "exit":
    foods.append(food)
print(f"you lik this food's : {foods}")