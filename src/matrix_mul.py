def matrix_mul(A, B, mod=None):
    """ 行列AとBの積を計算する
    """
    n = len(A)
    m = len(B[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(len(B)):
            for j in range(m):
                C[i][j] += A[i][k] * B[k][j]
                if mod is not None:
                    C[i][j] %= mod
    return C
