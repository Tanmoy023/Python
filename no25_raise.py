a = input("Enter the number in between 5 to 10 : ")
if a == "quit":
    print("oky")
elif(a > 5 or a < 9):
    raise ValueError("This is no required number")