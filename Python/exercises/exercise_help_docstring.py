# Escreva uma função que calcule o fatorial de um número passado como parâmetro e retorne o seu resultado
# Faça uma validação com outra função, permitindo que somente pares sejam retornados
# Crie um help para a sua função

def fatorial(n):
    """_summary_

    Args:
        n (int): _numero inteiro opcional para calcular o fatorial desse numero_

    Returns:
        _int_: _a funcao retorna o fatorial do numero que foi passado como parametro_
    """
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def par(x):
    """_summary_

    Args:
        x (_int_): _recebe um valor inteiro_

    Returns:
        _int_: _retorna um numero inteiro par ou impar_
    """
    if x %2 == 0:
        return fatorial(x)
    else:
        return "O numero informado não é Par"

print(par(6))
