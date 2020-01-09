import numpy as np

a = np.arange(start=0, stop=10, step=1, dtype=np.float64).reshape(2,5)
b = np.linspace(start=0., stop=10.0, num=20, dtype=np.float64).reshape(5, 4)
c = np.arange(start=0, stop=20, step=1, dtype=np.float64).reshape(5, 4)

# Add two matrices
d = b + c
print(f"b=\n{b}")
print(f"c=\n{c}")
print(f"d=\n{d}\n")

# element-wise multiplication of two matrices
# Note that the shape of both the matrices
# must be the same. If they are not, then
# one of the matrix must have same one dimention
# and all the other dimentaions are different
e = b*c
print(f"b=\n{b}")
print(f"c=\n{c}")
print(f"e=\n{e}\n")

# Metrix Multiplication
f = a@b # OR f = np.dot(a,b)
print(f"a=\n{a}")
print(f"b=\n{b}")
print(f"f=\n{f}\n")

