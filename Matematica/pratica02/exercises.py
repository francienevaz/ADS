# Convertendo números binários em decimal:
# 1. Pegar o número binário
# 2. Converter cada dígito binário em um número decimal
# 3. Multiplicar cada número decimal pelo valor de sua posição
# 4. Soma todos os números decimais
# 5. Retornar o resultado da soma
binario = input('Digite um número binário: ')

def bin2dec(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * 2 ** (len(binario) - i - 1)
    return decimal

print(bin2dec(binario))    

# Para fazer a conversão de forma manual, cada dígito binário é multiplicado por 2 elevado a sua posição correspondente, da direita para a esquerda
# Exemplo: 100111
# 1 * 2**5 + 0 * 2**4 + 0 * 2**3 + 1 * 2**2 + 1 * 2**1 + 1 * 2**0
# o decimal correspondente é: 39