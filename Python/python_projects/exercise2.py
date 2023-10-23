# Definindo as variáveis globais
quantidade_total_cp = 0  # Quantidade total de Cupuaçu
quantidade_total_ac = 0  # Quantidade total de Açaí
total_pedido = 0

# menu[sabor][tamanho] - como acessar o preço de cada item

menu = {
    'CP': {'P': 10.00, 'M': 15.00, 'G': 19.00},
    'AC': {'P': 12.00, 'M': 17.00, 'G': 21.00}
}

while True:
    print('''
    == Seja Bem Vindos - Açaí da Franciene Vaz ==

    =================== Menu ===================
    ---| Tamanho | Açaí [AC] | Cupuaçu [CP] |---
    ---|    P    |  $12,00   |    $10,00    |---
    ---|    M    |  $17,00   |    $15,00    |---
    ---|    G    |  $21,00   |    $19,00    |---
    ============================================

            Obrigada e volte sempre!
    ''')

    sabor = input("Escolha o sabor: (CP ou AC) ").upper()

    # Se o sabor não estiver no menu...
    if sabor not in menu:
        print("Sabor Inválido. Tente novamente!")
        continue

    tamanho = input("Escolha um tamanho (P/M/G): ").upper()

    # Se o tamanho não estiver no menu[sabor]...
    if tamanho not in menu[sabor]:
        print("Tamanho inválido. Tente novamente!")
        continue

    quantidade = int(input('Digite a quantidade desejada: '))

    preco_item = menu[sabor][tamanho]
    total_item = quantidade * preco_item

    quantidade_total_cp += quantidade if sabor == 'CP' else 0
    quantidade_total_ac += quantidade if sabor == 'AC' else 0

    total_pedido += total_item

    print(f'Você escolheu um {sabor} {tamanho} no valor de: R${preco_item:.2f}')
    print(f'Total do item: R${total_item:.2f}')

    opcao = input('Deseja incluir mais alguma coisa? Digite S para SIM e N para NÃO: ')
    # Se for digitado S, é retornado ao início do loop

    if opcao.upper() == 'N':
        print(f'Total do seu pedido: R${total_pedido:.2f}')
        break

