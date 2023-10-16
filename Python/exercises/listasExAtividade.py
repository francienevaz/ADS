# item = []
# mercado = []

# for i in range(3):
#     item.append(input('Nome do produto: '))
#     item.append(float(input('Preço do produto R$ ')))
#     item.append(int(input('quantidade: ')))
#     mercado.append(item[:])
#     item.clear()

# print(mercado)

# Outra forma de resolver o mesmo problema:

supermercado = []

for i in range(3):
    produto = input('Nome do produto: ')
    quantidade = int(input('quantidade: '))
    preco = float(input('Valor do produto R$: '))
    supermercado.append([produto, quantidade, preco])

print(supermercado)

soma = 0
print('Lista de Compras')
print('.' * 40)
print('Produto | Quantidade | Preço | Total do Item |')
for item in supermercado:
    print('{} | {} | {} | {} |'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += (item[1] * item[2])
    print('-' * 40)
print('Total a ser pago: {}'.format(soma))