# reference link : https://replit.com/@codewithharry/49-Day49-File-IO#main.py

# f = open("no34_myFile.txt", "r")  # if this file dose't exist it show error
# print(f)
# text = f.read()
# print(text)
# f.close()

# f2 = open("no34_myFile2.txt", "w")
# # if this file dose't exist it autometically create this file
# f2.write("writing this thing from no34_fileIO.py")
# # when this file in write mode it change the whole content of given file with those given massage
# f2.close()

# f3 = open("no34_myFile2.txt", "a")
# f3.write("appending this thing from no34_fileIO.py\n")
# # when this file in appending mode it add the given content on this file
# f3.close()

with open("no34_myFile2.txt", "a") as f4:
    f4.write("appending this thing from no35_fileIO.py\n")
