# Comando for
#  o comando for é usado para percorrer um objeto iterável.
#  Faz sentido usar for quando sabemos o número exato de vezes
#  que nosso bloco de código deve ser executado, ou quando
#  queremos percorrer um objeto iterável.

# O laço for in funciona assim: Para cada "letra" dentro do "texto" se executa um comando que será repetido até que a instrução que passamos se torne falsa. A variável "letra" é o índice, a variável texto será iterada e o valor iterado, nesse caso, cada letra, em cada repetição será atribuida a variável "letra"
# se "texto" receber a entrada "python", essa entrada será iterada e no exemplo na primeira repetição a variável "letra" irá receber "p", irá fazer a verificação e repetir o laço até que percorra toda a "string" recebida

texto = input("Escreva algo:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

    print() # adiciona uma quebra de linha
