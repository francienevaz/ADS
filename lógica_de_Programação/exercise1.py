ladoI = int(input("Digite um número: "))
ladoII = int(input("Digite outro número: "))
ladoIII = int(input("Digite mais um número: "))

if ladoI == ladoII == ladoIII:
    print("\nOs três lados são iguais, logo o triângulo é um Equilátero")
elif ladoI == ladoII or ladoI == ladoIII or ladoII == ladoIII:
    print ("\nDois dos lados são iguais, logo o triâgulo é um Isósceles.")
elif ladoI != ladoII != ladoIII:
    print('\nTodos os lados são diferentes, logo o triângulo é Escaleno.')