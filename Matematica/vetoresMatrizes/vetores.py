import numpy as np;

# Considere o vetor v que armazena os preços de venda, em dólares, de algumas mercadorias anunciadas em um comércio eletrônico:
# v=(22, 12, 54, 89, 11)
# e o vetor u que armazena os respectivos preços de custo, também em dólares
# u=(18, 4, 39, 61, 8)
# Sabendo que a margem de contribuição corresponde ao preço de venda menos o preço de custo, obtenha o vetor m que contém as respectivas margens de contribuição, em dólares, destas mercadorias.

# vetores
v = np.array([[22, 12, 54, 89, 11]])

u = np.array([[18, 4, 39, 61, 8]])

m = v - u

print(m)

# Logo, as margens de contribuição, em dólares, são, respectivamente, US$ 4.00, US$ 8.00, US$ 15.00, US$ 28.00 e US$ 3.00.