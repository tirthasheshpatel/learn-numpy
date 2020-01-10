import numpy as np

# Let's create a array
a = np.arange(12)
# We will create another array which we
# are going to use to index `a`
index_a = np.array([1, 3, 5, 7, 9, 11])

# this would print the elements
# with index as specified by the 
# elements of `index_a`
print(a[index_a])

# We can also use an array with different shape
# and index `a` using it. It will find the elements
# at the given index and return an array with
# the same shape as the array used to index it.
index_with_shape_a = np.array([[1, 3], [7, 9]])

print(a[index_with_shape_a])

# -------------------------------------------------
# MULTIDIMENATIONAL ARRAYS
# Say, we have an pallate of colors using
# which we want to create an image.

# Create a palatte of colors
palatte = np.array([
                    [0, 0, 0],
                    [255, 0, 0],
                    [0, 255, 0],
                    [0, 0, 255],
                    [255, 255, 255],
                    ])

# We can create the image by specifying
# which color we want to use for a pixel
image = np.array([
                    [1, 0, 2, 2],
                    [2, 3, 1, 4]
                    ])

print(palatte[image])

# Lastly, we can also index a two dimentional
# array using two different arrays of same
# dimentions.
a = np.arange(start=0, stop=20, step=1, dtype=np.int16).reshape(4, 5)

index_row = np.array(
                    [[0, 1], 
                    [1, 2]]
                    )

index_col = np.array(
                    [[2, 1],
                    [3, 3]]
                    )

print(a[index_row, index_col])

