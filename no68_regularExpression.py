import re

text = "Employment is a relationship between two parties regulating the provision of paid labour services. Usually based on a contract, one party, the employer, which might be a corporation, a not-for-profit organization, a co-operative, or any other entity, pays the other, the employee, in return for carrying out assigned work.[1] Employees work in return for wages, which can be paid on the basis of an hourly rate, by piecework or an annual salary, depending on the type of work an employee does, the prevailing conditions of the sector and the bargaining power between the parties. Employees in some sectors may receive gratuities, bonus payments or stock options. In some types of employment, employees may receive benefits in addition to payment. Benefits may include health insurance, housing, and disability insurance. Employment is typically governed by employment laws, organisation or legal contracts. Malary, "

# pattern = "salary"
# pattern = r"[A-Z]alary"
pattern = r"[A-Z]+alary"

match = re.search(pattern,text)
# print(match)
matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    # print(type(match.span()))
    print(text[match.span()[0]:match.span()[-1]])