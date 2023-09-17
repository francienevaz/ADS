msg = print('Calculadora Simples com Python')
calc = input("Escolha uma operação: \n [01] - adição \n [02] - subtração \n [03] - multiplicação \n [04] - divisão : ")
valorI = int(input("Digite um número: "))
valorII = int(input("Digite outro número: "))

soma = valorI + valorII
subtracao = valorI - valorII
multiplicacao = valorI * valorII 
divisao = valorI / valorII

if calc == "01":
    print(f'{valorI} + {valorII} = {soma}')
elif calc == "02":
    print(f'{valorI} - {valorII} = {subtracao}')
elif calc == "03":
    print(f'{valorI} * {valorII} = {multiplicacao}')
elif calc == "04":
    print(f'{valorI} / {valorII} = {divisao}')