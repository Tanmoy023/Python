double = lambda x: x*5 # make a function named 'double' which take argument 'x' and return 'x*5'
print(f"lamda function double(5) is : {double(5)}")

avg = lambda x, y : (x+y)/2
print(f"lamda function avg(5454,87) is : {avg(5454,87)}")

def double_add10(fn, n1): # 'n1' is take as argument which need for 'fn'
    return fn(n1)+10
print(f"double_add10(double, 20) which a function that contain another function, result : {double_add10(double, 20)}")