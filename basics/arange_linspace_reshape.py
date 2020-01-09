import numpy as np
from utils.print_det import print_det

# Create an array with continuous floating
# point numbers given the starting and end point
# and number of samples to generate.
# arange can only be used (consistently)
# with integers.
linspace_a = np.linspace(start=0.0, stop=1.0, num=20)

print_det(linspace_a)

# We can `reshape` an array using the reshape
# method available for arrays. The arrays are NOT
# reshaped inplace.
reshaped_linspace_a = linspace_a.reshape(4,5)

print_det(reshaped_linspace_a)

# we can also reshape without specifying
# any one of the dimentions. We use `-1`
# for the dimention we don't what to explicitly
# specify!
reshape_linspace_a_again = linspace_a.reshape(-1, 5)

print_det(reshape_linspace_a_again)

