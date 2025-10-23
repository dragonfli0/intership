def FastMatrixExponentiation(D, n, m):
    if n == 0:
        return [[1, 0], [0, 1]] # единичная 2×2 матрица
    if n % 2 == 0: # чётное значение
        Y = FastMatrixExponentiation(D, n/2, m)
        return Multiply2x2Matrices(Y, Y, m)
    else:
        Y = FastMatrixExponentiation(D, (n-1)/2, m)
        Y2 = Multiply2x2Matrices(Y, Y, m)
        return Multiply2x2Matrices(Y2, D, m)
def Multiply2x2Matrices(A, B, m):
    C = [[0, 0], [0, 0]]
    C[0][0] = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % m
    C[0][1] = (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % m
    C[1][0] = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % m
    C[1][1] = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % m
    return C
def FibonacciModuloM(n, m):
    M = [[0, 1], [1, 1]]
    P = FastMatrixExponentiation(M, n, m)
    return P[0][1]
print(FibonacciModuloM(*map(int, input().split())))