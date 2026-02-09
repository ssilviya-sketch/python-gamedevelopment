dict1 = {"henry":1,"maya":2,"jjj":4}
print(dict1)
dict1["Mika"] = 1
print(dict1)
for i in dict1 :
    print(str(i)+":"+str(dict1[i]))
    for key in dict1.keys() :
        print(key)
    for values in dict1.values() :
        print(values)
    for items in dict1.items() :
        print(items)