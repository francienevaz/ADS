# Soma de números binários:

# Na soma de números binários 1+1 = 10
# Na soma de números binários 1+0 = 1
# Na soma de números binários 0+1 = 1
# Na soma de números binários 0+0 = 0

# 1001 + 0101 = 1110

# Como na prática cada bit é armazenado em um determinado espaço
# reservado e computadores possuem limites de memória e de largura de bits, se
# estamos trabalhando com 4 bits e o resultado é um número com 5 bits, a
# informação será perdida. A mesma ideia é estendida para 8, 16, 32 ou 64 bits

a = int("1011", 2)
b = int("1101", 2)

soma_binaria = bin(a + b)

print(a + b)
print(soma_binaria)



