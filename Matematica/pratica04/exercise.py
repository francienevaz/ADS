import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import*

# Utilize o Python para gerar um conjunto de números inteiros que variam de -10 a 20. Em seguida, verifique se o número -1 está neste conjunto.

C = np.linspace(-10, 20, 31)

# print(C)

# print(-1 in C)

# . Em seguida, verifique se o número -11 está neste conjunto.

# print(-11 in C)

# Verifique, por meio do Python, se o valor R$ 350,00 está neste conjunto.

S={100, 112, 120, 130, 136, 151, 180, 200, 240, 260, 300, 350, 380, 415, 465, 510,
540, 545, 622, 678, 724, 788, 880, 937, 954, 998, 1039, 1045, 1100, 1212}

# print(350 in S)

# Para a entrada em uma residência, foram criadas 5 senhas numéricas: 452012, 323233, 787910, 528917 e 683524. Por meio do Python, crie um programa que armazena estas senhas em um conjunto e verifica se a senha digitada pelo usuário está ou não neste conjunto para permitir ou proibir a entrada na residência.

keys = [452012, 323233, 787910, 528917, 683524]

def liberarAcesso():
    while True:
        try:
            senha = int(input("Digite a senha: "))
            if senha in keys:
                print("Acesso liberado!")
                break
            else:
                print("Acesso negado!Tente Novamente!")
        except ValueError:
                print("Acesso negado!Tente Novamente!")


# liberarAcesso()

#  O vetor v contém os preços de venda de algumas mercadorias:
# v=(1210, 897, 1230, 1495, 799, 890, 1010)
# A loja está com uma promoção onde é dado um desconto de 20% em todas as
# mercadorias. Por meio do Python, obtenha o vetor que contém os preços destas
# mercadorias com o desconto.

v = np.array([1210, 897, 1230, 1495, 799, 890, 1010])
desconto = v*0.8
# print(desconto)


#  Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u+v utilizando o Python.

vetores  = np.array([10, 12, -1])
u = np.array([3, 4, 8])
print(vetores+u)

#  Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u-v utilizando o Python.

print(vetores-u)

#  Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u.v utilizando o Python.

print(u*vetores)

# Utilize o Python para obter a matriz C=A+B.

A = np.array([[3,5,9], [4,2,-3], [1,5,-5]])
B = np.array([[12,-6,7], [3,0,2], [-1,10,1]])
CII = A + B
print(CII)

# Por meio do Python, obtenha a matriz C=A.B.

CIII = A*B
print(CIII)

# Construa o gráfico da função y=x3-2x2+12x-1 no intervalo [-3, 4].

x = np.linspace(-3, 4)
y = x**3 - 2 * x**2 + 12 * x - 1

plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^3 - 2x^2 + 12x -1')
plt.show()

# Quais são as coordenadas do vértice da função f(x)=-2^2+21x-8?

a = -2
b = 21
c = -8

# Calculando o valor de x no vértice
xv = -b / (2 * a)
print("Vértice no eixo x: " + str(xv))

# Calculando o valor de y no vértice
delta = b**2 - 4 * a * c
yv = -delta / (4 * a)
print("Vértice no eixo y: " + str(yv))

# Uma empresa produz carregadores para um determinado modelo de telefone  celular e precisa obter a função que relaciona o lucro mensal com o preço de venda dos carregadores. Os custos fixos mensais da empresa correspondem a R$ 47.500,00. Para um preço de venda de R$ 12,00 por unidade, o lucro mensal corresponde a R$ 22.000,00. Quando cada carregador é vendido por R$ 20,00, o lucro mensal é de R$ 20.450,00. Obtenha o polinômio interpolador que relaciona o lucro y com o preço de venda x.

xI = [0, 12, 20]

yI = [-47500, 22000, 20450]

p = lagrange(xI, yI)

print(p)



