# match case
age = int(input("Enter your age :\n1. 1-10 year \n2. 11-18 \n3. 18 plus \n"))
match age:
    case 1:
        print("You are a kid")
    case 2:
        print("You are a child")
    case 3:
        print("You are a adult")
    case _ if(age<=0):
        print("Invalid age !!")
    case _ if(age>100):
        print("are you sure your age is above 100:")
        choice = input("Enter yes or No : \n")
        match choice:
            case "yes":
                print("You age is ",age)
            case "no":
                print("place Reenter your age")
            case _:
                print("Next time choce yes or no !!")