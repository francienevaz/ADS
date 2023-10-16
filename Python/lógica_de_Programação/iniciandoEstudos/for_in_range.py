# # Função range
# # Range é uma função built-in do Python, ela é usada para
# # produzir uma sequência de números inteiros a partir de um
# # ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(i, j)
# # será produzido:
# # i, , i+1, i+2, i+3, ..., j-1.
# # Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e
# # step opcional.

# # range
# # range(stop) -> range object
# # range(start, stop[, step]) - > range object
# print(list(range(4))) # se printarmos somente range(4) ele não retorna a lista detalhada

# # Utilizando range com for
# for numero in range(0, 11):
#   print(numero, end=" ")
# # >>> 0 1 2 3 4 5 6 7 8 9 10

# # exibindo a tabuada do 5
# for numero in range(0, 51, 5):
#   print(numero, end=" ")
# # >>> 0 5 10 15 20 25 30 35 40 45 50

for i in range(100,1000,10):
  print(i)
print("terminou")

i = 100
while i <= 999:
  print(i)
  i += 10