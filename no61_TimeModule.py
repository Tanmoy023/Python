import time

# def myWhile():
#     i = 0 
#     while(i<1000):
#         print(f"while - {i}")
#         i = i + 1
# def myFor():
#     for i in range(1000):
#         print(f"for - {i}")
# start = time.time()
# myWhile()
# whileEnd = time.time() - start
# myFor()
# forEnd = time.time() - start
# print(f"start : {start}, whileEnd : {whileEnd}, forEnd = {forEnd}")

# print("wait for 3 second")
# time.sleep(3)
# print("thanks for waition 3 seconds")

t = time.localtime()
formatedTime = time.strftime("%y / %m / %d -- %H : %M : %S")
print(f"formated time is : {formatedTime}")