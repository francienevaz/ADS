from scipy.interpolate import *

x = [1, 2, 3, 4]
y = [80, 95, 110, 122]
p = lagrange(x, y)
print(p)
