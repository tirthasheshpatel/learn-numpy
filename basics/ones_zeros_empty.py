import numpy as np
from utils.print_det import print_det

# Create a array with only zeros
zeros_a = np.zeros((2, 5), dtype=np.float32)

print_det(zeros_a)

# Create an array with the same dimentions
# and shape as an array `a` but the 
# values are initialized to zero.
zeros_like_a = np.zeros_like(zeros_a)

print_det(zeros_like_a)

# ones and ones_like are similar
ones_like_a = np.ones_like(zeros_a)

print_det(ones_like_a)

# empty and empty_like will create an
# empty (unititialized) array. When the
# data is printed, it behaves non-sense!
empty_like_a = np.empty_like(zeros_a)

print_det(empty_like_a)

