import os

folders = os.listdir("dataF")

for folderName in folders:
    print(folderName)
    print(os.listdir(f"dataF/{folderName}"))