dict1 = {"a":0,"u":0,"o":0,"e":0,"i":0}
question = str(input("enter the vowels"))
for i in question :
   if i.isalpha :
      if i in dict1 :
         dict1[i] = dict1[i] + 1
if dict1["a"] == 1 and dict1["u"] == 1 and dict1["o"] == 1 and dict1["e"] == 1 and dict1["i"] == 1 :
 print("Its contains all vowels")
else :
 print("It does not contain all vowels")
