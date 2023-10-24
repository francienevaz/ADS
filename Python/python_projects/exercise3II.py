def main(): 
    print("""
************* Seja Bem Vindo(a)s a Copiadora da Franciene Vaz *************
        """)

    def escolha_servico():
        while True:
            servico = input("""
                Digite o código do serviço desejado:
                    
                [DIG] - Digitalização
                [ICO] - Impressão Colorida
                [IBO] - Impressão em Preto e Branco
                [FOT] - Fotocópia
            """).upper()

            if servico not in ["DIG", "ICO", "IBO", "FOT"]:
                print("Código de Serviço Inválido!")
            else:
                return servico

    def num_pagina():
        while True:
            try:
                paginas = int(input("Entre com o número de páginas: "))
                if paginas < 0:
                    print("O número de páginas não pode ser negativo.")
                else:
                    return paginas
            except ValueError:
                print("Digite um valor válido para o número de páginas.")

    def servico_extra():
        while True:
            extra = 0
            opcao = input("""Deseja adicionar mais um serviço?
                Escolha uma opção:
                [1] - Encadernação Simples - R$10.00
                [2] - Encadernação Capa Dura - R$25.00
                [3] - Sem encadernação - Grátis
            """)
            
            if opcao not in ['1', '2', '3']:            
                print('Opção inválida')
            else:
                if opcao == '1':
                    extra += 10.00
                elif opcao == '2':
                    extra += 25.00
                else:
                    extra = 0

            return extra
    
    while True:
        servico = escolha_servico()
        paginas = num_pagina()

        serviceValue = {
            "DIG": 1.10,
            "ICO": 1.00,
            "IBO": 0.40,
            "FOT": 0.20
        }.get(servico, 0)

        descValue = 0
        if paginas < 10:
            descValue = 0
        elif 10 <= paginas < 100:
            descValue = 10
        elif 100 <= paginas < 1000:
            descValue = 15
        elif 1000 <= paginas < 10000:
            descValue = 20
        else:
            print("Excedeu o limite de páginas, digite um número de páginas menor!")
            continue            
        
        extra = servico_extra()
        valorTotal = (serviceValue * paginas) + extra
        desconto = (serviceValue * paginas) * descValue /100
        valorTotalDesconto = valorTotal - desconto

        print("Total: {:.2f} (serviço: {} * páginas: {} + extras: {})".format(valorTotalDesconto, serviceValue, paginas, extra))
        break

if __name__ == '__main__':
    main()
    