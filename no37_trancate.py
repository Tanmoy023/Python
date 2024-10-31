with open("no37_myFile.txt", "w") as f:
    f.write("Tanmoy Patra")
    f.truncate(6)  # restric the file size with 6 character length
    f.close()
with open("no37_myFile.txt", "r") as f2:
    print(f"after truncate(6) the containt : {f2.read()}")
    f2.close()
