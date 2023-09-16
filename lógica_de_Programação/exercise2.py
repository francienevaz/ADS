valorI = int(input("Digite um número: "))
valorII = int(input("Digite outro número: "))
calc = input("Escolha uma operação: \n adição \n subtração \n multiplicação \n divisão : ")

soma = valorI + valorII
subtracao = valorI - valorII
multiplicacao = valorI * valorII 
divisao = valorI / valorII

if calc == "adição":
    print(soma)
elif calc == "subtração":
    print(subtracao)
elif calc == "multiplicação":
    print(multiplicacao)
elif calc == "divisão":
    print(divisao)