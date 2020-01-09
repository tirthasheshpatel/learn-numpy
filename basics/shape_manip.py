import numpy as np
from utils.print_det import print_det

# Let's first create two random arrays
# of size 2, 5
a = np.random.randint(low=0, high=10, size=10, dtype=np.int16).reshape(2, 5)
b = np.random.randint(low=0, high=10, size=10, dtype=np.int16).reshape(2, 5)
print(f"a=\n{a}")
print(f"b=\n{b}")

# Now, let's stack them horizontally
hstacked_ab = np.hstack((a, b))
print(f"hstacked_ab=\n{hstacked_ab}")

# Similarly, we can create a vertically stacked array!
vstacked_ab = np.vstack((a, b))
print(f"vstacked_ab=\n{vstacked_ab}")

# A general concantenation can be done
# by using the `concatenate` method!
# We need to specify axis along which
# we want to concatenate!
# axis=0 => concat along rows
# axis=1 => concat along cols
row_concat_ab = np.concatenate((a, b), axis=0)
print(f"row_concat_ab=\n{row_concat_ab}")

# Now, we can use the .T property to calculate the transpose
print(f"a.T=\n{a.T}")

