# Tuple Method
countries = ("india", "rusia", "america", "france", "brazil")
# print(countries)
temp = list(countries)
temp.append("italy") # add
temp.pop(2) # remove
temp[2] = "germany" #change
countries = tuple(temp)
print(countries)

# tuple1 = (1,2,3,4,5)
# tuple2 = (6,7,8,9,10)
# sumTuple = tuple1 + tuple2
# print(sumTuple)

# tuple1 = (1,3,2,4,5,3,10,2,2,3,2,1,3,1,)
# length = len(tuple1)
# print("Length of tuple is : ",length)
# count = tuple1.count(3)
# print("total no 3 is : ",count)
# index = tuple1.index(10)
# print("index no. of 10 is : ",index)