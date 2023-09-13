# Old style %

nome = "Fran"
idade = 28
profissao = "Dev Frontend"
linguagem = "Javascript"

dados = {
    "nome": "Flávio",
    "idade": 28,
    "profissão": "Engenheiro"
}

# Uma forma mais antiquada de fazer a interpolação de variaáveis é usando o %s e %d. No exemplo abaixo é só substituir as chaves por %s para string e %d para o número

# Método format
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}" .format(nome, idade, profissao, linguagem))

# f-string // é um método mais fácil de trabalhar
print(f"Olá, eu sou a {nome}. Tenho  {idade} anos, e estou estudando {linguagem}, para me tornar {profissao} XD!")

# Formatar strings com f-string
# Veja que o 10 antes do ponto representa a quantidade de espaços antes do número. E por fim o 2f é a quantidade de casas decimais depois da vírgula

PI = 3.14159

print(f"Valor de PI é : {PI:.2f}")
print(f"Valor de PI é : {PI:10.2f}")

print("Nome: {nome} Idade: {idade} Profissão: {profissão}".format(**dados))