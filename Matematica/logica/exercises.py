

while True:
    senha = 705080

    tentativa = int(input("Digite a senha: "))
    if tentativa != senha:
        print("Senha incorreta. Tente novamente.")
    else:
        print("Entrada autorizada!")
        break

