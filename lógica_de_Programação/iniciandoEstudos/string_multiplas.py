# Strings triplas ou strings de mútiplas linhas

nome  = "Franciene"

mensagem = f""" 
Olá meu nome é {nome},
Estou aprendendo Python
"""
print(mensagem)

mensagem2 = f''' 
   Olá meu nome é {nome},
Estou aprendendo Python.
        Veja que os recuos permanecem...
'''

print(mensagem2)


#  o """ preserva os espaços:

print( """ 
    ============== Menu ==============

    1 - Depósito
    2 - Saque
    3 - Saldo
    4 - Extrato
    0 - Sair

    ==================================

            Obrigada e volte sempre!

""")




