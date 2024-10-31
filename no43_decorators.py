def greet(fx):
    def mfx(*args): # *args take argument as tuple & **kwargs take argument as disconary
        print("Wellcome and thank you for using this")
        fx(*args)
        print("Every thing is done sucessfully")
    return mfx

@greet # now hellow() is a decorated function by greet()
def hellow():
    print("Hellow World")

@greet
def add(a,b):
    print(f"{a} + {b} is : {a+b}")
    return a+b

# greet(hellow)() # use it if you don't want to specify a function as a decorated function for all time. you don't need to add @decoratFunc in top of function when you use this syntax 
# hellow()

# greet(add)(2,3)
add(2,3)