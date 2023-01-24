def matrix_mul(A, B, mod: int | None = None):
    """ 行列AとBの積を計算する

    Args:
        A, B: 行列
        mod (int): 各要素の剰余を求める際に指定する

    Returns:
        C: AとBの積
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
