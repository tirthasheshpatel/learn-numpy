import numpy as np

# Sample to random arrays to work with
a = np.random.randint(low=0, high=10, size=20, dtype=np.int32).reshape(4,5)
b = np.random.randint(low=0, high=10, size=10, dtype=np.int32).reshape(5,2)

# Compute the sin and cos operations on the arrays
# `np.sin` computes the element-wise sin operation.
c = np.sin(a)
d = np.cos(a) # similar to `np.sin`

# Compute e^x element-wise
e = np.exp(a)


