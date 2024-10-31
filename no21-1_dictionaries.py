myDict = {
    "Tanmoy" : "name",
    "CEMK" : "college",
    "CSE" : "depertment",
    23 : "college roll number"
}
# print(myDict["Tanmoy"])
# print(myDict["CSE"])
# print(myDict[23])

# print(myDict.get("CEMK")) # if serching key is not present in Dictionary so this syntex can't give error for outher word it return None .
# print(myDict.get("Year")) # proved

# print(myDict.keys())
# print(myDict.values())

# for i in myDict.keys(): # it is a way to get the dictionary value's
#     print(f"--> {i} is : {myDict[i]}")
for key, value in myDict.items(): # it is another way to get the dictionary value's
    print(f"--> {key} is : {value}")