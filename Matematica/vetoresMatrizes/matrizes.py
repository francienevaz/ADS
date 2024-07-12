import numpy as np


# Exemplo:
# Uma indústria de cadeiras gamer possui três modelos denominados de A, B e C, e possui duas fábricas chamadas de F1 e F2. Na fábrica F1, são produzidas as peças, e na fábrica F2 é feita a montagem das cadeiras.
# 

f1 = np.array([[400, 10], [480, 12], [600,15]])
f2 = np.array([[31, 11], [37, 11], [48, 11]])

CustoTotal = f1 + f2

print(CustoTotal)

# Sabendo que houve um aumento de 10% sobre os custos de fabricação das peças e sobre os respectivos custos de transporte, quais serão os valores após o aumento?

# Como o aumento foi de 10%, podemos dizer que o fator de aumento corresponde a 1,1, pois 100%+10%=110%=1,1. Para atualizarmos os valores, basta multiplicarmos os dados de F1 por 1,1. Podemos armazenar esses valores na própria matriz F1 por meio da expressão “F1=1.1*F1”.

F1 = 1.1 * f1

print(F1)