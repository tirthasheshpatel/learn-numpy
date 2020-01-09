import numpy as np

# Print all the details of an array
def print_det(a):
    # What did you just create?
    print(f"\ntype={type(a)}")

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

    # Print the array
    print(f"data=\n{a}\n")

