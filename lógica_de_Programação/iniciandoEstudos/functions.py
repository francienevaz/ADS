def soma(x, y):
  return x + y

print(soma(2,7))

def verifyValue (nome, id, age):
  try:
    print(input(nome))
    print(int(id))
    print(int(input(age)))
  except TypeError:
    print("Valor inválido, tente novamente!")
  else:
    print("Erro inesperado!")
  finally:
    print("fim da função")

verifyValue("Digite seu nome: ", 2, "Digite sua idade: ")
    
