import numpy as np
from utils.print_det import print_det

# Create an array consisting all zeros
zeros_a = np.zeros((3,5), dtype=np.float64)

print_det(zeros_a)

# Create an array consisting of all ones
ones_a = np.ones((3,5), dtype=np.float64)

print_det(ones_a)

# Create an array of evenly spaced 
# continuous integers in a given range
arange_a = np.arange(start=0, stop=15, step=1, dtype=np.float32)

print_det(arange_a)

