import numpy as np

# First, let's sample from the gaussian(0, 1) distribution
a = np.random.randn(5, 5)

# We know that the mean of the gaussian is near 0.
# Let's find it using numpy
no_axis_mean_a = np.mean(a) # alternatively, a.mean()
print(no_axis_mean_a)

# find mean of rows
row_mean_a = np.mean(a, axis=0)
print(row_mean_a)

# find mean along columns
col_mean_a = np.mean(a, axis=1)

# find mean along the last dimention
last_axis_mean_a = np.mean(a, axis=-1)
print(last_axis_mean_a)

# var => finds variance similar args as mean
# std => finds standard diviation
row_var_a = np.var(a, axis=0)
print(row_var_a)

row_std_a = np.std(a, axis=0)
print(row_std_a)

# calculate the sum of the array
no_axis_sum_a = np.sum(a)
print(no_axis_sum_a)

row_sum_a = np.sum(a, axis=0)
print(row_sum_a)

col_sum_a = np.sum(a, axis=1)
print(col_sum_a)

# cumulative sum
row_cumsum_a = np.cumsum(a, axis=0)
print(row_cumsum_a)

# sort an array
sorted_a = np.sort(a) # we can also specify axis!
print(sorted_a)

