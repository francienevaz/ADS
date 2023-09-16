# Expressões booleanas

soma = 2 + 2
print(soma<4); # False
# // pega a parte inteira da divisão de 7/3
print(7//3 == 1 + 1) # True
print((3**2 + 4**2) == 25) # True
print((2 + 4 + 6) > 12) # False

# 1387 é divisível por 19?
print(1387 %19 == 0)
# 31 é par?
print(31 %2 == 0)
# O menor valor entre: 34, 29, 31 é menor do que 30
print(min(34,29,31) < 30)


# Condicional simples

idade = 70
dano = 35
escudo = 0

if idade > 60:
    print("Você tem direitos aos benefícios")

if dano > 10 and escudo == 0:
    print("Você está morto!")

Norte = False
Sul = False
Leste = True
Oeste = False

if (Norte or Sul or Leste or Oeste == True):
    print("Você conseguiu escapar!")

# Em Python mais comumente usar and e or para operações lógicas
# Mas também funciona utilizar & e |, porém para comparações bitwise em nível de bit

ano = 2023

if (ano %4 == 0):
    print('É bissexto')
else:
    print ('Não é Bissexto')

cima  = True
baixo = False

if cima and baixo:
    print("Decida-se!")
else:
    print("Você escolheu um caminho!")