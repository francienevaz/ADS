print(''' ====== Seja Bem Vindos a Loja da Franciene Vaz! ====== \n''')
valor_do_produto = float(input("Digite aqui o valor do produto adquirido: \n R$"))
quantidade = float(input("Digite aqui quantos produtos você adquiriu: \n"))
valor_da_compra = float(valor_do_produto * quantidade)

porcentagem = 0

if valor_da_compra < 1000:
    porcentagem = 0
elif valor_da_compra  >= 1000 and valor_da_compra < 3000:
    porcentagem = 3
elif valor_da_compra > 3000 and valor_da_compra < 5000:
    porcentagem = 5
elif valor_da_compra > 5000:
    porcentagem = 8
else:
    print("Ocorreu um erro!")

desconto = (porcentagem/100) * valor_da_compra
total = valor_da_compra - desconto

print('\n Valor da sua compra sem desconto: R${:.2f}'.format((valor_da_compra)))
print('\n Valor da sua compra com o desconto aplicado: R${:.2f}\n'.format((total)))
print('''
========================================================
                Obrigada e volte sempre!
''')
