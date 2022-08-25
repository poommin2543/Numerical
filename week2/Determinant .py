import numpy as np

# a = np.array([[3, -2,-1], [-4, 7,-1],[-6,9,-3]])
# a = np.array([[12, -2,-1], [0, 7,-1],[0,9,-3]])
# a = np.array([[3, 12,-1], [-4, 0,-1],[-6,0,-3]])
a = np.array([[3, -2,12], [-4, 7,0],[-6,9,0]])
d = np.linalg.det(a)

print(d)