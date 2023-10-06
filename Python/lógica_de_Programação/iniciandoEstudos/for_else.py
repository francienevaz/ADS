#  for else
texto = input("Escreva algo:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")