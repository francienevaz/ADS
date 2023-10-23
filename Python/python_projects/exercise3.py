print("""
        *** Seja Bem Vindo(a)s a Copiadora da Franciene Vaz ***
    """)
def servicos():
   servico = input("""
            Digite o código do serviço desejado:
                
            [DIG] - Digitalização
            [ICO] - Impressão Colorida
            [IBO] - Impressão em Preto e Branco
            [FOT] - Fotocópia

        """).upper() 
   paginas = int(input("Entre com o número de páginas: "))
   serviceValue = 0
   descValue = 0
   extra = 0
   try:
       while True:   

        if (servico not in ["DIG", "ICO", "IBO", "FOT"]):
            print ("Código de Serviço Inválido!")
            print("Entre com o código do serviço novamente.")
            servicos()

        else:
            
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
                servicos()                    

        opcao = float(input("""Deseja adicionar mais um serviço?
                            Escolha uma opção:
                            [1] - Encadernação Simples - R$10.00
                            [2] - Encadernação Capa Dura - R$25.00
                            [3] - Sem encadernação - Grátis
                            """))
        if opcao == 1:
            extra += 10.00
        elif opcao == 2:
            extra += 25.00
        else:
            extra += 0

        valorTotal = (serviceValue * paginas) + extra
        desconto = (valorTotal * descValue)/100
        valorTotalDesconto = valorTotal - desconto

        print("Total: {:.2f} (serviço: {} * páginas: {} + extras: {}) ".format(valorTotalDesconto, serviceValue, paginas, extra))
        break

   except ValueError:
       print("\n Ocorreu um erro, digite um valor válido!") 
       servicos()  

servicos()
