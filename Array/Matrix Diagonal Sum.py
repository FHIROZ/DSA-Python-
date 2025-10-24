# 1572. Matrix Diagonal Sum
def matrix_diagonal(mat):
        n=len(mat)
        total=0
        for i in range(n):
            total+=mat[i][i] # primary diagonal
            total+=mat[i][n-i-1]
        if(n%2==1):
            return total-mat[n//2][n//2]
        return total

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
result=matrix_diagonal(mat)
print(result)
