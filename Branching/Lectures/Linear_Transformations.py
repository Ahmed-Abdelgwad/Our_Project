import numpy as np


def T(v):
    w = np.zeros((3, 1))
    w[0, 0] = 3*v[0, 0]
    w[2, 0] = -2*v[1, 0]

    return w


v = np.array([[3], [5]], dtype=np.dtype(int))
w = T(v)

print("Original vector:\n", v, "\n\n Result of the transformation:\n", w)
print(v.ndim)
