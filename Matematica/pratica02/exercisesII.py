# na conversão de um decimal para um binário basta fazer a divisão por 2
# e guardar o resto da divisão, depois de fazer a divisão, o número inteiro
# é o número que vai ser dividido novamente, até que o número inteiro seja 0
# o resto da divisão é o número binário, porém, o número deve ser invertido,
# pois o algoritmo de divisão por 2 é feito de  cabeca para baixo,
# e o número binário é escrito de cima para baixo, logo,
# o número deve ser invertido para que o resultado seja o
# número binário correto.

decimal = int(input("Digite um número decimal: "))

def decimal_para_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        resto = decimal % 2
        decimal = decimal // 2
        binario = str(resto) + binario
    return binario

print(decimal_para_binario(decimal))
