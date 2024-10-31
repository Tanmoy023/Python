# exeption handling

# number = input("Enter the number : ")
# try :
#     for i in range(1,11):
#         print(f"{i} * {int(number)} is {int(number)*i}")
# except :
#     print("something is worng !!")
    
try :
    number = int(input("Enter the number : "))
    a = [1,2,3,4,6,7]
    print(a[number])
except ValueError :
    print("There is some value error")
except IndexError :
    print("there is some index error")