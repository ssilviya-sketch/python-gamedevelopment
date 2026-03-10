matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# A matrix is a 3x3 dimension the first 3 is the numbers of rows and the 2nd three is the numbers of collums
print(matrix1)
print(len(matrix1))#to find the numbers of rows
print(len(matrix1[0]))#to find the numbers of collums
print(matrix1[2][0])
#printing the matrix 
for i in range(0,len(matrix1)) :
    for j in range(0,len(matrix1[0])) :
        print(matrix1[i][j],end = " ")
    print("\n")

