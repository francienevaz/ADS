# Tudo que está dentro do trio de aspas duplas é o que chamamos de "docstring"
# é chamado no começo da função para auxiliar o 'usuário' a compreender o que a função pede

def soma (x = 0, y = 0, z = 0):
    """_summary_

    Args:
        x (int, optional): _description_. Defaults to 0.
        y (int, optional): _description_. Defaults to 0.
        z (int, optional): _description_. Defaults to 0.
    """

    return x+y+z

print("A função soma retorna o valor de {}".format(soma(5,8,6)))
help(soma)