# def factorial(number):
#     if(number == 0 or number == 1):
#         return 1
#     else :
#         return number * factorial(number-1)
# number = int(input("Enter the number : "))
# print("Factorial of ",number,"is",factorial(number))

def fibonacci(number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
num = int(input("Enter the number : "))
print("The fibonacci of ",num ,"is",fibonacci(num))