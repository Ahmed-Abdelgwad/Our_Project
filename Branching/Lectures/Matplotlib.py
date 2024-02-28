'''import numpy as np
import time

x = [1, -2, -5]
y = [4, 3, -1]


def dot(x, y):
    s = 0
    for xi, yi in zip(x, y):
        s += xi * yi
    return s


print("The dot product of x and y is", dot(x, y))

a = np.random.rand(1000000)
b = np.random.rand(1000000)


tic = time.time()
c = dot(a, b)
toc = time.time()
print("Dot product: ", c)
print("Time for the loop version:" + str(1000*(toc-tic)) + " ms")
tic = time.time()
c = np.dot(a, b)
toc = time.time()
print("Dot product: ", c)
print("Time for the vectorized version, np.dot() function: " +
      str(1000*(toc-tic)) + " ms")

i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
print("The dot product of i and j is", np.dot(i, j))
'''

import numpy as np

A = np.array([[4, 9, 9], [9, 1, 6], [9, 2, 3]])
print("Matrix A (3 by 3):\n", A)

B = np.array([[2, 2], [5, 7], [4, 4]])
print("Matrix B (3 by 2):\n", B)

mat_mmul = np.matmul(A, B)
mat_mmul2 = A @ B
print(mat_mmul)
print(mat_mmul2)
# try:
#    np.matmul(B, A)
# except ValueError as err:
#    print(err)

x = np.array([1, -2, -5])
y = np.array([4, 3, -1])

print("Shape of vector x:", x.shape)
print("Number of dimensions of vector x:", x.ndim)
print("Shape of vector x, reshaped to a matrix:", x.reshape((3, 1)).shape)
print("Number of dimensions of vector x, reshaped to a matrix:",
      x.reshape((3, 1)).ndim)

# try:
#    np.matmul(x.reshape((3, 1)), y.reshape((3, 1)))
# except ValueError as err:
#    print(err)
print(np.dot(A, B))
