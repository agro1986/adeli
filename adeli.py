# Adeli: A Deep Learning Library
# By Agro Rachmatullah
# agro1986@gmail.com


def matrix(i, j):
    return [[0 for _ in range(j)] for _ in range(i)]


def matrix_row(m):
    return len(m)


def matrix_col(m):
    return len(m[0])


def dot(x, y):
    len1 = len(x)
    len2 = len(y)
    if len1 != len2:
        raise ValueError(f"The size of x ({len1}) does not match y ({len2}).")

    total = 0
    for i in range(0, len1):
        total += x[i] * y[i]

    return total

