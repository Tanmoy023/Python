def myGenerator():
    for i in range(1,5):
        yield i # it return a generator value and suspend the code
gen = myGenerator()

# print(next(gen))
# print(next(gen))
# print(next(gen))

for g in gen:
    print(g)