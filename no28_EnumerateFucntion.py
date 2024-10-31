marks = [48,64,52,100,30,52,72]

# for index, marks in enumerate(marks):
#     print(marks)
#     if index == 3:
#         print("Exeellent")
        
for index, marks in enumerate(marks,start=2): # specify the start index is 2
    print(marks)
    if index == 3:
        print("Exeellent")