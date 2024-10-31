# Tuple
myTuple = (1,2,3,4,5,"red","green",True)
print(myTuple)
print(myTuple[0])
print(myTuple[1])
print(myTuple[5])
print(myTuple[7])
print(myTuple[-1])

if "red" in myTuple:
    print("red is present in myTuple")
else :
    print("red is not present in myTuple")

tuple2 = myTuple[0:5]
print(tuple2)