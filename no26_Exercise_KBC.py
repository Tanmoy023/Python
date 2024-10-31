Questions = [["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],
["Who are the host of KBC ? ", "akshay kr.", "sarukh khan", "sanjay datt", "amitab bachan"],]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
for i in range(0, len(Questions)):
    Question = Questions[i]
    print(f">> This question for rs. {levels[i]}")
    print(f"\t1.{Question[0]} \n\t1. {Question[1]}   2. {Question[2]}   3. {Question[3]}   4. {Question[4]}")
    money = 0
    # print(f">>>>>{Question[-1]}")
    reply = int(input("\tEnter your answer : "))
    answer = Question[reply]
    if(answer == Question[4]):
        print(f"<<< your answer is right & you won rs.{levels[i]} >>>\n")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("wrong answer !")
        break