import numpy as np
from utils.print_det import print_det

# Create an identity matrix
a = np.eye(3, dtype=np.float32) # creates a 3x3 Identity matrix
print_det(a)

# Create a matrix with random entries

# Sample floats from uniform distribution
unif_a = np.random.rand(2, 5)
print_det(unif_a)

# Sample floats from a gaussian distribution
gauss_a = np.random.randn(4, 5)
print_det(gauss_a)

# Sample integers in a given range from uniform distribution
unif_int_a = np.random.randint(low=0, high=10, size=20, dtype=np.int32).reshape(4, 5)
print_det(unif_int_a)

# Find the max of a array
# Axis specifies the axis from which
# you wnat to find the maximum
# axis not specified => find max from the entire array.
# axis = 0 => find max from rows.
# axis = 1 => find min from columns
# axis = -1 => find max from lant dimention
no_axis_max_unif_int_a = np.max(unif_int_a)
print(no_axis_max_unif_int_a)

row_max_unif_int_a = np.max(unif_int_a, axis=0)
print(row_max_unif_int_a)

col_max_unif_int_a = np.max(unif_int_a, axis=1)
print(col_max_unif_int_a)

last_axis_max_unif_int_a = np.max(unif_int_a, axis=-1)
print(last_axis_max_unif_int_a)

# Similar syntax goes with min.
# We can also use argmin, argmax, etc.

