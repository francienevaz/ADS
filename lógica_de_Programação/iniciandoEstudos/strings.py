# Conhecendo métodos úteis da classe string

curso = "pYtHon"

print(curso.upper())
print(curso.lower())
print(curso.title())

curso = "   Python "

print(curso.strip()) # Esse método serve para remover espaços tanto do lado direito quanto do lado esquerdo

print(curso.lstrip()) #left
print(curso.rstrip()) #right

hello = "Hello World"

print(hello.center(20, "."))

print("-".join(hello))

for letra in hello:
    print(letra, end="-")


