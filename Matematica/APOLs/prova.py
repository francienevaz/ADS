import numpy as np

# Considere os números a = 7.0102*10**5 e b= 2.1233*10**3 na notação científica normalizada. Por meio do Python, calcule a+b apresentando o resultado com 10 casas decimais:

a = 7.0102e5
b = 0.021233e3
c = a + b

print(c)

print(f'{c:.10f}')

print('%.10e'%c)

