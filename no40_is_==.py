# is and == both are comparition operator
a = 4
b = "4"
print(f"a is b : {a is b}") # it check the identity(exact location of the object)
print(f"a is int(b) : {a is int(b)}")
print(f"a == b : {a == b}") # it check the value
print(f"a == int(b) : {a == int(b)}")

c = [1,2,3]
d = [1,2,3]
print(f"c is d : {c is d}") # just because of list is mutable it return False
print(f"c == d : {c == d}")

e = (4,5)
f = (4,5)
print(f"e is f : {e is f}") # just because of tuple is imutable it return True
print(f"e == f : {e == f}")
