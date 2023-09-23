# x = 10

# while (x > 0):
#     x = x - 1
#     print(x)
#     if x == 0:
#         print("Fogo!")

# escrever um algoritmo que calcule a média de notas
# 5 notas digitadas

soma = 0
count = 1

while count <= 5:
    x = float(input(f'Digite sua {count}ª nota: '))
    soma = soma + x
    count = count + 1
    media = soma/5    
print(f'A média das suas notas é {media}!')

if media < 7:
    print("Você foi reprovado!")
elif media > 7:
    print("Parabéns você foi aprovado!")
else:
    print("Estude mais")


