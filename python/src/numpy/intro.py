import numpy as np


ar = np.array([
    [1, 3, 4],
    [4, 6, 8],
    [4, 6, 8],
    [4, 3, 7]
])

print(dir(ar))

print(ar.ndim, ar.shape, ar.size, ar.dtype, ar.itemsize, ar.data)


print(ar.reshape(2,2,3))


a = np.arange(12).reshape(2,3,2)
print(a)
print(a.transpose().shape)
print(np.linspace(0, 10, 4,endpoint=False))




