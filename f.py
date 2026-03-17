#program for addition or substraction for 2d list matrix
m2 = [[1,2],[4,5]]
m3 = [[12,34],[56,78]]
addresult = [[0,0],[0,0]]
subtractresult = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        addresult[i][j] = m2[i][j]+m3[i][j]
for i in range(2):
    for j in range(2):
        print(addresult[i][j],end = " ")
    print("\n")
for i in range(2):
    for j in range(2):
        subtractresult[i][j] = m2[i][j]-m3[i][j]
for i in range(2):
    for j in range(2):
        print(subtractresult[i][j],end = " ")
    print("\n")
#square matrix means when the number of rows and collums are the same
ma = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#accesing diagonal entrys in a square matrix
for i in range(4):
    print(ma[i][i])