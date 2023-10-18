quantidade_total = 0
total_pedido = 0

while True:

    print('''
    == Seja Bem Vindos - Açaí da Franciene Vaz ==
    ''')
    print('''
        
    =================== Menu ===================
    ---| Tamanho |   Açaí    |   Cupuaçu    |---
    ---|    P    |  $12,00   |    $10,00    |---
    ---|    M    |  $17,00   |    $15,00    |---
    ---|    G    |  $21,00   |    $19,00    |---
    ============================================

            Obrigada e volte sempre!
    ''')

    print('''
        Qual sabor você vai querer hoje:
        
        1 - Açaí 
        
        2 - Cupuaçu 
        
        ''')
    sabor = int(input("Digite aqui a opção escolhida (1 ou 2): "))
    tamanho = input("Escolha um tamanho (P/M/G): ")

    valor = 0
    quantidade = 0
    
    if sabor == 1:
        if tamanho.upper() == 'P':
            valor = 12.00
            quantidade += 1      
            
        elif tamanho.upper() == 'M':
            valor = 17.00
            quantidade += 1         
            
        elif tamanho.upper() == 'G':
            valor = 21.00
            quantidade += 1
        else:
            print('Tamanho inválido')

        print(f'Você escolheu um Acaí {tamanho.upper()} no valor de: R${valor:.2f}')


    elif sabor == 2:
        if tamanho.upper() == 'P':
            valor = 10.00
            quantidade += 1         
        
        elif tamanho.upper() == 'M':
            valor = 15.00 
            quantidade += 1        
        
        elif tamanho.upper() == 'G':
            valor = 19.00
            quantidade += 1 
        
        print(f'Você escolheu um Cupuaçu {tamanho.upper()} no valor de: R${valor:.2f}')
    else:
        print('\nOpção inválida, por favor digite novamente!\n')

    opcao = input('Deseja incluir mais alguma coisa? Digite S para SIM e N para NÃO: ')

    if opcao.upper() == 'S':
        quantidade += float(input('\nDigite a quantidade desejada: '))
        quantidade_total += quantidade  # Atualize a quantidade total
        total_pedido += quantidade_total * valor  # Atualize o total do pedido
    elif opcao.upper() == 'N':
        print(f'Total do seu pedido: R${total_pedido:.2f}')
        break

# problema com cálculos resolvido
# falta tratar os erros, e usar o continue e break como é pedido na atividade