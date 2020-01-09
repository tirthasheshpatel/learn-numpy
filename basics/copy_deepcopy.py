import numpy as np

# ---------------------------------------------------------------
# NO COPY

a = np.arange(12)

b = a # no copy is created. 

# a and b point at the same array object!
print(f"b is a: {b is a}") # evaluates to True

b.shape = 3, 4 # changes also reflect in `a`.

print(f"a.shape={a.shape}") # a.shape has changed to (3,4)

# numpy array is passed by referance
# to the function.
def f(x):
    return id(x)

# returns the same id as the function doesn't
# create a copy of the array object but passes
# it to the function by referance!
print(f"id(a): {id(a)}\tf(a): {f(a)}")

# ----------------------------------------------------------------
# VIEW OR SHALLOW COPY

a = np.arange(12)

# Creates a copy of a and assigns it to b
# but the copy still contains some information
# about the array copied!
b = a.view()

print(f"b is a: {b is a}") # False as copy of the array is created
print(f"b.base is a: {b.base is a}") # True as the array `b` is copied from `a`

# Canges to b will now not reflect in a!

# ---------------------------------------------------------------
# DEEP COPY

a = np.arange(12)

# Creates a deep copy. Meaning, the new array
# `b` has no information of its base array `a`!
b = a.copy()

print(f"b is a: {b is a}") # False as copy of the array is created
print(f"b.base is a: {b.base is a}") # False as `b` has no info of `a`

# --------------------------------------------------------------
# END OF MODULE

