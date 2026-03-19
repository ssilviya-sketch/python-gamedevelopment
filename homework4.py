m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[12,34,66],[56,78,44],[11,22,33]]
addresult = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        addresult[i][j] = m1[i][j]+m2[i][j]
for i in range(3):
    for j in range(3):
       print(addresult[i][j],end = " ")
    print("\n")