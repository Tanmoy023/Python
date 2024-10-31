# If else
time = int(input("Enter current time : "))
AMorPM = input("Enter this time is AM or PM : ")
if (time<6)and(AMorPM == "am"):
    print("It is night time !!")
elif (time<12)and(AMorPM == "am"):
    print("Good Morning !!")
elif (time<6)and(AMorPM == "pm"):
    print("Good After noon !!")
elif (time<9)and(AMorPM == "pm"):
    print("Good Evining !!")
elif (time>9)and(time<12)and(AMorPM == "pm"):
    print("Good Night !!")
else :
    print("place enter the valid time !!")
    
# option = ["xiaomi","vivo","oppo","iphone"]
# print("Which is brand produce most costly phones ? \nChoice's are :")
# for i in range(len(option)):
#     print(i+1," for ",option[i])
# choice = int(input("Enter your choice : "))
# if(choice == 1 or choice == 2 or choice == 3):
#     print("your choice is worng !!")
# elif(choice == 4):
#     print("Congratulation \nyour choice is currect & you have win 1 coror ")
# else :
#     print("You choce out of choice !!")