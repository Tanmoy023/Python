with open("no36_myFile.txt", "r") as f:
    print(type(f))
    f.seek(10)  # for f.read(n) the actual starting index is now after 10 character
    print(
        f"current position of the file on where reading/other operation is completed : {f.tell()}"
    )
    data = f.read(5)  # from starting index read 5 character
    print(f"now f.tell() is : {f.tell()}")
    print(f"after seek(10) the f.read(5) is : {data}")
    f.close()
