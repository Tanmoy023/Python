# map, filter and reduce those are higher order function


def cube(x):
    return x**3
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newl = list(map(cube, l)) # map function take a function and a list/tuple/disctionary for function argument
print(f"newl is : {newl}")


def more125(x):
    return x>125
newl2 = list(filter(more125, newl)) # if function return True then it store this number otherwise dose't store 
print(f"newl2 is : {newl2}")


from functools import reduce
sum = lambda x, y : (x+y)
result = reduce(sum, newl2)
print(f"result of reduce(sum, newl2) is : {reduce(sum,newl2)}")