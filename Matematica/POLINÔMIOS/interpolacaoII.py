import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Uma empresa produz carregadores para um determinado modelo de telefone celular e precisa obter a função que relaciona o lucro mensal com o preço de venda dos carregadores. Os custos fixos mensais da empresa correspondem a R$ 50 000,00. Para um preço de venda R$15,00 por unidade, o lucro mensal corresponde a R$ 30 000,00. Quando cada carregador é vendido por R$17,00, o lucro mensal é de R$28 000,00. Obtenha o polinômio interpolar que relaciona o luvro y com o preço de venda x.

# Dados fornecidos
precos = np.array([15, 17])
lucros = np.array([30000, 28000])

# Interpolação pelo método de Lagrange
polinomio = lagrange(precos, lucros)

# Exibir o polinômio
print("Polinômio interpolador de Lagrange:")
print(polinomio)

# Avaliar o polinômio em um conjunto de pontos para plotar
x_vals = np.linspace(14, 18, 400)
y_vals = polinomio(x_vals)

# Plotar o polinômio
plt.plot(x_vals, y_vals, label="Polinômio interpolador")
plt.scatter(precos, lucros, color='red', label="Pontos fornecidos")
plt.xlabel("Preço de venda (x)")
plt.ylabel("Lucro mensal (y)")
plt.title("Interpolação Polinomial de Lagrange")
plt.legend()
plt.grid(True)
plt.show()

# Função para encontrar o valor do lucro para um preço específico
def lucro_para_preco(preco):
    return polinomio(preco)

# Testar a função com um preço específico
preco_teste = 16
lucro_estiamdo = lucro_para_preco(preco_teste)
print(f"Para o preço de venda {preco_teste}, o lucro estimado é: {lucro_estiamdo}")
