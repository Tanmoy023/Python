import os

if(not os.path.exists("dataF")): # it check in currently working folder if there is and folder which named dataF is present so it return false
    os.mkdir("dataF")

for i in range (0, 10):
    if(not os.path.exists(f"dataF/subData_{i+1}")):
        os.mkdir(f"dataF/subData_{i+1}") # it create subData_n folder in the path of dataF

print(f"current working directory is : {os.getcwd()}")

# os.chdir("/User") # change the current directory into /User

# Reference Link : https://www.w3schools.com/python/module_os.asp