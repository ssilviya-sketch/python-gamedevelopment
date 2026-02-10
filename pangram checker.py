question = str(input("Enter the string"))
dict1 = {}
for c in question :
    if c.isalpha() :
        if c in dict1 :
            dict1[c] = dict1[c] + 1
        else :
            dict1[c] = 1
if len(dict1) == 26 :
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