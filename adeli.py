# Adeli: A Deep Learning Library
# By Agro Rachmatullah
# agro1986@gmail.com


from math import sqrt


def matrix(i, j):
    return [[0.0 for _ in range(j)] for _ in range(i)]


def matrix_row(m):
    return len(m)


def matrix_col(m):
    return len(m[0])


def frobenius_norm(m):
    total = 0.0
    for i in range(matrix_row(m)):
        for j in range(matrix_col(m)):
            total += m[i][j] * m[i][j]
    return sqrt(total)


def dot(x, y):
    len1 = len(x)
    len2 = len(y)
    if len1 != len2:
        raise ValueError(f"The size of x ({len1}) does not match y ({len2}).")

    total = 0
    for i in range(0, len1):
        total += x[i] * y[i]

    return total


def is_diagonal(m):
    for i in range(matrix_row(m)):
        for j in range(matrix_col(m)):
            if i == j:
                continue
            if m[i][j] != 0:
                return False
    return True


def matrix_diagonal(v):
    size = len(v)
    m = matrix(size, size)
    for i in range(size):
        m[i][i] = v[i]
    return m


def matrix_identity(n):
    return matrix_diagonal([1.0] * n)


def is_identity(m):
    row = matrix_row(m)
    col = matrix_col(m)
    if row != col:
        return False
    for i in range(row):
        for j in range(col):
            if i == j:
                if m[i][j] != 1.0:
                    return False
            elif m[i][j] != 0.0:
                return False
    return True


def elementwise_product(m, n):
    row = matrix_row(m)
    col = matrix_col(m)
    row2 = matrix_row(n)
    col2 = matrix_col(n)
    if row2 != row or col2 != col:
        raise ValueError(f"The size of m ({row}x{col}) does not match n ({row2}x{col2}).")
    o = matrix(row, col)
    for i in range(row):
        for j in range(col):
            o[i][j] = m[i][j] * n[i][j]
    return o


def matrix_equal(m, n):
    row = matrix_row(m)
    col = matrix_col(m)
    row2 = matrix_row(n)
    col2 = matrix_col(n)
    if row2 != row or col2 != col:
        return False
    for i in range(row):
        for j in range(col):
            if m[i][j] != n[i][j]:
                return False
    return True

def matrix_transpose(m):
    row = matrix_row(m)
    col = matrix_col(m)
    mt = matrix(col, row)
    for i in range(row):
        for j in range(col):
            mt[j][i] = m[i][j]
    return mt

def matrix_is_square(m):
    return matrix_row(m) == matrix_col(m)


def matrix_is_symmetric(m):
    mt = matrix_transpose(m)
    return matrix_equal(m, mt)
