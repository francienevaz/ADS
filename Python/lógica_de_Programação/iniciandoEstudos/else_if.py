# EM PYTHON A IDENTAÇÂO É IMPORTANTE, POIS DELIMITA O FIM DE UMA FUNÇÂO
# NO CASO DOS IFs por exemplo

MAIOR_IDADE = 18

idade = int(input("Infome sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você já pode tirar a sua CNH.")

elif idade < MAIOR_IDADE:
    print("Você ainda não pode tirar a CNH.")
    texto = f"Aguarde {MAIOR_IDADE - idade} anos!"
    print(texto)

else:
    print("Ainda não pode tirar a CNH")


#  elif é usado para estabelecer várias condições em python, é como se fosse o else if em Javascript
# If aninhado:

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450
status= "Sucesso" if saldo >= saque else "Falha" # Essa é uma condição ternária em Python - if ternário 
# em JS saldo >= saque ? "Sucesso" : "Falha"

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
    
else:
    print("Nosso sistema não reconheceu o seu tipo de conta, por favor entre em contato com o seu gerente!")
