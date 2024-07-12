import numpy as np

A = np.array([[3,1,3], [6,5,5]])
B = np.array([[100, 50], [50,100], [50,50]])

C = np.matmul(A, B)

print(C)