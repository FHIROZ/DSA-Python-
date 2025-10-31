def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zeros = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros.append((i, j))
    for (i, j) in zeros:
        for k in range(n):
            matrix[i][k] = 0
        for k in range(m):
            matrix[k][j] = 0
    return matrix
matrix = [
    [1, 2, 3, 0],
    [5, 0, 7, 8],
    [9, 10, 11, 12]
]
result = setZeroes(matrix)
print("Final Matrix:")
for row in result:
    print(row)
