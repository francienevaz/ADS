numberI = int(input("Digite um número inteiro: "))
numberII = int(input("Digite um outro número inteiro: "))

if (numberI < numberII):
    print(f"O número {numberII} é maior que o número {numberI}")

else:
    print(f'O número {numberII} é menor que número {numberI}')

if numberII %2 == 0:
    print(f'O número {numberII} é Par')
elif numberII %2 != 0:
    print(f'O número {numberII} é Ímpar')


if numberI %2 == 0:
    print(f'O número {numberI} é Par')
else:
    print(f'O número {numberI} é Ímpar')