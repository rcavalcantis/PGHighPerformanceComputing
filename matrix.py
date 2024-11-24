

def mult_matrixis(A, B):
    nRowA = len(A)
    nColA = len(A[0])
    nColB = len(B[0])

    M = []

    for row in range(nRowA):
        M.append([])
        for col in range(nColB):
            M[row].append(0)
            for k in range(nColA):
                M[row][col] += A[row][k] * B[k][col]
    return M

A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[1,1,1], [1,1,1], [1,1,1]]

print(mult_matrixis(A, B))