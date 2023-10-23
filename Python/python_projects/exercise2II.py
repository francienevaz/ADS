# Definindo as variáveis globais
quantidade_total_cp = 0  # Quantidade total de Cupuaçu
quantidade_total_ac = 0  # Quantidade total de Açaí
total_pedido = 0

while True:
    print('''
    == Seja Bem Vindos - Açaí da Franciene Vaz ==
              
    =================== Menu ===================
    ---| Tamanho |   Açaí    |   Cupuaçu    |---
    ---|    P    |  $12,00   |    $10,00    |---
    ---|    M    |  $17,00   |    $15,00    |---
    ---|    G    |  $21,00   |    $19,00    |---
    ============================================

            Obrigada e volte sempre!
    ''')

    sabor = input("Escolha o sabor: (CP ou AC) ")

    if sabor.upper() not in ['CP', 'AC']:
        print("Sabor Inválido. Tente novamente.")
        continue  # Volte ao início do loop
    else:
        tamanho = input("Escolha um tamanho (P/M/G): ")
        if tamanho.upper() not in ['P', 'M', 'G']:
            print("Tamanho inválido. Tente novamente.")
            continue # Volte ao início do loop
        else:
            if sabor == 'CP':
                if tamanho.upper() == 'P':
                    valor = 10.00
                elif tamanho.upper() == 'M':
                    valor = 15.00
                else:
                    valor = 19.00

                quantidade = float(input('Digite a quantidade desejada: '))
                quantidade_total_cp += quantidade
                total_pedido += quantidade * valor
                print(f'Você escolheu um Cupuaçu {tamanho.upper()} no valor de: R${valor:.2f}')

            elif sabor == 'AC':
                if tamanho.upper() == 'P':
                    valor = 12.00
                elif tamanho.upper() == 'M':
                    valor = 17.00                     
                else:
                    valor = 21.00

                quantidade = int(input('Digite a quantidade desejada: '))
                quantidade_total_ac += quantidade
                total_pedido += quantidade * valor
                print(f'Você escolheu um Açaí {tamanho.upper()} no valor de: R${valor:.2f}')

    opcao = input('Deseja incluir mais alguma coisa? Digite S para SIM e N para NÃO: ')

    if opcao.upper() == 'N':
        print(f'Total do seu pedido: R${total_pedido:.2f}')
        print(f'Quantidade total de Cupuaçu: {quantidade_total_cp}')
        print(f'Quantidade total de Açaí: {quantidade_total_ac}')
        break
