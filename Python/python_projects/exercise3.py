SERVICOS = []

def servicos() :
    MESSAGE = print("""
        *** Seja Bem Vindo(a)s a Copiadora da Franciene Vaz ***
    """)
    servico = input("""
        Digite o código do serviço desejado:
            
        [DIG] - Digitalização
        [ICO] - Impressão Colorida
        [IBO] - Impressão em Preto e Branco
        [FOT] - Fotocópia
    
    """).upper()
    print(servico)
    while True:
            if (servico != "DIG" and "ICO" and "IMP" and "FOT"):
                print ("Código de Serviço Inválido!")
                print("Entre com o código do serviço novamente.")
                print(input("""
                    Digite o código do serviço desejado:
                        
                    [DIG] - Digitalização
                    [ICO] - Impressão Colorida
                    [IBO] - Impressão em Preto e Branco
                    [FOT] - Fotocópia

                """))
            else:
                paginas = print(int(input("Entre com o número de páginas: ")))
                porcentagem = 0

                if paginas < 10:
                    porcentagem = 0
                elif paginas  >= 10 and paginas < 100:
                    porcentagem = 10
                elif paginas >= 100 and paginas < 1000:
                    porcentagem = 15
                elif paginas >= 1000 and paginas < 10000:
                    porcentagem = 20
                else:
                    print("Excedeu o limite de páginas, digite um número de páginas menor!")
print(input("""Deseja adicionar mais um serviço?
    Escolha uma opção:
      [1] - Encadernação Simples - R$10.00
      [2] - Encadernação Capa Dura - R$25.00
      [3] - Sem encadernação - Grátis
    """))
servicos()
