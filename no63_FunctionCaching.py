from functools import lru_cache
import time

@lru_cache(maxsize=None)
def sleep2(n):
    time.sleep(5)

sleep2(2) # after complete sleep2(2) it store its corresponding value in cache memory and next time if sleep2(2) will call it fetch and return the result from cache memory
print("sleep2(2) done")
sleep2(4)
print("sleep2(4) done")
sleep2(6)
print("sleep2(6) done")

sleep2(2)
print("sleep2(2) done")
sleep2(4)
print("sleep2(4) done")
sleep2(6)
print("sleep2(6) done")