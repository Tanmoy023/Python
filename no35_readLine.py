# f = open("no35_myFile.txt", "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()


# f = open("no35_myFile.txt", "r")
# i = 0
# while True:
#     line = f.readline()
#     if not line:
#         break
#     i = i + 1
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Student no {i}, marks :{m1}, {m2}, {m3}")
# f.close()


f = open("no35_myFile2.txt", "w")
lines = ["line-1\n", "line-2\n", "line-3\n"]
f.writelines(lines)
f.close()
