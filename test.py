from adeli import *

print("Hello")
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8]

#dot(1, 2)
print(dot(a, b))
#print(dot(a, c))

print("Done")

m = matrix(3, 2)
m[0][0] = 3.0
m[0][1] = 4.0
print(m)
print(matrix_row(m))
print(matrix_col(m))

print(frobenius_norm(m))
