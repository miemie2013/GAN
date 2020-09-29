

import numpy as np


a = np.zeros((2, 3, 3))

ai = np.array([[[0, 0, 0], [0, 255, 77], [0, 0, 0]]]).astype(np.int32)

n = 2

p = np.where(ai >= n)

ai[p] = n-1


np.put_along_axis(a, ai, 99, axis=0)


print()








