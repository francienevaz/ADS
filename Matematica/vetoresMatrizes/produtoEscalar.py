import numpy as np

notas = np.array([[90, 85, 70, 100]])
pesos = np.array([[0.3, 0.3, 0.2, 0.2]])

# os respectivos componentes dos vetores são multiplicados e os resultados destas multiplicações são somados.

# É uma operação muito útil para obtermos, por exemplo, a média ponderada, ou seja, a média de um conjunto de dados onde cada um deles tem um determinado peso.

# No Python, o produto escalar é obtido pela função “inner()” da biblioteca numpy.

# a função inner vai multiplicar cada item da array, com os itens na posição correspondente, e fazer a soma

media = np.inner(notas, pesos)

print(media)