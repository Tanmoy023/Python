# Function
# def calculateGmean(a, b): # ---> Required Argument's Function
#     Gmean = (a*b)/(a+b)
#     print(Gmean)
# a = 10
# b = 2
# calculateGmean(a, b)

# def fruit(first = "apple ", second = "banana ", third = "mango "): # --> Default Argument Function
#     print("fruit's are : ", first, second, third)
# fruit()
# fruit("watermelon")
# fruit(second="pineapple")

# def avarage(* number): # --> Variable Length Argument
#     sum = 0
#     for i in number:
#         sum = sum + i
#     print("The avarage  is : ",sum/len(number)) # --> len(number) is how much number we have take
# avarage(9,11)

def name(**full_name): # --> Return Argument Function
    print("Hellow ",full_name["firstName"], full_name["secondName"], full_name["thirdName"])
name(firstName = "Anup", secondName = "Kumar", thirdName = "patra")