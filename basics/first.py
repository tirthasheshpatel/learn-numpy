import numpy as np

a = np.array(
        [[1.1, 1.2, 1.3],
        [1.4, 1.5, 1.6],
        [1.7, 1.8, 1.9]],
        dtype = np.float64
        )

# What did you just create?
print(f"type={type(a)}")

# Print the number of dimentions of the array
print(f"dims={a.ndim}")

# Print the shape of the array (num_dim1, num_dim2, ..., num_dimk)
# for a k-dimentional array!
print(f"shape={a.shape}")

# print the size of the array (product of all members of shape)
print(f"size={a.size}")

# Print the dtype of elements present in the array
print(f"dtype={a.dtype}")

# Print the item size of items present in the array
print(f"itemsize={a.itemsize}")

