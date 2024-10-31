def f1():
    try:
        num = int(input("Enter the number : "))
        list = [100,101,102,103,104,105]
        print(list[num])
        return 1
    except:
        print("some problem is occor !!")
        return 0
    finally:
        print("finally it is executed")
print(f1())