def main(): 
    print("""
            *** Seja Bem Vindo(a)s a Copiadora da Franciene Vaz ***
        """)

    def escolha_servico():
        servico = input("""
                Digite o código do serviço desejado:
                    
                [DIG] - Digitalização
                [ICO] - Impressão Colorida
                [IBO] - Impressão em Preto e Branco
                [FOT] - Fotocópia

            """).upper()
        print(servico)

        if (servico not in ["DIG", "ICO", "IBO", "FOT"]):
                print ("Código de Serviço Inválido!")
                servico = input("""
                Digite o código do serviço desejado:
                    
                [DIG] - Digitalização
                [ICO] - Impressão Colorida
                [IBO] - Impressão em Preto e Branco
                [FOT] - Fotocópia

            """).upper()

    def num_pag():
        try:
            while True:
                paginas = int(input("Entre com o número de páginas: "))
                serviceValue = 0
                descValue = 0

                    if servico == "DIG":
                        serviceValue += 1.10
                    elif servico == "ICO":
                        serviceValue += 1.00
                    elif servico == "IBO":
                        serviceValue += 0.40
                    elif servico == "FOT":
                        serviceValue += 0.20
                    else:
                        pass
                                
                    if paginas < 10:
                        descValue = 0
                    elif paginas  >= 10 and paginas < 100:
                        descValue = 10
                    elif paginas >= 100 and paginas < 1000:
                        descValue = 15
                    elif paginas >= 1000 and paginas < 10000:
                        descValue = 20
                    else:
                        print("Excedeu o limite de páginas, digite um número de páginas menor!")
                        num_pag()

                valorTotal = (serviceValue * paginas)
                desconto = (valorTotal * descValue)/100
                valorTotalDesconto = valorTotal - desconto

                print("Total: {:.2f} (serviço: {} * páginas: {}) ".format(valorTotalDesconto, serviceValue, paginas))
        except ValueError:
        print("\n Ocorreu um erro, digite um valor válido!") 

    def servico_extra():
        extra = 0
        opcao = float(input("""Deseja adicionar mais um serviço?
                                Escolha uma opção:
                                [1] - Encadernação Simples - R$10.00
                                [2] - Encadernação Capa Dura - R$25.00
                                [3] - Sem encadernação - Grátis
                                """))
        print(opcao)

        if opçao not in ['1', '2', '3']:
            opcao = float(input("""Deseja adicionar mais um serviço?
                                Escolha uma opção:
                                [1] - Encadernação Simples - R$10.00
                                [2] - Encadernação Capa Dura - R$25.00
                                [3] - Sem encadernação - Grátis
                                """))
            print(opcao)
        else:
            if opcao == 1:
                extra += 10.00
            elif opcao == 2:
                extra += 25.00
            else:
                extra = 0

valorTotal = (serviceValue * paginas) + extra
desconto = (valorTotal * descValue)/100
valorTotalDesconto = valorTotal - desconto

print("Total: {:.2f} (serviço: {} * páginas: {} + extras: {}) ".format(valorTotalDesconto, serviceValue, paginas, extra))
 
    