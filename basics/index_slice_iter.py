import numpy as  np
from utils.print_det import print_det

# Generate a random array
a = np.random.randint(low=0, high=10, size=20, dtype=np.int32).reshape(4, 5)
print(a)

# Index!
print("a[0][0]:", a[0][0])
print("a[0][:]:", a[0][:])
print("a[0, :]:", a[0, :])
print("a[:, 0]:", a[:, 0])
print("a[:, :]:", a[:, :])

# Slice!
print("a[0:2, 0]:", a[0:2, 0])
print("a[0:2, :]:", a[0:2, :])
print("a[0:2, 2:5]:", a[0:2, 2:5])
print("a[:-1, 0:]:", a[:-1, 0:])
print("a[0:, :5:2]:", a[0:, :5:2])

# Iterate!
for rows in a:
    for i in rows:
        print(i, end=" ")
    print()

