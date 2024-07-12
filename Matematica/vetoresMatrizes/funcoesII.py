import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 16, 100)
y = -340 * x**2 + 5700 * x - 9500

plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = -340x^2 + 5700x - 9500')
plt.show()

a = -340
b = 5700
c = -9500

# Calculando o valor de x no vértice
xv = -b / (2 * a)
print("Preço ótimo: " + str(xv))

# Calculando o valor de y no vértice
delta = b**2 - 4 * a * c
yv = -delta / (4 * a)
print("Lucro máximo: " + str(yv))
