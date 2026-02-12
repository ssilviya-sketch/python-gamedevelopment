question = str(input("Enter the number pangram"))
dict1 = {}
for i in question :
    if i.isdigit() :
        if i in dict1 :
            dict1[i] = dict1[i] + 1
        else :
            dict1[i] = 1
if len(dict1) == 10 :
    status = True
    for v in dict1.values() :
        if v == 0 :
            status = False
    if status == True :
        print("Its a pangram")
    else :
        print("Its not a pangram")
else :
    print("Its not a pangram")